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

