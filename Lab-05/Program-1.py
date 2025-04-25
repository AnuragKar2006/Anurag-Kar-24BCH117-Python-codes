input_string = input("Enter a string: ")

vowel_count = 0

for char in input_string:
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or
            char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
        vowel_count = vowel_count + 1

print("Number of vowels:", vowel_count)
