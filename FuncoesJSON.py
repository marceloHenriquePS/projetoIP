import json, os

dadosMEMBROS = {'Membros': []}
dadosLIVROS = {'Livros': []}

arquivoBaseMEMBROS = "BancoMEMBROS.json"
arquivoBaseLIVROS = "BancoLIVROS.json"


def carregarMEMBROS():
    if os.path.exists(arquivoBaseMEMBROS):
        with open(arquivoBaseMEMBROS, 'r') as arqJson:
            return json.load(arqJson)
    else: 
        return {'Membros': []}

def gravarDadosMEMBROS():

    with open('BancoMEMBROS.json', 'w', encoding='utf-8') as arqJson:
        json.dump(dadosMEMBROS, arqJson, ensure_ascii=False, indent=2)

def carregarLIVROS():
    if os.path.exists(arquivoBaseLIVROS):
        with open(arquivoBaseLIVROS, 'r') as arqJson:
            return json.load(arqJson)
    else: 
        return {'Livros': []}

def gravarDadosLIVROS():
    with open('BancoLIVROS.json', 'w', encoding='utf-8') as arqJson:
        json.dump(dadosLIVROS, arqJson, ensure_ascii=False, indent=2)