import random

answer = random.randint(1,100)
guesses = [0]
print(answer)

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
        if abs(guesses[-1] - answer) < abs(guesses[-2] - answer):
            print('Your getting WARMER!')

        else:
            print('Your getting COLDER!')

    elif abs(guess - answer) < 10:
        print('You are WARM!')

    else:
        print('You are COLD!')
    pass
