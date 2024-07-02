letras = set()
palavra = input('Digite uma letra para acertar a forcaa palavra que o seu adversário deve adivinhar: ').upper()
palavra_adivinhada = ['_' for _ in palavra]
letras_erradas = []
tentativas = 6

while True:
    letra = input('Digite uma letra para acertar a forca: ').upper()

    if letra in letras:
        print(f'Você já tentou a letra {letra}, tente outra.')
        continue

    letras.add(letra)

    if letra in palavra.upper():
        for idx, char in enumerate(palavra.upper()):
            if char == letra:
                palavra_adivinhada[idx] = letra
        print(f'Você acertou uma letra: {letra}')
    else:
        letras_erradas.append(letra)
        print(f'Errou')

    print('Letras erradas até agora:', ', '.join(letras_erradas))
    print('Progresso atual da palavra:', ' '.join(palavra_adivinhada))

    if '_' not in palavra_adivinhada:
        print('Parabéns! Você adivinhou a palavra:', palavra)
        break
    if len(letras_erradas) >= tentativas:
            print('Você excedeu o número máximo de tentativas erradas. Fim de jogo!')
            print(f'A palavra era: {palavra}')
            break