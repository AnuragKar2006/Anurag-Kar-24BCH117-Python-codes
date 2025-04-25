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