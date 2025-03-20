class Hissi:
    def __init__(self, alas_kerros, ylös_kerros):
        self.alas_kerros = alas_kerros
        self.ylös_kerros = ylös_kerros
        self.nykyinen_kerros = alas_kerros

    def siirry_kerrokseen(self, kohdekerros):
        if self.alas_kerros <= kohdekerros <= self.ylös_kerros:
            print(f"Hissi siirtyy kerrokseen {kohdekerros}.")
            self.nykyinen_kerros = kohdekerros
        else:
            print("Virheellinen kerrosnumero.")

        class Talo:
            def __init__(self, alas_kerros, ylös_kerros, hissien_lkm):
                self.hissit = [Hissi(alas_kerros, ylös_kerros) for _ in range(hissien_lkm)]

            def aja_hissia(self, hissin_numero, kohdekerros):
                if 0 <= hissin_numero < len(self.hissit):
                    print(f"Ajetaan hissi {hissin_numero} kerrokseen {kohdekerros}.")
                    self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
                else:
                    print("Virheellinen hissinumero.")