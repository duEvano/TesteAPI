import requests

import bb.constantes_BB
import wrikeUtil
from bb import constantes_BB


# todo :  criar rotina de verificação do status do WebHook e fazer um reset automatico dele

def abrir_webhook(id_folder, eventos, hookurl, querystring):
    url = 'folders/' + id_folder + '/webhooks'
    webhook_url = 'https://www.wrike.com/api/v4/' + url
    payload = {
        'hookUrl': hookurl,
        'events': '[' + eventos + ']',
        'recursive': 'true',
    }
    headers = {
        'Authorization': "Bearer eyJ0dCI6InAiLCJhbGciOiJIUzI1NiIsInR2IjoiMSJ9.eyJkIjoie1wiYVwiOjM5NTEzNTMsXCJpXCI6NzMxMTgxMixcImNcIjo0NjIyNjM2LFwidVwiOjg2NDc1MzQsXCJyXCI6XCJVU1wiLFwic1wiOltcIldcIixcIkZcIixcIklcIixcIlVcIixcIktcIixcIkNcIixcIkRcIixcIk1cIixcIkFcIixcIkxcIixcIlBcIl0sXCJ6XCI6W10sXCJ0XCI6MH0iLCJpYXQiOjE2MDUxMDE2MTR9.roVljjEPzdcFBAQE1uix2jbmD_zSPmPT4FbOvp6k88I",
        'cache-control': "no-cache",

    }

    jsondata = ''
    try:
        with requests.request("POST", webhook_url, data=payload, headers=headers, params=querystring) as response:
            if response.status_code == 200:
                jsondata = response.json()
            else:
                # print(webhook_url)
                jsondata = response.status_code
    except:
        print('Error while fetching data!')
    return jsondata


# print (abrir_webhook('IEADYSXZI4QSY3QA','TaskStatusChanged','https://wrike-api-hml.azurewebsites.net/updatedatastatus',''))
#print (abrir_webhook('IEADYSXZI4W4J75G','TaskStatusChanged','https://wrike-api-hml.azurewebsites.net/bcommercerDOAC',''))
#print (abrir_webhook('IEADYSXZI4QRZ4ZS','TaskCustomFieldChanged','https://wrike-api-hml.azurewebsites.net/financeiroBBPromo',''))
# web hook de teste para customfields - >IEADYSXZJAABDB5O
#IEADYSXZJAABFWK2
#print (abrir_webhook('IEADYSXZI42PPQZX','TaskCustomFieldChanged','https://wrike-api-hml.azurewebsites.net/financeiroBBSeguros',''))


def atualiza_webhook(id_hook, status):
    url = 'webhooks/' + id_hook
    webhook_url = url
    q = 'status=' + status
    wrikeUtil.WrikePut(webhook_url, q)


# [POST] /folders/IEADYSXZI4QSY3QA/webhooks
#Active
#Suspended
print(atualiza_webhook('IEADYSXZJAABCNAY', 'Active'))
