x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x > 0:
    if y > 0:
      print("Point lies in the first quadrant.")
    else:
       print("Point lies in the fourth quadrant.")
elif y > 0:
   print("Point lies in the second quadrant.")
elif y < 0:
   print("Point lies in the third quadrant.")
else:
   print("Point lies on origin.")
