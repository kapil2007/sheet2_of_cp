N = int(input("Enter the digit: "))
count = 0
while N > 0:
    count += 1
    N //= 10
print("Count of digits =", count)
