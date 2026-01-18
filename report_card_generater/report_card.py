print('welcome to the Report card generator program\n')

student_name= input("enter student's name:")
student_class =input("enter student's class:")

subject = ['maths','science','English','Computer']

marks ={}

for item in subject:
    score = int(input(f"enter marks for {item}:"))
    marks[item] = score

    total_marks = sum(marks.values())
   # average = total_marks / 4
    average = total_marks / len(subject)


#assign grades basing on average

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "c"
else:
    grade = "F"

# Dispaly the report card

print("\nReport Card")
print(f"name:{student_name}")
print(f"class: {student_class}")
print("Subject marks:")

for item,score in marks.items():
    print(f"{item}:{score}")

print(f"\nTotal Marks:{total_marks}")
print(f"Average {average:2f}")
print(f"Grade: {grade}")

#Comments
if grade in ["A","B"]:
    print("Excellent")
elif grade in("c"):
    print("Good")
else:
    print("fail")
