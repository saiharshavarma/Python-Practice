Number = int(input("Enter a Number : "))
Counter = 1
Checker = 0
while (Counter <= Number):
    if ((Number % Counter) == 0):
        Checker += 1
    Counter += 1
if Checker == 2:
    print(Number, "is a Prime")
else:
    print(Number, "is not a Prime")