#write a program upper triangle matrix.
# we will displayed the upper triangle matrix by relacing lower triangle elements to zero.
arr=[[1,3,4],
     [5,6,7],
     [4,8,9]]
print("the original matrix:")
for row in arr:
    print(row)
print()
print("the upper triangular matrix:")
if(len(arr) != len(arr[0])):
    print("matrix should be a square matrix")
else:
    for i in range(3):
        for j in range(3):
            if(i<=j):
                print(arr[i][j],end=" ")
            else:
                print(0,end=" ")
        print()
