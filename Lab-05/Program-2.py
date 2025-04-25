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

