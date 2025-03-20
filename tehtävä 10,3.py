class Hissi:
    def __init__(self, alas_kerros, ylos_kerros):
        self.alas_kerros = alas_kerros
        self.ylos_kerros = ylos_kerros
        self.nykyinen_kerros = alas_kerros

    def siirry_kerrokseen(self, kohdekerros):
        if self.alas_kerros <= kohdekerros <= self.ylos_kerros:
            print(f"Hissi siirtyy kerrokseen {kohdekerros}.")
            self.nykyinen_kerros = kohdekerros
        else:
            print("Virheellinen kerrosnumero.")


class Talo:
    def __init__(self, alas_kerros, ylos_kerros, hissien_lkm):
        self.alas_kerros = alas_kerros
        self.hissit = [Hissi(alas_kerros, ylos_kerros) for _ in range(hissien_lkm)]

    def aja_hissia(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"Ajetaan hissi {hissin_numero} kerrokseen {kohdekerros}.")
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
        else:
            print("Virheellinen hissinumero.")

    def palohalytys(self):
        print("Palohälytys! Kaikki hissit siirtyvät pohjakerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alas_kerros)