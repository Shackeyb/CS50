import random
import sys

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a positive integer.")

def main():
    level = get_positive_integer("Level: ")

    target = random.randint(1, level)
    
    while True:
        guess = get_positive_integer("Guess: ")

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()

if __name__ == "__main__":
    main()
