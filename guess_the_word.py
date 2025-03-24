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

# Function containing core game logic.
def game():
    word_to_guess = select_random_word()  # The word user needs to guess
    current_letter = 0  # Index of current letter for guess comparison
    incorrect_guesses = set()  # A Set which holds wrong guesses for the current letter.
    attempts_remaining = 10  # Tracks the remaining number of wrong guesses allowed.
    
    print(f"\nWord: {"".join(["_" for _ in word_to_guess])}\n")

    # Main game loop. Game continues until the words has been guess in
    # its entirety, or allowed attempts have run out.
    while (current_letter < len(word_to_guess)) and (attempts_remaining > 0):
        guess = input("Guess a letter: ")  # Get user's guess
        print()

        # Check user's guess against the word
        if check_guess(guess, word_to_guess, current_letter):
            # Guess is correct.
            current_letter += 1  # Update current letter
            incorrect_guesses = set()  # Reset incorrect guesses
            print("CORRECT!")  # Print success message for user
        else:
            # Guess was wrong
            attempts_remaining -= 1  # Reduce attempts remaining.
            incorrect_guesses.add(guess.lower())  # Log the incorrect guess
            print(f"WRONG. {attempts_remaining} attempts remaining.")  # Diplay failure message
        
        # Display current word progress, and any incorrect guesses made for current letter 
        print(f"\nWord: {word_to_guess[:current_letter]}{\
            "".join(["_" for _ in range(len(word_to_guess) - current_letter)])}")
        print(f"Incorrect Guesses: {", ".join(incorrect_guesses)}\n")

    # Display whether player won or lost the game.
    if current_letter == len(word_to_guess):
        print("Congratulations! You won!")
    else:
        print("You lost... Better luck next time.")

if __name__ == "__main__":
    game()  # Starts the game