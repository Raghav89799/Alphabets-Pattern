num = int(input("Enter the Number : "))

for i in range(num):
    for j in range(num):
        if j == i or i + j == num-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()