import random
print("I'm thinking of a number between 1-100.")
print("Can you guess the number?")

num = random.randint(1,100)
guess = 0
attempts = 0
while guess!=num :
    guess = int(input("Enter your guess = "))
    attempts+=1
    if (guess>num):
        print("Too high")
    elif (guess<num):
        print("Too low")

if (guess==num):
    print(f"Congratulations, you got it. The number was = {num}")
print(f"It took you {attempts} attempts.")
    

