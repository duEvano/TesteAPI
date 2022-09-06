import wrikeUtil
from Monumenta.Financeiro.Model.oc import oc as ocModel
from Monumenta.Financeiro.Controller.oc import oc as ocC
import Monumenta.Financeiro.Model.oc_constantes
from utils.pdf.pdf_orcamento import pdf_orcamento
from data import datareader
import os


class oc:
    def __init__(self, id):
        self.__id = id
        self.__permalink = ''

    def __init__(self, per,id):
        self.__permalink = per
        self.__id = id

    def gerarPDF(self):
        my_oc = ocModel()
        print ('chegamos na geracao')
        if self.__permalink != '':
            jsonData =  wrikeUtil.loadByPermalink(self.__permalink,True)
            self.__id = jsonData['data'][0]['id']
        print('Temos o permalink' + self.__permalink)

        nome_logo = 'logoMonu.png'

        directory = './static/'

        file_path = os.path.join(directory, nome_logo)
        ocregra = ocC(self.__id)
        print('Iniciamos a regra OC')
        my_oc = ocregra.loadOcbyPermalink()
        print('Carregamos os dados')
        my_oc.logo = file_path
        my_oc.endererecoEmpresa = Monumenta.Financeiro.Model.oc_constantes.ENDERECO_MONU
        pdf = pdf_orcamento(myOC=my_oc)
        r = pdf.go()
        return r


# ocx = oc('IEADYSXZI435UATJ')
# ocx.gerarPDF()
