nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7:
    print(f'Parabéns! Sua média é {media:.2f}. Você foi aprovado.')
elif 5 <= media < 7:
    print(f'Sua média é {media:.2f}. Você está de recuperação.')
else:
    print(f'Sua média é {media:.2f}. Você foi reprovado.')
