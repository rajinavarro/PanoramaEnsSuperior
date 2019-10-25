import requests, json, uni, os
from cidades import cidades, curso

nomeCurso = str(input('\nDigite pelo o menos as 3 primeiras letras do curso: '))
nomeCurso = nomeCurso.upper()
try:
    dir = './csv'
    os.makedirs(dir)
    cidades(curso(nomeCurso))

except:
    cidades(curso(nomeCurso))

print('FIM')