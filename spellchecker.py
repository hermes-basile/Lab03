import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        print("Ricerca normale")
        inizio1 = time.time()
        md1= md.MultiDictionary()
        md1.searchWord(txtIn,language)
        lista_errate1 = md1.lista_errate
        fine1= time.time()
        for parola in lista_errate1:
            print(parola)
        print(f"Il tempo impiegato: {fine1-inizio1}")

        print("-"*30)
        print("Ricerca Lineare")
        inizio2 = time.time()
        md2=md.MultiDictionary()
        md2.searcWordLinear(txtIn,language)
        lista_errate2 = md2.lista_errate
        fine2= time.time()
        for parola in lista_errate2:
            print(parola)
        print(f"Il tempo impiegato: {fine2-inizio2}")
        print("-"*30)
        print("Ricerca dicotomica")
        misurazione_inizio = time.time()
        md3 = md.MultiDictionary()
        md3.searchWordDicotomyc(txtIn,language)
        lista_errate3 = md3.lista_errate
        for parola_errata in lista_errate3:
            print(parola_errata)
        misurazione_fine = time.time()
        print(f"il tempo misurato è:{misurazione_fine-misurazione_inizio}")





    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    da_cambiare = "-_.:,;!?\|/'"
    for char in da_cambiare:
        text = text.replace(char,"")
    return text