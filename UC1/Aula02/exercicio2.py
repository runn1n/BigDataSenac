nota1=5
nota2=7
nota3=4
nota4=1

Nota=nota1+nota2+nota3+nota4
media=Nota/4
print(media)

if media > 7:
    print('aprovado')
elif media >= 5 and media <= 7:
    print('recuperacao')
elif media < 5:
    print('reprovado')
else:
    print('Informe um valor correto')