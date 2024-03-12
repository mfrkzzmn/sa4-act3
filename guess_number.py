number = 10

while True:
    print("I'm thinking of a number...")
    guess = input("What number am I thinking of? ")
    upper_bound = 15
    lower_bound = 5

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
                if num > upper_bound:
                    print("Sorry! the number is too high.")
                elif num < lower_bound:
                    print("Sorry! The number is too low.") 
                else:
                    print("Sorry! Try again.")
        except:
            print("Enter a number or q.")