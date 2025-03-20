import random


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
        return f"{self.rekisteritunnus:10} | {self.huippunopeus:5} km/h | {self.nopeus:5} km/h | {self.kuljettu_matka:7} km"

if __name__ == "__main__":
    autot = [Auto(f"ABC-{i + 1}", random.randint(100, 200)) for i in range(10)]

    kilpailu_kaynnissa = True
    while kilpailu_kaynnissa:
        for auto in autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)
            if auto.kuljettu_matka >= 10000:
                kilpailu_kaynnissa = False
                break

    print(f"{'Rekisteri':10} | {'Huippu':5} | {'Nopeus':5} | {'Matka':7}")
    print("-" * 35)
    for auto in autot:
        print(auto)