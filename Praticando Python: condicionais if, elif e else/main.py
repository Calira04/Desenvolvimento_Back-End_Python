macas_vendidas = int(input('Digite a quantidade de maçãs vendidas: '))
bananas_vendidas = int(input('Digite a quantidade de bananas vendidas: '))

if macas_vendidas > bananas_vendidas:
    print('As maçãs tiveram mais vendas.')
elif bananas_vendidas > macas_vendidas:
    print('As bananas tiveram mais vendas.')
else:
    print('As vendas de maçãs e bananas foram iguais.')
