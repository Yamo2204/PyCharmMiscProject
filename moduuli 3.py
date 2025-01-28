# kirjoita ohjelma, joka kysyy käyttäjän iän
# jos ikä on Vähintään 18, tulostetaan "tervetulua"


print("Olen ravintolan poke")

ikä = int(input("kuinka vanha olet?"))


if ikä >= 23:
    print("tervetuloa!")

elif ikä == 18 or ikä == 19:
    print("Hmm, näytät aika nuorelta")
    vastaus = input("onko sinulle paperaita (kyllä/ei)?")
    if vastaus == "kyllä":
        print("noh, tule nyt sitten")
    else:
        print("hyvä yritys, mutta lähde kotiisi")



print("ohjelman suoritus loppuu")

