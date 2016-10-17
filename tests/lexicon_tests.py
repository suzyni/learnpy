from nose.tools import *
from people import lexicon

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])

def test_sentence1():
    result = lexicon.scan("go kill the bear 105 bus")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('stop', 'the'),
                          ('noun', 'bear'),
                          ('number', 105),
                          ('error', 'bus')])
