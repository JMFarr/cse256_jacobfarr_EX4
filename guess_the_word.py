# Jacob Farr
# CIS256 Spring 2025
# EX 4

def game():
    attempts_remaining = 10
    current_letter = 0
    word_to_guess = "testing"
    incorrect_guesses = set()
    while (current_letter < len(word_to_guess)) and (attempts_remaining > 0):
        guess = input("Guess a letter: ")
        if guess.lower() == word_to_guess[current_letter].lower():
            current_letter += 1
            incorrect_guesses = set()
            print("CORRECT!")
        else:
            attempts_remaining -= 1
            incorrect_guesses.add(guess.lower())
            print(f"WRONG. {attempts_remaining} attempts remaining.")
        print(f"Word: {word_to_guess[:current_letter]}{"".join(["_" for _ in range(len(word_to_guess) - current_letter)])}")
        print(f"Incorrect Guesses: {", ".join(incorrect_guesses)}")
    if current_letter == len(word_to_guess):
        print("Congratulations! You won!")
    else:
        print("You lost... Better luck next time.")
