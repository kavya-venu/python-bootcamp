#print number pyramid
rows=int(input("enter number of rows:"))
p=0
for i in range(1,rows+1):
    for space in range(1, (rows-i)+1):
        print(end=" ")
    while p!=(2*i-1):
        print("* ",end="")
        p+=1
    p=0
    print()
