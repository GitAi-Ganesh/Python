# 1. Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []
f1 = int(input("enter marks")) #here int is used to convert string input to integer
marks.append(f1)
f2 = int(input("enter marks"))
marks.append(f2)
f3 = int(input("enter marks"))
marks.append(f3)
f4 = int(input("enter marks"))
marks.append(f4)
marks.sort()
print(marks)