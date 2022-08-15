import admin_bb.model.Demanda
import wrikeUtil


class admin:
    def __init__(self, idTarefa):
        self.__idTarefa = idTarefa

    def loadTarefa(self):
        desc = ''
        tit = ''
        dataCriacao = ''

        jsonData = wrikeUtil.WrikeResponse(url='/tasks/' + self.__idTarefa, querystring='')['data']
        for row in jsonData:
            desc = row['description']
            tit = row['title']
            dataCriacao = row['createdDate']

        item = admin_bb.model.Demanda.Demanda(
            descricao=desc,
            titulo=tit,
            dataInicio=dataCriacao
        )
        return item
