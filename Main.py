#Rock-Paper-Scissors game
import random

#default score for both players
user_wins = 0
computer_wins =0

#declaring the variables and values to the player
print("R represents rock")
print("P represents paper")
print("S represents scissors")
print()
#A list of options for selection
options = ["R","P", "S"]

#while loop for the rock-paper-scissors game
while True:
      user_input = input("Pick an option among R, P, S: ")
      print()
      if user_input not in options:
          print("Error, try again")
          continue
     #intructing the computer to pick any option from random
      random_number = random.choice(options)
      computer_pick = random_number
      print("Player", user_input + ".", "Computer", computer_pick + ".")

    #comparing the options of the computer and the player
      if user_input == "R" and computer_pick == "S":
          print("You won!")
          user_wins+=1
          print("Player",user_wins ,":" ,"Computer",computer_wins)
      elif user_input == "P" and computer_pick == "R":
          print("You won!")
          user_wins+=1
          print("Player", user_wins,":", "Computer", computer_wins)
      elif user_input == "S" and computer_pick == "P":
          print("You won!")
          user_wins+=1
          print("Player",user_wins,":" ,"Computer",computer_wins) 
      elif user_input == "S" and computer_pick == "S":
          print("It's a tie")
          print("Player",user_wins,":" ,"Computer",computer_wins) 
      elif user_input == "R" and computer_pick == "R":
          print("It's a tie")
          print("Player",user_wins,":" ,"Computer",computer_wins) 
      elif user_input == "P" and computer_pick == "P":
          print("It's a tie")
          print("Player",user_wins,":" ,"Computer",computer_wins) 
      else:
          print("Ooops, You loss")
          computer_wins+=1
          print("Player",user_wins ,":" ,"Computer",computer_wins)
      if computer_wins == 3:
          print("Computer Win!")
          print("Game over")
          break
      elif user_wins == 3:
          print("You Win ")
          break
      else:
          print("continue playing")
          continue
    