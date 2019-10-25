import requests, json, csv, os

def dadosCurso(curso, id_cidade, lista, cidade, idcursoRepetido):

    base_url = f'https://www.educamaisbrasil.com.br/api/Curso/ConsultarListaOfertas?modalidade=G&tipoCurso=&idCidade={id_cidade}&tipoBusca=C&nomeBusca={curso}&listaOpcCurso=&carregarCidades=false&periodoInteresse=&carregarQtdAvaliacao=true'
    r = requests.get(base_url)
    #lista = []
    coments = json.loads(r.content)
    
    if coments['listOfertas'] != []:
        ofertas = coments['listOfertas'] 

        for i in range(len(ofertas)):
            chaves = []
            for e in ofertas[i]:
                chaves.append(e)
            
            lista_chaves_index = []
            for e in range(len(chaves)):
                lista_chaves_index.append(ofertas[i][chaves[e]])
            lista.append(lista_chaves_index)

        return escreverCSV(lista, curso, cidade, coments, id, id_cidade, chaves)


def escreverCSV(lista, curso, cidade, ofertas, id, id_cidade, chaves):   
    
    try:
        with open(f'./csv/{curso}.csv', mode='w', encoding='utf-8', newline='') as csv_file:
            fieldnames = chaves
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            writer.writeheader()
            for i in range(len(lista)):  
                dic_backup = {}
                for e in range(len(chaves)):
                    dic_backup[chaves[e]] = lista[i][e]
                writer.writerow(dic_backup)
        #print('Escrevendo...')
        return  0
    
    except:
        return 'Vazio'
