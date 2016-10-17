from nose.tools import *
from people import ex49
from people import lexicon

def test_success():
    sentence = ex49.parse_sentence(lexicon.scan("kill the bear now"))
    assert_equal(sentence.subject, "player")
    assert_equal(sentence.verb, "kill")
    assert_equal(sentence.object, "bear")

def test_fail():
    word_list = lexicon.scan("south and kill the bear")
    assert_raises(ex49.ParserError, ex49.parse_sentence, word_list)
