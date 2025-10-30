# diadasemana=int(input('Qual dia da semana você quer sabe? '))

# if diadasemana==1:
#     print('Domingo')
# elif diadasemana==2:
#     print('Segunda')
# elif diadasemana==3:
#     print('Terça')
# elif diadasemana==4:
#     print('Quarta')
# elif diadasemana==5:
#     print('Quinta')
# elif diadasemana==6:
#     print('Sexta')
# elif diadasemana==7:
#     print('Sábado')
# else:
#     print('Número inválido para essa pergunta')

try:
    diadasemana=int(input('Qual dia da semana você quer sabe? '))
    match diadasemana:
        case 1:
            print('Domingo')
        case 2:
            print('Segunda')
        case 3:
            print('Terça')
        case 4:
            print('Quarta')
        case 5:
            print('Quinta')
        case 6:
            print('Sexta')
        case 7:
            print('Sábado')
        case _:
            print('Número inválidoooo')
except ValueError:
    print('Informação inválida, por favor informe um número de 1 a 7')