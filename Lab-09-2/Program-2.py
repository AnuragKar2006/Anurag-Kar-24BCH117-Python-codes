def binary(n):
if n == 0:
return ""
return binary(n // 2) + str(n % 2)
num = int(input("Enter a number: "))
print("Binary equivalent:", binary(num) or "0")
