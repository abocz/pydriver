from selenium import webdriver

from webdriver.view import View


class Driver(object):
    def __init__(self, driver=webdriver.Firefox()):
        self.driver = driver

    def open(self, destination):
        if isinstance(destination, View):
            destination.__set_driver__(self)
            destination.driver.get(destination.url())
            return destination
        else:
            self.get(destination)

    def get(self, url):
        self.driver.get(url)

    def title(self):
        return self.driver.title

    def maximize(self):
        self.driver.maximize_window()

    def refresh(self):
        self.driver.refresh()

    def close(self):
        self.driver.close()

    def find_element(self, by, value):
        return self.driver.find_element(by, value)
