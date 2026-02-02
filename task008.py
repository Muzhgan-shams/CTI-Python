# Rock Paper Scissors
import random
arts = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",  """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
choices = ["Rock", "Paper", "Scissors"]
print("Welcome to Rock, Paper and Scissors game! Let's play😃")
user = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors: "))
if user >= 0 and user <= 2:
    computer = random.randint(0, 2)
    print(f"Your choice: {arts[user]}")
    print(f"Computer choice: {arts[computer]}")

    if user == computer:
        print(f"{choices[user]} and {choices[computer]}\nIt is a draw 🤝")
    elif (user == 0 and computer == 2) or (user == 2 and computer == 1) or (user == 1 and computer == 0):
        print(f"{choices[user]} beats {choices[computer]}\nYou Win🏆🎉")
    else:
        print(f"{choices[computer]} beats {choices[user]}\nYou Lose❌😭")
else:
    print("Invalid choice. Please select 0, 1, or 2.")
