import random

random_integers = [random.randint(1, 100) for _ in range(20)]
print("List of 20 random integers:", random_integers)
target_number = int(input("Enter a number to find its positions: "))
positions = [index for index, value in enumerate(random_integers)
if value == target_number:
print("Positions of occurrences:", positions)
