#find the max element in the given list.
#12 23 36 44 45 57
# o/p:57
list=list(map(int,input().split()))
m=list[0]
for i in range(0,len(list)):
    if(m<list[i]):
      m=list[i]
print(m)