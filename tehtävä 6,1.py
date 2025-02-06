import random


def heitta_noppaa():
    return random.randint(1, 6)
def pääohjelma():
    while (tulos := heita_noppaa()) != 6:
        print(f"Heiton tulos: {tulos}")
    print("Heiton tulos: 6 (Loppu)")