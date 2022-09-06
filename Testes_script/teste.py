import json
import pandas
import wrikeUtil


# def get_taskid(jsondata):
#     retorno = ''
#     for row in jsondata['data']:
#         retorno = row['taskId']
#     return retorno


# dados = [{
#     'oldStatus': 'Comp. aprovada cliente',
#     'status': 'Ajustar comprovação',
#     'oldCustomStatusId': 'IEADYSXZJMBSAEM6',
#     'customStatusId': 'IEADYSXZJMBSTNTI',
#     'taskId': 'IEADYSXZKQ2H3JIK',
#     'webhookId': 'IEADYSXZJAABCM3Q',
#     'eventAuthorId': 'KUAIH43O',
#     'eventType': 'TaskStatusChanged',
#     'lastUpdatedDate': '2022-04-18T19:24:26Z'
#     }]
#
# print(dados[0]["taskId"])
# #print(df['taskId'])
#http://127.0.0.1:5000
q = 'permalink="https://www.wrike.com/open.htm?id=552388364"'
print(wrikeUtil.WrikeResponse('/folders/', q))
#IEADYSXZI42PPQZX

#IEADYSXZI435UATJ

#ID DA PSTA DE PROJETOS
#IEADYSXZI4QOZRYM

#q = 'descendants=true'
#q = q + '&fields=["superParentIds","hasAttachments","recurrent","briefDescription","responsibleIds","metadata","sharedIds","authorIds","dependencyIds","subTaskIds","parentIds","description","superTaskIds","attachmentCount","customFields"]'
#print(wrikeUtil.WrikeResponse('/folders/IEADYSXZI435UATJ/tasks', q))


# import subprocess
#
# # using the check_output() for having the network term retrieval
# devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
#
# # decode it to strings
# #devices = devices.decode('ascii')
# devices = str(devices).replace("\r", "")
#
# # displaying the information
# print(devices)

def getCustomFields(idtask):
    # todo : buscar o template pra description
    q = ''
    jsonData = wrikeUtil.WrikeResponse('/tasks/' + idtask, q)
    NomeCliente = ''
    for row in jsonData['data']:
        NomeCliente = row['title']
        jsonCustomField = row['customFields']

    v = wrikeUtil.get_tuplaCustomFields(jsonCustomField)

    blocos = []
    blocos.append(NomeCliente)
    for i in v:
        txt1 = '<b>{0} - {1}</b> : {2}'.format(i.Titulo, i.valor)
        blocos.append(txt1)
    return txt1


#print(getCustomFields('IEADYSXZKQ2P6TL2'))
# folder pra valer
