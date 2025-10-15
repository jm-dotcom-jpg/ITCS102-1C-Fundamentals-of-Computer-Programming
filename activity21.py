import random

print("Guess a Number")
print("---------------------")

random_value = random.randint(1,50)
tries = 0
guess = True


name = input("What's your name?-->")
while guess == True:
    number = eval(input("Guess a number from 1 - 5-->"))
    tries += 1

    if number == random_value:
        print("You Win!")
        break
    else:
        print("Please Guess again.")
        continue

print(f"Hi {name},Congratulations, your guess is correct!, Number of tries {tries}")
