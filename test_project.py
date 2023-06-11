# file to test return 'Hello World'

from project import say_hi


def test_say_hi():
    assert say_hi() == 'Hello master'
