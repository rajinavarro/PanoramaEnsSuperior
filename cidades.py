import requests, json, uni
from uni import dadosCurso


def curso(nomeCurso):
    auto_completar_url = 'https://www.educamaisbrasil.com.br/api/Curso/ListarCursoCidade?modalidade=S&ead=null&idcidade=1345&etapa=undefined&url_etapa=undefined&flg_pagina=undefined&flg_conteudo_institucional=CFA'
    ac = requests.get(auto_completar_url)
    ac_json = json.loads(ac.content)
    possiveisCursos = []

    listCurso = ac_json['listCurso']
    
    for i in range(len(listCurso)):
      
        if nomeCurso[0:(len(nomeCurso))] == listCurso[i]['DESC_CURSO'][0:(len(nomeCurso))]:
            possiveisCursos.append(listCurso[i]['URL_CURSO'])
    #oi
    for i in range(len(possiveisCursos)):
        if i < 10:
            print(f'ID: {i}  |', possiveisCursos[i].replace('-', ' '))
        else:
            print(f'ID: {i} |', possiveisCursos[i].replace('-', ' '))
    id = input('Digite o ID: ')
    
    url_curso = possiveisCursos[int(id)]
    print(url_curso)
    
    return url_curso

def cidades (curso):
    lista = []
    idcursoRepetido = []
    cidades_url = f'https://www.educamaisbrasil.com.br/api/Curso/ConsultarListaOfertas?modalidade=G&tipoCurso=&idCidade=&tipoBusca=C&nomeBusca={curso}&listaOpcCurso=true&carregarCidades=true&periodoInteresse=&carregarQtdAvaliacao=true'
    uc = requests.get(cidades_url)
    uc_json = json.loads(uc.content)
    
    for i in uc_json['listCidades']:
        id_cidade = i['ID_CIDADE']
        cidade = i['CIDADE']
        
        dadosCurso(curso, id_cidade, lista, cidade, idcursoRepetido)
    
    return 0

