import random

answer = random.randint(1,100)
guesses = [0]

print("--Guessing Game Challenge--")
print("Think you can win??")
print("Try and guess my random number between 1 and 100...")

while True:
    guess = int(input("I'm thinking of a number between 1 and 100: "))

    if guess < 1 or guess > 100:
        print("your guess must be between 1 and 100")
        continue

    if guess == answer:
        print("CORRECT!!!")
        break

    guesses.append(guess)

    if guesses[-2]:

        #TODO: warmer
        #TODO: colder

    #TODO: Warm
    #TODO: Cold

    pass
