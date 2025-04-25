def count_vowels(s, index=0, count=0):
vowels = "aeiouAEIOU"
if index == len(s):
return count
return count_vowels(s, index + 1, count + (1 if s[index] in vowels else 0))
text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))