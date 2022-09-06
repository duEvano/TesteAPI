from datetime import timedelta, datetime,date

from data import datareader
from Monumenta.Projetos.model.Projeto import Projeto as proModel


class oc:

    def __init__(self):
        self.__logoEmpresa = ''
        self.__enderecoEmpresa = ''
        self.__porcentagem = ''
        self.__imposto = ''
        self.__seed = 1
        self.__id = ''
        self.__dataOC = ''
        # todo : Preciso verificar se já existe um numero de OC, senão nem relo aqui
        self.__numero = ''
        self.__permalink = ''
        self.__titulo = ''
        self.__projeto = None
        self.__metaDados = ''
        self.__listaOrcamento = []
        self.__totais = None
        self.__dataGeracao = date.today()
        self.__nomeArquivo = ''
        self.__dataValidade = None

    def getLogo(self):
        return self.__sigla

    def setLogo(self, s):
        self.__sigla = s

    logo = property(getLogo, setLogo)

    def getEnderecoEmpresa(self):
        return self.__enderecoEmpresa

    def setEnderecoEmpresa(self, s):
        self.__enderecoEmpresa = s

    endererecoEmpresa = property(getEnderecoEmpresa, setEnderecoEmpresa)

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

    def getData(self):
        return self.__dataOC

    def setData(self, s):
        self.__dataOC = s

    data = property(getData, setData)



    def getNumOC(self):
        return self.__numero

    def setNumOC(self, s):
        self.__numero = s

    numeroOC = property(getNumOC, setNumOC)

    def getPermalink(self):
        return self.__permalink

    def setPermalink(self, s):
        self.__permalink = s

    permalink = property(getPermalink, setPermalink)

    def getProjeto(self):
        return self.__projeto

    def setProjeto(self, p: proModel):
        self.__projeto = p

    projeto = property(getProjeto, setProjeto)

    def getListaOrcamento(self):
        return self.__listaOrcamento

    def setListaOrcamento(self, p):
        self.__listaOrcamento = p

    listaOrcamento = property(getListaOrcamento, setListaOrcamento)

    def getTotais(self):
        return self.__totais

    def setTotais(self, p: proModel):
        self.__totais = p

    totais = property(getTotais, setTotais)

    def getNomeArquivo(self):
        return self.__nomeArquivo

    def setNomeArquivo(self, p: proModel):
        self.__nomeArquivo = p

    nomeArquivo = property(getNomeArquivo, setNomeArquivo)

    def getDataValidade(self):
        date_time_obj = self.__dataGeracao + timedelta(days=30)
        return date_time_obj.strftime("%d/%m/%Y")

    def setDataValidade(self, p: datetime):
        self.__dataValidade = p.strftime("%d/%m/%Y")

    dataValidade = property(getDataValidade, setDataValidade)

    def getDataGeracao(self):
        return self.__dataGeracao.strftime("%d/%m/%Y")

    def setDataGeracao(self, p: datetime):
        self.__dataGeracao = p.strftime("%d/%m/%Y")

    dataGeracao = property(getDataGeracao, setDataGeracao)
