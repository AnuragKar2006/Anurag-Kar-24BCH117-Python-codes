def remove_substring_basic(main_string, string_to_remove):
    final_string = ""
    len_main = 0
    for char in main_string:
        len_main = len_main + 1

    len_remove = 0
    for char in string_to_remove:
        len_remove = len_remove + 1

    i = 0
    while i < len_main:
        found = False
        j = 0
        while j < len_remove:
            if i + j < len_main and main_string[i + j] == string_to_remove[j]:
                j = j + 1
            else:
                break
        if j == len_remove:
            found = True
            i = i + len_remove
        else:
            final_string = final_string + main_string[i]
            i = i + 1

    return final_string

one_string = "abcdef"
remove_string = "cd"
final_string = remove_substring_basic(one_string, remove_string)
print(f"Original string: {one_string}")
print(f"String to remove: {remove_string}")
print(f"Final string: {final_string}")

