1)
filename = input("Enter the CSV filename: ")
header = input("Enter the header row: ").split(',')
data_rows = []
while True:
    row_input = input("Enter a data row: ")
    if row_input.lower() == 'done':
        break
    data_rows.append(row_input.split(','))

try:
    file = open(filename, 'w')
    header_str = ''
    for i in range(len(header)):
        header_str += header[i]
        if i < len(header) - 1:
            header_str += ','
    file.write(header_str + '\n')

    for row in data_rows:
        row_str = ''
        for i in range(len(row)):
            row_str += row[i]
            if i < len(row) - 1:
                row_str += ','
        file.write(row_str + '\n')
    file.close()
    print(f"CSV file '{filename}' created.")
except Exception as e:
    print(f"Error creating file: {e}")

2)
import openpyxl

filename = input("Enter Excel filename: ")
workbook = openpyxl.load_workbook(filename)
sheet = workbook.active
header = [cell.value for cell in sheet[1]]
roll_index = -1
name_index = -1
marks_indices = []
for i, col in enumerate(header):
    col_lower = str(col).lower() if col else ''
    if 'roll' in col_lower: roll_index = i
    elif 'name' in col_lower: name_index = i
    elif 'marks' in col_lower: marks_indices.append(i)

student_data = {}
for row_num in range(2, sheet.max_row + 1):
    row_values = [cell.value for cell in sheet[row_num]]
    if roll_index != -1 and name_index != -1 and len(marks_indices) == 3:
        roll = int(row_values[roll_index]) if row_values[roll_index] else None
        name = str(row_values[name_index]) if row_values[name_index] else ''
        marks = [int(row_values[i]) if row_values[i] else 0 for i in marks_indices]
        total = sum(marks) if marks else 0
        if roll is not None:
            student_data[roll] = {'Name': name, 'Marks': marks, 'Total': total}

print(student_data)


3)
def create_vcard():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email (optional): ")
    org = input("Enter Organization (optional): ")

    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}"""

    if email:
        vcard += f"\nEMAIL:{email}"
    if org:
        vcard += f"\nORG:{org}"

    vcard += "\nEND:VCARD"

    filename = name.replace(" ", "_") + ".vcf"
    try:
        with open(filename, "w") as f:
            f.write(vcard)
        print(f"V-card '{filename}' created successfully.")
        print(f"You can import this file into your mobile contacts.")
    except Exception as e:
        print(f"Error creating v-card file: {e}")

create_vcard()

4)
import os

source_dir = input("Source sub-directory: ")
file_name = input("File to copy: ")
dest_dir = input("New sub-directory: ")

current_path = ""
for char in os.getcwd():
    current_path += char

source_path = ""
for part in [current_path, source_dir, file_name]:
    if source_path:
        source_path += os.sep
    source_path += part

dest_path = ""
for part in [current_path, dest_dir]:
    if dest_path:
        dest_path += os.sep
    dest_path += part

dest_file_path = ""
for part in [dest_path, file_name]:
    if dest_file_path:
        dest_file_path += os.sep
    dest_file_path += part

if not os.path.exists(dest_path):
    try:
        os.makedirs(dest_path)
        print(f"'{dest_dir}' created.")
    except OSError as e:
        print(f"Error creating '{dest_dir}': {e}")
        exit()

try:
    source_file = open(source_path, 'rb')
    dest_file = open(dest_file_path, 'wb')
    while True:
        chunk = source_file.read(4096)
        if not chunk:
            break
        dest_file.write(chunk)
    source_file.close()
    dest_file.close()
    print(f"'{file_name}' copied to '{dest_dir}'.")
except FileNotFoundError:
    print(f"Error: '{file_name}' not found in '{source_dir}'.")
except Exception as e:
    print(f"Error copying: {e}")

5)
source_name = input("Enter source file name: ")
dest_name = input("Enter destination file name: ")

source_file = open(source_name, 'r')
dest_file = open(dest_name, 'w')

for line in source_file:
    upper_line = ''
    for char in line:
        if 'a' <= char <= 'z':
            upper_line += chr(ord(char) - 32)
        else:
            upper_line += char
    dest_file.write(upper_line)

source_file.close()
dest_file.close()

print(f"Contents of '{source_name}' converted to uppercase and copied to '{dest_name}'.")

6)
def merge_files_alternatively(file1_name, file2_name, output_file_name):
    file1 = open(file1_name, 'r')
    file2 = open(file2_name, 'r')
    output_file = open(output_file_name, 'w')

    line1 = file1.readline()
    line2 = file2.readline()

    while line1 or line2:
        if line1:
            output_file.write(line1)
            line1 = file1.readline()
        if line2:
            output_file.write(line2)
            line2 = file2.readline()

    file1.close()
    file2.close()
    output_file.close()

file1 = input("Enter the name of the first file: ")
file2 = input("Enter the name of the second file: ")
output_file = input("Enter the name for the output file: ")

merge_files_alternatively(file1, file2, output_file)

print(f"Contents of '{file1}' and '{file2}' merged alternatively into '{output_file}'.")

7)
class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

def serialize_emp(emp, filename):
    data = f"{emp.empcode},{emp.empname},{emp.doj},{emp.salary}\n"
    file = open(filename, 'w')
    file.write(data)
    file.close()
    print(f"Saved to '{filename}'")

def deserialize_emp(filename):
    file = open(filename, 'r')
    data = file.readline().strip().split(',')
    file.close()
    if len(data) == 4:
        return Employee(data[0], data[1], data[2], data[3])
    else:
        print("Error reading data")
        return None

emp = Employee("101", "Rajesh", "2023-08-15", "50000")
file_name = "emp.txt"
serialize_emp(emp, file_name)
loaded_emp = deserialize_emp(file_name)

if loaded_emp:
    print(f"Code: {loaded_emp.empcode}, Name: {loaded_emp.empname}, Joined: {loaded_emp.doj}, Salary: {loaded_emp.salary}")

8)
def process_file_basic(input_filename, output_filename):
    infile = open(input_filename, 'r')
    outfile = open(output_filename, 'w')
    words_to_delete = ['a', 'an', 'the']

    for line in infile:
        output_line = ''
        for word in line.lower().split():
            if word not in words_to_delete:
                output_line += word + ' '
        outfile.write(output_line.strip() + '\n')

    infile.close()
    outfile.close()
    print(f"Processed to '{output_filename}'")

in_file = input("Input file: ")
out_file = input("Output file: ")
process_file_basic(in_file, out_file)



























