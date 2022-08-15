import model.task_financeira

# todo : zerar todos campos de valor real
# todo : se tem custo interno a receita será igual a custo interno
# todo : não tem custo ? e tem honorário -
#   todo : Valor honorário = Valor (qtd * valor uinitario) * %honorario
#   todo : Valor total Real = Valor total + valro honrário
#   todo : receita = valor honorário
import wrikeUtil
import Monumenta.Financeiro.constante_financeiras
from model.Fornecedor import Fornecedor


def calculosValoreItens(idtask,porcentagemHonor):
    # todo : procurar valor da porcentagem do honorário

    jsonData = wrikeUtil.WrikeResponse('/tasks/' + idtask, '')

    for row in jsonData['data']:
        jsonCustomField = row['customFields']

    arr = wrikeUtil.get_tuplaCustomFields(jsonCustomField)
    tem_valores = False
    for x in arr:
        if x.id == Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_VALOR_UNITARIO:
            tem_valores = True
            break

    # validando se tem campo de valor unitário
    qtd = 1
    v = 0
    c = False
    perc = porcentagemHonor
    vTemp = '0'
    percent_encargo = 0
    tipo_custo = '🤑Custo Interno - Agência'
    cnpj = ''
    task_fornecedora = ''
    if tem_valores:
        for i in arr:
            if i.valor == '':
                vTemp = '0'
            else:
                vTemp = i.valor

            if i.id == Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_META_TAREFA_MAE:
                task_fornecedora = str(i.valor)

            if i.id == Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_CNPJ_FORNECEDOR:
                cnpj = str(i.valor)

            if i.id == Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_BOX_TIPO_CUSTO:
                tipo_custo = i.valor

            if i.id == Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_PORCENTAGEM_ENCARGO:
                percent_encargo = float(str(vTemp))

            if i.id == Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_QTD:
                qtd = int(vTemp)

            if i.id == Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_VALOR_UNITARIO:
                v = float(str(vTemp))

        taskF = model.task_financeira.task_financeira(qtd=qtd, valor=v, tipoCusto=tipo_custo, percertualHonor=perc,
                                                      percentualEncargo=percent_encargo, cnpjFornecedor=cnpj)
        nomeF = ''
        idF = ''
        if (cnpj != ''):
            f = Fornecedor(idTask='', cnpj=cnpj)
            nomeF = f.get_nome()
            idF = f.get_ID()

        arrCampos = [
            Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_VALOR_HONORARIO,
            Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_VALOR_REAL,
            Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_RECEITA,
            Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_VALORTERCEIRO,
            Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_VALOR_ENCARGO,
            Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_NOME_FORNECEDOR

        ]
        arrValores = [
            taskF.get_valorHonorario(),
            taskF.get_valorTotalReal(),
            taskF.get_valorReceita(),
            taskF.get_valorTerceiro(),
            taskF.get_valorEncargo(),
            nomeF
        ]

        wrikeUtil.update_custom_field(idtask, arrCampos, arrValores)
        #--- vou deixar sem a linkagem, ficou bem estranho !
        # arrC1 = []
        # arrV1 = []
        # if task_fornecedora != '':
        #     wrikeUtil.removerLinkTarefa(idtask, task_fornecedora)
        # if idF != '':
        #     wrikeUtil.linkartarefa(idtask, idF)
        #     arrC1.append(Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_META_TAREFA_MAE)
        #     arrV1.append(idF)
        # else:
        #     arrC1.append(Monumenta.Financeiro.constante_financeiras.ID_CUSTOM_META_TAREFA_MAE)
        #     arrV1.append('')
        # wrikeUtil.update_custom_field(idtask=idtask, arr_campos=arrC1, arr_valores=arrV1)


#calculosValoreItens('IEADYSXZKQ2PFX6S')

# calculosValoreItens('IEADYSXZKQ2P6TL2')
# valor - IEADYSXZJUABQ27R
# Receita - IEADYSXZJUABVSGX
# q = 'descendants=true&subTasks=true&customField={"id":"IEADYSXZJUABQ27R","comparator":"IsNotEmpty"}&fields=["hasAttachments","sharedIds","superTaskIds","parentIds","authorIds","responsibleIds","recurrent","customFields","subTaskIds","description","briefDescription","attachmentCount","dependencyIds","superParentIds","metadata"]'
# jsonData = wrikeUtil.WrikeResponse('/folders/IEADYSXZI42H3JBZ/tasks', q)
# temreceita = False
# arrc = ['IEADYSXZJUABRTMH','IEADYSXZJUABVSGX']
# arrv = ['true','']
# for row in jsonData['data']:
#    calculosValoreItens(row['id'])
# wrikeUtil.update_custom_field(row['id'],arrc,arrv)
# for i in row['customFields']:
#    if (i['id'] == 'IEADYSXZJUABVSGX' and i['value'] != ''):
#         temreceita = True
# if not temreceita:
#     calculosValoreItens(row['id'])
# temreceita = False

# vamos atualziar os campo do custo interno pra Status correto
# print(jsonData)

# arrc = ['IEADYSXZJUACYMQE']
# arrv = ['Custo Interno - Agência']
# arrv2 = ['Custo Terceiro c/ honorário']
# for row in jsonData['data']:
#     # wrikeUtil.update_custom_field(row['id'],arrc,arrv)
#     for i in row['customFields']:
#         if (i['id'] == 'IEADYSXZJUABRTMH'):
#             if (i['value'] == 'true'):
#                 wrikeUtil.update_custom_field(row['id'], arr_campos=arrc, arr_valores=arrv)
#             if (i['value'] == 'false'):
#                 wrikeUtil.update_custom_field(row['id'], arr_campos=arrc, arr_valores=arrv2)
#             if (i['value'] == ''):
#                 wrikeUtil.update_custom_field(row['id'], arr_campos=arrc, arr_valores=arrv2)
