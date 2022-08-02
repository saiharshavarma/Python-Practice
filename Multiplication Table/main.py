print("Multiplication Table")
Number = int(input("Enter a Number to print it's Multiplication Table : "))
for counter in range(1,11):
    print(Number, "*", counter, "=", (Number*counter))
