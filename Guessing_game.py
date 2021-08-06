# A random guessing game with python
from random import randint
import sys  # the import sys module will help us quit the program if the user guess an invalid number
try:
    num = int(input("Enter guessing range: "))
    flag = int(input("How many time do you want to guess ? : "))
except ValueError:
    sys.exit  # Exit the program if the user used an invalid number


count = 1  # To count the total number of guess
while True:
    try:
        answer = randint(1, num)
        if count > flag:
            print(f"You\'ve guessed {flag} times without the correct answer")
            break
        print("Lets play")
        guess = int(
            input(f'Guess a number from 1 to {num}, this is your {count} guess  : '))
        if guess > 0 and guess < num:
            if guess == answer:
                print(
                    f" the correct number is {answer} and your guess is {guess} which is Correct and and this took you {count} try to get the correct answer")
                break
            else:
                print(
                    f"The Correct answer is {answer} and you guesed {guess} which is wrong")
                count += 1
                continue
        else:
            print('Number is out of range')
            continue
    except:
        print("The number you entered is invalid ")
        break
#  in the future try and improve the code, by putting how many times the user guessed, and if the user guess the
# correct answer once it should be you guess the correct answer 1time, instead of 1times

# This code can still be improved, remember this is your first project with python
