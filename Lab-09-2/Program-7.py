def avg(lst, n):
if n == 0:
return 0
return (lst[n - 1] + (n - 1) * avg(lst, n - 1)) / n
numbers = list(map(int, input("Enter numbers: ").split()))
print("Average:", avg(numbers, len(numbers)))