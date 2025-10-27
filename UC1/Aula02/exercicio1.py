a=int(input('informe seu primeiro numero:'))
b=int(input('informe seu segundo numero:'))
c=int(input('informe seu terceiro numero:'))

primeiro=None
segundo=None
terceiro=None
if a<b and a<c:
    primeiro=a
    if b<c:
        segundo=b
        terceiro=c
    else:
        segundo=c
        terceiro=b
elif b<a and b<c: # bac ou bca
    primeiro=b
    if a<c:       # bac
        segundo=a
        terceiro=c
    else:         #bca
        segundo=c
        terceiro=a