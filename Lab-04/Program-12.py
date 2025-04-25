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
    
