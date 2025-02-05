luvut = []
while Ture:
    luku = input ("syötä luku ( tai jätä tyhjä lopuksi")
    if luku == "":

    else:
        luvut.append(luku)
        print("Viisi suurinta luku ovat:")
        for luku in luvut [:5]:
            print(luku)