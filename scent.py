import sniffer
import termstyle

# you can customize the pass/fail colors like this
pass_fg_color = termstyle.green
pass_bg_color = termstyle.bg_default
fail_fg_color = termstyle.red
fail_bg_color = termstyle.bg_default


def run_tests(*args):
        import unittest
        tests = unittest.TestLoader().discover('./tests', '*.py')
        result = unittest.TextTestRunner().run(tests)
        return result.wasSuccessful()

sniffer.Sniffer.run = run_tests
