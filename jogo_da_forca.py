palavra = "python"
letras_acertadas = []
erros = 0
limite_erros = 6

while erros < limite_erros:
    # Exibe a palavra com underscores para letras não descobertas
    # ...

    # Pede letra ao usuário
    letra_usuario = input("Chute uma letra: ")

    if letra_usuario in palavra:
        letras_acertadas.append(letra_usuario)
        # Verifica vitória
        if len(letras_acertadas) == len(set(palavra)):
            print("Você Venceu!")
            break
    else:
        erros += 1
        print(f"Errou! {limite_erros - erros} tentativas restantes.")

if erros == limite_erros:
    print("Game Over! Você perdeu.")
