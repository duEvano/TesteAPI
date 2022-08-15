class Cliente:
    def __init__(self):
        self.__apelido = ''
        self.__sigla = ''
        self.__porcentagem = ''
        self.__imposto = ''
        self.__seed = 1
        self.__id = ''
        self.__nome = ''
        self.__cnpj = ''
        self.__insc = ''
        self.__endereco = ''

    def __init__(self, apelido):
        self.__apelido = apelido
        self.__sigla = ''
        self.__porcentagem = ''
        self.__imposto = ''
        self.__seed = 1

    def getSigla(self):
        return self.__sigla

    def setSigla(self, s):
        self.__sigla = s

    sigla = property(getSigla, setSigla)

    def getSeed(self):
        return self.__seed

    def setSeed(self, s):
        self.__seed = s

    seed = property(getSeed, setSeed)

    def getApelido(self):
        return self.__apelido

    def setApelido(self, s):
        self.__apelido = s

    apelido = property(getApelido, setApelido)

    def getID(self):
        return self.__id

    def setID(self, s):
        self.__id = s

    id = property(getID, setID)

    def getNome(self):
        return self.__nome

    def setNome(self, s):
        self.__nome = s

    nome = property(getNome, setNome)

    def getCNPJ(self):
        return self.__cnpj

    def setCNPJ(self, s):
        self.__cnpj = s

    cnpj = property(getCNPJ, setCNPJ)

    def getInsc(self):
        return self.__insc

    def setInsc(self, s):
        self.__insc = s

    inscr = property(getInsc, setInsc)

    def getEndereco(self):
        return self.__endereco

    def setEndereco(self, s):
        self.__endereco = s

    endereco = property(getEndereco, setEndereco)
