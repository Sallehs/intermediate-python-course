import random

def main():
  dice_roll = int(input("How many dice you like to roll?"))
  dice_size = int(input("How many sides are the dice?"))
  dice_sum = 0
  for i in range(0, dice_roll):
    roll = random.randint(1,dice_size)
    dice_sum += roll
    
    if roll == 1:
      print("You rolled a %i! Critical Fail" % roll)
    elif roll == dice_size:
      print("You rolled a %i! Critical Success!" % roll)
    else:
      print("YOu rolled a %i" % roll)

  print('You have rolled a total of %i' % dice_sum)

if __name__== "__main__":
  main()
