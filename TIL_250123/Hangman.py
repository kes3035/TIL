## 250123 Today I Learned

import time

userName = input("What is your name?")
print("Welcome!! " + userName + ". Let's play hangman game!")

print()

time.sleep(1)

print("Start Loading...")
print()
time.sleep(0.5)

# 정답 단어
answerWord = "turtle"

guesses = ''

turns = 10

## 핵심 루프
while turns > 0:
    failed = 0

    for char in answerWord:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
            failed += 1

    if failed == 0:
        print()
        print()
        print('Wow..Correct!!')
        break
    print()

    print()
    guess = input("Guess a character.")
    guesses += guess

    if guess not in answerWord:
        turns -= 1
        print("Oops! You are wrong..")

        print("You have ", turns, " more guesses!")

        if turns == 0:
            print("You have failed Hangman Game..Bye!")

                








