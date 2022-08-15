import wrikeUtil
import Monumenta.Projetos.model.Projeto
import Monumenta.Projetos.model.ConstanteProjetos
import Monumenta.Cliente.constantes_cliente
from datetime import date


class Projeto:
    def __init__(self, id):
        self.__idProjeto = id

    def loadProjeto(self):
        desc = ''
        tit = ''
        cliente = ''
        pit = ''

        jsonData = wrikeUtil.WrikeResponse(url='/folders/' + self.__idProjeto, querystring='')['data']

        jsonCustomField = []
        for row in jsonData:
            tit = row['title']
            jsonCustomField = row['customFields']

        arr = wrikeUtil.get_tuplaCustomFields(jsonCustomField)

        for i in arr:
            if i.id == Monumenta.Projetos.model.ConstanteProjetos.ID_CUSTOM_CLIENTE:
                cliente = str(i.valor)
            if i.id == Monumenta.Projetos.model.ConstanteProjetos.ID_CUSTOM_PIT:
                pit = str(i.valor)


        item = Monumenta.Projetos.model.Projeto.Projeto(
            titulo=tit,
            id=self.__idProjeto,
            apelidocliente=cliente
            # precisamos pegar os campos custom
        )
        item.set_PIT(pit)
        item = self.definirPIT(item)
        self.updateProjeto(item)
        return item

    def definirPIT(self, proj: Monumenta.Projetos.model.Projeto.Projeto):
        if proj.get_PIT() == '' or proj.get_PIT() == 'Nº do PIT Aqui':
            seed_str = ''
            semente = proj.get_Cliente().seed + 1
            if semente / 10 >= 1:
                seed_str = '00' + str(semente)
            else:
                seed_str = '000' + str(semente)
            ano = date.today().year
            sig = proj.get_Cliente().sigla
            proj.set_PIT(sig + '-' + str(seed_str) + ' ' + str(ano))
            proj.get_Cliente().setSeed(semente)
            proj.set_Titulo(proj.get_PIT() + ' | ' + proj.get_Titulo())

            arrCampos2 = [
                Monumenta.Cliente.constantes_cliente.ID_CUSTOM_SEED
            ]
            arrValores2 = [
                str(semente)
            ]
            wrikeUtil.update_custom_field(idtask=proj.get_Cliente().id,
                                                 arr_campos=arrCampos2,
                                                 arr_valores=arrValores2)
        return proj

    def updateProjeto(self, proj: Monumenta.Projetos.model.Projeto.Projeto):
        # wrikeUtil.update_custom_field_folder()
        arrCampos = [
            Monumenta.Projetos.model.ConstanteProjetos.ID_CUSTOM_PIT
        ]
        arrValores = [
            proj.get_PIT()
        ]
        wrikeUtil.update_custom_field_folder(idFolder=proj.get_ID(),
                                             arr_campos=arrCampos,
                                             arr_valores=arrValores)
        #atualizando o nome do Projeto
        wrikeUtil.updatecampo_folder(idFolder = proj.get_ID(),
                                     nomecampo= 'title',
                                     valor= proj.get_Titulo())



