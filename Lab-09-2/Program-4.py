def reverse_list(lst):
if not lst:
return []
return [lst[-1]] + reverse_list(lst[:-1])
numbers = list(map(int, input("Enter numbers: ").split()))
print("Reversed List:", reverse_list(numbers))