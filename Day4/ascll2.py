'''for i in range(32,128):
    print(chr(i),end="")'''
    
#sum of digit number using ascli values
inp=input()
sum=0
for i in inp:
    if(ord(i)>=48 and ord(i)<=57):
        sum+=int(i)
print(sum)