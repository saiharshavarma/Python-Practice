N = float(input("Enter the amount Bob has : Rs."))
C = float(input("Enter the cost of one chocolate : Rs."))
M = int(input("For how many wrappers does Bob get one free chocolate : "))
S1 = int(N/C) #S1 = No. of chocolates Bob gets
if M==0:
    S2 = 0 #S2 = No. of free chocolates Bob gets
else:
    S2 = int(S1/M) #S2 = No. of free chocolates Bob gets
S3 = int(S1 + S2) #S3 = Total no. of chocolates Bob gets
print("Total number of chocolates Bob gets :", S3)