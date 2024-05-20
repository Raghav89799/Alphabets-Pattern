num = int(input("Enter the Number : "))

for i in range(num):
    for j in range(num):
        if j==0 or i==num-1 and j<=num//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
