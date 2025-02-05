def alkuluku(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
luku = int(input("Anna kokonaisluku: "))
if (luku):
    print(f"{luku} on alkuluku.")
else:
    print(f"{luku} ei ole alkuluku.")
