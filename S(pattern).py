num = int(input("Enter the Number : "))

for i in range(num):
    for j in range(num):
        if i==0 or i==num-1 or j==0 and i < num//2 or i == num//2 or j==num-1 and i > num//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()