import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

    def kiihdyta(self, muutos):
        self.nopeus = max(0, min(self.huippunopeus, self.nopeus + muutos))


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisteri':<12}{'Nopeus (km/h)':<15}{'Matka (km)':<10}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<12}{auto.nopeus:<15}{auto.matka:<10}")
        print("-" * 40)

    def kilpailu_ohi(self):
        return any(auto.matka >= self.pituus for auto in self.autot)
