
'''
Build a number guessing game where there is a target number the user must find it,
when the user enter a number, you must indicate if the desired one is less or more than the input,
the user has 10 attempts, if he did not find the number within those attempts,
he loses, if he finds it he wins, you should put that in a function. Note: you can use the library random 
to generate the target number or you can simply put it manually in your code.
'''


import random

def main():

    x = rand_difficulty()
    tries = 10
    try:
        guess = int(input(f"Guess the random number you have {tries} left: "))
    except: 
        print("Please, just use numbers")
        exit(1)
        
    while (not true_false(x, guess)):
        tries -= 1
        if tries == 0:
            print("Game over. No more tries left!")
            return 
        print(f"{tries} left ")
        try:
             guess = int(input("Try again: "))
        except:
            print("Please, just use numbers")
            exit(1)

def true_false(x, input):
    if x == input:
        print(f"Congrats! The answer was {x} !")
        return True
    elif x<input:
        print("Too high ! Try again")
    else:
        print("Too low! Try again")

    return False

def rand_difficulty():
    diff = input("Choose the difficulty 1-easy / 2-medium / 3-hard: ")
    if diff == '2':
        return random.randint(1, 100)
    elif diff == '3':
        return random.randint(1, 1000)
    else:
        return random.randint(1, 10)
    
if __name__ == '__main__':
    main()
