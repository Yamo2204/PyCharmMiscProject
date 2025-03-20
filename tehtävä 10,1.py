class Hissi:
    def __init__(self, alas_kerros, ylös_kerros):
        self.alas_kerros = alas_kerros
        self.ylös_kerros = ylös_kerros
        self.nykyinen_kerros = alas_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylös_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alas_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kohdekerros):
        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()

if __name__ == "__main__":
    h = Hissi(1, 10)
    h.siirry_kerrokseen(5)
    h.siirry_kerrokseen(1)