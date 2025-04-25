angle1 = float(input("Enter the first angle: "))
    angle2 = float(input("Enter the second angle: "))
    angle3 = float(input("Enter the third angle: "))

    
    if angle1 + angle2 + angle3 == 180:
        print("The triangle is valid.")
    else:
        print("The triangle is not valid.")