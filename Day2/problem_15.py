#find the missing number in an array.
# 1 2 3 4 5 6 7 8 9 10===55
#
n=int(input())
list=list(map(int,input().split()))
sum=(n*(n+1)//2)
sum2=0
for i in range(0,len(list)):
    sum2+=list[i]
print(sum-sum2)