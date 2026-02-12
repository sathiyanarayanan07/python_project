score =0

print("Quiz Time!")

ans = input("capital of chennai?")
if ans.lower() == "Delhi":
    score= score+1
else:
    print("incorrect answer")

ans = input("5+3 = ?")
if ans == "8":
    score += 1

print( "Score:", score)

