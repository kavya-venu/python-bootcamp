# prime number in a given range using square
a=int(input("enter a number of a:"))
b=int(input("enter a number of b:"))
for i in range(a,b+1):
   for j in range(2,1):
       if i%j==0:
           break
   else:
        print(i,end=" ")