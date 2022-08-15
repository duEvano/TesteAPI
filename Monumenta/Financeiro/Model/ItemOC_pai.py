class itemOC_pai:
    def __init__(self):
        self.__titulo = ''
        self.__soma = 0
        self.__id = ''
        self.__itens = []
        self.__desc = ''

    def __init__(self,id,title):
        self.__titulo = title
        self.__soma = 0
        self.__id = id
        self.__itens = []
        self.__desc = ''


    def getTitulo(self):
        return self.__titulo

    def setTitulo(self, s):
        self.__titulo = s

    titulo = property(getTitulo, setTitulo)

    def getID(self):
        return self.__id

    def setID(self, s):
        self.__id = s

    id = property(getID, setID)

    def getItens(self):
        return self.__itens

    def setItens(self, s):
        self.__itens = s

    itens = property(getItens, setItens)

    def getSomaGeral(self):
        return self.__soma

    def setSomaGeral(self, s):
        self.__soma = s

    somaGeral = property(getSomaGeral, setSomaGeral)
