import random
print("Welcome to the Number Guessing Game!\nTry to guess the number between 1 and 100")
r = random.randrange(1,100)
n = -1
k=0
while r != n:
    try:
            
        n = int(input("Enter your guess:"))
        if n < r:
            print("Too low!")
        elif n > r :
            print("Too high")
        else:
            print(f"Congratulation! You've guessed in {k} attempts.")
        k +=1
    except ValueError:
        print("Invalid Input. Please Enter valid Input.")

    
