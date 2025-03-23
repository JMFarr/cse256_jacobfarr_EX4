# Jacob Farr
# CIS256 Spring 2025
# EX 4

def check_guess(remaining_letters, guess):
    if len(remaining_letters) == 0:
        return (False, "")
    if remaining_letters[0] == guess:  
        return (True, remaining_letters[1:])
    else:
        return (False, remaining_letters)

