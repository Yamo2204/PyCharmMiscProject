class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros  # Hissi alkaa alimmasta kerroksesta

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa")

    def siirry_kerrokseen(self, kohdekerros):
        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"Ajetaan hissiä {hissin_numero} kerrokseen {kohdekerros}")
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
        else:
            print("Virhe: Ei löydy hissiä annetulla numerolla.")

    def palohälytys(self):
        print("Palohälytys! Kaikki hissit siirtyvät pohjakerrokseen.")
        for i, hissi in enumerate(self.hissit):
            print(f"Siirretään hissi {i} pohjakerrokseen.")
            hissi.siirry_kerrokseen(self.alin_kerros)


h = Hissi(1, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)

talo = Talo(1, 10, 3)

talo.aja_hissiä(0, 7)
talo.aja_hissiä(1, 3)
talo.aja_hissiä(2, 10)
talo.palohälytys()
