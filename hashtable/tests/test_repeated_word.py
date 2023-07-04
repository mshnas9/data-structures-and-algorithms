import pytest
from repeated_word import repeated_word

def test_no_repeated_words():
    """Test the function with no repeated words."""
    sentence = 'hello world'
    expected = None
    actual = repeated_word(sentence)
    assert expected == actual

def test_repeated_words():
    """Test the function with multiple repeated words."""
    sentence = 'this is a loop, this is a loop'
    expected = 'this'
    actual = repeated_word(sentence)
    assert expected == actual

def test_repeated_words_case_sensitive():
    """Test the function with repeated words (case-sensitive)."""
    sentence = 'Hello world, hello World'
    expected = 'hello'
    actual = repeated_word(sentence)
    assert expected == actual

def test_repeated_words_with_punctuation():
    """Test the function with repeated words containing punctuation."""
    sentence = 'This is a test. This is only a test!'
    expected = 'this'
    actual = repeated_word(sentence)
    assert expected == actual

def test_empty_sentence():
    """Test the function with an empty sentence."""
    sentence = ''
    expected = None
    actual = repeated_word(sentence)
    assert expected == actual

def test_long_sentence_with_repeated_word():
    """Test the function with a long sentence containing a repeated word."""
    sentence = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam facilisis ligula at mauris efficitur, sit amet aliquam mauris lobortis. Curabitur vel velit a turpis aliquam luctus. Integer iaculis quam sit amet libero iaculis, et accumsan lacus cursus. Sed eu turpis auctor, cursus ipsum at, placerat est. Mauris congue velit a dui rutrum, ut interdum lectus varius. Aenean at est ut lacus efficitur interdum. Nunc at mi sit amet neque tempor feugiat. Sed venenatis nibh at ante convallis ullamcorper. Duis euismod, odio in suscipit pulvinar, sem felis fringilla arcu, et ultrices ligula sem nec nunc. Quisque feugiat, risus ut ullamcorper convallis, turpis arcu dapibus ligula, et aliquam velit mauris at odio. Sed tempus est et erat cursus varius. Integer pharetra nulla vel consectetur auctor. Sed id felis risus. Aenean elementum, elit ut malesuada feugiat, lectus lacus viverra diam, at finibus nisi est eget nulla. Mauris tristique ullamcorper malesuada.'
    expected = 'sit'
    actual = repeated_word(sentence)
    assert expected == actual

if __name__ == '__main__':
    pytest.main()
