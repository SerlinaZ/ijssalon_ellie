from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_nieuw = prijs - (prijs*korting)
    teruggeefwaarde = "Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {0}, van {1} euro voor {2} euro.".format(smaak, prijs, prijs_nieuw)
    #In de nieuwere versies zou dit het moeten zijn: f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_nieuw} euro."
    return teruggeefwaarde

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    #Opgave 6: return totaal
    bedrag = totaal * btw
    teruggeefwaarde = "Het totaal van alle inkomsten van deze week is {0} euro, waarover {1} euro btw betaald dient te worden.".format(totaal, bedrag)
    #In de nieuwere versies zou dit het moeten zijn: f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    return teruggeefwaarde

def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]

def gemiddelde(mijn_lijst):
    bedrag = sum(mijn_lijst) / len(mijn_lijst)
    #Opgave 9: return waarde
    uitvoer = "De gemiddelde inkomsten deze week zijn {0} euro.".format(bedrag)
    #In de nieuwere versies zou dit het moeten zijn: f"De gemiddelde inkomsten van deze week zijn {waarde} euro."
    return uitvoer

def meervoudig(invoer_lijst):
    waardes = laag_en_hoog(invoer_lijst)
    return waardes

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(*korte_lijst)
    return uitvoer

teruggeefwaarde = combinatie([10,5,3,2,1,2,9])
print(teruggeefwaarde)