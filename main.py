import random
numbers = random.randint(1, 99)

while True:
  try:
    guess = int(input("Guess the number (1 - 99): "))
    if numbers != guess:
      print('Incorrect! Try Again')
      match guess > numbers:
        case True:
          print("Hint: Your Guess is Too High")
          print('——————————')
        case False:
          print("Hint: Your Guess is Too Low")
          print('——————————')
    else:
      print('Correct Guess! Congrats You beat AI')
      break

  except ValueError:
    print("Please Enter Number Only")
