#remove all the  brackets from the given algebraic expression.
# (a+b)[a-b]
#o/p=a+b a-b
inp=input()
for i in inp:
    if (ord(i)==41 or ord(i)==40 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end=" ")
print()