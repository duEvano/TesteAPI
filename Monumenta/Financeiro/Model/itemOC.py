class itemOC :
    def __init__(self):
        self.__titulo = ''
        self.__qtd = 0
        self.__valorReal = 0
        self.__valorUnit = 0
        self.__honorario = 0
        self. __encargo = 0
        self.__id = ''
        self.__idPai = ''
        self.__desc = ''
        self.__tipoCusto = ''


    def __init__(self, id, title):
        self.__titulo = title
        self.__id = id
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

    def getValor(self):
        return self.__valorUnit

    def setValor(self, s):
        self.__valorUnit = s

    valor = property(getValor, setValor)

    def getValorReal(self):
        return self.__valorReal

    def setValorReal(self, s):
        self.__valorReal = s

    valorReal = property(getValorReal, setValorReal)

    def getParentId(self):
        return self.__idPai

    def setParentId(self, s):
        self.__idPai = s

    parentID = property(getParentId, setParentId)

    def getHonorario(self):
        return self.__honorario

    def setHonorario(self, s):
        self.__honorario = s

    honorario = property(getHonorario, setHonorario)

    def getQtd(self):
        return self.__qtd

    def setQtd(self, s):
        self.__qtd = s

    qtd = property(getQtd, setQtd)

    def getEncargo(self):
        return self.__encargo

    def setEncargo(self, s):
        self.__encargo = s

    encargo = property(getEncargo, setEncargo)

    def getDesc(self):
        return self.__desc

    def setDesc(self, s):
        self.__desc = s

    descricao = property(getDesc, setDesc)

    def getTipoCusto(self):
        return self.__tipoCusto

    def setTipoCusto(self, s):
        self.__tipoCusto = s

    tipoCusto = property(getTipoCusto, setTipoCusto)