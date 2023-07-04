import pytest
from repeated_word import repeated_word
def test_no_repeated_words():
    """test the function with no repeated words"""
    sentence = 'hello world'
    expected = None
    actual = repeated_word(sentence)
    assert expected == actual

def test_repeated_words():
    """test the function with multiple repeated words"""
    sentence = 'this is a loop, this is a loop'
    expected = 'this'
    actual = repeated_word(sentence)
    assert expected == actual

