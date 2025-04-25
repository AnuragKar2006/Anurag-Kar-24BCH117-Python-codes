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
