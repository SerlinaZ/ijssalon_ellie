def decoreer(tekst=""):
    tekst = "header"
    lengte = len(tekst) + 4
    print
    print(lengte * "*")
    print("* {0} *".format(tekst))
    print(lengte * "*")
    print

def fooi_pp(bedrag, personen):
    bedrag_pp = bedrag / personen
    return "Het bedrag per persoon is {0} euro".format(bedrag_pp)

def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

def som(dictionary):
    return sum(dictionary.values())