# Take three sides and check if they form a valid triangle.
def is_valid_triangle(a , b , c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
    
# Take three sides as input from the user
side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))
# Check if the sides form a valid triangle
if is_valid_triangle(side1, side2, side3):
    if side1 == side2:
      if side2 == side3:
          print("Triangle is an  equilateral.")
      else:
          print("Triangle is isosceles.")
    elif side2 == side3:
        print("Triangle is isosceles.")
    else:
        print("Triangle is scalene.")

else:
    print("The sides do not form a valid triangle.")
    
