p = int(input())
temp = input().split(" ")
m = int(temp[0])
n = int(temp[1])
moves = []
board = []
num1 = int(input())
for counter in range(num1):
    moves.append(input().lower())
temp = input().split(" ")
m1 = int(temp[0])
n1 = int(temp[1])
for counter in range(num1):
    if moves[counter] == 'l':
        if n > 0:
            n -= 1
    elif moves[counter] == 'r':
        if n < (p-1):
            n += 1
    elif moves[counter] == 'u':
        if m < (p-1):
            m += 1
    elif moves[counter] == 'd':
        if m > 0:
            m -= 1
    if m == m1 and n == n1:
        print("Win")
        break
if m != m1 and n != n1:
    print("Loss")
