def prime_factors(n, divisor=2):
if n <= 1:
return []
if n % divisor == 0:
return [divisor] + prime_factors(n // divisor, divisor)
return prime_factors(n, divisor + 1)
num = int(input("Enter a number: "))
print("Prime factors:", prime_factors(num))
