number = 10
limit = 5

print(f"You can try {limit} times to guess a number.")

while True:
    print("I'm thinking of a number...")
    guess = input("What number am I thinking of? ")

    limit = limit - 1

    if (limit <= 0):
        print("You have reached your limit to attempt for a guessed number.")
        break

    if guess == 'q':
        print(f"The correct number was {number}.")
        break
    else:
        try:
            num = int(guess)
            if num == number:
                print("Congratulations! You guessed the right number.")
                break
            else:
                print("Sorry! Try again.")
                print(f"You have {limit} attempt(s) left.")
        except:
            print("Enter a number or q.")