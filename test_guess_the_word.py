# Jacob Farr
# CIS256 Spring 2025
# EX 4

from guess_the_word import check_guess

class TestCheckGuessFunction:
    def test_correct_guess_returns_expected_result(self):
        assert check_guess("Letters", "L") == (True, "etters")
    
    def test_wrong_guess_returns_expected_result(self):
        assert check_guess("Letters", "X") == (False, "Letters")

    def test_guess_on_empty_string_returns_expected(self):
        assert check_guess("", "L") == (False, "")