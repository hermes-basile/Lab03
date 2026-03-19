import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input("inserisci un numero da 1 a 4:")
    if txtIn.isdigit() and int(txtIn)<=4 and int(txtIn)>0:

        if int(txtIn) == 1:
            print("Inserisci la tua frase in Italiano\n")
            txtIn = input()
            sc.handleSentence(txtIn,"italian")
            continue

        if int(txtIn) == 2:
            print("Inserisci la tua frase in Inglese\n")
            txtIn = input()
            sc.handleSentence(txtIn,"english")
            continue

        if int(txtIn) == 3:
            print("Inserisci la tua frase in Spagnolo\n")
            txtIn = input()
            sc.handleSentence(txtIn,"spanish")
            continue

        if int(txtIn) == 4:
            break
    else:
        print("hai sbagliato inserimento, può essere solo un numero da 1 a 4.")

