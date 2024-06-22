import random
import tkinter as tk

def GuessNumbers():
    """
    Function to handle the guess logic for the Guess the Number game.
    Generates a secret number between 1 and 30, compares it with user input,
    and updates the result label accordingly.
    """
    # Seed the random number generator (optional, for reproducibility)
    random.seed(2)
    
    # Generate a secret number between 1 and 30
    SecretNumber = random.randint(1, 30)
    
    # Get the user's guess from the entry widget
    GuessNumber = int(guess_entry.get())
    
    # Validate if the guessed number is within the range of 1 to 30
    if GuessNumber in range(1, 31):
        
        # Compare the user's guess with the secret number
        if GuessNumber < SecretNumber:
            result_label.config(text="Too low, Try Again!", fg="red")
            
        elif GuessNumber > SecretNumber:
            result_label.config(text="Too high, Try Again!", fg="red")
            
        elif GuessNumber == SecretNumber:
            result_label.config(text="Congratulations! You guessed it right!", fg="green")
            
    else:
        # Invalid guess outside the range of 1 to 30
        result_label.config(text="Invalid Number! Enter a number between 1 and 30.", fg="red")


# Create the main window
window = tk.Tk()
window.title("Guess a Number Game")

# Create labels, entry widget, and result label
instructions_label = tk.Label(window, text="Guess a number between 1 and 30:", font=("Arial", 16, "bold"))
guess_entry = tk.Entry(window)
result_label = tk.Label(window)

# Create a button to check the guess
check_button = tk.Button(window, text="Check", fg="blue", command=GuessNumbers)

# Position the widgets using the pack layout manager
instructions_label.pack()
guess_entry.pack()
check_button.pack()
result_label.pack()

# Start the tkinter main event loop to display the window
window.mainloop()
