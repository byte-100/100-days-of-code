
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

image=[rock,paper,scissors]

user = int(input("What do you choose? Rock = 0, Paper = 1 or Scissors = 2.\n"))

if user < 0 or user > 2:
    print("Invalid choice! You must choose 0, 1, or 2.")
else:
    # Show user choice
    print(f"You chose:")
    print(image[user])


computer_choice = random.randint(0, 2)
print("Computer chose:")
print(image[computer_choice])


if computer_choice == user:
    print("draw")
elif computer_choice == "scissors" and user == "paper":
    print("cpu wins ")
elif computer_choice == "paper" and user == "rock" :
    print("cpu wins ")
elif computer_choice == "rock" and user == "scissors":
    print("cpu wins ")
else:
    print("user wins")
