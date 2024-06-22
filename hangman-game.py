# Hangman Game Project.

import random

def Hangman():
    """
    Play a simple Hangman game where the player guesses letters of a randomly chosen word from a list.
    
    The game provides feedback on correct and incorrect guesses, displays the current state of the guessed word,
    and ends when the player correctly guesses the word or runs out of tries.
    """
    # List of words for the game.
    words = ["apple", "orange", "banana", "lemon", "pear", "mango", "strawberry"]
    
    # Select a random word from the list.
    word = random.choice(words)
    
    # List to store guessed letters.
    guessed_letters = []
    
    # Number of tries allowed.
    tries = 5
    
    # Main game loop.casefold()
    while tries > 0:
        guessed_word = ""
        
        # Build the word with guessed letters and placeholders.
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"
       
        # Print the current state of the guessed word.
        print("Word:", guessed_word) 
        
        # Check if the player has guessed the entire word correctly.
        if guessed_word == word:
            print("Congratulations! You guessed the word right. The correct word is", word.title() + ".")
            break

        # Display number of tries left.
        print("You have", tries, "tries left.\n")
        
        # Prompt the player to enter a guess.
        Guess = input("Enter a guess: ").lower()

        # Check if the guess has already been guessed.
        if Guess in guessed_letters:
            print("You already guessed that letter")      
    
        # Check if the guess is correct and update guessed_letters.
        elif Guess in word:
            print("Correct guess!")
            guessed_letters.append(Guess)
        
        # Incorrect guess, decrement tries and update guessed_letters.
        else:
            print('Wrong guess!')
            tries -= 1
            guessed_letters.append(Guess)
    
        # Player runs out of tries.
        if tries == 0:
            print("Sorry you lost!", end=" ")
            print("The word was", word + ".")



# Start the Hangman game when the script is executed.
if __name__ == "__main__":
    Hangman()


