renda_mensal = float(input('Digite sua renda mensal: R$ '))
valor_parcela = float(input('Digite o valor da parcela do empréstimo: R$ '))

porcentagem_renda = (valor_parcela / renda_mensal) * 100

if porcentagem_renda > 30:
    print('Empréstimo negado. A parcela excede 30% da sua renda mensal.')
else:
    print('Empréstimo aprovado. A parcela está dentro do limite permitido.')
