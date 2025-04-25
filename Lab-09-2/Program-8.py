def string_length(s):
return 0 if not s else 1 + string_length(s[1:])
text = input("Enter a string: ")
print("Length of string:", string_length(text))

