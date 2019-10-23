from uni import dadosCurso, os, listCidades

curso = str(input('\nDigite pelo o menos as 3 primeiras letras do curso: '))

try:
    dir = './csv'
    os.makedirs(dir)
    dadosCurso(curso, 1345)

except:
    dadosCurso(curso, 1345)

