num = int(input("Enter the Number : "))


for i in range(num):
    for j in range(num):
        if  j==num//2 or i+j==num-1 and j>num//2 or j==i and j>num//2:
            print("*",end=" ")
        else:
            print("",end=" ")
    print()