def ("luvut") :
    return [luku for luku in luvut if luku % 2 == 0]
def paaohjelma():
    luvut \= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu = karsi_parittomat(luvut)
    print(f"Alkuperäinen lista: {luvut}")
    print(f"Karsittu lista: {karsittu}")
