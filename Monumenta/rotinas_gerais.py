# atualizat todas as tarefas de uma pasta colocando o custo interno dentro da combo de tipo de custo
import bb.banco_do_brasil
import constantes_gerais
import wrikeUtil
import Monumenta.Financeiro.constante_financeiras
from model.Fornecedor import Fornecedor
import Monumenta.Financeiro.valores_itens
import utils.html_factore
import pandas as pd


def atualiza_BBDIGITAL(idFolder):
    q = 'descendants=true&subTasks=true&customField={"id":"' + Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_VALOR_UNITARIO + '","comparator":"IsNotEmpty"}&fields=["hasAttachments","sharedIds","superTaskIds","parentIds","authorIds","responsibleIds","recurrent","customFields","subTaskIds","description","briefDescription","attachmentCount","dependencyIds","superParentIds","metadata"]'
    jsonData = wrikeUtil.WrikeResponse('/folders/' + idFolder + '/tasks', q)
    arrC = []
    arrV = []
    arrC.append(Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_BOX_TIPO_CUSTO)
    arrV.append('🤑Custo Interno - Agência')
    qtd = 0
    for row in jsonData['data']:
        wrikeUtil.update_custom_field(row['id'], arrC, arrV)
        qtd = qtd + 1
        print(qtd)

    # for i in row['customFields']:


def atualiza_BBDIGITALHonorarios(idFolder):
    qtd = 0
    q = 'descendants=true&subTasks=true&customField={"id":"' + Monumenta.Financeiro.constante_financeiras.ID_TEM_HONORARIO + '","comparator":"IsNotEmpty"}&fields=["hasAttachments","sharedIds","superTaskIds","parentIds","authorIds","responsibleIds","recurrent","customFields","subTaskIds","description","briefDescription","attachmentCount","dependencyIds","superParentIds","metadata"]'
    jsonData = wrikeUtil.WrikeResponse('/folders/' + idFolder + '/tasks', q)
    arrC = []
    arrV = []
    arrC.append(Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_BOX_TIPO_CUSTO)
    arrV.append('🙃Custo Terceiro c/ honorário')
    for row in jsonData['data']:
        qtd = qtd + 1
        wrikeUtil.update_custom_field(row['id'], arrC, arrV)
        print(qtd)

        # wrikeUtil.update_custom_field(row['id'],arrC,arrV)


def atualiza_tipo_custo(idFolder):
    q = 'descendants=true&subTasks=true&customField={"id":"' + Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_VALOR_UNITARIO + '","comparator":"IsNotEmpty"}&fields=["hasAttachments","sharedIds","superTaskIds","parentIds","authorIds","responsibleIds","recurrent","customFields","subTaskIds","description","briefDescription","attachmentCount","dependencyIds","superParentIds","metadata"]'
    jsonData = wrikeUtil.WrikeResponse('/folders/' + idFolder + '/tasks', q)
    q1 = ''
    arrC = []
    arrV = []
    arrC.append(Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_BOX_TIPO_CUSTO)
    arrV.append('🤑Custo Interno - Agência')
    qtd = 0
    for row in jsonData['data']:
        arrV[0] = '🙃Custo Terceiro c/ honorário'
        jsonData2 = wrikeUtil.WrikeResponse('/tasks/' + row['id'], q1)
        for r in jsonData2['data']:
            jsonCustomField = row['customFields']
            arr = wrikeUtil.get_tuplaCustomFields(jsonCustomField)

            for i in arr:
                if i.id == Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_CUSTO_INTERNO:
                    if i.valor == 'true':
                        arrV[0] = '🤑Custo Interno - Agência'
                    else:
                        arrV[0] = '🙃Custo Terceiro c/ honorário'
                    break
            # print(row['title'])
            qtd = qtd + 1
            print(qtd)
            wrikeUtil.update_custom_field(row['id'], arrC, arrV)

            # wrikeUtil.update_custom_field(row['id'], )


def atualiza_custo_interno_correto(idFolder):
    q = 'descendants=true&subTasks=true&customField={"id":"' + Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_VALOR_UNITARIO + '","comparator":"IsNotEmpty"}&fields=["hasAttachments","sharedIds","superTaskIds","parentIds","authorIds","responsibleIds","recurrent","customFields","subTaskIds","description","briefDescription","attachmentCount","dependencyIds","superParentIds","metadata"]'
    jsonData = wrikeUtil.WrikeResponse('/folders/' + idFolder + '/tasks', q)
    arrc = ['IEADYSXZJUACYMQE']
    arrv = ['Custo Interno - Agência']
    arrv2 = ['Custo Terceiro c/ honorário']
    for row in jsonData['data']:
        # wrikeUtil.update_custom_field(row['id'],arrc,arrv)
        for i in row['customFields']:
            if (i['id'] == 'IEADYSXZJUABRTMH'):
                if (i['value'] == 'true'):
                    wrikeUtil.update_custom_field(row['id'], arr_campos=arrc, arr_valores=arrv)
                if (i['value'] == 'false'):
                    wrikeUtil.update_custom_field(row['id'], arr_campos=arrc, arr_valores=arrv2)
                if (i['value'] == ''):
                    wrikeUtil.update_custom_field(row['id'], arr_campos=arrc, arr_valores=arrv2)
                break


def get_nome_itens(idFolder):
    q = 'descendants=true&subTasks=true&customField={"id":"' + Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_VALOR_UNITARIO + '","comparator":"IsNotEmpty"}&fields=["hasAttachments","sharedIds","superTaskIds","parentIds","authorIds","responsibleIds","recurrent","customFields","subTaskIds","description","briefDescription","attachmentCount","dependencyIds","superParentIds","metadata"]'
    jsonData = wrikeUtil.WrikeResponse('/folders/' + idFolder + '/tasks', q)
    posicaoInicial = 0
    posicaoFinal = 0
    item = ''
    arrC = []
    arrV = []
    arrC.append('IEADYSXZJUACY4U2')
    arrV.append('')
    for row in jsonData['data']:
        posicaoInicial = str(row['title']).find('::') + len('::')
        posicaoFinal = len(str(row['title']))
        item = str(row['title'])[posicaoInicial:posicaoFinal].strip()
        arrV[0] = item.upper()
        wrikeUtil.update_custom_field(row['id'], arrC, arrV)
        # print(row['title'])
        # print(item)


def set_nome_itens(idFolder, alias):
    q = 'descendants=true&subTasks=true&customField={"id":"' + Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_VALOR_UNITARIO + '","comparator":"IsNotEmpty"}&fields=["hasAttachments","sharedIds","superTaskIds","parentIds","authorIds","responsibleIds","recurrent","customFields","subTaskIds","description","briefDescription","attachmentCount","dependencyIds","superParentIds","metadata"]'
    jsonData = wrikeUtil.WrikeResponse('/folders/' + idFolder + '/tasks', q)
    posicaoInicial = 0
    posicaoFinal = 0
    item = ''
    arrC = []
    arrV = []
    arrC.append('IEADYSXZJUACZH5K')
    arrV.append('')
    for row in jsonData['data']:
        arrV[0] = alias
        wrikeUtil.update_custom_field(row['id'], arrC, arrV)
        # print(row['title'])
        # print(item)


# get_nome_itens('IEADYSXZI4XRC3VJ')
# atualiza_BBDIGITAL('IEADYSXZI4QSY6MC')
# atualiza_BBDIGITALHonorarios('IEADYSXZI4QSY6MC')
# atualiza_tipo_custo('IEADYSXZI42WLTE7')
# atualiza_tipo_custo('IEADYSXZI4YFQDE2')
def teste_chamadas(idTask):
    # f = Fornecedor(idTask)
    # wrikeUtil.updatecampo(idTask, 'description', f.get_description())
    # print(wrikeUtil.getTaskByCustomField('IEADYSXZI42PKFWO','','IEADYSXZJUABRZBZ','1212121'))
    f = Fornecedor(cnpj='1212121', idTask='')
    print(f.nome)


# # brain
# get_nome_itens('IEADYSXZI4XOLHGB')
# # seo
# get_nome_itens('IEADYSXZI4XOLEYN')
# # blog
# get_nome_itens('IEADYSXZI4ZJCWK3')
# # admin
# get_nome_itens('IEADYSXZI4ZLXX42')
# # 3.0
# get_nome_itens('IEADYSXZI4ZQKDT7')
# # 3.0 2021
# get_nome_itens('IEADYSXZI4TBD7CH')

# id do alias
# IEADYSXZJUACZH5K
# Brain
# set_nome_itens('IEADYSXZI4XOLHGB','Brain')

# # seo
# set_nome_itens('IEADYSXZI4XOLEYN', 'SEO')
# # blog
# set_nome_itens('IEADYSXZI4ZJCWK3','BLOG')
# # admin
# set_nome_itens('IEADYSXZI4ZLXX42','ADMIN')
# # 3.0td
# set_nome_itens('IEADYSXZI4ZQKDT7','Portal 3.0')
# # 3.0 2021
# set_nome_itens('IEADYSXZI4TBD7CH','Portal 3.0 2021')
# Portal 4.0
# set_nome_itens('IEADYSXZI4XRC3VJ','Portal 4.0')

# Manutençao 3.0
# set_nome_itens('IEADYSXZI4QUHXN7','Manutenção Portal 3.0 ')

def updateValoresDigitais(idFolder):
    querystring = 'descendants=true&subTasks=true&customField={"id":"IEADYSXZJUABQ27R","comparator":"IsNotEmpty"}&fields=["hasAttachments","sharedIds","superTaskIds","parentIds","authorIds","responsibleIds","recurrent","customFields","subTaskIds","description","briefDescription","attachmentCount","dependencyIds","superParentIds","metadata"]'
    jsonData = wrikeUtil.WrikeResponse('/folders/' + idFolder + '/tasks', querystring)
    for row in jsonData['data']:
        Monumenta.Financeiro.valores_itens.calculosValoreItens(idtask=row['id'], porcentagemHonor=5)


def updatemeseData(idFolder):
    querystring = 'descendants=true&subTasks=true&customField={"id":"IEADYSXZJUACXE75","comparator":"IsNotEmpty"}&fields=["hasAttachments","sharedIds","superTaskIds","parentIds","authorIds","responsibleIds","recurrent","customFields","subTaskIds","description","briefDescription","attachmentCount","dependencyIds","superParentIds","metadata"]'
    jsonData = wrikeUtil.WrikeResponse('/folders/' + idFolder + '/tasks', querystring)
    for row in jsonData['data']:
        bb.banco_do_brasil.atualiza_data_trocastatus(row['id'])


def updateValoresPromo(idFolder):
    querystring = 'descendants=true&subTasks=true&customField={"id":"IEADYSXZJUABQ27R","comparator":"IsNotEmpty"}&fields=["hasAttachments","sharedIds","superTaskIds","parentIds","authorIds","responsibleIds","recurrent","customFields","subTaskIds","description","briefDescription","attachmentCount","dependencyIds","superParentIds","metadata"]'
    jsonData = wrikeUtil.WrikeResponse('/folders/' + idFolder + '/tasks', querystring)
    qtd = 0
    for row in jsonData['data']:
        qtd = qtd + 1
        # Monumenta.Financeiro.valores_itens.calculosValoreItens(idtask=row['id'], porcentagemHonor=5)
        print(qtd)


# updateValoresPromo('IEADYSXZI42WLTE7') #DIPES
# dimac
# updateValoresPromo('IEADYSXZI42WLTDF') #

def importFornecedores():
    df = pd.read_excel('C:\\Users\\etavares\\Downloads\\fronecedoresNovos.xls', sheet_name=1)
    idNovatask = ''
    for i in df.index:
        print(df["Nome"][i])
        d = {
            'title': df['Nome'][i],
            'description': '',
        }
        url = 'folders/IEADYSXZI42PKFWO/tasks'
        jsonData = wrikeUtil.WrikePost(url, d)
        idNovatask = ''
        print(jsonData)
        for row in jsonData['data']:
            idNovatask = row['id']

        lista_campos = [
            'IEADYSXZJUABRZBZ',  # CNPJ
            'IEADYSXZJUACYYSO'  # razao social
            , 'IEADYSXZJUACY4R2'  # inscri municiapl
            , 'IEADYSXZJUACY4R5'  # tipoSevico
            , 'IEADYSXZJUACY4R6'  # apelido,
            , 'IEADYSXZJUACY4R7'  # edenreco
            , 'IEADYSXZJUACY4SA'  # edenrecoCobranca
            , 'IEADYSXZJUACY4SB'  # Telefone
            , 'IEADYSXZJUACZAC4'  # email

            # constantes_gerais.ID_CUSTOM_EH_FATURAVEL,
            # constantes_gerais.ID_CUSTOM_CUSTO_INTERNO,
            # constantes_gerais.ID_CUSTOM_TOTAL_REAL
        ]
        lista_valores = [
            df['CGC'][i],
            df['RAZAO_SOC'][i],
            df['INSCRICAO'][i],
            df['TipoServico'][i],
            df['Nome'][i],
            df['Endereco Completo'][i],
            df['Endereco Completo'][i],
            df['TELEFONE'][i],
            df['EMAIL'][i]
            # demanda01.get_valorTotal(),
            # 'true',
            # 'true',
            # demanda01.get_valorTotal()
        ]
        wrikeUtil.update_custom_field(idtask=idNovatask, arr_campos=lista_campos, arr_valores=lista_valores)

    return ''


# importFornecedores()
# BB seguros -> IEADYSXZI4Q75BUA

def updateValoresBBSeguros(idFolder):
    querystring = 'descendants=true&subTasks=true&customField={"id":"IEADYSXZJUABQ27R","comparator":"IsNotEmpty"}&fields=["hasAttachments","sharedIds","superTaskIds","parentIds","authorIds","responsibleIds","recurrent","customFields","subTaskIds","description","briefDescription","attachmentCount","dependencyIds","superParentIds","metadata"]'
    jsonData = wrikeUtil.WrikeResponse('/folders/' + idFolder + '/tasks', querystring)
    qtd = 0
    for row in jsonData['data']:
        qtd = qtd + 1
        Monumenta.Financeiro.valores_itens.calculosValoreItens(idtask=row['id'], porcentagemHonor=5)
        print(qtd)

updateValoresBBSeguros('IEADYSXZI4Q75BUA')