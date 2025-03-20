class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit

    def __str__(self):
        return (f"Rekisteritunnus: {self.rekisteritunnus}\n"
                f"Huippunopeus: {self.huippunopeus} km/h\n"
                f"Tämänhetkinen nopeus: {self.nopeus} km/h\n"
                f"Kuljettu matka: {self.kuljettu_matka} km")

if __name__ == "__main__":
    auto = Auto("ABC-123", 142)  # Poistettu ylimääräiset heittomerkit ja virheelliset sulkeet
    auto.kiihdyta(30)
    auto.kiihdyta(70)
    auto.kiihdyta(50)
    print(f"Nopeus kiihdytyksen jälkeen: {auto.nopeus} km/h")

    auto.kiihdyta(-200)
    print(f"Nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h")

    auto.kulje(1.5)
    print(f"Kuljettu matka ajon jälkeen: {auto.kuljettu_matka} km")
