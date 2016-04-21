from selenium.webdriver.common.by import By

from pydriver.webdriver import Driver, TextInput
from pydriver.webdriver.view import View


class GoogleView(View):
    search_input = TextInput(By.NAME, 'q')

    def url(self):
        return 'http://www.google.com'


driver = Driver()
google_view = driver.open(GoogleView())
google_view.search_input.clear_and_type('Hello')
