Number = int(input("Enter a Number : "))
Quotient = Number
Sum = 0
while (Quotient > 0):
    Remainder = Quotient % 10
    Sum = Sum + Remainder
    Quotient //= 10
print("The sum of individual digits of the number", Number, "is", Sum)