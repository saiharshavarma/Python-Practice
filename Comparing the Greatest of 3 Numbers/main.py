print("Enter the three numbers that you want to compare :")
Number1 = float(input("Number 1 : "))
Number2 = float(input("Number 2 : "))
Number3 = float(input("Number 3 : "))
if Number1 > Number2:
    if Number1 > Number3:
        print(Number1, "is the greatest")
    else:
        print(Number3, "is the greatest")
else:
    if Number2 > Number3:
        print(Number2, "is the greatest")
    else:
        print(Number3, "is the greatest")
