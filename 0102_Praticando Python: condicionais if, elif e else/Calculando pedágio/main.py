distancia_percorrida = float(input('Digite a distância percorrida em km: '))

if distancia_percorrida > 200:
    pedagio = distancia_percorrida * 30
elif 100 < distancia_percorrida <= 200:
    pedagio = distancia_percorrida * 20
else:
    pedagio = distancia_percorrida * 10

print(f'O valor total do pedágio é: R$ {pedagio:.2f}')
