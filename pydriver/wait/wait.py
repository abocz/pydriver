import polling

from pydriver.webdriver.exceptions import PyDriverTimeoutException


def wait_until(predicate, timeout_at=30, poll_every=1):
    try:
        polling.poll(predicate, poll_every, timeout=timeout_at)
    except polling.TimeoutException:
        raise PyDriverTimeoutException('Timed out after {} seconds waiting for {} to be true. '
                                       'The predicate was polled every {} seconds.'.format(timeout_at, predicate,
                                                                                           poll_every))
