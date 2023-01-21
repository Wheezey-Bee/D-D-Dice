import random

def dice_roll(dice_type):
  if dice_type == 'd4':
    d4_call = random.randint(1,4)
    print('You have rolled a ' +str(d4_call)+ ' on the d4.')
  elif dice_type == 'd6':
    d6_call = random.randint(1,6)
    print('You have rolled a ' +str(d6_call) +' on the d6.')
  elif dice_type == 'd8':
    d8_call = random.randint(1,8)
    print('You have rolled a ' +str(d8_call)+ ' on the d8.')
  elif dice_type == 'd10':
    d10_call = random.randint(1,10)
    print('You have rolled a ' +str(d10_call)+ ' on the d10.')
  elif dice_type == 'd12':
    d12_call = random.randint(1,12)
    print('You have rolled a ' +str(d12_call)+ ' on the d12.')
  elif dice_type == 'd20':
    d20_call = random.randint(1,20)
    print('You have rolled a ' +str(d20_call)+ ' on the d20.')
  elif dice_type == 'd100':
    d100_call = random.choice([00,10,20,30,40,50,60,70,80,90])
    print('You have rolled a ' +str(d100_call)+ ' on the d100.')
  else:
    print('Invalid Dice. Please check you have entered the right dice :)')
      
def backup_dice():
  question = input("Would you like to roll a dice?")
  if question == "yes":
    dice = input('What dice would you like to roll?')
    dice_type = str(dice)
    dice_roll(dice_type)
    backup_dice()
  elif question == "no":
    print("Thank you for using my code. See you again soon!")
  else:
    print("Please answer yes or no.")
    backup_dice()

backup_dice()