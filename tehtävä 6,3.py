("gallonat_litroiksi")
("gallonat * 3.785")
while True:
    gallonat = float(input("Anna bensiinimäärä gallonina: "))
if gallonat < 0:
    litrat = gallonat_litroiksi(gallonat)
    print(f"{gallonat} gallonaa on {litrat:.2f} litraa.")