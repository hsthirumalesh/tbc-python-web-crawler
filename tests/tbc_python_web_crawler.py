import urllib2
import sys
import os
import webbrowser
from bs4 import BeautifulSoup

def get_details(link, index):
    """ Crawls through the given link for book or chapter details

    Parameters
    --------------
    link : string
        link of the book(.html) or chapter(.html or .ipynb)

    index : int
        Getting details from book or chapter is set by index value
        * index = 1 --> gets details of the book
        * index = 0 --> gets details of the chapter

    Returns
    --------------
    details_list : list
        list of lists contains names and links of the book or chapter

    """
    details_list = []

    src = BeautifulSoup(urllib2.urlopen(link))
    table = src.find('table')
    for row in table.find_all('tr'):
        column = row.find_all('td')  
        name = column[index].a.string.encode('ascii', 'ignore')
        link = 'http://tbc-python.fossee.in%s' %(column[index].a.get("href"))
        details_list.append([name, link])

    return details_list


def get_chapter_errors(chap_link):
    """ Crawls through the chapters and finds number of errors 

    Parameters
    --------------
    chap_link : string
        .ipynb/html link of the chapter

    Returns
    --------------
    error : int or NoneType or Exception
        number of errors present in the given chapter link or Page fecth error
        if the link is broken

    """
    try:
        chp_src = BeautifulSoup(urllib2.urlopen(chap_link))
        example_errors = chp_src.find_all('div', {'class': 
                                   'output_subarea output_text output_error'})
        error = len(example_errors)
        if not example_errors:
            error = None 

    except urllib2.HTTPError as e:
        error = str(e)

    return error


def error_log_to_html(error_log):
    """ Uses jinja2 template to convert python dictionary into html format.
	Data from error_log is converted into formatted html tags, which can be
	viewed as a webpage.
    
    Parameters
    --------------
    error_log: dictionary
        contains details of the uploaded example codes which have errors.

    Returns
    --------------
    html: html data
    	error_log in html format       
    
    """
    from jinja2 import Template

    temp = """
    <html>
     <title>Errors in the uploaded python codes in TBC website!!!</title>
    <tbody>
        <center>
            <h2> Python TBC errors </h2>
        </center>
      {% for key, value in error_log.iteritems() %}
            <a href={{ value.url }}>{{ value.name }}</a>
        {% for k, v in  value.iteritems() %}
            {% if k == "chapters" %}
                <table>
                {% for c in v %}
                <tr>
                  <td>Errors: {{c.errors}}  <a href={{ c.chapter_url }}>{{ c.name }}</a>  </td>
                </tr>
                {% endfor %}
                </table>
            {% endif %}
        {% endfor %}
        <br/>       
      {% endfor %} 
    </tbody>
    </html>
    """

    template = Template(temp)
    html = template.render(error_log=error_log)

    return html

def main():
    full_log = {}
    error_dict = {}
    error_log = {}

    url = sys.argv[1] # accept url as argument
    book_details_list = get_details(url, index=1)

    webbrowser.open('file://' + os.path.realpath("tbc-errors.html"), new=0)

    # Get details of the book
    for book_name, book_link in book_details_list:
        chapter_details_list = get_details(book_link, index=0)
        _id = book_link.strip('http://tbc-python.fossee.in/book-details')
        
        chapters = []
        # Get details of the chapter
        for chap_name, chap_link in chapter_details_list:
            error = get_chapter_errors(chap_link)
            
            # If error is present in the chapter, store details in error_log
            if error != None:
            
                error_dict = {'name': book_name,
                              'url': book_link,
                             }

                chapters.append({'name': chap_name,
                                 'errors': error,
                                 'chapter_url': chap_link
                                })

                error_dict['chapters'] = chapters
                error_log.update({_id: error_dict})
                print 'Error: ', book_name, chap_name

                html = error_log_to_html(error_log)
                html_file = open("tbc-errors.html","w")
                html_file.write(html)
                html_file.close()
            else:
                print 'No errors: ', book_name, chap_name
       
        
if __name__ == '__main__':
    main()
