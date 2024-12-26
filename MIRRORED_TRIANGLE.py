h = int(input("Enter a height for the triangle: "))
for i in range(1,h+1):
    for j in range(1,h+1):
        if (j <= (h - i)):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()