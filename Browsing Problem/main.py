print("The maximum number of hours of Browsing is 7")
Number_of_Hours = int(input("Enter the number of Hours of Browsing : "))
Number_of_Minutes = int(input("Enter the number of Minutes of Browsing : "))
if Number_of_Minutes >= 60:
    Number_of_Hours = Number_of_Minutes // 60
    Number_of_Minutes = Number_of_Minutes % 60
if Number_of_Hours >= 7:
    print("The maximum number of hours of Browsing is 7. You can't exceed this limit")
else:
    if Number_of_Hours >= 5:
        Bill = 200 + ((Number_of_Hours - 5) * 50) + (Number_of_Minutes * 1)
    else:
        Bill = (Number_of_Hours * 50) + (Number_of_Minutes * 1)
    print("Bill :", round(Bill, 2))