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