import random

jackpot = random.randint(1,1000)

guess = int(input('Guess the number :'))
counter = 1

while guess != jackpot:
    if guess<jackpot:
        print("Wrong number !!! Guess higher")
    else:
        print("Wrong number !!! Guess lower")
    guess = int(input('Guess the number :'))
    counter += 1
else:
    print("Hurray!!! You've done it")
    print("Attempts",counter)