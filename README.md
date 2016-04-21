pydriver
============

Selenium/"Page Object" Python wrapper inspired by [darcy-framework](http://github.com/darcy-framework).

Usage
------------

Create a class that inherits **View** and then add at least one field to look for on the page to be considered loaded.

Override the **url(self)** method and provide a URL to open for the view.

~~~python
import pydriver

from pydriver.webdriver import Driver, TextInput, View


class GoogleView(View):
    search_input = TextInput(By.NAME, 'q')

    def url(self):
        return 'http://www.google.com'


driver = Driver()
google_view = driver.open(GoogleView())
google_view.search_input.clear_and_type('Hello')
driver.close()
~~~