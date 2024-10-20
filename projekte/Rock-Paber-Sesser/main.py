import random 
# make a list of the play options
options = ["Rock", "Peber", "Seser"]
# get the user input
user_chosse = input("Enter your chosse (Rock, Peber, Seser): ").title()
# let the combuter chooes 
chosse = random.choice(options)

print(chosse)
# til the winer this he win
if user_chosse == chosse:
  print("No bady win!!")

elif (user_chosse == "Rock") and (chosse == "Peber"):
  print("You lost (^_^)")

elif (user_chosse == "Peber") and (chosse == "Seser"):
  print("You lost (^_^)")

elif (user_chosse == "Seser") and (chosse == "Rock"):
  print("You lost (^_^)")

else:
  print("You win(^~^)")

