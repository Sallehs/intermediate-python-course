import random

def main():
  dice_roll = 2
  dice_sum = 0
  for i in range(0, dice_roll):
    roll = random.randint(1,6)
    print('You rolled a %i' % roll)
    dice_sum += roll

  print('You have rolled a total of %i' % dice_sum)

if __name__== "__main__":
  main()
