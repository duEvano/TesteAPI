from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from datetime import timedelta, date
# os devidos Importe do model da OC
from Monumenta.Financeiro.Model.oc import oc
import utils.formating as format
import os


class pdf_orcamento:
    # definições das constantes a serem utilizadas
    def __init__(self, myOC: oc):
        self.__oc = myOC
        self.__elements = []

    def __cabecalhoMonu(self):
        # Carregando a Logo da Monu
        img = Image(self.__oc.logo)
        img.drawHeight = 2.60 * inch * img.drawHeight / img.drawWidth
        img.drawWidth = 2.60 * inch

        # Estilo da Tabela
        table_style = TableStyle(
            [
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('BACKGROUND', (0, 0), (-1, -1), colors.white),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('line-height', (0, 0), (-1, -1), -10),
                ('BACKGROUND', (2, 1), (-1, -2), colors.lightgrey),
                ('BACKGROUND', (1, 1), (-2, -2), colors.lightgrey),
                ('INNERGRID', (0, 0), (-1, -1), 0.1, colors.black),
                ('BOX', (0, 0), (-1, -1), 0.1, colors.black)
            ]
        )

        # estilo das informações da OC
        table_style_info = TableStyle(
            [
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTSIZE', (0, 0), (1, 0), 18),
                ('TOPPADDING', (0, 0), (-1, -1), 15)

            ]
        )

        # Creating mock data and cols to add a new table inside the third a row
        data_info_oc = [[self.__oc.numeroOC],
                        ['Data : ' + self.__oc.getData()]]
        tabelo_oc = Table(data_info_oc, style=table_style_info, colWidths=120)
        data_table = [
            [img, self.__oc.endererecoEmpresa, tabelo_oc]
        ]

        final_table = Table(data_table, style=table_style, colWidths=[220, 230, 120], rowHeights=95)
        self.__elements.append(final_table)

    def __dadosOC(self):
        table_style = TableStyle(
            [
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('ALIGN', (0, 0), (0, 4), 'RIGHT'),
                ('BACKGROUND', (0, 0), (-1, -1), colors.white),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('INNERGRID', (0, 0), (-1, -1), 0.1, colors.white),
                ('BOX', (0, 0), (-1, -1), 0.1, colors.black),
            ]
        )

        labelStyle = ParagraphStyle('yourtitle',
                                    fontSize=8,
                                    alignment=2,
                                    spaceAfter=14)

        data = [
            [
                Paragraph('<b>Data de apresentação:</b>', labelStyle), self.__oc.dataGeracao,
                Paragraph('<b>Data final:</b>', labelStyle), self.__oc.dataGeracao,
            ],
            [
                Paragraph('<b>PIT:</b>', labelStyle), self.__oc.projeto.get_PIT(),
                # todo: acrescentar 30 dias para a data de validade
                Paragraph('<b>Validade:</b>', labelStyle), self.__oc.dataValidade
            ],
            [
                Paragraph('<b>Nome:</b>', labelStyle), self.__oc.projeto.get_Titulo(), '', ''
            ],
            [
                Paragraph('<b>Espécie :</b>', labelStyle), 'Campanha', '', ''
            ]
        ]

        final_table = Table(data, style=table_style, colWidths=[100, 185, 100, 185])
        self.__elements.append(final_table)

    def dadosCliente(self):
        table_style_heading = TableStyle(
            [('BOX', (0, 0), (-1, -1), 0.1, colors.black),
             ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey), ]

        )
        headingStyle = ParagraphStyle('yourtitle',
                                      fontSize=9,
                                      alignment=1,
                                      spaceAfter=14)
        data_heading = [[Paragraph('<b>Cliente</b>', headingStyle)]]
        headingTable = Table(data_heading, style=table_style_heading, colWidths=570)
        self.__elements.append(headingTable)
        # Set a table style
        table_style = TableStyle(
            [
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('ALIGN', (0, 0), (0, 4), 'RIGHT'),
                ('BACKGROUND', (0, 0), (-1, -1), colors.white),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BACKGROUND', (2, 1), (-1, -2), colors.lightgrey),
                ('BACKGROUND', (1, 1), (-2, -2), colors.lightgrey),
                ('INNERGRID', (0, 0), (-1, -1), 0.1, colors.white),
                ('BOX', (0, 0), (-1, -1), 0.1, colors.black),
            ]
        )

        labelStyle = ParagraphStyle('yourtitle',
                                    fontSize=8,
                                    alignment=2,
                                    spaceAfter=14)
        data = [[Paragraph('<b>Cliente:</b>', labelStyle), self.__oc.projeto.get_Cliente().nome],

                [Paragraph('<b>CNPJ:</b>', labelStyle), self.__oc.projeto.get_Cliente().cnpj],
                [Paragraph('<b>Endereço:</b>', labelStyle), self.__oc.projeto.get_Cliente().endereco],
                [Paragraph('<b>Insc. Estadual :</b>', labelStyle), self.__oc.projeto.get_Cliente().inscr]]

        final_table = Table(data, style=table_style, colWidths=[100, 470])
        self.__elements.append(final_table)

    def corpoOrcamento(self, tituloMaster, valormaster, l, index):
        table_style_heading = TableStyle(
            [('BOX', (0, 0), (-1, -1), 0.1, colors.black),
             ('BACKGROUND', (0, 0), (-1, -1), colors.white),
             ('FONTSIZE', (0, 0), (-1, -1), 6),
             ('VALIGN', (0, 0), (-1, -1), 'TOP'),
             ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
             ('TOPPADDING', (0, 0), (-1, -1), 0),
             ('TOPPADDING', (0, 0), (-1, 1), 3)
             ]

        )

        headingStyle = ParagraphStyle('yourtitle',
                                      fontSize=6,
                                      alignment=0,
                                      spaceAfter=8,
                                      justifyBreaks=1)
        headingStyleBold = ParagraphStyle('yourtitle',
                                          fontSize=7,
                                          alignment=0,
                                          spaceAfter=14,
                                          justifyBreaks=1)
        data_heading = []

        lineprincipal = [Paragraph('<b>' + str(index) + ' - ' + tituloMaster + '</b>', headingStyleBold),
                         Paragraph('', headingStyle),
                         Paragraph('', headingStyle), Paragraph('', headingStyle), Paragraph('', headingStyle),
                         Paragraph('', headingStyle),
                         Paragraph('<b>' + format.formatMoney(valormaster) + '</b>', headingStyleBold)]
        data_heading.append(lineprincipal)
        count = 0
        for y in l:
            count = count + 1

            lineprincipal = [
                Paragraph(str(index) + '.' + str(count) + ' - ' + y.titulo + y.descricao, headingStyle),
                Paragraph(str(y.qtd), headingStyle), Paragraph(format.formatMoney(y.valor), headingStyle),
                Paragraph(format.formatMoney(float(y.valor) * float(y.qtd)), headingStyle),
                Paragraph(format.formatMoney(y.honorario), headingStyle),
                Paragraph(format.formatMoney(y.encargo), headingStyle),
                Paragraph(format.formatMoney(y.valorReal), headingStyle)]
            data_heading.append(lineprincipal)

        headingTable = Table(data_heading, style=table_style_heading,
                             colWidths=[220, 350 / 6, 350 / 6, 350 / 6, 350 / 6, 300 / 6, 400 / 6])
        self.__elements.append(headingTable)

    def cabecalhoOrcamento(self):
        table_style_heading = TableStyle(
            [('BOX', (0, 0), (-1, -1), 0.1, colors.black),
             ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey), ]

        )
        headingStyle = ParagraphStyle('yourtitle',
                                      fontSize=7,
                                      alignment=0,
                                      spaceAfter=14)
        data_heading = [[
            Paragraph('<b>Descrição</b>', headingStyle),
            Paragraph('<b>Qtd</b>', headingStyle),
            Paragraph('<b>Valor Un.</b>', headingStyle),
            Paragraph('<b>Total</b>', headingStyle),
            Paragraph('<b>Honorários</b>', headingStyle),
            Paragraph('<b>Encargos</b>', headingStyle),
            Paragraph('<b>Valor Final</b>', headingStyle)
        ]]
        headingTable = Table(data_heading, style=table_style_heading,
                             colWidths=[220, 350 / 6, 350 / 6, 350 / 6, 350 / 6, 300 / 6, 400 / 6])
        self.__elements.append(headingTable)

    def dadosTotais(self):
        table_style_heading = TableStyle(
            [('BOX', (0, 0), (-1, -1), 0.1, colors.black),
             ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey), ]

        )
        headingStyle = ParagraphStyle('yourtitle',
                                      fontSize=9,
                                      alignment=1,
                                      spaceAfter=14)
        data_heading = [[Paragraph('<b>Totais</b>', headingStyle)]]
        headingTable = Table(data_heading, style=table_style_heading, colWidths=570)
        self.__elements.append(headingTable)
        # Set a table style
        table_style = TableStyle(
            [
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('ALIGN', (0, 0), (5, 5), 'RIGHT'),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BOX', (0, 0), (-1, -1), 0.1, colors.black),
                ('BOX', (4, 0), (-3, -1), 0.1, colors.black),
                ('BACKGROUND', (-2, -1), (-1, -1), colors.lightgrey),
            ]
        )

        labelStyle = ParagraphStyle('yourtitle',
                                    fontSize=8,
                                    alignment=2,
                                    spaceAfter=14)
        data = [['', '',
                 Paragraph('Total Custo Interno', labelStyle), format.formatMoney(self.__oc.totais.totalCustoInterno)],
                ['', '', Paragraph('Total Custo de Terceiros:', labelStyle),
                 format.formatMoney(self.__oc.totais.totalCustoTerceiros)],
                ['', '', 'SubTotal Interno + Terceiros', format.formatMoney(self.__oc.totais.totalCustoTerceiros + self.__oc.totais.totalCustoInterno )],
                ['', '', 'Total Honorários', format.formatMoney(self.__oc.totais.totalHonorarios)],
                ['', '', 'Total de Encargos', format.formatMoney(self.__oc.totais.totalEncargos)],
                ['', '', Paragraph('<b>Total Geral</b>', labelStyle), Paragraph('<b>'+format.formatMoney(self.__oc.totais.totalGeral)+'</b>', labelStyle)]]

        final_table = Table(data, style=table_style, colWidths=[100, 250, 120, 100])
        self.__elements.append(final_table)

    def especificacao(self):
        table_style_heading = TableStyle(
            [('BOX', (0, 0), (-1, -1), 0.1, colors.black),
             ('BACKGROUND', (0, 1), (-1, -2), colors.lightgrey),
             ('INNERGRID', (0, 0), (-1, -1), 0.1, colors.black)
             ]

        )
        headingStyle = ParagraphStyle('yourtitle',
                                      fontSize=9,
                                      alignment=1,
                                      spaceAfter=14)
        mioloStyle = ParagraphStyle('yourtitle',
                                    fontSize=7,
                                    alignment=0,
                                    spaceAfter=14)
        data_heading = [[Paragraph('-', headingStyle)],
                        [Paragraph('<b>ESPECIFICAÇÃO</b>', headingStyle)],
                        [Paragraph("""<br/><br/><br/><br/><br/>""", mioloStyle)]]
        headingTable = Table(data_heading, style=table_style_heading, colWidths=570)
        self.__elements.append(headingTable)

    def rodapeOrcamento(self):
        table_style_heading = TableStyle(
            [('BOX', (0, 0), (-1, -1), 0.1, colors.white),
             ('BACKGROUND', (0, 0), (-1, -1), colors.white),
             ('VALIGN', (0, 0), (-1, -1), 'TOP'),
             ('BOX', (0, 0), (0, 0), 0.1, colors.black),
             ('BOX', (2, 0), (3, 0), 0.1, colors.black),
             ('INNERGRID', (2, 0), (3, 0), 0.1, colors.black),
             ]

        )
        headingStyle = ParagraphStyle('yourtitle',
                                      fontSize=7,
                                      alignment=0,
                                      spaceAfter=14)
        data_heading = [[
            Paragraph('<b>MONUMENTA COM. E ESTRAT. SOC</b>', headingStyle),
            '',
            Paragraph('<b>Aprovação pelo Cliente</b>', headingStyle),
            Paragraph('<b>Data</b>', headingStyle),

        ]]
        headingTable = Table(data_heading, style=table_style_heading,
                             colWidths=[250, 20, 200, 100], rowHeights=35)

        self.__elements.append(headingTable)

    def MontaOrcamentoMonu(self):
        self.__cabecalhoMonu()
        self.__dadosOC()
        self.dadosCliente()
        self.cabecalhoOrcamento()
        count = 0
        for x in self.__oc.listaOrcamento:
            count = count + 1
            self.corpoOrcamento(tituloMaster=x.titulo, valormaster=x.somaGeral, l=x.itens, index=count)
        # self.corpoOrcamento()
        self.dadosTotais()
        self.especificacao()
        self.__elements.append(Spacer(12, 15))
        self.rodapeOrcamento()


    def go(self):
        nome_arquivo = 'oc_'+ str(self.__oc.numeroOC) + '.pdf'
        self.__oc.nomeArquivo = nome_arquivo

        directory = './static/ocs/'

        file_path = os.path.join(directory, nome_arquivo)

        doc = SimpleDocTemplate(file_path, topMargin=8)
        self.MontaOrcamentoMonu()
        doc.build(self.__elements)
        print('Gerou o PDF')
        return self.__oc
