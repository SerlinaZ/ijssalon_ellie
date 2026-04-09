def presenteer(mijn_dict, totaal):
    for key, value in mijn_dict.items():
        print("{0} : {1} euro".format(key, value))
    print("==========================")
    print("Totaal : {0} euro".format(totaal))

