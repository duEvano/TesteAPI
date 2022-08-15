import Monumenta.Fornecedor.constante_fornecedor
import wrikeUtil
from utils import html_factore
import os

class Fornecedor:
    def __init__(self, idTask,cnpj):
        self.nome = ''
        self.idTask = ''
        self.cnpj = ''
        if(idTask != '') :
            self.idTask = idTask
            self.description = self.geraDescriptioncliente()
        else:
            if (cnpj != '') :
                self.cnpj = cnpj
                self.get_nomeFornecedorByCNPJ()



    def geraDescriptioncliente(self):
        # todo : buscar o template pra description
        q = ''
        jsonData = wrikeUtil.WrikeResponse('/tasks/' + self.idTask, q)
        NomeFornecedor = ''
        for row in jsonData['data']:
            NomeFornecedor = row['title']
            jsonCustomField = row['customFields']

        v = wrikeUtil.get_tuplaCustomFields(jsonCustomField)

        blocos = []
        self.nome = NomeFornecedor
        blocos.append(NomeFornecedor)
        for i in v:
            txt1 = '<b>{0}</b> : {1}'.format(i.Titulo, i.valor)
            blocos.append(txt1)

        print(blocos)
        htmlfull = ''
        #htmlfull = html_factore.read_template_Fisico('C:\\Evano\\Python\\TesteAPI\\templates\\description_cliente.html')
       #
        # wrikeUtil.updatecampo(idtask, 'description', htmlfull)

        htmlfull = html_factore.read_template_Fisico(os.getcwd() +'\\templates\\description_fornecedor.html')
        htmlfull = htmlfull.format(blocos[0],
                                   blocos[1],
                                   blocos[2],
                                   blocos[3],
                                   blocos[4],
                                   blocos[5],
                                   blocos[6],
                                   blocos[7],
                                   blocos[8],
                                   blocos[9]
                                   )
        return htmlfull

    def get_description(self):
        return self.description

    def get_nomeFornecedorByCNPJ(self):
        arr = wrikeUtil.getTaskByCustomField(Monumenta.Fornecedor.constante_fornecedor.ID_CUSTOM_SPACE,
                                       '',
                                       Monumenta.Fornecedor.constante_fornecedor.ID_CUSTOM_CNPJ,
                                       self.cnpj)
        for x in arr:
            self.nome = x.Titulo
            self.idTask = x.id

    def get_nome(self):
        return self.nome

    def get_ID(self):
        return self.idTask