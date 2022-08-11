# # Calcula a média de um aluno baseando-se em duas notas, onde a média necessária para passar é 6.
nota1 = input('Insira a 1º nota: ')  # Entrada de dados das notas
nota2 = input('Insira a 2º nota: ')
nota3 = input('Insira a 3º nota: ')
aprovado = 'Parabéns! Você foi aprovado.'  # Variáveis com as mensagens de aprovação e reprovação
reprovado = 'Infelizmente você foi reprovado.'

if nota1.isdigit() and nota2.isdigit():  # Checa se o que foi inserido são números
    nota1 = int(nota1)  # Converte de string para int (typecast)
    nota2 = int(nota2)
    nota3 = int(nota3)
    media = (nota1 + nota2 + nota3) / 2  # Decisão: Calculo feito baseado nas notas e que decide se o aluno é
    # aprovado ou não.
    if media >= 6:  # Sea média dele for maior que 6.
        print(aprovado)  # Mostra a mensagem de aprovado
    else:  # se não 
        print(reprovado)  # Mostra mensagem de reprovado
else:
    print('Insira apenas números, por favor.')  # Caso qualquer outra coisa além de números sejam
# inseridos, essa mensagem de erro é mostrada.
