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

#Write your code below this line 👇

user_choice= int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))



if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
elif user_choice ==2:
  print(scissors)

computer_choise=random.randint(0,2)
if computer_choise == 0:
  print(rock)
elif computer_choise == 1:
  print(paper)
elif computer_choise ==2:
  print(scissors)



#decide who win, lost or if its a draw:

if(user_choice == computer_choise):
  print("Draw")
elif user_choice == 0 and computer_choise == 1:
  print("You lose")
elif  user_choice == 0 and computer_choise == 2:
  print("You win")
elif  user_choice == 1 and computer_choise == 0:
  print("You win")
elif  user_choice == 1 and computer_choise == 2:
  print("You lose")
elif  user_choice == 2 and computer_choise == 0:
  print("You lose")
elif  user_choice == 2 and computer_choise == 1:
  print("You win")
else:
  print("you typed an invalid number , you lose!!")
 





