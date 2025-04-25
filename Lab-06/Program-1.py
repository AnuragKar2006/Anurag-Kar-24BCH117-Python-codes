import random

odd_integers = [random.choice(range(1, 100, 2))
 for _ in range(5):
  print("List of 5 odd integers:", odd_integers)
even_integers = [random.choice(range(0, 100, 2))
 for _ in range(4):
  print("List of 4 even integers:", even_integers)
 if odd_integers[2] = even_integers:
  print("Updated odd integers list:", odd_integers)
flattened_list = [item for sublist in odd_integers for item in (sublist if
isinstance(sublist, list) else [sublist])]
print("Flattened list:", flattened_list)
sorted_list = sorted(flattened_list)
print("Sorted list:", sorted_list)