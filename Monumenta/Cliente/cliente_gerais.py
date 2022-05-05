import wrikeUtil
# Regras de negócio para controle do Cliente
from utils import html_factore


def geraDescriptioncliente(idtask):
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
       txt1 = '<b>{0}</b> : {1}'.format(i.Titulo,i.valor)
       blocos.append(txt1)

    htmlfull = html_factore.read_template_Fisico('C:\\Evano\\Python\\TesteAPI\\templates\\description_cliente.html')
    htmlfull = htmlfull.format(blocos[0],
                               blocos[1],
                               blocos[2],
                               blocos[3],
                               blocos[4],
                               blocos[5],
                               blocos[6],
                               blocos[7],
                               blocos[8],
                               blocos[9],
                               blocos[11]
                               )
    wrikeUtil.updatecampo(idtask,'description',htmlfull)
    return ""


#geraDescriptioncliente('IEADYSXZKQ2PPAJV')
