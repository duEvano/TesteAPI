import Monumenta.Cliente.constantes_cliente
import wrikeUtil
from Monumenta.Financeiro.Model.oc import oc as ocModel
from Monumenta.Financeiro.Controller.itemOC_pai import itemOC_Pai as itemPai
from Monumenta.Projetos.model.Projeto import Projeto as proModel
from Monumenta.Projetos.controller.Projeto import Projeto as proRegra
import Monumenta.Financeiro.Model.oc_constantes as ocConstantes
from Monumenta.Financeiro.Model.itemOC import itemOC as itemO
from Monumenta.Financeiro.Model.totalizadores import totalizadores as totais
from data import datareader
from datetime import date

class oc:

    def __init__(self, p):
        self.__id = p
        self.__paizao = None
        self.__listaPais =[]

    def loadOcbyPermalink(self):
        ch = []
        ch.append(self.__id)
        jsonData = wrikeUtil.loadByChild(ch)
        # print (jsonData)
        ocX = ocModel()
        parentid = ''
        jsonCustomField = None
        temmetaid = False
        idPaizao = ''
        for row2 in jsonData['data'][0]['customFields']:
            if row2['id'] == ocConstantes.ID_CUSTOM_PAI and row2['value'] != '':
                idPaizao = row2['value']
                temmetaid = True
            if row2['id'] == ocConstantes.ID_CUSTOM_DATA_OC:
                ocX.data = row2['value']
            if row2['id'] == ocConstantes.ID_CUSTOM_NUMERO_OC:
                ocX.numeroOC = row2['value']



        for row in jsonData['data']:
            #ocX.permalink = self.__permanlink
            ocX.id = row['id']
            if temmetaid:
                parentid = idPaizao
            else:
                parentid = row['parentIds'][0]

                # print(jsonData['data'][0]['childIds'])
        it = itemPai()
        ocX.listaOrcamento = it.loadItemPai(listaFilhos=jsonData['data'][0]['childIds'], id=ocX.id)
        print(self.__listaPais)
        totaisX = totais()
        for y in ocX.listaOrcamento:
            for i in y.itens:
                totaisX.totalHonorarios = float(totaisX.totalHonorarios) + float(i.honorario)
                totaisX.totalEncargos = float(totaisX.totalEncargos) + float(i.encargo)
                totaisX.totalGeral = float(totaisX.totalGeral) + float(i.valorReal)
                if(i.tipoCusto == '🤑Custo Interno - Agência') :
                    totaisX.totalCustoInterno = float(totaisX.totalCustoInterno) + (float(i.valor) * float(i.qtd))
                if i.tipoCusto == '🙃Custo Terceiro c/ honorário' or i.tipoCusto == '😪Custo Terceiro s/ honorário':
                    totaisX.totalCustoTerceiros = float(totaisX.totalCustoTerceiros) + (float(i.valor) * float(i.qtd))

        ocX.totais = totaisX
        #aqui calcula os totais
        self.loadParent(parentid, True)
        tah_dentro_de_OC = True
        if ocX.numeroOC == '':
            tah_dentro_de_OC = False
            for r in self.__listaPais :
                if r == '2 - OCs' or r == 'OCs' or r == '1 - Orçamentos' or r =='2 - Orçamentos':
                    tah_dentro_de_OC = True
                    break
        if not tah_dentro_de_OC :
            raise Exception("O orçamento precisa estar dentro da pasta de OCs")

        idPaizao = self.__paizao['id']
        pr = proRegra(idPaizao)
        ocX.projeto = pr.loadProjeto()
        if ocX.numeroOC == '':
            ocX.numeroOC = datareader.readSeed('num_oc')
            ocX.data = date.today().strftime("%d/%m/%Y")

        if not temmetaid:
            arrCampos = []
            arrValores = []
            arrCampos.append(ocConstantes.ID_CUSTOM_PAI)
            arrCampos.append(ocConstantes.ID_CUSTOM_NUMERO_OC)
            arrCampos.append(ocConstantes.ID_CUSTOM_DATA_OC)

            arrValores.append(idPaizao)
            arrValores.append(ocX.numeroOC)
            arrValores.append(ocX.data)

            wrikeUtil.update_custom_field_folder(ocX.id,arr_campos=arrCampos,arr_valores=arrValores)


        #o link irá gerar sempre as informações da tarefa !
        #vou colocar fora do if para que possa sempre atualizar os valores
        str_descricao = """Orçamento {0} <br/>Número da OC : {1} <br/>Data de geração: {2} <br/>Clique o link para download <br/> {3}"""
        descricaoComLink = """<a href='https://wrike-api-hml.azurewebsites.net/downloadOc?id={0}' target='_blank'>Orçamento</a>"""
        descricaoComLink = descricaoComLink.format(ocX.id)
        retornoString = str_descricao.format(ocX.projeto.titulo,ocX.numeroOC,ocX.data,descricaoComLink)
        wrikeUtil.updatecampo_folder(ocX.id,'description',retornoString)
        return ocX

    def loadParent(self, ID, isFolder):
        q = ID
        # q = q + '?fields=["hasAttachments","customFields","description","superParentIds","metadata"]'
        url = 'folders' if isFolder else "task"
        jsonData = wrikeUtil.WrikeResponse('/' + url + '/' + ID, '')

        #print(jsonData)
        self.__listaPais.append(jsonData['data'][0]['title'])
        print(self.__listaPais)
        idparente = ''
        #um teste alem
        for row in jsonData['data']:
            try:
                idparente = row['project']
                self.__paizao = row
                break
            except Exception as e:
                self.loadParent(row['parentIds'][0], isFolder)
                print('aqui q tá a recursividade' + str(e))
                break
