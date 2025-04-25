1) 
a = int(input("Enter a number"))
if (a>0):
  b=a**2
  c=a**3
 print (square= b, cube= c)
else:
 print (Invalid data)

2)
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if a > b:
  print(f"{a} is greater than {b}")
elif b > a:
  print(f"{b} is greater than {a}")
else:
  print("Both numbers are equal")



3)
a = int(input("Enter a number"))
if( a%2==0):
    print("The number is even")
else:
    print("The number is odd")


4)
a = int(input("Enter an integer: "))

if a % 7 == 0:
  print(f"{a} is divisible by 7")
else:
  print(f"{a} is not divisible by 7")

5)
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
