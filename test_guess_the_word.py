# Jacob Farr
# CIS256 Spring 2025
# EX 4

from guess_the_word import *

def test_that_selected_word_is_from_list():
    assert select_random_word() in word_list

def test_check_guess_evaluates_correct_guesses_appropriately():
    assert check_guess("l", "apple", 3) == True

def test_check_guess_evaluates_wrong_guesses_appropriately():
    assert check_guess("x", "apple", 0) == False