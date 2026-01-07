def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print
    print(lengte * "*")
    print("* {0} *".format(tekst))
    print(lengte * "*")
    print

def fooi_pp(bedrag, personen):
    try:
        bedrag_pp = bedrag / personen
    except:
        bedrag_pp = "??"
    return "Het bedrag per persoon is {0} euro".format(bedrag_pp)