physics_marks = float(input("Enter marks obtained in Physics: "))
chemistry_marks = float(input("Enter marks obtained in Chemistry: "))
biology_marks = float(input("Enter marks obtained in Biology: "))


average_marks = (physics_marks + chemistry_marks + biology_marks) / 3
print(f"Average Marks: {average_marks:.2f}%")

if average_marks >= 80:
  grade = "Distinction"
elif average_marks >= 60:
  grade = "First Division"
elif average_marks >= 45:
  grade = "Second Division"
elif average_marks >= 40:
  grade = "Pass"
else:
  grade = "Promotion not granted"

print(f"Grade Obtained: {grade}")