import dictionary as d
import richWord as rw
import spellchecker


class MultiDictionary:

    def __init__(self):
        self.dictionary = {}
        self.lista_errate = []

        d_it = d.Dictionary() #creo un dictionary vuoto e gli do il nome di d_it
        d_it.loadDictionary("resources/Italian.txt") #dico al dictionary chiamato d_it, di usare il suo metodo "loadD.."

        d_en = d.Dictionary()
        d_en.loadDictionary("resources/English.txt")

        d_sp = d.Dictionary()
        d_sp.loadDictionary("resources/Spanish.txt")

        #a questo punto riempio il self.dictionary con chiave/valore
        self.dictionary["italian"] = d_it
        self.dictionary["english"] = d_en
        self.dictionary["spanish"] = d_sp



    def printDic(self, language):
        if language in self.dictionary:
            self.dictionary[language].printAll()





    def searchWord(self, words, language):
        lista_words= words.split() #prende una frase(words) e crea una lista parola per parola, sfruttando gli spazi

        if language in self.dictionary:
            lista_termini= self.dictionary[language].dict


            for parola in lista_words:
                rw1= rw.RichWord(parola)
                if parola in lista_termini:
                    rw1.corretta = True
                else:
                    rw1.corretta = False
                    self.lista_errate.append(rw1.__str__())

        else:
            raise ValueError("la lingua non è inserita o hai sbagliato a digitare language.")

    def searcWordLinear(self, words, language):
        words = spellchecker.replaceChars(words)

        lista_utente = words.split()
        if language in self.dictionary:
            dizionario = self.dictionary[language]
            lista_dizionario = dizionario.dict
            for parola in lista_utente:
                parola_trovata= False
                for termine in range(0,len(lista_dizionario)):
                    if parola == lista_dizionario[termine]:
                        parola_trovata = True
                        continue

                if parola_trovata == False:
                    self.lista_errate.append(parola)

    def searchWordDicotomyc(self,words,language):
        words = spellchecker.replaceChars(words)
        lista_parole = words.split()
        if language in self.dictionary:
            vocabolario = self.dictionary[language]
            lista_vocabolario = vocabolario.dict
            indice_parola = int(len(lista_vocabolario)/2)
            parola_confronto = lista_vocabolario[indice_parola]
            for parola in lista_parole:
                if parola < parola_confronto:
                    parola_trovata = False
                    for i in range(0,indice_parola):
                        if parola == lista_vocabolario[i]:
                            parola_trovata = True
                    if not parola_trovata == True:
                        self.lista_errate.append(parola)
                if parola> parola_confronto:
                    parola_trovata= False
                    for i in range(indice_parola,len(lista_vocabolario)):
                        if parola== lista_vocabolario[i]:
                            parola_trovata=True
                    if not parola_trovata == True:
                        self.lista_errate.append(parola)











