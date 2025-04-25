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
