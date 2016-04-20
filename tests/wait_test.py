import unittest

from wait.wait import wait_until
from webdriver.exceptions import PyDriverTimeoutException


class WaitTest(unittest.TestCase):
    def test_should_wait_for_condition(self):
        truth = False
        try:
            wait_until(lambda: truth is True, 5, 1)
        except PyDriverTimeoutException:
            truth = True
        wait_until(lambda: truth is True, 5, 1)
