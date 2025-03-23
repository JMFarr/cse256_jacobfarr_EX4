# Jacob Farr
# CIS256 Spring 2025
# EX 4

from guess_the_word import *

def test_that_selected_word_is_from_list():
    assert select_random_word() in word_list
    