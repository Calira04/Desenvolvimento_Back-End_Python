def contador(palavra):
    total = len(palavra)
    print(f'A palavra "{palavra}" tem {total} caracteres.')

palavra = str(input("Digite uma palavra: "))

contador(palavra)