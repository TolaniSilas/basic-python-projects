# The pizza homepage Project.

"""
An interactive Tkinter application to verify age and display corresponding information.

This application prompts the user to enter their age, then displays relevant information
based on the entered age category using labels and buttons.

Widgets Used:
- tk.Label: Displays instructions and output messages.
- tk.Entry: Accepts user input for age.
- tk.Button: Triggers actions based on user input.

Instructions:
1. Enter the customer's age in the provided Entry widget.
2. Click the button to check and display information based on the age category.

Note:
- For ages under 4, the displayed information indicates a specific price.
- For ages between 4 and 18, another price is displayed.
- For ages between 18 and 65, a different price is shown.
- Ages 65 and over also display a specific price. 
"""


import tkinter as tk

def pizza_price():
    """
    Calculate and display the price of a pizza based on the customer's age.

    This function retrieves the age entered by the user from the Age_entry widget,
    determines the price based on age categories, and updates the price_label accordingly.
    """
    age_entry = int(Age_entry.get())
    
    if age_entry < 4:
        price_label.config(text="The price of the pizza is $2.")
    elif age_entry < 18:
        price_label.config(text="The price of the pizza is $5.")
    elif age_entry < 65:
        price_label.config(text="The price of the pizza is $10.")
    else:
        price_label.config(text="The price of the pizza is $2.")


# Create the main window.
window = tk.Tk()
window.title("Home | Pepperazi")  # Set the title of the window

# Create labels and entry widget.
instruction_label = tk.Label(window, text="Enter customer's age:", font=("Arial", 20, "bold"))
Age_entry = tk.Entry(window)
price_label = tk.Label(window)

# Create the button widget.
button = tk.Button(window, text="Check price of the pizza", fg="blue", command=pizza_price)

# Position the widgets using the pack layout manager.
instruction_label.pack()
Age_entry.pack()
button.pack()
price_label.pack()

# Run the Tkinter event loop.
window.mainloop()
