print("1. Addition \n"
      "2. Subtraction \n"
      "3. Multiplication \n"
      "4. Division \n"
      "5. Power \n"
      "6. Exit")
Result = 0.0
Choice = int(input("Enter the number of the operation you want to perform on the operands : "))
if (Choice > 0 and Choice <= 5):
    Number1 = float(input("Enter the first number : "))
    Number2 = float(input("Enter the second number : "))
    if Choice == 1:
        Result = Number1 + Number2
    elif Choice == 2:
        Result = Number1 - Number2
    elif Choice == 3:
        Result = Number1 * Number2
    elif Choice == 4:
        Result = Number1 / Number2
    elif Choice == 5:
        Result = Number1 ** Number2
    print("Result :", Result)
elif Choice == 6:
    print()
else:
    print("Invalid Input")