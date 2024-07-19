#given an space separated interger list find the avg of elements present in the even index.
my_list=list(map(int,input().split()))
sum=0
n=len(my_list)
for i in range(n):
     if(i%2==0):
       sum+=my_list[i] 
print((sum/n))            #count+=1
                          #print(sum/count)