1)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
  largest = num1
  smallest = num2
elif num2 > num1:
  largest = num2
  smallest = num1
else:
  largest = num1  
  smallest = num2 

print(f"The largest value is: {largest}")
print(f"The smallest value is: {smallest}")

2)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


largest = num1
smallest = num1

if num2 > largest:
  largest = num2
if num2 < smallest:
  smallest = num2

if num3 > largest:
  largest = num3
if num3 < smallest:
  smallest = num3

print(f"The largest value is: {largest}")
print(f"The smallest value is: {smallest}")



3)
age = int(input("Enter the age of the person: "))

  if age < 18:
    print("Minor")
  else:
    print("Major")

4)
number = int(input("Enter a number: "))

numberofdigit = len(number)

print(f"The number of digits in the entered number is: {numberofdigits}")

5)

year = int(input("Enter a year: "))

    if (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

6)
    angle1 = float(input("Enter the first angle: "))
    angle2 = float(input("Enter the second angle: "))
    angle3 = float(input("Enter the third angle: "))

    
    if angle1 + angle2 + angle3 == 180:
        print("The triangle is valid.")
    else:
        print("The triangle is not valid.")
7)
number = float(input("Enter a number: "))

    if number >= 0:
        absolute_value = number
    else:
        absolute_value = -number

    
    print(f"The absolute value of {number} is: {absolute_value}")

8)
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))

    area = length * breadth

    
    perimeter = 2 * (length + breadth)
    
    if area > perimeter:
        print("The area of the rectangle is greater than its perimeter.")
    elif area < perimeter:
        print("The area of the rectangle is less than its perimeter.")
    else:
        print("The area of the rectangle is equal to its perimeter.")

9)
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
    print("Yes")
else:
    print("No")

10)
import math

cx = float(input())
cy = float(input())
r = float(input())
px = float(input())
py = float(input())

distance_squared = pow(px - cx, 2) + pow(py - cy, 2)
radius_squared = pow(r, 2)

if distance_squared < radius_squared:
    print("Inside")
elif distance_squared == radius_squared:
    print("On")
else:
    print("Outside")

11)
def convert_to_words(num):
    if 0 <= num <= 19:
        words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                 "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        return words[num]
    else:
        return "Number out of range (0-19)"

12)
subject1_input = input("Enter marks for Subject 1 (or 'absent'): ")
subject2_input = input("Enter marks for Subject 2 (or 'absent'): ")
subject3_input = input("Enter marks for Subject 3 (or 'absent'): ")

subject1_marks = None
subject2_marks = None
subject3_marks = None

try:
    if subject1_input.lower() != 'absent':
        subject1_marks = int(subject1_input)
    if subject2_input.lower() != 'absent':
        subject2_marks = int(subject2_input)
    if subject3_input.lower() != 'absent':
        subject3_marks = int(subject3_input)
except ValueError:
    print("Invalid input. Please enter numbers or 'absent'.")
    exit()

total_marks = 0
subjects_present = 0
failed = False

if subject1_marks is not None:
    total_marks = total_marks + subject1_marks
    subjects_present = subjects_present + 1
    if subject1_marks <= 39:
        failed = True

if subject2_marks is not None:
    total_marks = total_marks + subject2_marks
    subjects_present = subjects_present + 1
    if subject2_marks <= 39:
        failed = True

if subject3_marks is not None:
    total_marks = total_marks + subject3_marks
    subjects_present = subjects_present + 1
    if subject3_marks <= 39:
        failed = True

print("\n--- Result ---")

subject1_grade = "NA"
if subject1_marks is not None:
    if subject1_marks <= 39:
        subject1_grade = "F"
    elif subject1_marks <= 44:
        subject1_grade = "P"
    elif subject1_marks <= 49:
        subject1_grade = "C"
    elif subject1_marks <= 54:
        subject1_grade = "B"
    elif subject1_marks <= 59:
        subject1_grade = "B+"
    elif subject1_marks <= 69:
        subject1_grade = "A"
    elif subject1_marks <= 79:
        subject1_grade = "A+"
    elif subject1_marks <= 100:
        subject1_grade = "O"
print(f"Subject 1: {subject1_marks if subject1_marks is not None else 'Absent'}, Grade: {subject1_grade}")

subject2_grade = "NA"
if subject2_marks is not None:
    if subject2_marks <= 39:
        subject2_grade = "F"
    elif subject2_marks <= 44:
        subject2_grade = "P"
    elif subject2_marks <= 49:
        subject2_grade = "C"
    elif subject2_marks <= 54:
        subject2_grade = "B"
    elif subject2_marks <= 59:
        subject2_grade = "B+"
    elif subject2_marks <= 69:
        subject2_grade = "A"
    elif subject2_marks <= 79:
        subject2_grade = "A+"
    elif subject2_marks <= 100:
        subject2_grade = "O"
print(f"Subject 2: {subject2_marks if subject2_marks is not None else 'Absent'}, Grade: {subject2_grade}")

subject3_grade = "NA"
if subject3_marks is not None:
    if subject3_marks <= 39:
        subject3_grade = "F"
    elif subject3_marks <= 44:
        subject3_grade = "P"
    elif subject3_marks <= 49:
        subject3_grade = "C"
    elif subject3_marks <= 54:
        subject3_grade = "B"
    elif subject3_marks <= 59:
        subject3_grade = "B+"
    elif subject3_marks <= 69:
        subject3_grade = "A"
    elif subject3_marks <= 79:
        subject3_grade = "A+"
    elif subject3_marks <= 100:
        subject3_grade = "O"
print(f"Subject 3: {subject3_marks if subject3_marks is not None else 'Absent'}, Grade: {subject3_grade}")

print(f"Total Marks: {total_marks}")

if subjects_present > 0:
    average_marks = total_marks / subjects_present
    print(f"Average Marks: {average_marks:.2f}")
else:
    print("Average Marks: NA")

if failed:
    print("Pass/Fail: Fail")
else:
    print("Pass/Fail: Pass")
    























