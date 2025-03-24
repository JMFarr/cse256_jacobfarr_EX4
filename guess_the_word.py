# Jacob Farr
# CIS256 Spring 2025
# EX 4

import random

# Word list to be randomly selected from
word_list = ["hard",
"pony",
"sin",
"sensitive",
"survivor",
"patience",
"overeat",
"request",
"leak",
"civilian",
"execution",
"create",
"tank",
"harass",
"incident",
"tower",
"vote",
"fee",
"ferry",
"carve"]

# Function which randomly selects a word from the list.
def select_random_word():
    return random.choice(word_list)

# Function which returns true if the guess matches the current
# letter, or false if it does not. Comparison is case-insensitive
def check_guess(guess, word, index):
    return guess.lower() == word[index].lower()

def game():
    attempts_remaining = 10
    current_letter = 0
    word_to_guess = "testing"
    incorrect_guesses = set()
    while (current_letter < len(word_to_guess)) and (attempts_remaining > 0):
        guess = input("Guess a letter: ")
        print()
        if check_guess(guess, word_to_guess, current_letter):
            current_letter += 1
            incorrect_guesses = set()
            print("CORRECT!")
        else:
            attempts_remaining -= 1
            incorrect_guesses.add(guess.lower())
            print(f"WRONG. {attempts_remaining} attempts remaining.")
        
        print(f"\nWord: {word_to_guess[:current_letter]}{"".join(["_" for _ in range(len(word_to_guess) - current_letter)])}")
        print(f"Incorrect Guesses: {", ".join(incorrect_guesses)}\n")

    if current_letter == len(word_to_guess):
        print("Congratulations! You won!")
    else:
        print("You lost... Better luck next time.")

if __name__ == "__main__":
    game()