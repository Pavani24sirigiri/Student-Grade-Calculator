
subjects = int(input("Enter number of subjects: "))
total = 0
for i in range(1, subjects + 1):
    marks = int(input(f"Enter marks for subject {i}: "))
    total += marks
average = total / subjects
if average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("\n----- Student Result -----")
print("Total Marks :", total)
print("Average     :", average)
print("Grade       :", grade)