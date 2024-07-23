# write a program lower traingular matrix
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
            if(j<=i):
                print(arr[i][j],end=" ")
            else:
                print(0,end=" ")
        print()
