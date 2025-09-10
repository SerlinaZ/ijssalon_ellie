prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}
aanbieding = prijzen["aardbei"] * 0.8
#Het euro teken geeft enorme errors en het lukt me niet dit op te lossen, vandaar de E als euroteken.
reclame_tekst = "Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts E {}".format(aanbieding)
#In de nieuwere versies zou dit het moeten zijn: reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts E {aanbieding}"
reclame_tekst2 = reclame_tekst[:63]
#Bij mij komen er dus geen extra nullen als waarde te staan... Maar dit is hoe het zou moeten.
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split(" ")
for el in reclame_tekst4:
    if len(el) > 4:
        print(el.upper())
    else:
        print(el.lower())