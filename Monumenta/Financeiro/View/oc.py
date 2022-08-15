from Monumenta.Financeiro.Model.oc import oc as ocModel
from Monumenta.Financeiro.Controller.oc import oc as ocC
import Monumenta.Financeiro.Model.oc_constantes
from utils.pdf.pdf_orcamento import pdf_orcamento
from data import datareader


class oc:
    def __init__(self,id):
        self.__id = id

    def gerarPDF(self):
        my_oc = ocModel()
        ocregra = ocC(self.__id)

        my_oc = ocregra.loadOcbyPermalink()
        my_oc.logo = Monumenta.Financeiro.Model.oc_constantes.LOGO_MONU
        my_oc.endererecoEmpresa = Monumenta.Financeiro.Model.oc_constantes.ENDERECO_MONU
        pdf = pdf_orcamento(myOC=my_oc)
        r = pdf.go()
        return r

ocx = oc('IEADYSXZI435UATJ')
ocx.gerarPDF()
