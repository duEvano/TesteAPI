import model.item_contrato
import utils.html_factore


class demanda_Bcommerce:
    def __init__(self, descricao):
        self.__descricaoNova = None
        self.__valorTotal = None
        self.__mkt = None
        self.__descricao = descricao

        # pegando o mkt
        inicio = '<b>MKT/ Ação</b><br />'
        fim = '<br /><br /><b>Localizador</b><br />'
        self.__mkt = utils.html_factore.GetTextoString(self.__descricao, inicio, fim)

        # pegando a demanda escrita pelo cliente
        inicio = '<b>Descrição</b><br />'
        fim = '<br /><br /><b>Objetivos</b><br />'
        self.__demandaescrita = utils.html_factore.GetTextoString(self.__descricao, inicio, fim)

        # pegando o titulo da demanda
        inicio = '<b>Nome da demanda</b><br />'
        fim = '<br /><br /><b>Descrição</b>'
        self.__titulo = utils.html_factore.GetTextoString(self.__descricao, inicio, fim)

        self.__itens = self.inteligencia_Demanda()
        # print(self.__itens)
        # def desativar(self):

    #     self.__ativo = False
    #     print("A pessoa foi desativada com sucesso")

    def get_mkt(self):
        return self.__mkt

    def get_titulo(self):
        return self.__titulo

    def set_description(self, description):
        self.__descricao = description

    def get_demandaEscrita(self):
        return self.__demandaescrita;

    def get_itens(self):
        return self.__itens;

    def get_valorTotal(self):
        return self.__valorTotal

    def set_valorTotal(self, valorT):
        self.__valorTotal = valorT

    def get_descricaoNova(self):
        return self.__descricaoNova

    def set_descricaoNova(self, desc):
        self.__descricaoNova = desc

    def inteligencia_Demanda(self):
        self.__demandaescrita
        palavras_validas = [
            ('1.1', 'HÓRUS',
             'Desenvolvimento de peças estáticas incluindo redação, revisão, </br>layout e entrega digital, com ou sem link em HTML, </br>para uso em portais, sites, hotsites, </br>notícias, aplicativos e games.',
             791.08),
            ('1.1', 'APF',
             'Desenvolvimento de peças estáticas incluindo redação, revisão, </br>layout e entrega digital, com ou sem link em HTML, </br>para uso em portais, sites, hotsites, </br>notícias, aplicativos e games.',
             791.08),
            ('1.1', 'APJ',
             'Desenvolvimento de peças estáticas incluindo redação, revisão, </br>layout e entrega digital, com ou sem link em HTML, </br>para uso em portais, sites, hotsites, </br>notícias, aplicativos e games.',
             791.08),
            ('1.1', 'CPPS',
             'Desenvolvimento de peças estáticas incluindo redação, revisão, </br>layout e entrega digital, com ou sem link em HTML, </br>para uso em portais, sites, hotsites, </br>notícias, aplicativos e games.',
             791.08),
            ('1.1', 'FALE COM',
             'Desenvolvimento de peças estáticas incluindo redação, revisão, </br>layout e entrega digital, com ou sem link em HTML, </br>para uso em portais, sites, hotsites, </br>notícias, aplicativos e games.',
             791.08),
            ('1.5', 'EMKT',
             'Desenvolvimento de peças estáticas, incluindo redação, revisão, </br>layout e entrega digital, com ou sem link em HTML, </br>para uso em e-mail marketing.',
             1397.11),
            ('1.5', 'EMK',
             'Desenvolvimento de peças estáticas, incluindo redação, revisão, </br>layout e entrega digital, com ou sem link em HTML, </br>para uso em e-mail marketing.',
             1397.11),
            ('1.5', 'EMAIL',
             'Desenvolvimento de peças estáticas, incluindo redação, revisão, </br>layout e entrega digital, com ou sem link em HTML, </br>para uso em e-mail marketing.',
             1397.11),
            ('1.1', 'HORUS',
             'Desenvolvimento de peças estáticas incluindo redação, revisão, </br>layout e entrega digital, com ou sem link em HTML, </br>para uso em portais, sites, hotsites, </br>notícias, aplicativos e games.',
             791.08),
            ('1.1', 'TAA',
             'Desenvolvimento de peças estáticas incluindo redação,revisão, layout e entrega digital, com ou sem link em HTML, para uso em totens, caixas eletrônicos, TV Digital, videowall, terminais de chamadas de clientes, merchandising eletrônico, sistemas touch screen e displays.',
             857.81),
            ('1.5', 'PEÇAS DE HTML',
             'Desenvolvimento de peças estáticas, incluindo redação, revisão, </br>layout e entrega digital, com ou sem link em HTML, </br>para uso em e-mail marketing.',
             1397.11),

        ]
        # procurar conjunto de palavras
        qtd = 0
        items = []
        self.__demandaescrita = '  ' + str(self.__demandaescrita).upper()
        ptemp = self.__demandaescrita
        for p in palavras_validas:
            # print(str(self.__demandaescrita).find(p))

            if (str(ptemp).find(p[1])) > 0:
                # pegar a qtd
                posI = str(ptemp).find(p[1]) - 3
                posF = str(ptemp).find(p[1]) - 1
                qtd = str(ptemp[posI:posF]).strip()
                ptemp = ptemp.replace(p[1], "")
                try:
                    qtdInt = int(qtd)
                except:
                    qtdInt = 0
                item = model.item_contrato.item_contrato(descricao=p[2], numero=p[0], valor=p[3], apelido=p[1],
                                                         qtd=qtdInt)
                items.append(item)
                # agora pesquisa no dataset dos itens de contratos

        for i in items:
            if i.get_numero() == '1.5':
                item = model.item_contrato.item_contrato(
                    descricao='Desenvolvimento de html para peças com campos variáveis (entre 1 e 10 campos variáveis), a exemplo de e-mails marketing e soluções similares que venham a ser adotadas pelo Banco.',
                    numero='1.38',
                    valor=2391.79,
                    apelido='EMAIL MKT HTML',
                    qtd=i.get_qtd())
                items.append(item)
            # print(p)
        return items
