class Dictionary:
    def __init__(self):

        self._dict = []

    def loadDictionary(self,path): #legge un file(elenco di parole italiane) e salva le parole
        #le salva in una lista che è nel costruttore e che ho chiamato _dict
        with open(path,"r",encoding="utf-8") as file:
            for line in file:
                riga = line.strip()
                self._dict.append(riga)

    def printAll(self): #stampa tutte le parole salvate
        for element in self._dict:
            print(element)


    @property
    def dict(self):
        return self._dict