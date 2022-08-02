print(":AND Gate:")
Input1 = int(input("Enter a value (0 or 1) A : "))
Input2 = int(input("Enter a value (0 or 1) B : "))
Output = Input1 * Input2
if (Input1 in (0,1) and Input2 in (0,1)):
    print("Output :", Output)
else:
    print("Invalid Input")