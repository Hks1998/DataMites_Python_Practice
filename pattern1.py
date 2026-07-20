n=int(input("Enter number of rows: "))
for i in range(0,n+1):
    print(" ")
    for j in range(0,n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(f" {k} ",end=" ")
    print()