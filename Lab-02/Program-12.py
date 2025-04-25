import math

cx = float(input())
cy = float(input())
r = float(input())
px = float(input())
py = float(input())

distance_squared = pow(px - cx, 2) + pow(py - cy, 2)
radius_squared = pow(r, 2)

if distance_squared < radius_squared:
    print("Inside")
elif distance_squared == radius_squared:
    print("On")
else:
    print("Outside")