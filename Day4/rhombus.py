#print rhombus
num=int(input("enter the number:"))
for i in range(num):
    for s in range(i):
        print(" ",end="")
    for j in range(num):
        print("*",end="")
    print()