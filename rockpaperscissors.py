import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        # Label for instructions
        instructions_label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors:")
        instructions_label.pack(pady=10)

        # Buttons for user choices
        rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play_round("Rock"))
        rock_button.pack(side=tk.LEFT, padx=10)

        paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play_round("Paper"))
        paper_button.pack(side=tk.LEFT, padx=10)

        scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play_round("Scissors"))
        scissors_button.pack(side=tk.LEFT, padx=10)

        # Label for displaying result
        self.result_var = tk.StringVar()
        result_label = tk.Label(self.root, textvariable=self.result_var)
        result_label.pack(pady=20)

        # Label for displaying scores
        self.score_var = tk.StringVar()
        score_label = tk.Label(self.root, textvariable=self.score_var, font=('Helvetica', 12, 'bold'))
        score_label.pack(pady=10)

    def play_round(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        result = self.determine_winner(user_choice, computer_choice)

        # Display the result
        self.result_var.set(f"Result: You chose {user_choice}. Computer chose {computer_choice}. {result}")

        # Update scores
        if result == "You win!":
            self.user_score += 1
        elif result == "You lose!":
            self.computer_score += 1

        # Update the score display
        self.update_score_display()

        # Ask if the user wants to play again
        self.ask_play_again()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Scissors" and computer_choice == "Paper") or
            (user_choice == "Paper" and computer_choice == "Rock")
        ):
            return "You win!"
        else:
            return "You lose!"

    def update_score_display(self):
        self.score_var.set(f"Score: You {self.user_score} - {self.computer_score} Computer")

    def ask_play_again(self):
        play_again = messagebox.askyesno("Play Again?", "Do you want to play another round?")
        if play_again:
            self.result_var.set("")
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
