def main():
    nimet = set()
    while True:
        nimi = input("syötä nimi):")
        if nimi in nimet:
            print("syötä nimi")
        else:
            print("Uusi nimi")
            nimet.add(nimi)

            print("syötetyt nimet:")
            for nimi in nimet:
                print(nimi)