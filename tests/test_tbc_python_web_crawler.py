import unittest
import os
from tbc_python_web_crawler import get_chapter_errors, get_details, error_log_to_html
from jinja2 import Template

chapter_details = [['Chapter 1 Introduction',
  'http://tbc-python.fossee.in/convert-notebook/Fundamentals_of_Fluid_Mechanics/ch_1.ipynb'],
 ['Chapter 2 Fluid Statistics',
  'http://tbc-python.fossee.in/convert-notebook/Fundamentals_of_Fluid_Mechanics/Ch_2.ipynb'],
 ['Chapter 3 Elementary Fluid Dynamics',
  'http://tbc-python.fossee.in/convert-notebook/Fundamentals_of_Fluid_Mechanics/ch_3.ipynb'],
 ['Chapter 4 Fluid Kinematics',
  'http://tbc-python.fossee.in/convert-notebook/Fundamentals_of_Fluid_Mechanics/Ch_4.ipynb'],
 ['Chapter 5 Fluid Control Volume Analysis',
  'http://tbc-python.fossee.in/convert-notebook/Fundamentals_of_Fluid_Mechanics/Ch_5.ipynb'],
 ['Chapter 6 Differential Analysis of Fluid Flow',
  'http://tbc-python.fossee.in/convert-notebook/Fundamentals_of_Fluid_Mechanics/Ch_6.ipynb'],
 ['Chapter 7 Similitude ,Dimensional Analysis and Modelling',
  'http://tbc-python.fossee.in/convert-notebook/Fundamentals_of_Fluid_Mechanics/Ch_7.ipynb'],
 ['Chapter 8 Viscous Flow in Pipes',
  'http://tbc-python.fossee.in/convert-notebook/Fundamentals_of_Fluid_Mechanics/Ch_8.ipynb'],
 ['Chapter 9 Flow Over Immersed Bodies',
  'http://tbc-python.fossee.in/convert-notebook/Fundamentals_of_Fluid_Mechanics/Ch_9.ipynb'],
 ['Chapter 10 Open Channel Flow',
  'http://tbc-python.fossee.in/convert-notebook/Fundamentals_of_Fluid_Mechanics/ch_10.ipynb'],
 ['Chapter 11 Compressible Flow',
  'http://tbc-python.fossee.in/convert-notebook/Fundamentals_of_Fluid_Mechanics/ch_11.ipynb'],
 ['Chapter 12 Turbomachines',
  'http://tbc-python.fossee.in/convert-notebook/Fundamentals_of_Fluid_Mechanics/ch_12.ipynb']]


html = """\n    <html>\n     <title>Errors in the uploaded python codes in TBC website!!!</title>\n    <tbody>\n        <center>\n            <h2> Python TBC errors </h2>\n        </center>\n      \n            <a href=http://tbc-python.fossee.in/book-details/15/>C++ in Action - Industrial-Strength Programming Techniques by Bartosz Milewski</a>\n        \n            \n        \n            \n        \n            \n                <table>\n                \n                <tr>\n                  <td>Errors: 2  <a href=http://tbc-python.fossee.in/convert-notebook/C++_in_Action_-_Industrial-Strength_Programming_Techniques/ch1.ipynb>Chapter 1 Naming</a>  </td>\n                </tr>\n                \n                <tr>\n                  <td>Errors: 1  <a href=http://tbc-python.fossee.in/convert-notebook/C++_in_Action_-_Industrial-Strength_Programming_Techniques/ch2.ipynb>Chapter 2 Organizing the code</a>  </td>\n                </tr>\n                \n                <tr>\n                  <td>Errors: 3  <a href=http://tbc-python.fossee.in/convert-notebook/C++_in_Action_-_Industrial-Strength_Programming_Techniques/ch10.ipynb>Chapter 10 Object-oriented programming</a>  </td>\n                </tr>\n                \n                <tr>\n                  <td>Errors: 1  <a href=http://tbc-python.fossee.in/convert-notebook/C++_in_Action_-_Industrial-Strength_Programming_Techniques/ch12.ipynb>Chapter 12 Error handling</a>  </td>\n                </tr>\n                \n                <tr>\n                  <td>Errors: 1  <a href=http://tbc-python.fossee.in/convert-notebook/C++_in_Action_-_Industrial-Strength_Programming_Techniques/ch13.ipynb>Chapter 13 Parts of C++ to Avoid</a>  </td>\n                </tr>\n                \n                <tr>\n                  <td>Errors: 2  <a href=http://tbc-python.fossee.in/convert-notebook/C++_in_Action_-_Industrial-Strength_Programming_Techniques/ch15.ipynb>Chapter 15 Portability</a>  </td>\n                </tr>\n                \n                </table>\n            \n        \n        <br/>       \n       \n    </tbody>\n    </html>\n    """    

error_log = {'15':
 {'url': 'https://tbc-python.fossee.in/book-details/15/', 
  'name': u'C++ in Action - Industrial-Strength Programming Techniques by Bartosz Milewski', 
  'chapters':
    [{'errors': 2, 
      'name': u'Chapter 1 Naming', 
      'chapter_url': 'http://tbc-python.fossee.in/convert-notebook/C++_in_Action_-_Industrial-Strength_Programming_Techniques/ch1.ipynb'}, 
     {'errors': 1, 
      'name': u'Chapter 2 Organizing the code', 
      'chapter_url': 'http://tbc-python.fossee.in/convert-notebook/C++_in_Action_-_Industrial-Strength_Programming_Techniques/ch2.ipynb'},
     {'errors': 3, 
      'name': u'Chapter 10 Object-oriented programming', 
      'chapter_url': 'http://tbc-python.fossee.in/convert-notebook/C++_in_Action_-_Industrial-Strength_Programming_Techniques/ch10.ipynb'}, 
     {'errors': 1, 
      'name': u'Chapter 12 Error handling', 
      'chapter_url': 'http://tbc-python.fossee.in/convert-notebook/C++_in_Action_-_Industrial-Strength_Programming_Techniques/ch12.ipynb'}, 
     {'errors': 1, 
      'name': u'Chapter 13 Parts of C++ to Avoid', 
      'chapter_url': 'http://tbc-python.fossee.in/convert-notebook/C++_in_Action_-_Industrial-Strength_Programming_Techniques/ch13.ipynb'}, 
     {'errors': 2, 
      'name': u'Chapter 15 Portability', 
      'chapter_url': 'http://tbc-python.fossee.in/convert-notebook/C++_in_Action_-_Industrial-Strength_Programming_Techniques/ch15.ipynb'}
    ]
  }
 }


class ErrorsTestCase(unittest.TestCase):

    def test_has_2_example_errors(self):
        example_errors = get_chapter_errors('file://' + os.path.realpath("test_has_2_example_errors.html"))
        self.assertTrue(example_errors == 2)

    def test_has_none_example_errors(self):
        example_errors = get_chapter_errors('file://' + os.path.realpath("test_has_none_example_errors.html"))
        self.assertTrue(example_errors == None)

    def test_has_page_loading_error(self):
        page_error = get_chapter_errors('file://' + os.path.realpath("test_has_page_error.html"))
        self.assertRaises('HTTP Error 500: Internal Server Error', page_error)

    def test_get_chapter_details(self):
        self.assertTrue(chapter_details == get_details('http://tbc-python.fossee.in/book-details/14/', 0)) 
    
    def test_error_log_to_html(self):
    	self.assertTrue(html == str(error_log_to_html(error_log)))
    
if __name__ == '__main__':
    unittest.main()
