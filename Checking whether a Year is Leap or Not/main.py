Year = int(input("Enter a Year : "))
if (Year%4==0 and Year%100!=0) or Year%400==0:
    print(Year, "is a Leap Year")
else:
    print(Year, "is not a Leap Year")