from art import logo
import random
print(logo)
print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty= input("choose the difficulty. Type 'easy' or'hard': ")
if difficulty == "easy":
  attempts = 10
else:
  attempts=5
print(f"you have {attempts} attempts remaining to guess the number.")
ideal_num= random.randint(1,100)
for i in range(attempts):
  print("\n") 
  guess=int(input("Make a guess: "))
  if guess > ideal_num:
    print("Too high")
    print("Guess again")
  elif guess < ideal_num:
    print("Too low")
    print("Guess again")
  else:
    print(f"You got it! The answer was {ideal_num}")
    break