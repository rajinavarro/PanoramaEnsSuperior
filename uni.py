import requests, json, csv, os

def dadosCurso(curso, cidade):
    auto_completar_url = f'https://www.educamaisbrasil.com.br/api/Curso/ListarCursoAutoCompletar?descricaoCurso={curso}&modalidade=G&tipoCurso=&idCidade={cidade}&idInstituicao='
    ac = requests.get(auto_completar_url)
    ac_json = json.loads(ac.content)
    dic = {}

    for i in range(len(ac_json)):
        dic[ac_json[i]['NOME']] = ac_json[i]['ID'], ac_json[i]['URL']
    
    for i in dic:
        print(i, f'ID: {int(dic[i][0])}')
    
    id = ''
    while (id == ''):
        id = int(input('\nDigite o ID: '))
    
    for i in dic:
        if dic[i][0] == id:
            url_curso = dic[i][1]

    base_url = f'https://www.educamaisbrasil.com.br/api/Curso/ConsultarListaOfertas?modalidade=G&tipoCurso=&idCidade=1345&tipoBusca=C&nomeBusca={url_curso}&listaOpcCurso=&carregarCidades=false&periodoInteresse=&carregarQtdAvaliacao=true'
    r = requests.get(base_url)

    coments = json.loads(r.content)
    curso = coments['listOfertas'][0]['DESCRICAO_CURSO']


    
    with open(f'./csv/{curso}.csv', mode='w', encoding='utf-8', newline='') as csv_file:
        fieldnames = ['SIGLA_INSTITUICAO','BAIRRO_INSTITUICAO', 'VALOR_MENSALIDADE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        
        for i in range(len(coments['listOfertas'])):
            coments2 = coments['listOfertas'][i]
            if coments2['SIGLA_INSTITUICAO'] != None and coments2['VALOR_MENSALIDADE'] != None:
                writer.writerow({'SIGLA_INSTITUICAO': coments2['SIGLA_INSTITUICAO'],'BAIRRO_INSTITUICAO':coments2['BAIRRO_INSTITUICAO'], 'VALOR_MENSALIDADE': coments2['VALOR_MENSALIDADE']})
    return  print(f'\n{curso}.csv salvo no diretorio "/csv" com sucesso!')

def listCidades(curso):
    auto_completar_url = f'https://www.educamaisbrasil.com.br/api/Curso/ConsultarListaOfertas?modalidade=G&tipoCurso=&idCidade=&tipoBusca=C&nomeBusca={curso}&listaOpcCurso=true&carregarCidades=true&periodoInteresse=&carregarQtdAvaliacao=true'
    ac = requests.get(auto_completar_url)
    ac_json = json.loads(ac.content)
    ac_json = ac_json['listCidades']
    for i in range(len(ac_json)):
        dadosCurso(curso, ac_json)