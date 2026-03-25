# loops practice

# for loop type 1
n = int(input("enter size :"))
for i in range(n+1):
    if i == n:
        print(i, end=" ")
    else:
        print(i, end="+")

# for loop type 2
s = int(input("enter start number :"))
e = int(input("enter end number :"))
for i in range(s, e):
    print(i, end=" ")

# for loop type 3
s = int(input("enter start number :"))
e = int(input("enter end number :"))
inc = int(input("enter increment value :"))
for i in range(s, e, inc):
    print(i, end=" ")

# for loop type 4
e = int(input("enter end number :"))
s = int(input("enter start number :"))
dec = int(input("enter decrement value :"))
for i in range(e, s, -dec):
    print(i, end=" ")

# for loop type 5 - loop through list
k = [11, 44, 55, 66, 77, 88, 12, 34]
for i in k:
    print(i)

# even numbers from list
h = [10, 12, 14, 15, 16, 13, 17, 19, 21, 20, 23, 27, 29]
for i in h:
    if i % 2 == 0:
        print(i)

# negative values from list
h = [-8, 9, -10, 12, 15, -16, 18]
for i in h:
    if i < 0:
        print(i)

# sum of numbers
n = int(input("enter the size :"))
k = 0
for i in range(n+1):
    k = k + i
    if i == n:
        print(i, end=" ")
    else:
        print(i, end=" + ")
print("=", k)

# sum of even numbers only
n = int(input("enter the size :"))
k = 0
for i in range(n+1):
    if i % 2 == 0:
        k = k + i
        if i == n:
            print(i, end=" ")
        else:
            print(i, end=" + ")
print("=", k)

# count negative values
num = [1, -2, -3, -4, 5, 6, -7, -8, -9, 0, 11, 12, 13, 14]
count = 0
for i in num:
    if i < 0:
        count = count + 1
print("the count of negative numbers is :", count)

# while loop - forward
s = int(input("enter starting number :"))
e = int(input("enter ending number :"))
while s <= e:
    print(s, end=" ")
    s += 1

# while loop - reverse
e = int(input("enter ending number :"))
s = int(input("enter starting number :"))
while e >= s:
    print(e, end=" ")
    e -= 1

# while loop - sum forward
s = int(input("enter starting number :"))
e = int(input("enter ending number :"))
tot = 0
while s <= e:
    print(s, end=" ")
    tot = tot + s
    s += 1
print("\ntotal:", tot)

# while loop - sum reverse
e = int(input("enter ending number :"))
s = int(input("enter starting number :"))
tot = 0
while e >= s:
    print(e, end=" ")
    tot = tot + e
    e -= 1
print("total:", tot)

# while loop - find vowels
name = input("Enter the text :")
vow = "aeiouAEIOU"
i = 0
while i < len(name):
    if name[i] in vow:
        print(name[i], end=" ")
    i += 1

# while loop - count vowels
name = input("Enter the text :")
vow = "aeiouAEIOU"
i = 0
c = 0
while i < len(name):
    if name[i] in vow:
        print(name[i], end=" ")
        c += 1
    i += 1
print("\nTotal no of vowels:", c)

# nested loop - forward matrix
for i in range(1, 6):
    for j in range(1, 6):
        print(i, j, end=" ", sep="")
    print()

# nested loop - reverse matrix
for i in range(5, 0, -1):
    for j in range(5, 0, -1):
        print(i, j, end=" ", sep="")
    print()

# nested loop - runtime rows and cols
r = int(input("enter no. of rows:"))
c = int(input("enter no. of cols:"))
for i in range(r):
    for j in range(c):
        print(i, j, end=" ", sep="")
    print()

# nested loop - star pattern
r = int(input("enter no. of rows:"))
for i in range(1, r+1):
    for j in range(1, i+1):
        print(end=" * ", sep="")
    print()

# nested loop - name pattern forward
name = input("enter no. of name:")
n = len(name)
for i in range(n):
    for j in range(0, i+1):
        print(name[j], end=" ", sep="")
    print()

# nested loop - name pattern reverse
name = input("enter no. of name:")
n = len(name)
for i in range(n, 0, -1):
    for j in range(0, i):
        print(name[j], end="", sep="")
    print()
