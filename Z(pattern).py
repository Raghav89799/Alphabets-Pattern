num = int(input("Enter the Number : "))

for i in range(num):
    for j in range(num):
        if i == 0 or i + j == num-1 or i == num-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()