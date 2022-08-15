from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

PAGE_HEIGHT = defaultPageSize[1]
styles = getSampleStyleSheet()
Title = "Generating Reports with Python"
Author = "Brian K. Jones"
URL = "http://protocolostomy.com"
email = "bkjones@gmail.com"
Abstract = """This is a simple example document that illustrates how to put together a basic PDF with a chart.
I used the PLATYPUS library, which is part of ReportLab, and the charting capabilities built into ReportLab."""
Endereco = """Q SAUN QUADRA 5 LOTE B TORRES I, II E III  ANDAR 1 A 16 SALA 101 A 1601 ANDAR 1
A 16 SALA 101 A 1601 ANDAR 1 A 16
SALA 101 A 12221
Brasilia- DF"""
Elements = []
HeaderStyle = styles["Heading1"]
ParaStyle = styles["Normal"]
PreStyle = styles["Code"]

endereco = """MONUMENTA COMUNICAÇÃO E EST. SOC. LTDA.
SRTVS Q. 701 BL. O SL. 589 70340-000 BRASILIA-DF
FONE (61) 3213-5700 FAX (61) 3213-5701
CNPJ: 04.692.238/0001-86
Inscr. Estadual: 0742678400164
www.monumenta.com.br"""


def header(txt, style=HeaderStyle, klass=Paragraph, sep=0.3):
    s = Spacer(0.2 * inch, sep * inch)
    Elements.append(s)
    para = klass(txt, style)
    Elements.append(para)


def p(txt):
    return header(txt, style=ParaStyle, sep=0.1)


def go():
    doc = SimpleDocTemplate('gfe.pdf', topMargin=8)
    doc.build(Elements)


def cabecalhoMonu():
    # data = [['00', '01', '02', '03', '04'],
    #         ['10', '11', '12', '13', '14'],
    #         ['20', '21', '22', '23', '24'],
    #         ['30', '31', '32', '33', '34']]
    # t = Table(data, 5 * [0.6 * inch], 4 * [0.4 * inch])

    # Creating a simple pdfdoc = SimpleDocTemplate(aa)
    story = []

    img = Image('../static/logoMonu.png')
    img.drawHeight = 2.75 * inch * img.drawHeight / img.drawWidth
    img.drawWidth = 2.75 * inch

    # Set a table style
    table_style = TableStyle(
        [
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

            ('BACKGROUND', (0, 0), (-1, -1), colors.white),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('line-height', (0, 0), (-1, -1), -10),

            ('BACKGROUND', (2, 1), (-1, -2), colors.lightgrey),

            ('BACKGROUND', (1, 1), (-2, -2), colors.lightgrey),

            ('INNERGRID', (0, 0), (-1, -1), 0.1, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.1, colors.black),
        ]
    )

    # Creating mock data and cols to add a new table inside the third a row
    data_table = [
        [img, endereco, 'Info de OC']
    ]
    print(defaultPageSize[0])
    final_table = Table(data_table, style=table_style, colWidths=[220, 220, 130], rowHeights=85)
    Elements.append(final_table)


def dadosCliente():
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
    Elements.append(headingTable)
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
    data = [[Paragraph('<b>Cliente:</b>', labelStyle), 'Banco do Brasil'],

            [Paragraph('<b>CNPJ:</b>', labelStyle), '109.1221.1221/001'],
            [Paragraph('<b>Endereço:</b>', labelStyle), Endereco],
            [Paragraph('<b>Insc. Estadual :</b>', labelStyle), '--']]

    final_table = Table(data, style=table_style, colWidths=[100, 470])
    Elements.append(final_table)


def dadosOC():
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
    data = [[Paragraph('<b>Data de apresentação:</b>', labelStyle), '12/12/2022',
             Paragraph('<b>Data final:</b>', labelStyle), '12/12/2022'],
            [Paragraph('<b>PIT:</b>', labelStyle), 'DG-1221/2022', Paragraph('<b>Validade:</b>', labelStyle),
             '12/12/2022'],
            [Paragraph('<b>Nome:</b>', labelStyle), 'Nome do projeto', '', ''],
            [Paragraph('<b>Especie :</b>', labelStyle), '--', '', '']]

    final_table = Table(data, style=table_style, colWidths=[100, 185, 100, 185])
    Elements.append(final_table)


def cabecalhoOrcamento():
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
                         colWidths=[220, 350 / 6, 350 / 6, 350 / 6, 350 / 6, 350 / 6, 350 / 6])
    Elements.append(headingTable)


def corpoOrcamento():
    table_style_heading = TableStyle(
        [('BOX', (0, 0), (-1, -1), 0.1, colors.black),
         ('BACKGROUND', (0, 0), (-1, -1), colors.white),
         ('FONTSIZE', (0, 0), (-1, -1), 6),
         ('VALIGN', (0, 0), (-1, -1), 'TOP')
         ]

    )

    headingStyle = ParagraphStyle('yourtitle',
                                  fontSize=6,
                                  alignment=0,
                                  spaceAfter=14,
                                  justifyBreaks=1)
    data_heading = [[
        Paragraph('<b>1 KITS</b>', headingStyle),
        Paragraph('', headingStyle),
        Paragraph('', headingStyle),
        Paragraph('', headingStyle),
        Paragraph('', headingStyle),
        Paragraph('', headingStyle),
        Paragraph('<b>R$ 416.666,25</b>', headingStyle)
    ],
        [Paragraph(
            """1.1 CAMISA GOLO POLO <br/> """ +
            """Camisa com Gola Polo Abertura com botões
Pato amarelo Com trava
reforçada Sublimada Tecido Dry fit Sublimada""", headingStyle),
            Paragraph('5500', headingStyle),
            Paragraph('R$ 52,00', headingStyle),
            Paragraph('R$ 286.000,00', headingStyle),
            Paragraph('R$ 14.300,00', headingStyle),
            Paragraph('--', headingStyle),
            Paragraph('R$ 300.300,00', headingStyle)
        ],
        [
            Paragraph("""1.2 CAIXA PERSONALIZADA <br/>""" +
            """CAIXA MICRO ONDULADA embalagem produzida em micro ondulado com
impressão off-set 1 cor Nas medidas de
30x29x5 cm altura""", headingStyle),
            Paragraph('5500', headingStyle),
            Paragraph('R$ 52,00', headingStyle),
            Paragraph('R$ 286.000,00', headingStyle),
            Paragraph('R$ 14.300,00', headingStyle),
            Paragraph('--', headingStyle),
            Paragraph('R$ 300.300,00', headingStyle)
        ]
    ]
    headingTable = Table(data_heading, style=table_style_heading,
                         colWidths=[220, 350 / 6, 350 / 6, 350 / 6, 350 / 6, 350 / 6, 350 / 6])
    Elements.append(headingTable)

def dadosTotais():
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
    Elements.append(headingTable)
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
             Paragraph('Total Custo Interno', labelStyle), 'R$ 10.221.000,00'],
            ['', '', Paragraph('Total Custo de Terceiros:', labelStyle),
             'R$ 1221.000,00'],
            ['', '', 'SubTotal Interno + Terceiros', 'R$ 221.000,00'],
            ['', '', 'Total Honorários', 'R$ 1221.000,00'],
            ['', '', Paragraph('<b>Total Geral</b>', labelStyle), Paragraph('<b>R$ 10.221.000,00</b>', labelStyle)]]

    final_table = Table(data, style=table_style, colWidths=[100, 250, 120, 100])
    Elements.append(final_table)

def especificacao():
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
                    [Paragraph('<br/>Aqui entra a descrição<br/><br/>', mioloStyle)]]
    headingTable = Table(data_heading, style=table_style_heading, colWidths=570)
    Elements.append(headingTable)

def rodapeOrcamento():
    table_style_heading = TableStyle(
        [('BOX', (0, 0), (-1, -1), 0.1, colors.white),
         ('BACKGROUND', (0, 0), (-1, -1), colors.white),
         ('VALIGN', (0, 0), (-1, -1),'TOP'),

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
    Elements.append(headingTable)

cabecalhoMonu()
dadosOC()
dadosCliente()
cabecalhoOrcamento()
corpoOrcamento()
corpoOrcamento()
dadosTotais()
especificacao()
Elements.append(Spacer(12, 15))
rodapeOrcamento()

header(Title)
header(Author, sep=0.1, style=ParaStyle)
header(URL, sep=0.1, style=ParaStyle)
header(email, sep=0.1, style=ParaStyle)
header("ABSTRACT")
p(Abstract)

go()
