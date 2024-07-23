#find the  elements that is present in k+n index 
#k is given by user
#k=3 n=2 ex:3 4 56 6 7
#o/p is 7
list=list(map(int,input().split()))
k=int(input("enter the k value"))
n=int(input("enter the n value")) 
length=len(list)
if(length<(k+n)):
    print("error")
else:
    for i in list:
        a=(list[k+n])
    print(a)
    
