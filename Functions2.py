1)
def prime_factors(n, divisor=2):
if n <= 1:
return []
if n % divisor == 0:
return [divisor] + prime_factors(n // divisor, divisor)
return prime_factors(n, divisor + 1)
num = int(input("Enter a number: "))
print("Prime factors:", prime_factors(num))

2)
def binary(n):
if n == 0:
return ""
return binary(n // 2) + str(n % 2)
num = int(input("Enter a number: "))
print("Binary equivalent:", binary(num) or "0")


3)
def count_vowels(s, index=0, count=0):
vowels = "aeiouAEIOU"
if index == len(s):
return count
return count_vowels(s, index + 1, count + (1 if s[index] in vowels else 0))
text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))

4)
def reverse_list(lst):
if not lst:
return []
return [lst[-1]] + reverse_list(lst[:-1])
numbers = list(map(int, input("Enter numbers: ").split()))
print("Reversed List:", reverse_list(numbers))

5)
def power(a, b):
if b == 0:
return 1
return a * power(a, b - 1)
a, b = map(int, input("Enter a and b: ").split())
print(f"{a}^{b} =", power(a, b))

6)
def sanitize_list(lst, index=0):
if index == len(lst):
return lst
if lst[index] < 0:
lst[index] = 0
return sanitize_list(lst, index + 1)
numbers = list(map(int, input("Enter numbers: ").split()))
print("Sanitized List:", sanitize_list(numbers))

7)
def avg(lst, n):
if n == 0:
return 0
return (lst[n - 1] + (n - 1) * avg(lst, n - 1)) / n
numbers = list(map(int, input("Enter numbers: ").split()))
print("Average:", avg(numbers, len(numbers)))

8)
def string_length(s):
return 0 if not s else 1 + string_length(s[1:])
text = input("Enter a string: ")
print("Length of string:", string_length(text))






























