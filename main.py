from art import logo
from replit import clear
import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

#Make function to set difficulty.
def check_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

  if difficulty == "easy":
    attempts = 10
    return EASY_LEVEL_ATTEMPTS

  elif difficulty == "hard":
    attempts = 5
    return HARD_LEVEL_ATTEMPTS

#Function to check user's guess against actual answer.

def check_guess(guess,answer,attempts):

  """ Checks user's guess against actual answer."""

  if guess > answer:
    print("Your guess is higher than answer. Try again. 🤔")
    return attempts - 1
  elif guess < answer:
    print("Your guess is lower than answer. Try again. 🤔")
    return attempts -1
  else:
    print(f"Congratulations!! The answer is {answer}. 😃😃")


#Function starts to game and compare user's guess between answer
def play_game():
  
  print(logo)
  print("Welcome to Number Guess Game..")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1,100)
  #Testing code 
  #print(f"Psst, the answer is {answer} actually. ")

  attempts = check_difficulty()
  guess = 0
  while guess != answer:

    print(f"You have {attempts} attempts remaining to guess the number.")

    #Get user's guess here.
    guess = int(input("Make a guess: "))

    attempts = check_guess(guess,answer,attempts)

    if attempts == 0:
      clear()
      print(f"You lost. 🙁 There's {attempts} attempts left. \n The number was {answer}.")
      return
    

# Starting game 
while input("Press enter for start the game.") == "":
  clear()
  play_game()

    
