# TBC python web crawler

This python script crawls through all the completed textbooks in http://tbc-python.fossee.in/
It checks for any errors present in the uploaded python codes and this error data is stored in
`error_log` dictionary
* Codes with errors are fetched
* Chapters with broken urls are fetched


# Requirements:
* Python version 2.7.6
* BeautifulSoup 4
  
  If you’re using a recent version of Debian or Ubuntu Linux, you can install Beautiful Soup 
  with the system package manager:

  `apt-get install python-bs4`
  
  If unable to install with system package manager, try:

  `easy_install beautifulsoup4`  or  `pip install beautifulsoup4` 
  
  If you don’t have `easy_install` or `pip` installed,  
  [you can download Beautiful Soup source tarball](http://www.crummy.com/software/BeautifulSoup/bs4/download/4.4/) and install it with `setup.py`
  
* urllib2
* Jinja2 template engine 

  `easy_install jinja2` or  `pip install jinja2`

# Web crawler usage:

Run the following command from the directory where `tbc_python_web_crawler.py` is present.

`python tbc_python_web_crawler.py http://tbc-python.fossee.in/completed-books/`

# Testing:
* Run the following command from `/tbc-python-web-crawler/testing` folder.

`python test_tbc_web_crawler.py`

* Following tests are implemented in the `test_tbc_web_crawler.py` file
  * Testing `get_chapter_errors` function with `2 example errors` and `None example errors`
  * Testing `get_chapter_errors` function with page loading error
  * Testing `get_details` function with fetching chapter details 
  * Testing `error_log_to_html` function with sample html output
