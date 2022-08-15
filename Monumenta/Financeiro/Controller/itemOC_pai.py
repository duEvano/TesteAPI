import wrikeUtil
from Monumenta.Financeiro.Model.ItemOC_pai import itemOC_pai as itemP
from Monumenta.Financeiro.Model.itemOC import itemOC as itemO
import Monumenta.Financeiro.constante_financeiras as cFin


class itemOC_Pai:
    def __init__(self):
        id = ''

    def loadItemPai(self, id,listaFilhos):
        # print(listaFilhos)
        jsonData = wrikeUtil.loadByChild(listaFilhos)
        listaP = []
        listaO = []

        jsonDataTask = wrikeUtil.loadTaskDescendent(id=id)
        for f in jsonDataTask['data']:
            #print(f['title'])
            i = itemO(f['id'], f['title'])
            if f['description'] != '':
                i.descricao = """<br/>""" + f['description']
            i.parentID = f['parentIds'][0]
            for ct in f['customFields'] :
                if ct['id'] == cFin.ID_CUSTOM_VALOR_UNITARIO:
                    i.valor = ct['value']
                if ct['id'] == cFin.ID_CUSTOM_VALOR_REAL:
                    i.valorReal = ct['value']
                if ct['id'] == cFin.ID_CUSTOM_VALOR_HONORARIO:
                    i.honorario = ct['value']
                if ct['id'] == cFin.ID_CUSTOM_QTD:
                    i.qtd = ct['value']
                if ct['id'] == cFin.ID_CUSTOM_VALOR_ENCARGO:
                    i.encargo = ct['value']
                if ct['id'] == cFin.ID_CUSTOM_BOX_TIPO_CUSTO:
                    i.tipoCusto = ct['value']

            listaO.append(i)

        for f in jsonData['data']:
            i = itemP(f['id'],f['title'])
            listaP.append(i)

        for x in listaO:
            for y in listaP :
                if(x.parentID == y.id) :
                    y.itens.append(x)
                    y.somaGeral = float(y.somaGeral) + float(x.valorReal)


        for x in listaP:
            print(x.titulo)
            for y in x.itens :
                print(y.titulo)

        return listaP #print(x.titulo + '-' +x.valor + '-' +x.parentID)