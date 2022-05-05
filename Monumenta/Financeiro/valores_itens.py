import model.task_financeira

# todo : zerar todos campos de valor real
# todo : se tem custo interno a receita será igual a custo interno
# todo : não tem custo ? e tem honorário -
#   todo : Valor honorário = Valor (qtd * valor uinitario) * %honorario
#   todo : Valor total Real = Valor total + valro honrário
#   todo : receita = valor honorário
import wrikeUtil
import Monumenta.Financeiro.constante_financeiras


def calculosValoreItens(idtask):
    # todo : procurar valor da porcentagem do honorário

    jsonData = wrikeUtil.WrikeResponse('/tasks/' + idtask, '')

    for row in jsonData['data']:
        jsonCustomField = row['customFields']

    arr = wrikeUtil.get_tuplaCustomFields(jsonCustomField)

    qtd = 1
    v = 0
    c = False
    perc = 5
    vTemp = '0'
    for i in arr:
        if i.id == Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_CUSTO_INTERNO:
            c = i.valor
        else:
            if i.valor == '':
                vTemp = '0'
            else:
                vTemp = i.valor

        if i.id == Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_QTD:
            qtd = int(vTemp)

        if i.id == Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_VALOR_UNITARIO:
            v = float(str(vTemp))

    taskF = model.task_financeira.task_financeira(qtd=qtd, valor=v, custo_interno=c, percertualHonor=perc)

    arrCampos = [
        Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_VALOR_HONORARIO,
        Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_VALOR_REAL,
        Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_RECEITA
    ]
    arrValores = [
        taskF.get_valorHonorario(),
        taskF.get_valorTotalReal(),
        taskF.get_valorReceita()
    ]
    wrikeUtil.update_custom_field(idtask, arrCampos, arrValores)


# querystring = 'descendants=true&subTasks=true&customField={"id":"IEADYSXZJUABQ27R","comparator":"IsNotEmpty"}&fields=["hasAttachments","sharedIds","superTaskIds","parentIds","authorIds","responsibleIds","recurrent","customFields","subTaskIds","description","briefDescription","attachmentCount","dependencyIds","superParentIds","metadata"]'

# calculosValoreItens('IEADYSXZKQ2P6TL2')
q = 'descendants=true&subTasks=true&customField={"id":"IEADYSXZJUABQ27R","comparator":"IsNotEmpty"}&fields=["hasAttachments","sharedIds","superTaskIds","parentIds","authorIds","responsibleIds","recurrent","customFields","subTaskIds","description","briefDescription","attachmentCount","dependencyIds","superParentIds","metadata"]'
jsonData = wrikeUtil.WrikeResponse('/folders/IEADYSXZI4YUR7SB/tasks', q)
temreceita = False
for row in jsonData['data']:
    for i in row['customFields']:
        if (i['id'] == 'IEADYSXZJUABVSGX' and i['value'] != ''):
            temreceita = True
    if not temreceita:
        calculosValoreItens(row['id'])
    temreceita = False
