# python basics
# variables and datatypes

a = 20
b = 40.3
c = 'karur'
d = True
e = "i love karur"

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# basic calculation
a = 10
b = 20
c = 30
t = a - b + c
print("final values:", t)

# integer addition
m1 = int(input("Enter mark1:"))
m2 = int(input("Enter mark2:"))
m3 = int(input("Enter mark3:"))
m4 = int(input("Enter mark4:"))
m5 = int(input("Enter mark5:"))
total = m1 + m2 + m3 + m4 + m5
print("total mark:", total)

# float addition
a = float(input("enter number 1:"))
b = float(input("enter number 2:"))
c = a + b
print("float total:", c)

# arithmetic operators
a = 10
b = 3
print("addition:", a + b)
print("subtraction:", a - b)
print("multiply:", a * b)
print("divide:", a / b)
print("floor division:", a // b)
print("modulo:", a % b)
print("exponential:", a ** b)

# assignment operator
a = 3
b = 2
a += b
print("answer:", a)
b -= 2
print("answer:", b)

# relational operator
a = "bala"
b = "kish"
print(a, "<", b, "=", a < b)
print(a, ">", b, "=", a > b)
print(a, "==", b, "=", a == b)
print(a, "!=", b, "=", a != b)

# logical operator
m1 = 100
m2 = 100
m3 = 100
m4 = 100
m5 = 33
res = m1 > 34 and m2 > 34 and m3 > 34 and m4 > 34 and m5 > 34
print("result:", res)
res = m1 > 34 or m2 > 34 or m3 > 34 or m4 > 34 or m5 > 34
print("result:", res)
res = not(m1 > 34 or m2 > 34 or m3 > 34 or m4 > 34 or m5 > 34)
print("result:", res)

# slicing
num = "pradeepa"
print(num[::2])
print(num[:3])
print(num[3:7])
print(num[3:])
