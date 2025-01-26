## 250123 Today I Learned

import time
import csv
import random
import winsound


userName = input("What is your name?")
print("Welcome!! " + userName + ". Let's play hangman game!")

print()

time.sleep(1)

print("Start Loading...")
print()
time.sleep(0.5)

# 정답 단어

words = []

with open('./resource/word_list.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for c in reader:
        words.append(c)

random.shuffle(words)

q = random.choice(words)

answerWord = q[0].strip()


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
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        print('Wow..Correct!!')
        break
    print()

    print()
    print('Hint : {}'.format(q[1].strip()))
    guess = input("Guess a character.")
    guesses += guess

    if guess not in answerWord:
        turns -= 1
        print("Oops! You are wrong..")

        print("You have ", turns, " more guesses!")

        if turns == 0:
            winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            print("You have failed Hangman Game..Bye!")

                








