despesas_total = float(input('Digite o total de despesas do mês: R$ '))

if despesas_total > 3000:
    print('Atenção! Você ultrapassou o orçamento mensal.')
else:
    print('Parabéns! Você está dentro do orçamento mensal.')
