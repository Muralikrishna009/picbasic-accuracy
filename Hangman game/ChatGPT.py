import random

# Initialize game variables
word_list = [
    'COMPLY', 'THREE', 'VACATION', 'INFORMATION', 'TECHNOLOGY',
    'ORLANDO', 'COMPUTER', 'ROUTER', 'PRINTER', 'BUDGE',
    'SOFTWARE', 'HARDWARE', 'OBJECTIVE', 'FILE', 'EMPLOYEE',
    'SECURITY', 'DATA', 'REPORT', 'PROPERTY', 'OWNERSHIP'
]

max_guesses = 7
attempted_letters = []
wrong_guesses = 0
correct_guesses = 0

# Select a mystery word
mystery_word = random.choice(word_list)
display_word = ['_' for _ in mystery_word]

# Function to display the game screen
def show_game_screen():
    print("\nWelcome to Hangman! You have seven attempts to uncover the mystery word.")
    print(' '.join(display_word))
    print("Attempted letters: " + ' '.join(attempted_letters))

# Function to get a valid letter input from the user
def get_letter_input():
    while True:
        player_letter = input("Guess a letter: ").strip().upper()
        if len(player_letter) != 1 or not player_letter.isalpha():
            print("Please enter a single alphabetic character.")
        elif player_letter in attempted_letters:
            print(f"You have already guessed '{player_letter}'. Try another letter.")
        else:
            attempted_letters.append(player_letter)
            return player_letter

# Function to process the player's guess
def process_letter(player_letter):
    global wrong_guesses, correct_guesses
    if player_letter in mystery_word:
        for idx, char in enumerate(mystery_word):
            if char == player_letter:
                display_word[idx] = player_letter
                correct_guesses += 1
        print(f"Good job! '{player_letter}' is in the word.")
    else:
        wrong_guesses += 1
        print(f"Sorry, '{player_letter}' is not in the word. Remaining attempts: {max_guesses - wrong_guesses}")

# Main game loop
def game_loop():
    global wrong_guesses, correct_guesses
    while wrong_guesses < max_guesses and correct_guesses < len(mystery_word):
        show_game_screen()
        player_letter = get_letter_input()
        process_letter(player_letter)

    # Game result
    if correct_guesses == len(mystery_word):
        print(f"\nCongratulations! You found the word: {mystery_word}")
    else:
        print(f"\nSorry, you ran out of attempts. The mystery word was '{mystery_word}'.")

# Start the game
game_loop()
