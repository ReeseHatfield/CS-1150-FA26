

numStudents = input("How many students? ")


numStudents = int(numStudents)

# for(int i = 0; i < numStudents; i++)

for i in range(numStudents):

    name = input("What is the name?: ")
    percent = input("What is your percent?: ")
    percent = int(percent)
    
    # var grade
    # grade
    if percent >= 90:
        grade = "A"
    # else if
    elif percent >= 80:
        grade = "B"
    elif percent >= 70:
        grade = "C"
    elif percent >= 60:
        grade = "D"
    else:
        grade = "F"

    if name == "Reese" or name == "Andrew":
        print("Grade was: A")
    else:
        print("Grade was: " + grade)
    
