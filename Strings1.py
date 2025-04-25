1)
input_string = input("Enter a string: ")

vowel_count = 0

for char in input_string:
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or
            char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
        vowel_count = vowel_count + 1

print("Number of vowels:", vowel_count)

2)
def to_lower_case(input_string):
    lower_string = ''
    for char in input_string:
        if 'A' <= char <= 'Z':
            
            lower_char = chr(ord(char) + 32)
            lower_string += lower_char
        else:
            lower_string += char
    return lower_string

def to_upper_case(input_string):
    upper_string = ''
    for char in input_string:
        if 'a' <= char <= 'z':
            
            upper_char = chr(ord(char) - 32)
            upper_string += upper_char
        else:
            upper_string += char
    return upper_string

def to_toggle_case(input_string):
    toggled_string = ''
    for char in input_string:
        if 'A' <= char <= 'Z':
            toggled_char = chr(ord(char) + 32)
            toggled_string += toggled_char
        elif 'a' <= char <= 'z':
            toggled_char = chr(ord(char) - 32)
            toggled_string += toggled_char
        else:
            toggled_string += char
    return toggled_string


test_string = "HeLlO wOrLd 123"

lower = to_lower_case(test_string)
upper = to_upper_case(test_string)
toggled = to_toggle_case(test_string)

print(f"Original string: {test_string}")
print(f"Lower case: {lower}")
print(f"Upper case: {upper}")
print(f"Toggled case: {toggled}")


3)
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if string1 in string2:
    print(f"'{string1}' is present in '{string2}'")
elif string2 in string1:
    print(f"'{string2}' is present in '{string1}'")
else:
    print("Neither string is present in the other.")

4)
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





























