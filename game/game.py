import random

def get_random_number(n):

    return random.randint(0, n)

def main():
    while True:
        try:
            level_number = int(input("LEVEL: "))
            if level_number <= 0:
                continue
            result = get_random_number(level_number)
            break
        except ValueError:
           pass
    while True:
        try:
            guess_number = int(input("GUESS: "))
            if guess_number == result:
                print("Just Right!")
                break
            elif guess_number < result:
                print("Too Small!")
            else:
                print("Too Large!")
        except ValueError:
            print("Invalid guess. Please enter a valid integer.")

if __name__ == "__main__":
    main()
