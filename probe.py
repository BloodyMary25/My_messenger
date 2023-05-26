
n = int(input("N: "))
start = 1 if n % 2 else 2
for i in range(start + 2, n + 1, 2):
    start *= i
print(start)
#



