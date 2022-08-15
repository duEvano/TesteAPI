import wrikeUtil
import Monumenta.Cliente.model.Cliente
import Monumenta.Cliente.constantes_cliente


class Cliente:
    def __init__(self, apelido):
        self.__apelido = apelido

    def loadByApelido(self, nickName):
        url = 'tasks/'
        q = 'descendants=true&subTasks=true&customField={"id":"' + Monumenta.Cliente.constantes_cliente.ID_CUSTOM_APELIDO + '","comparator":"EqualTo","value":"' + nickName + '"}&fields=["hasAttachments","sharedIds","superTaskIds","parentIds","authorIds","responsibleIds","recurrent","customFields","subTaskIds","description","briefDescription","attachmentCount","dependencyIds","superParentIds","metadata"]'

        jsonData = wrikeUtil.WrikeResponse(url, q)
        cliente_i = Monumenta.Cliente.model.Cliente.Cliente(apelido=nickName)
        id = ''
        for row in jsonData['data']:
            id = row['id']
            #cliente_i.nome = row['title']
            for r2 in row['customFields']:
                # pegando a sigla
                if r2['id'] == Monumenta.Cliente.constantes_cliente.ID_CUSTOM_SIGLA:
                    cliente_i.sigla = str(r2['value'])
                if r2['id'] == Monumenta.Cliente.constantes_cliente.ID_CUSTOM_SEED:
                    cliente_i.seed = int(r2['value'])
                if r2['id'] == Monumenta.Cliente.constantes_cliente.ID_CUSTOM_APELIDO:
                    cliente_i.apelido = str(r2['value'])
                if r2['id'] == Monumenta.Cliente.constantes_cliente.ID_CUSTOM_CNPJ:
                    cliente_i.cnpj = str(r2['value'])
                if r2['id'] == Monumenta.Cliente.constantes_cliente.ID_CUSTOM_ENDERECO:
                    cliente_i.endereco = str(r2['value'])
                if r2['id'] == Monumenta.Cliente.constantes_cliente.ID_CUSTOM_INSC:
                    cliente_i.inscr = str(r2['value'])
                if r2['id'] == Monumenta.Cliente.constantes_cliente.ID_CUSTOM_RAZAO:
                    cliente_i.nome = str(r2['value'])

        cliente_i.id = id
        return cliente_i
