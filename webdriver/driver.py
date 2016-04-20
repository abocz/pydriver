from selenium import webdriver


class Driver(object):
    def __init__(self, driver=webdriver.Firefox()):
        self.driver = driver

    def open(self, url):
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
