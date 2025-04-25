
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if num1 > num2:
  largest = num1
  smallest = num2
elif num2 > num1:
  largest = num2
  smallest = num1
else:
  largest = num1 
  smallest = num2 

# Print the results
print(f"The largest value is: {largest}")
print(f"The smallest value is: {smallest}")