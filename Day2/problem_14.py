#replace the elements in an array with the avg of max and min elements.
 #12 1 34 56 44
#min=1 max=56
#avg=56+1/2=>57/2=>28
list=list(map(int,input().split()))
max=list[0]
min=list[0]
for i in range(0,len(list)):
    if(min>list[i]):
       min=list[i]
for i in range(0,len(list)):
    if(max<list[i]):
      max=list[i]
avg=(max+min)//2
for i in range(len(list)):
    list[i]=avg
print(list)

