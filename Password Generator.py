import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    # Define different types of character sets
    Lcase = string.ascii_lowercase
    Ucase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation  # includes symbols like !@#$%^&*()

    # Combine all character sets
    all = Lcase + Ucase + digits + special

    # Generate password by randomly selecting characters from all
    password = ''.join(random.choice(all) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length should be greater than zero.")
            return
        
        password = generate_password(length)
        label_result.config(text=f"Your new password is: {password}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry('300x300')

heading=tk.Label(window,text='Password Generator', font=('Times New Roman',20))
heading.pack(pady=10)
# Create a label and entry for password length
label_length = tk.Label(window, text="Enter desired password length:")
label_length.pack(pady=10)

entry_length = tk.Entry(window)
entry_length.pack(pady=5)

# Create a button to generate the password
button_generate = tk.Button(window, text="Generate Password", command=on_generate)
button_generate.pack(pady=10)

# Create a label to display the generated password
label_result = tk.Label(window, text="")
label_result.pack(pady=10)

# Start the GUI event loop
window.mainloop()

