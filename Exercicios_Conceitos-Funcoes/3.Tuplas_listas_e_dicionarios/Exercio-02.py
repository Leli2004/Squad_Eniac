### Exercícios 
#### Tuplas, listas e dicionários
# #2. Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
import numpy as np

listaNotas = []
notasAlunos = []

for i in range(2):
    media = 0
    notasAlunos = []
    print('Aluno: ' + str(i+1))
    for j in range(4):
        notasAlunos.append(float(input('Nota: '+ str(j+1) + '\n')))
    print(notasAlunos)
    mediat = np.average(notasAlunos)
    print(f'media dos aluno {i+1}: {mediat:,.2f}')
    listaNotas.append(mediat)

#print(listaNotas)

nota_max = max(listaNotas)
nt_notas=[]
for i in range(2):
    if(listaNotas[i] >= 7):
        nt_notas.append(listaNotas[i])
        print(listaNotas[i])

print(f'Total de notas maior ou igual a 7.0: {len(nt_notas)}')
    