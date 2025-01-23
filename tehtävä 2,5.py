import math

print("Anna leiviskät")
leiviskät = float(input())
print("Anna naulat")
naulat = float(input())
print("Anna luodit")
luodit = float(input())

grammoina = ((leiviskät * 20 * 32) + (naulat * 32) + luodit) * 13.3
kilot = math.floor(grammoina / 1000)
jämägrammat = grammoina - (kilot * 1000)

print("Massa nykymittojen mukaan:")
print(f"{kilot} kilogrammaa ja {jämägrammat:.2f} gramma")
