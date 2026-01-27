dias_atividade_a = int(input('Informe os dias para a atividade A: '))
dias_atividade_b = int(input('Informe os dias para a atividade B: '))
dias_atividade_c = int(input('Informe os dias para a atividade C: '))

if dias_atividade_a < 0 or dias_atividade_b < 0 or dias_atividade_c < 0:
    print('Erro: O número de dias não pode ser negativo.')
else:
    tempo_total_projeto = dias_atividade_a + dias_atividade_b + dias_atividade_c
    print(f'O tempo total do projeto é de {tempo_total_projeto} dias.')