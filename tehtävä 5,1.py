import random

lkm = int(input("kuinka monta kerta heitetään noppaa? "))
summa = 0
for i in range(lkm):
    silmäluku = random.randint(1,6)
    summa += silmäluku

print(f'silmälukuja summa on {summa}')
print(f'keskimääräinen silmäluku on {summa / lkm}')
