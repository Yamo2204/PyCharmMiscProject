oikea_tunnus = "python"
oikea_salasana = "rules"

input("Anna käyttäjätunnus: ")
input("Anna salasana: ")

if tunnus == oikea_tunnus and salasana == oikea_salasana:
    print("Tervetuloa!")
else:
    print("Virheellinen käyttäjätunnus tai salasana.")
