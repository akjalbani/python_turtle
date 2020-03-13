#simple demo to test while loop
import random

number = random.randint(1, 25) # generate random value between 1 and 25
number_of_guesses = 0  

while number_of_guesses < 5:  # check the no .of attempts
  print('Guess a number between 1 and 25:')
  guess = int(input())
  if guess == number:
    print("Correct guess ")
    break
  else:
    print("Sorry!! Try again later")
    print("-------------------------")
    number_of_guesses = number_of_guesses + 1

