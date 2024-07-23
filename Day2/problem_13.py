#find the min  element in the given list.
list=list(map(int,input().split()))
m=list[0]
for i in range(0,len(list)):
    if(m>list[i]):
      m=list[i]
print(m)