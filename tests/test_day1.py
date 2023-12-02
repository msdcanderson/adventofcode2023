import pytest
from adventofcode2023.day1.main import word_or_digit_to_digit


# Test with digit inputs
def test_with_digit_input() -> None:
    assert word_or_digit_to_digit("123", 0) == "1"
    assert word_or_digit_to_digit("123", -1) == "3"


# Test with word inputs
def test_with_word_input() -> None:
    assert word_or_digit_to_digit("one", 0) == "1"
    assert word_or_digit_to_digit("twenty", 0) != "2"


# Test with invalid inputs
def test_with_invalid_input() -> None:
    with pytest.raises(ValueError):
        word_or_digit_to_digit("invalid", 0)


# Test with edge cases
def test_edge_cases() -> None:
    assert word_or_digit_to_digit("0", 0) == "0"
    assert word_or_digit_to_digit("0", -1) == "0"
    assert word_or_digit_to_digit("ten", 0) == "10"
