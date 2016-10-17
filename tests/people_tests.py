from nose.tools import *
from people.people import Name

def setup():
    pass

def teardown():
    pass

def test_title_ss():
    name = Name('ss').title()
    assert_equal('Dr.', name)

def test_title_fe():
    """
    >>> print Name('fe').title()
    Mr.
    """
