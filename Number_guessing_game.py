import random
score =0

number =  random.randint( 1, 100)

while True:
    guess = int(input("guess number (1 -100):"))
    if guess == number:
        print("correct")
        score =score+2
        print("Score:",score)
        break
    elif guess < number:
        print("to low")
    else:
        print("too high")