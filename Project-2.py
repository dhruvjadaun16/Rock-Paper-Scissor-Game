# DESIGN A ROCK PAPER SCISSOR GAME IN PYTHON [TASK-2]
import random
user_choice=int(input("Enter the Choice: 0 for Rock, 1 for Paper, 2 for Scissor.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You entered invalid number, You Lose.")
else:
    computer_choice=random.randint(0,2)
    print("Computer_Chose:")
    print(computer_choice)
    if computer_choice == user_choice:
        print("It's a Draw.")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose.")
    elif user_choice == 0 and computer_choice == 2:
        print("You Win.")   
    elif computer_choice > user_choice:
        print("You Lose.")
    elif user_choice > computer_choice:
        print("You Win.")
    