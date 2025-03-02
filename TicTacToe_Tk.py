import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.configure(bg='#F4C2C2')  # Baby Pink Background

# Global variables
current_player = "X"
winner = False
buttons = []

def check_winner():
    global winner
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    
    for combo in win_patterns:
        if buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text'] != "":
            for index in combo:
                buttons[index].config(bg="#FFD700")  # Glowy Golden Color for Winner
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            return
    
    # Check for a tie
    if all(button['text'] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a Tie!")
        winner = True

def button_click(index):
    global current_player, winner
    
    if buttons[index]['text'] == "" and not winner:
        buttons[index]['text'] = current_player
        buttons[index].config(fg="black", font=("Arial", 24, "bold"))
        check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s Turn")

def reset_game():
    global current_player, winner
    current_player = "X"
    winner = False
    for button in buttons:
        button.config(text="", bg="#ADD8E6")  # Baby Blue Reset Color
    label.config(text=f"Player {current_player}'s Turn")

# Create label
label = tk.Label(root, text=f"Player {current_player}'s Turn", font=("Arial", 18, "bold"), bg='#F4C2C2')
label.grid(row=0, column=0, columnspan=3, pady=10)

# Create buttons
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, bg="#ADD8E6", activebackground="#FFB6C1", relief="raised", bd=5, command=lambda i=i: button_click(i))
    btn.grid(row=1 + i // 3, column=i % 3, padx=5, pady=5)
    buttons.append(btn)

# Restart button
reset_btn = tk.Button(root, text="Restart Game", font=("Arial", 14, "bold"), bg="#FF69B4", fg="white", relief="ridge", bd=3, command=reset_game)
reset_btn.grid(row=4, column=0, columnspan=3, pady=10)

# Run the main loop
root.mainloop()
