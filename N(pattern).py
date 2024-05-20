num = int(input("Enter the Number : "))

for i in range(num):
    for j in range(num):
        if j==0 or j==num-1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
