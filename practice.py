count = 0
for n in range(1, 11):
    factor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            factor_sum += i
    if factor_sum > n:
        count += 1
        print(f"{n} is abundant")
print("Abundant numbers count:", count)