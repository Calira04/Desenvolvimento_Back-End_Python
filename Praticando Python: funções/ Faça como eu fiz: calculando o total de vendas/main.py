import os

def calcular_total_vendas(valores_vendas):
    os.system('clear')
    
    for valor in valores_vendas:
        valor_convertido = float(valor)
        vendas_convertidas.append(valor_convertido)
    for venda in vendas_convertidas:
        venda += venda
    print(f'O total de vendas é: R$ {venda:.2f}')

valores_vendas = input('Digite os valores das vendas: ').split()
vendas_convertidas = []

calcular_total_vendas(valores_vendas)