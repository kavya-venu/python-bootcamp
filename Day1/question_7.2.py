#your given with a space separated interger list and find no.of even elements no.of odd elements in given list.
my_list=list(map(int,input().split()))
even=0
odd=0
for i in range(0,len(my_list)):
    if(my_list[i]%2==0):
      even+=1
else:
    odd+=1
print(even)
print(odd)