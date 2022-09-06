from flask import Flask, request, abort, send_file, render_template

import Monumenta.Financeiro.valores_itens
from Monumenta.Financeiro.View.oc import oc as ocView
import bb.bcommercer
from bb import banco_do_brasil
import os
import utils.formating as format1
from Monumenta.Projetos.controller.Projeto import Projeto as pro

app = Flask(__name__)


@app.route('/')
def index():
    directory = './static/ocs/'
    filename = "oc_1360.pdf"
    file_path = os.path.join(directory, filename)
    print('Tá logando')
    print(file_path)
    return file_path
    #return os.getcwd() + '\\' + """static\logoMonu.png"""


# Função que atualiza a data da mudança de status
@app.route('/updatedatastatus', methods=['POST'])
def update_data_troca():
    if request.method == 'POST':
        print(request.json)
        banco_do_brasil.atualiza_data_trocastatus(request.json[0]["taskId"],str(request.json[0]["oldStatus"]))
        return 'success', 200
    else:
        abort(400)


# Função geraDoac do BCOMMERCER - Escuta da pasta : IEADYSXZI4W4J75G
# webHook responsavel : IEADYSXZJAABC5AF
@app.route('/bcommercerDOAC', methods=['POST'])
def update_criardoacBcommercer():
    # return bb.bcommercer.criar_tarefa_orcamento('IEADYSXZKQ2O2CU2').get_descricaoNova()
    if request.method == 'POST':

        if request.json[0]["oldStatus"] == 'A Fazer' and request.json[0]["status"] == 'In Progress':
            bb.bcommercer.criar_tarefa_orcamento(request.json[0]["taskId"])
        return 'success', 200
    else:
        abort(400)


# Função dos valores financeiros baseado na troca de valores de custom
# webHook responsavel : IEADYSXZJAABDB5O (apagado)
#web hook da LTM : IEADYSXZJAABG2SM

@app.route('/financeiroValores', methods=['POST'])
def update_financeiroValores():
    # return bb.bcommercer.criar_tarefa_orcamento('IEADYSXZKQ2O2CU2').get_descricaoNova()
    if request.method == 'POST':
        print(request.json)
        # if request.json[0]["oldStatus"] == 'A Fazer' and request.json[0]["status"] == 'In Progress':
        Monumenta.Financeiro.valores_itens.calculosValoreItens(request.json[0]["taskId"], porcentagemHonor=5)
        # bb.banco_do_brasil(request.json[0]["taskId"])
        return 'success', 200
    else:
        abort(400)


#web hook da LTM BB Seguros : IEADYSXZJAABG2SR
@app.route('/financeiroValoresLTMBBSeguros', methods=['POST'])
def update_financeiroValoresLTMBBSEGUROS():
    # return bb.bcommercer.criar_tarefa_orcamento('IEADYSXZKQ2O2CU2').get_descricaoNova()
    if request.method == 'POST':
        print(request.json)
        # if request.json[0]["oldStatus"] == 'A Fazer' and request.json[0]["status"] == 'In Progress':
        Monumenta.Financeiro.valores_itens.calculosValoreItens(request.json[0]["taskId"], porcentagemHonor=7)
        # bb.banco_do_brasil(request.json[0]["taskId"])
        return 'success', 200
    else:
        abort(400)


# webHook responsavel : IEADYSXZJAABDB5O (apagado)
#web hook da LTM BB Seguros : IEADYSXZJAABG2SU
@app.route('/financeiroValoresLTMGeral', methods=['POST'])
def update_financeiroValoresLTMGeral():
    # return bb.bcommercer.criar_tarefa_orcamento('IEADYSXZKQ2O2CU2').get_descricaoNova()
    if request.method == 'POST':
        print(request.json)
        # if request.json[0]["oldStatus"] == 'A Fazer' and request.json[0]["status"] == 'In Progress':
        Monumenta.Financeiro.valores_itens.calculosValoreItens(request.json[0]["taskId"], porcentagemHonor=10)
        # bb.banco_do_brasil(request.json[0]["taskId"])
        return 'success', 200
    else:
        abort(400)

# WeebBokk das tarefas financeiras para o BB Digital
# webHook responsavel : IEADYSXZJAABDL6G
@app.route('/financeiroBBDigital', methods=['POST'])
def update_financeiroValoresBBDigital():
    # return bb.bcommercer.criar_tarefa_orcamento('IEADYSXZKQ2O2CU2').get_descricaoNova()
    if request.method == 'POST':
        print(request.json)
        Monumenta.Financeiro.valores_itens.calculosValoreItens(request.json[0]["taskId"], porcentagemHonor=6)
        return 'success', 200
    else:
        abort(400)


# WeebBokk das tarefas financeiras para o BB Promo
# webHook responsavel : IEADYSXZJAABDM2L
@app.route('/financeiroBBPromo', methods=['POST'])
def update_financeiroValoresBBPromo():
    if request.method == 'POST':
        print(request.json)
        Monumenta.Financeiro.valores_itens.calculosValoreItens(request.json[0]["taskId"], porcentagemHonor=5)
        return 'success', 200
    else:
        abort(400)


# WeebBokk das tarefas financeiras para o BB Seguros
# webHook responsavel : IEADYSXZJAABDM2L
@app.route('/financeiroBBSeguros', methods=['POST'])
def update_financeiroValoresBBSeguros():
    if request.method == 'POST':
        print(request.json)
        Monumenta.Financeiro.valores_itens.calculosValoreItens(request.json[0]["taskId"], porcentagemHonor=5)
        return 'success', 200
    else:
        abort(400)


@app.route('/downloadOc', methods=['GET'])
def downloadOC():
    args = request.args
    id = args.get("id")
    ocV = ocView(id=id)
    n = ocV.gerarPDF()
    path = 'static/ocs/' + n.nomeArquivo
    return send_file(path, as_attachment=True)


@app.route('/downloadGerada', methods=['GET'])
def downloadOCGerada():
    args = request.args
    nome = args.get("nome")
    path = 'static/ocs/' + nome
    return send_file(path, as_attachment=True)


@app.route('/trocaStatusOC', methods=['POST'])
def trocaStatusOC():
    if request.method == 'POST':
        try:
            print(request.json)
        except:
            print('Error while fetching data!')

        return 'success', 200
    else:
        abort(400)


@app.route('/geradorOC')
def geradorOC():
    return render_template('geracaoOC.html') \

@app.route('/getInfoOC')
def getInfoOC():
    print('Tá logando o get Info')
    retorno = ''



    try:
        args = request.args
        l = args.get("link")
        print('Temos o link')
        if l == '':
            raise Exception("É necessário informar o link Permanente")
        ocV = ocView(per=l, id='')
        print('Iniciou o objeto view')
        n = ocV.gerarPDF()
        # path = 'static/ocs/' + n.nomeArquivo
        retorno = '{"cliente": "' + str(n.projeto.get_Cliente().nome) + '","projeto":"' + str(
            n.projeto.get_Titulo()) + '","NumeroOC":"' + str(n.numeroOC) + '","nomeArquivo":"' + str(
            n.nomeArquivo) + '","Valortotal":"' + str(format1.formatMoney(n.totais.totalGeral)) + '","vacilo":"0"}'
    except Exception as e:
        retorno = '{"cliente": "' + "" + '","projeto":"' + "" + '","NumeroOC":"' + "" + '","nomeArquivo":"' + "" + '","Valortotal":"' + "" + '","vacilo":"' + str(
            e) + '"}'

        # retorno = '"{"vacilo": "' + str(e) + '"}'
    return retorno


# Vamos fazer então o esquema do formulário em post :-)
# https://stackoverflow.com/questions/14525029/display-a-loading-message-while-a-time-consuming-function-is-executed-in-flask
# criar  um WebHook para escutar a pasta de orcamento, e o evento de FolderCustomFieldChanged
# https://pythonbasics.org/flask-template-data/
# https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application

# WeebBokk criacao de projetos na psta maeh - IEADYSXZI4QOZRYM
# webHook responsavel : IEADYSXZJAABG6ZF
@app.route('/criarProjeto', methods=['POST'])
def createProject():
    if request.method == 'POST':
        try:
            if request.json[0]["oldStatus"] == 'Novo Projeto':
                c = pro(request.json[0]["taskId"])
                c.loadProjeto()
            return 'success', 200
        except Exception as e:
            print(str(e))
    else:
        abort(400)

if __name__ == '__main__':
    app.run()
# data': [{'id': 'IEADYSXZJAABDL6G', 'accountId': 'IEADYSXZ', 'folderId': 'IEADYSXZI4QSY3QA'

# o webhook q vamos usar serã o do ProjectStatusChanged (para calculo do numero do PIT)
