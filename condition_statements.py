# condition statements

# simple if
mark = int(input("enter your mark:"))
if mark > 34:
    print("pass")

# if else
mark = int(input("enter your mark:"))
if mark > 34:
    print("pass")
else:
    print("fail")

# mark grade program
print("enter five marks:")
m1 = int(input("enter the m1:"))
m2 = int(input("enter the m2:"))
m3 = int(input("enter the m3:"))
m4 = int(input("enter the m4:"))
m5 = int(input("enter the m5:"))

tot = m1 + m2 + m3 + m4 + m5
avg = tot / 5

if m1 > 34 and m2 > 34 and m3 > 34 and m4 > 34 and m5 > 34:
    res = "pass"
else:
    res = "fail"

if res == "pass":
    if avg >= 85:
        gra = "outstanding"
    elif avg >= 75:
        gra = "excellent"
    elif avg >= 65:
        gra = "very good"
    elif avg >= 55:
        gra = "good"
    else:
        gra = "fair"
else:
    gra = "no grade because fail"

print("total mark:", tot)
print("average mark:", avg)
print("result:", res)
print("grade:", gra)

# nested if - marriage eligibility
gender = input("enter the gender:")
age = int(input("enter the age:"))
if gender == "male":
    if age >= 23:
        print("Eligible for marriage")
    else:
        print("Not eligible")
elif gender == "female":
    if age >= 21:
        print("Eligible for marriage")
    else:
        print("Not eligible")
else:
    print("Invalid gender")

# voter eligibility
age = int(input("enter your age:"))
if age >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote")

# even or odd
num = int(input("enter your number:"))
if num % 2 == 0:
    print("even number")
else:
    print("odd number")

# palindrome
name = input("enter your string:")
rname = name[::-1]
print("reverse name:", rname)
if name == rname:
    print("palindrome")
else:
    print("not palindrome")

# greatest among 3 numbers
num1 = int(input("enter the num1:"))
num2 = int(input("enter the num2:"))
num3 = int(input("enter the num3:"))
num = max(num1, num2, num3)
print("greatest number is:", num)

# positive negative or zero
num = float(input("enter the number:"))
if num > 0:
    print("positive value")
elif num < 0:
    print("negative value")
else:
    print("zero value")
