import requests, json, csv, os, uni
from uni import dadosCurso

with open(f'./csv/{curso}.csv', mode='w', encoding='utf-8', newline='') as csv_file:
            fieldnames = ['SIGLA_INSTITUICAO','BAIRRO_INSTITUICAO', 'VALOR_MENSALIDADE', 'cidade']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for i in range(len(coments['listOfertas'])):
                coments2 = coments['listOfertas'][i]
                if coments2['SIGLA_INSTITUICAO'] != None and coments2['VALOR_MENSALIDADE'] != None:
                    print(coments2['SIGLA_INSTITUICAO'], coments2['BAIRRO_INSTITUICAO'])
                    writer.writerow({'SIGLA_INSTITUICAO': coments2['SIGLA_INSTITUICAO'],'BAIRRO_INSTITUICAO':coments2['BAIRRO_INSTITUICAO'], 'VALOR_MENSALIDADE': coments2['VALOR_MENSALIDADE'], 'cidade': cidade})