#print the element in particular index-cyclic printing
list=list(map(int,input().split()))
k=int(input("enter the k value"))
index=k%len(list)
#print(list[index-1])
print(list[index])