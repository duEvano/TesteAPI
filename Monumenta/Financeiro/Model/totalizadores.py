from Monumenta.Financeiro.Model.ItemOC_pai import itemOC_pai


class totalizadores:
    def __init__(self):
        self.__totalCustosInternos = 0
        self.__custoTerceiros = 0
        self.__subTotal = 0
        self.__honorarios = 0
        self.__total = 0
        self.__encargos = 0

        # carregando os totalizadores

    def getHonorario(self):
        return self.__honorarios

    def setHonorario(self, s):
        self.__honorarios = s

    totalHonorarios = property(getHonorario, setHonorario)

    def getCustoInterno(self):
        return self.__totalCustosInternos

    def setCustoInterno(self, s):
        self.__totalCustosInternos = s

    totalCustoInterno = property(getCustoInterno, setCustoInterno)

    def getCustoTerceiros(self):
        return self.__custoTerceiros

    def setCustoTerceiros(self, s):
        self.__custoTerceiros = s

    totalCustoTerceiros = property(getCustoTerceiros, setCustoTerceiros)

    def getEncargos(self):
        return self.__encargos

    def setEncargos(self, s):
        self.__encargos = s

    totalEncargos = property(getEncargos, setEncargos)

    def getTotalGeral(self):
        return self.__total

    def setTotalGeral(self, s):
        self.__total = s

    totalGeral = property(getTotalGeral, setTotalGeral)
