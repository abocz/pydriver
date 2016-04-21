import unittest

from pydriver.wait import wait_until
from pydriver.webdriver import PyDriverTimeoutException


class WaitTest(unittest.TestCase):
    def test_should_wait_for_condition(self):
        truth = False
        try:
            wait_until(lambda: truth is True, 5, 1)
        except PyDriverTimeoutException:
            truth = True
        wait_until(lambda: truth is True, 5, 1)


if __name__ == '__main__':
    unittest.main()
