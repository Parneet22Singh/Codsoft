import tkinter as tk
import random

def computer():
    #Generate a random choice for the computer
    return random.choice(['rock', 'paper', 'scissors'])

def winner(user, comp):
    #Determine the winner of the game
    if user == comp:
        return "It's a tie!"
    elif (user == 'rock' and comp == 'scissors') or \
         (user == 'scissors' and comp == 'paper') or \
         (user == 'paper' and comp == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play(user):
    #Main function to play the game
    comp = computer()
    result_text = winner(user, comp)

    result_label.config(text=f"Computer chose: {comp}\n{result_text}")

    # Update scores
    global uscore, cscore
    if result_text == "You win!":
        uscore += 1
    elif result_text == "You lose!":
        cscore += 1

    score_label.config(text=f"Score - You: {uscore}, Computer: {cscore}")

# Initialize scores
uscore = 0
cscore = 0

def reset_game():
    #Reset the game scores and result
    global uscore, cscore
    uscore = 0
    cscore = 0
    score_label.config(text="Score - You: 0, Computer: 0")
    result_label.config(text="")



# Set up the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors")

# Title Label
title_label = tk.Label(window, text="Rock-Paper-Scissors", font=("Times New Roman", 20))
title_label.pack(pady=10)

# Create buttons for user choices
rock_button = tk.Button(window, text="Rock", width=10, command=lambda: play('rock'))
rock_button.pack(pady=10)

paper_button = tk.Button(window, text="Paper", width=10, command=lambda: play('paper'))
paper_button.pack(pady=10)

scissors_button = tk.Button(window, text="Scissors", width=10, command=lambda: play('scissors'))
scissors_button.pack(pady=10)

# Add a Reset button
reset_button = tk.Button(window, text="Reset", width=10, command=reset_game)
reset_button.pack(pady=10)
# Result label
result_label = tk.Label(window, text="", font=("Calibri", 14))
result_label.pack(pady=15)

# Score label
score_label = tk.Label(window, text="Score - You: 0, Computer: 0", font=("Times New Roman", 14))
score_label.pack(pady=10)

# Run the main loop
window.mainloop()
