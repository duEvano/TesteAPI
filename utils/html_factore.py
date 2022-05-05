from __future__ import division, unicode_literals
import os
import codecs


def read_template_task(arquivohtml):
    caminho_html = os.getcwd() + '/' + arquivohtml
    #document = open(documnet_path, 'r')
    with open(caminho_html, "r", encoding='utf-8') as f1:
        text = f1.read()
    return text

def read_template_Fisico(arquivohtml):
    caminho_html = arquivohtml
    #document = open(documnet_path, 'r')
    with open(arquivohtml, "r", encoding='utf-8') as f1:
        text = f1.read()
    return text

def GetTextoString(texto,inicio,fim):
    posicaoInicial = texto.find(inicio) + len(inicio)
    posicaoFinal = texto.find(fim)
    return texto[posicaoInicial:posicaoFinal]

#print(read_template_task('../templates/doac_BCommercer.html').format('2990'))
