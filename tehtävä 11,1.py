class kirja(Julkaisu):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tulosta_tiedot(self):
            print(f"nimi : {self.name}")

class kirja(julkisu):
    def __init__(self, name, kirjoittaja, sivumäärä):
            self.kirjoittaja = kirjoittaja
            self.sivumäärä
            super().__init__(nimi)
    def tulosta_tiedot(self):
         print(f"kirjoittaja : {self.kirjoittaja}")
         print(f"sivumäärä  : {self.sivumäärä}")
         super().tulosta_tiedot


class lehti(julkisu):

    def __init__(self, name, päätoimittaja):
            self.päätoimittaja
            super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"päätoimittaja : {self.päätoimittaja}")
        super().tulosta_tiedot()

    aku = Lehti("Aku Ankka", "Aki Hyppä")
    kirja = kirja("Hytti nro 6", "Rosa Likson", 200 )
    aku.tulosta_tiedot()
    kirja.tulosta_tiedot()