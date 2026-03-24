secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))
    
    if guess == secret:
        print("You win!")
    else:
        print("Try again!")
