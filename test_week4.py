from week4 import get_squares

import pytest


class TestGetSquares:

    #  Returns a list of squared numbers in ascending order for a list of positive integers
    def test_positive_integers(self):
        numbers = [1, 2, 3, 4, 5]
        expected = [1, 4, 9, 16, 25]
        assert get_squares(numbers) == expected

    #  Returns an empty list for an empty input list
    def test_empty_list(self):
        numbers = []
        expected = []
        assert get_squares(numbers) == expected

    #  Returns a list with one element for a list with one element
    def test_one_element(self):
        numbers = [2]
        expected = [4]
        assert get_squares(numbers) == expected

    #  Returns a list of squared numbers in ascending order for a list of negative integers
    def test_negative_integers(self):
        numbers = [-5, -4, -3, -2, -1]
        expected = [1, 4, 9, 16, 25]
        assert get_squares(numbers) == expected

    #  Returns a list of squared numbers in ascending order for a list of mixed positive and negative integers
    def test_mixed_integers(self):
        numbers = [-3, -2, -1, 0, 1, 2, 3]
        expected = [0, 1, 1, 4, 4, 9, 9]
        assert get_squares(numbers) == expected

    #  Returns a list of squared numbers in ascending order for a list of large positive integers
    def test_large_positive_integers(self):
        numbers = [1000000, 2000000, 3000000]
        expected = [1000000000000, 4000000000000, 9000000000000]
        assert get_squares(numbers) == expected

    #  Returns a list of squared numbers in ascending order for a list of large negative integers
    def test_large_negative_integers(self):
        numbers = [-1000000, -2000000, -3000000]
        expected = [1000000000000, 4000000000000, 9000000000000]
        assert get_squares(numbers) == expected

    #  Raises an exception if a non-integer element is present in the input list
    def test_non_integer_element(self):
        numbers = [1, 2, '3', 4, 5]
        with pytest.raises(Exception):
            get_squares(numbers)

    #  Raises an exception if a non-numeric element is present in the input list
    def test_non_numeric_element(self):
        numbers = [1, 2, 'three', 4, 5]
        with pytest.raises(Exception):
            get_squares(numbers)

    #  Raises an exception if a None element is present in the input list
    def test_none_element(self):
        numbers = [1, 2, None, 4, 5]
        with pytest.raises(Exception):
            get_squares(numbers)
