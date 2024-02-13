#Write a program that classifies a triangle based on its side lengths.
#Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).

side1 = int(input("Enter the side1"))
side2 = int(input("Enter the side2"))
side3 = int(input("Enter the side3"))
if side1 == side2 == side3 :
    print("Equilateral triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("Scalene triangle")
else :
    print("ISOsceles")

