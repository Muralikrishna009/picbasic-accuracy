"""
Hangman Game
Converted from PICBASIC to Python
"""

import os
import random


def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def initialize_game():
    """Initialize game variables"""
    global word_list, attempted_letters, wrong_guesses, correct_guesses
    global max_guesses, mystery_word
    
    clear_screen()
    
    word_list = [
        'COMPLY', 'THREE', 'VACATION', 'INFORMATION', 'TECHNOLOGY',
        'ORLANDO', 'COMPUTER', 'ROUTER', 'PRINTER', 'BUDGE',
        'SOFTWARE', 'HARDWARE', 'OBJECTIVE', 'FILE', 'EMPLOYEE',
        'SECURITY', 'DATA', 'REPORT', 'PROPERTY', 'OWNERSHIP'
    ]
    
    attempted_letters = []
    wrong_guesses = 0
    correct_guesses = 0
    max_guesses = 7
    
    # Select random word
    word_count = len(word_list)
    word_index = random.randint(0, word_count - 1)
    mystery_word = word_list[word_index]


def show_game_screen():
    """Display the game screen"""
    print("Welcome to Hangman! You have seven attempts to uncover the mystery word.")
    print("_" * len(mystery_word))
    print("Guess a letter  : ")
    print("Attempted letters: ")


def get_letter_input():
    """Get user letter input"""
    while True:
        print(" " * 100, end="\r")
        player_letter = input("Enter a letter: ").strip()
        print(" " * 50)
        
        if len(player_letter) > 1:
            print(f"'{player_letter}' has more than one character.")
            continue
        
        player_letter = player_letter.upper()
        if not player_letter.isalpha():
            print(f"'{player_letter}' is not a valid letter.")
            continue
        
        if player_letter in attempted_letters:
            print(f"{player_letter} was already guessed.")
            continue
        
        attempted_letters.append(player_letter)
        print("Attempted letters:", " ".join(attempted_letters))
        return player_letter


def process_letter(letter):
    """Process the guessed letter"""
    global wrong_guesses, correct_guesses
    
    # Check if letter exists in mystery word
    position = mystery_word.find(letter)
    
    if position >= 0:
        # Display the letter at its position(s)
        print_word = list("_" * len(mystery_word))
        for i, char in enumerate(mystery_word):
            if char == letter or mystery_word[i] in attempted_letters:
                print_word[i] = char
        
        print("".join(print_word))
        
        # Count correct guesses
        correct_guesses += mystery_word.count(letter)
        
    else:
        wrong_guesses += 1
        draw_hangman()
        remaining_guess = max_guesses - wrong_guesses
        print(f"{letter} is incorrect. Remaining attempts: {remaining_guess}")


def draw_hangman():
    """Draw hangman display based on wrong guesses"""
    # Draw the gallows first time
    if wrong_guesses == 1:
        print("  _______")
        print("  |     |")
        print("  |     |")
        print("  |     |")
        print("  |     |")
        print("  |     |")
        print(" _|_____|_")
    
    # Add body parts based on wrong guesses
    if wrong_guesses == 1:
        print("  O", end="", flush=True)  # Head
    elif wrong_guesses == 2:
        print("  |", end="", flush=True)  # Body
    elif wrong_guesses == 3:
        print(" /", end="", flush=True)   # Left arm
    elif wrong_guesses == 4:
        print(" \\", end="", flush=True)  # Right arm
    elif wrong_guesses == 5:
        print("  |", end="", flush=True)  # Lower body
    elif wrong_guesses == 6:
        print(" /", end="", flush=True)   # Left leg
    elif wrong_guesses == 7:
        print(" \\", end="", flush=True)  # Right leg (Game Over)


def game_loop():
    """Main game loop"""
    global mystery_word
    
    while wrong_guesses < max_guesses and correct_guesses < len(mystery_word):
        letter = get_letter_input()
        process_letter(letter)


# Main program
initialize_game()
show_game_screen()
game_loop()

# Display final result
if wrong_guesses == max_guesses:
    print(f"Sorry, you ran out of attempts.")
    print(f"The mystery word was '{mystery_word}'")
else:
    print(f"Congratulations! You found the word!")