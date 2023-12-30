a = int(input("enter value of a"))
b = int(input("enter value of b"))
c = int(input("enter value of c"))

largest = 0

if a > b and a > c:
    largest = a
if b > a and b > c:
    largest = b
if c > a and c > b:
    largest = c

print(largest, "is the largest of three numbers.")
