# funçoes para otimização da gestão dos relatórios
# Autor: Evano
# Data de criação : 15/04/22

from bb import constantes_BB
import datetime
import wrikeUtil


def atualiza_data_trocastatus(idTask):
    id_campo_data = ''
    lista_campos = [constantes_BB.ID_CAMPO_DATA_STATUS]
    # Fazer a formatação da data
    # valores_campos = [constantes_BB.]
    dataNova = datetime.date.today()
    valores_campos = [dataNova]
    # atualizando o campos da data da troca
    wrikeUtil.update_custom_field(idTask, lista_campos, valores_campos)


# q = 'descendants=true&title="teste de Item"&subTasks=true&fields=["hasAttachments","sharedIds","superTaskIds","parentIds","authorIds","responsibleIds","recurrent","customFields","subTaskIds","description","briefDescription","attachmentCount","dependencyIds","superParentIds","metadata"]'

#q = 'permalink="https://www.wrike.com/open.htm?id=555545394"'
#print(wrikeUtil.WrikeResponse('/folders', q))
# print(wrikeUtil.WrikePut ('/webhooks/IEADYSXZJAABCKFR',''))
# atualiza_data_trocastatus('IEADYSXZKQ2H3JIK')
