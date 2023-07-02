rent = []
rent2 = []
n = 3
n = float(n)
while n < 20:
    if n - int(n) < 0.5:
        n = int(n)
    rent.append(f"{n}万円以上")
    rent2.append(f"{n}万円以下")
    n = float(n)
    n += 0.5

n = int(n)
while n <= 50:
    rent.append(f"{n}万円以上")
    rent2.append(f"{n}万円以下")
    n += 1

rent.append("100万円以上")
rent2.append("100万円以下")


print(rent)
print(rent2)
