# area and perimeter programs

# area of square
a = int(input("area of square:"))
res = a * a
print("area of square:", res)

# area of rectangle
length = int(input("enter length:"))
breath = int(input("enter breath:"))
area = length * breath
print("area of rectangle:", area)

# area of triangle
b = int(input("enter breath:"))
h = int(input("enter height:"))
cal = (b * h) / 2
print("area of triangle:", cal)

# area of circle
r = float(input("enter the radius:"))
circle = 3.14 * r * r
print("area of the circle:", circle)

# area of cone
r = float(input("enter the radius:"))
h = float(input("enter the height:"))
area = 0.33 * 3.14 * r * r * h
print("area of cone:", area)

# perimeter of circle
r = float(input("enter the radius:"))
perimeter = 2 * 3.14 * r
print("perimeter of the circle:", perimeter)

# perimeter of square
a = int(input("perimeter of square:"))
perimeter = 4 * a
print("perimeter of square:", perimeter)

# unit conversion
# feet to cm
ft = 30.48
cm = float(input("enter feet:"))
ans = cm * ft
print("total cms:", ans)

# days to hours
days = 24
hrs = float(input("enter the days:"))
ans = days * hrs
print("total hrs:", ans)

# meter to cm
meter = 100
cm = int(input("enter the meter:"))
ans = meter * cm
print("total cms:", ans)

# kilometer to meter
kilometer = 1000
meter = int(input("enter the kilometer:"))
ans = kilometer * meter
print("total meters:", ans)
