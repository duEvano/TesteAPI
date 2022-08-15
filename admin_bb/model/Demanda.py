from datetime import datetime
import utils.html_factore


class Demanda:
    def __init__(self, descricao, titulo, dataInicio):
        self.__descricao = descricao
        self.__nomeDemandante = None
        self.__diretoria = None
        self.__titulo = titulo
        self.__nomePagina = None
        self.__dataInicio = dataInicio[2:dataInicio.find('T')]
        self.__tipo = 'Ajuste de Página'
        self.__sla = 1

        marcadorInicio = '<h3>Informação sobre sua área</h3><b>Diretoria demandante</b><br />'
        marcadorFim = ''

        #load do demandante
        self.__nomeDemandante = utils.html_factore.GetTextoString(
            inicio='<h5>Deixe suas informações de contato</h5><b>Nome</b><br />',
            fim='<br /><br /><b>E-mail</b>',
            texto=self.__descricao
        )


        #date_time_obj = datetime.strptime(dataInicio, '%y-%m-%d')

        marcadorInicio_description = '<h3>Informações da página que você pretende alterar!</h3><b>Nome da Página</b><br />'
        marcadorFim_description = '<br /><br /><b>Link da página a ser alterada'
        subTitulo = ''

        if titulo.find('Solicitação de Ajuste de página') >= 0:
            marcadorInicio_description = '<h3>Informações da página que você pretende alterar!</h3><b>Nome da Página</b><br />'
            marcadorFim_description = '<br /><br /><b>Link da página a ser alterada'
            self.__tipo = 'Ajuste de Página'
            subTitulo = 'Solicitação de Ajuste de página'
            marcadorFim = '<h3>Informações sobre o arquivo</h3>'
            self.__sla = 1

        if titulo.find('Criação de Redirect') >= 0:
            marcadorInicio_description = '<h3>Informações sobre o redirecionamento</h3><b>Nome da Página</b><br />'
            marcadorFim_description = '<br /><br /><b>Indicar link da página que deverá ser criado redirect</b><br />'
            self.__tipo = 'Criação de Redirect'
            subTitulo = 'Criação de Redirect'
            marcadorFim = '<h3>Informações sobre o redirecionamento</h3>'
            self.__sla = 1

        if titulo.find('Solicitação de Criação de Página') >= 0:
            marcadorInicio_description = '<h3>Informações da página que você pretende criar!</h3><b>Nome da Página</b><br />'
            marcadorFim_description = '<br /><br /><b>Link da página a ser usada como Modelo</b><br />'
            self.__tipo = 'Criação de Página'
            subTitulo = 'Solicitação de Criação de Página'
            marcadorFim = '<h3>Informações da página que você pretende criar!</h3>'
            self.__sla = 5


        self.__nomePagina = utils.html_factore.GetTextoString(
           inicio=marcadorInicio_description,
           fim=marcadorFim_description,
           texto=self.__descricao
        )

        self.__titulo = titulo[0:self.__titulo.find(subTitulo)] + self.__tipo + ' - ' + self.__nomePagina




    def get_NomeDemandante(self):
        return self.__nomeDemandante

    def get_Titulo(self):
        return self.__titulo

