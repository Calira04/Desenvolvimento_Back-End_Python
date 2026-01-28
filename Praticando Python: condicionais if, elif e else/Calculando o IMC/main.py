peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}. Você está abaixo do peso.')
elif 18.5 <= imc < 24.9:
    print(f'Seu IMC é {imc:.2f}. Você está com o peso normal.')
elif 25 <= imc < 29.9:
    print(f'Seu IMC é {imc:.2f}. Você está com sobrepeso.')
else:
    print(f'Seu IMC é {imc:.2f}. Você está com obesidade.')
