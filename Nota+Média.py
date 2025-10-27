Aluno = 'Bruno'
total_notas = 0 
total_pontos = 0 
media = 0 

while total_notas <4:
    notas = int(input('Qual foi a sua nota?: '))
    total_notas = total_notas + 1 
    total_pontos = total_pontos + notas
    media = total_pontos / total_notas
    print(f'A nota do Bruno foi de {notas}, com uma média de {media:.2f}')

if notas >= 6:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')