import requests
from datetime import datetime
from collections import namedtuple

# Response do Wrike
import constantes_gerais


def WrikeResponse(url, querystring):
    wrikeurl = 'https://www.wrike.com/api/v4/' + url
    payload = ""
    headers = {
        'Authorization': "Bearer eyJ0dCI6InAiLCJhbGciOiJIUzI1NiIsInR2IjoiMSJ9.eyJkIjoie1wiYVwiOjM5NTEzNTMsXCJpXCI6NzMxMTgxMixcImNcIjo0NjIyNjM2LFwidVwiOjg2NDc1MzQsXCJyXCI6XCJVU1wiLFwic1wiOltcIldcIixcIkZcIixcIklcIixcIlVcIixcIktcIixcIkNcIixcIkRcIixcIk1cIixcIkFcIixcIkxcIixcIlBcIl0sXCJ6XCI6W10sXCJ0XCI6MH0iLCJpYXQiOjE2MDUxMDE2MTR9.roVljjEPzdcFBAQE1uix2jbmD_zSPmPT4FbOvp6k88I",
        'cache-control': "no-cache",
    }
    jsondata = ''
    try:
        with requests.request("GET", wrikeurl, data=payload, headers=headers, params=querystring) as response:
            if response.status_code == 200:
                jsondata = response.json()
            else:
                jsondata = response.status_code
    except:
        print('Error while fetching data!')
    return jsondata


# pull

def WrikePut(url, querystring):
    wrikeurl = 'https://www.wrike.com/api/v4/' + url
    payload = ''
    headers = {
        'Authorization': "Bearer eyJ0dCI6InAiLCJhbGciOiJIUzI1NiIsInR2IjoiMSJ9.eyJkIjoie1wiYVwiOjM5NTEzNTMsXCJpXCI6NzMxMTgxMixcImNcIjo0NjIyNjM2LFwidVwiOjg2NDc1MzQsXCJyXCI6XCJVU1wiLFwic1wiOltcIldcIixcIkZcIixcIklcIixcIlVcIixcIktcIixcIkNcIixcIkRcIixcIk1cIixcIkFcIixcIkxcIixcIlBcIl0sXCJ6XCI6W10sXCJ0XCI6MH0iLCJpYXQiOjE2MDUxMDE2MTR9.roVljjEPzdcFBAQE1uix2jbmD_zSPmPT4FbOvp6k88I",
        'cache-control': "no-cache",
    }
    response = requests.request("PUT", wrikeurl, data=payload, headers=headers, params=querystring)
    print(response)


def WrikePost(url, data):
    url_geral = 'https://www.wrike.com/api/v4/' + url

    headers = {
        'Authorization': "Bearer eyJ0dCI6InAiLCJhbGciOiJIUzI1NiIsInR2IjoiMSJ9.eyJkIjoie1wiYVwiOjM5NTEzNTMsXCJpXCI6NzMxMTgxMixcImNcIjo0NjIyNjM2LFwidVwiOjg2NDc1MzQsXCJyXCI6XCJVU1wiLFwic1wiOltcIldcIixcIkZcIixcIklcIixcIlVcIixcIktcIixcIkNcIixcIkRcIixcIk1cIixcIkFcIixcIkxcIixcIlBcIl0sXCJ6XCI6W10sXCJ0XCI6MH0iLCJpYXQiOjE2MDUxMDE2MTR9.roVljjEPzdcFBAQE1uix2jbmD_zSPmPT4FbOvp6k88I",
        'cache-control': "no-cache",
    }
    querystring = ''

    jsondata = ''
    try:
        with requests.request("POST", url_geral, data=data, headers=headers, params=querystring) as response:
            if response.status_code == 200:
                jsondata = response.json()
            else:
                # print(webhook_url)
                jsondata = response.status_code
    except:
        print('Error while fetching data!')
    return jsondata


def updatecampo(idtask, nomecampo, valor):
    querystring = nomecampo + '=' + valor
    url = 'tasks/' + idtask
    WrikePut('tasks/' + idtask, querystring)


def update_custom_field(idtask, arr_campos, arr_valores):
    querystring = 'customFields=['
    for index, item in enumerate(arr_campos):
        querystring = querystring + '{"id":"' + item + '","value":"' + str(arr_valores[index]) + '"},'

    # querystring = querystring +'{"id":"'+idCustomField+'","value":"'+str(valor)+'"}'
    querystring = querystring[0:len(querystring) - 1]
    querystring = querystring + ']'
    url = 'tasks/' + idtask
    WrikePut('tasks/' + idtask, querystring)


def get_tuplaCustomFields(jsonTarefas):
    pesquisaCF = ''
    valores = []
    retorno = []
    for i in jsonTarefas:
        pesquisaCF = pesquisaCF + i['id'] + ','
        valores.append(i['value'])

    q = ''
    if pesquisaCF != '' :
        jsonData = WrikeResponse('/customfields/' + pesquisaCF, q)
        CustomTuple = namedtuple('customTuple', ['Titulo', 'id', 'valor'])
        count = 0
        for row in jsonData['data']:
            customF = CustomTuple(row['title'],row['id'],valores[count])
            retorno.append(customF)
            count = count + 1

    return retorno
