import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)
def paaohjelma():
    tahkot = int(input("Anna nopan tahkojen määrä: "))
    maksimi = tahkot
    while (tulos := heita_noppaa(tahkot)) != maksimi:
        print
        ('heiton tulos: {tulos}')
    print
    ('Heiton tulos: {maksimi} (Loppu)')