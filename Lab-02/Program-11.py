x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
    print("Yes")
else:
    print("No")