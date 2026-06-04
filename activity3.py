import random #importing module
playing =True #initialise
number = str(random.randint(0,10))

print("i will generate a number from a number from 0 to 10 and you have to guess the number one digit at a time.")
print("the game ends when you get 1 hero")

while playing:
    guess = input("give me your best guess! \n")
    if number == guess:
        print("you win the game")
        print("the number was",number)
        break

    else:
        print("your guess isn't quite right, try again\n")