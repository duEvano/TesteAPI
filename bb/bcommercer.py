import wrikeUtil
import constantes_gerais
import bb.constantes_BB
from bb import constantes_BB
from model.BCommerce import demanda_Bcommerce
from utils import html_factore, formating


# todo : Desenvolver formas de capturar a entrada da demanda de BCommrcer

def criar_tarefa_orcamento(idtask):


    demanda01 = escuta_tarefa_entrada(idtask)
    d = {
        'title': '[numero DOAC] -' + demanda01.get_titulo(),
        'description': demanda01.get_descricaoNova(),
    }
    url = 'folders/' + constantes_BB.iD_FOLDER_DOAC_BCOMMERCE + '/tasks'
    jsonData = wrikeUtil.WrikePost(url, d)

    idNovatask = ''
    for row in jsonData['data']:
        idNovatask = row['id']

    lista_campos = [
                    constantes_gerais.ID_CUSTOM_QTDE,
                    constantes_gerais.ID_CUSTOM_VALOR_UNITARIO,
        constantes_gerais.ID_CUSTOM_EH_FATURAVEL,
        constantes_gerais.ID_CUSTOM_CUSTO_INTERNO,
        constantes_gerais.ID_CUSTOM_TOTAL_REAL
    ]
    lista_valores = [
        '1',
        demanda01.get_valorTotal(),
        'true',
        'true',
        demanda01.get_valorTotal()
    ]

    wrikeUtil.update_custom_field(idtask=idNovatask,arr_campos=lista_campos,arr_valores=lista_valores)

    return demanda01


def escuta_tarefa_entrada(idTask):
    # todo : buscar as tarefas e entram nessa pasta

    # q = 'permalink="https://www.wrike.com/open.htm?id=880649295"'
    querystring = ''
    #querystring = 'descendants=true&subTasks=true&fields=["hasAttachments","sharedIds","superTaskIds","parentIds","authorIds","responsibleIds","recurrent","customFields","subTaskIds","description","briefDescription","attachmentCount","dependencyIds","superParentIds","metadata"]'
    # todo : VALENDO - Mudar a constante da página

    jsonData = wrikeUtil.WrikeResponse('tasks/' + idTask, querystring)
    for row in jsonData['data']:
        description = row['description']

    demandaGeral = demanda_Bcommerce.demanda_Bcommerce(description)
    mkt = demandaGeral.get_mkt()

    # quebrar o demanda escrita pelo usuário
    # print(demandaGeral.get_demandaEscrita())
    print('Chegamos aqui')
    txt1 = html_factore.read_template_task('templates/item_Bcommerce_isolado.html')
    print('se passou daqui é pq tá na leitura')
    txt = ''
    valor_total = 0
    for p in demandaGeral.get_itens():
        txt = txt + txt1.format(p.get_numero(), p.get_description(), str(p.get_qtd()), p.get_apelido(),
                                formating.formatMoney(p.get_valorUnitario()), formating.formatMoney(p.get_valorTotal()))
        valor_total = valor_total + p.get_valorTotal()

    demandaGeral.set_valorTotal(valor_total)
    htmlfull = html_factore.read_template_task('templates/doac_Bcommercer.html')
    htmlfull = htmlfull.format(mkt, demandaGeral.get_demandaEscrita(), txt, formating.formatMoney(valor_total),
                               formating.formatMoney(valor_total),
                               str(demandaGeral.get_titulo()))
    # print(htmlfull)
    demandaGeral.set_descricaoNova(htmlfull)
    return demandaGeral





