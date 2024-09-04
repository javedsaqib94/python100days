
import random


######### ROCK PAPER SCISSOR GAME ###############

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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


get_choice = [rock, paper, scissor]

# print(get_choice[0])
# print(get_choice[1])
# print(get_choice[2])

print('Welcome to "Rock" , "paper" and "Scissor" game !!! ')

get_input = input ("Select your Choice = ")

comp_input = random.choice(get_choice)

if ( get_input == "Rock" or get_input == "rock" ):
    print("true")
    print(f"Your choice is : {get_choice[0]}")
    print(f"computer choice: {comp_input}")
    if comp_input == get_choice[0]:
        print("Drawn !!! Please re-run the program!! ")
    elif comp_input == get_choice[1]:
        print("Computer wins the Game !!! Better Luck next time !!! ")
    elif comp_input == get_choice[2]:
        print("YOU win !!! Hurray !!! ")
    else:
        print("Your choice is not correct !!! ")

elif  ( get_input == "Paper" or get_input == "paper"):
    print("insdie next else if statement")
    print(f"Your choice is : {get_choice[1]}")
    print(f"computer choice: {comp_input}")
    if comp_input == get_choice[0]:
        print("YOU win !!! Hurray !!! ")
    elif comp_input == get_choice[1]:
        print("Drawn !!! Please re-run the program!! ")
    elif comp_input == get_choice[2]:
        print("Computer wins the Game !!! Better Luck next time !!! ")
    else:
        print("Your choice is not correct !!! ")  

elif  (get_input == "Scissor" or get_input == "scissor"):
    print(f"Your choice is : {get_choice[2]}")
    print(f"computer choice: {comp_input}")
    if comp_input == get_choice[0]:
        print("Computer wins the Game !!! Better Luck next time !!! ")
    elif comp_input == get_choice[1]:
        print("YOU win !!! Hurray !!! ")
    elif comp_input == get_choice[2]:
        print("Drawn !!! Please re-run the program!! ")
    else:
        print("Your choice is not correct !!! ")   

else:
    print("your choice is not valid, please try again later.")