import random

def desenhar_forca(tentativas_restantes):
    # estágio atual do jogo, dependendo da quantia de erros. Os 'r' no começo de cada linha é para ignorar sintaxe.
    estagios_forca = [
    
    [r" ___________.._______",
    r"| .__________))______|",
    r"| | / /      ||",
    r"| |/ /       ||",
    r"| | /        ||",
    r"| |/         ||",
    r"| |          ||",
    r"| |          ||",
    r"| |         // \ ",
    r"| |        ((  ))",
    r"| |         \ //",
    r"| |          """,
    r"| |",
    r"| |",
    r"| |",
    r"| |",
    r"| |",
    r"| |",
    r"''''''''''''''''''''''''|",
    r"|'|'''''''''''''''''''|'|",
    r"| |                   | |",
    r": :                   : :",
    r". .                   . ."],
    
    [r" ___________.._______",
    r"| .__________))______|",
    r"| | / /      ||",
    r"| |/ /       ||",
    r"| | /        ||",
    r"| |/         ||.—''.",
    r"| |          |/  _  \ ",
    r"| |          ||  `/,|",
    r"| |          (\`_.'",
    r"| |           `——'",
    r"| |",
    r"| |",
    r"| |",
    r"| |",
    r"| |",
    r"| |",
    r"| |",
    r"| |",
    r"''''''''''''''''''''''''|",
    r"|'|'''''''''''''''''''|'|",
    r"| |                   | |",
    r": :                   : :",
    r". .                   . ."],
    
    [r" ___________.._______",
    r"| .__________))______|",
    r"| | / /      ||",
    r"| |/ /       ||",
    r"| | /        ||",
    r"| |/         ||.—''.",
    r"| |          |/  _  \ ",
    r"| |          ||  `/,|",
    r"| |          (\`_.'",
    r"| |         .—`——'.",
    r"| |         \ . . /",
    r"| |          |   |",
    r"| |          | . |",
    r"| |          |___|",
    r"| |",
    r"| |",
    r"| |",
    r"| |",
    r"''''''''''''''''''''''''|",
    r"|'|'''''''''''''''''''|'|",
    r"| |                   | |",
    r": :                   : :",
    r". .                   . ."],
    
    [r" ___________.._______",
    r"| .__________))______|",
    r"| | / /      ||",
    r"| |/ /       ||",
    r"| | /        ||",
    r"| |/         ||.—''.",
    r"| |          |/  _  \ ",
    r"| |          ||  `/,|",
    r"| |          (\`_.'",
    r"| |         .—`——'.",
    r"| |        /Y . . /",
    r"| |       // |   |",
    r"| |       || | . |",
    r"| |       ') |___|",
    r"| |",
    r"| |",
    r"| |",
    r"| |",
    r"''''''''''''''''''''''''|",
    r"|'|'''''''''''''''''''|'|",
    r"| |                   | |",
    r": :                   : :",
    r". .                   . ."],
    
    [r" ___________.._______",
    r"| .__________))______|",
    r"| | / /      ||",
    r"| |/ /       ||",
    r"| | /        ||",
    r"| |/         ||.—''.",
    r"| |          |/  _  \ ",
    r"| |          ||  `/,|",
    r"| |          (\`_.'",
    r"| |         .—`——'.",
    r"| |        /Y . . Y\ ",
    r"| |       // |   | '\ ",
    r"| |       || | . |  '\ ",
    r"| |       ') |___|   (`",
    r"| |",
    r"| |",
    r"| |",
    r"| |",
    r"''''''''''''''''''''''''|",
    r"|'|'''''''''''''''''''|'|",
    r"| |                   | |",
    r": :                   : :",
    r". .                   . ."],
    
    [r" ___________.._______",
    r"| .__________))______|",
    r"| | / /      ||",
    r"| |/ /       ||",
    r"| | /        ||",
    r"| |/         ||.—''.",
    r"| |          |/  _  \ ",
    r"| |          ||  `/,|",
    r"| |          (\`_.'",
    r"| |         .—`——'.",
    r"| |        /Y . . Y\ ",
    r"| |       // |   | '\ ",
    r"| |       || | . |  '\ ",
    r"| |       ') |   |   (`",
    r"| |          ||——'",
    r"| |          ||",
    r"| |          ||",
    r"| |          ||",
    r"''''''''''|_/ |     |'''|",
    r"|'|'''''''\ \—'     ''|'|",
    r"| |        \ \        | |",
    r": :         \ \       : :",
    r". .          `'       . ."],
    
    [r" ___________.._______",
    r"| .__________))______|",
    r"| | / /      ||",
    r"| |/ /       ||",
    r"| | /        ||",
    r"| |/         ||.—''.",
    r"| |          |/  _  \ ",
    r"| |          ||  `/,|",
    r"| |          (\`_.'",
    r"| |         .—`——'.",
    r"| |        /Y . . Y\ ",
    r"| |       // |   | '\ ",
    r"| |       || | . |  '\ ",
    r"| |       ') |   |   (`",
    r"| |          ||—||",
    r"| |          || ||",
    r"| |          || ||",
    r"| |          || ||",
    r"''''''''''|_/ | | \ |'''|",
    r"|'|'''''''\ \—'  —' ''|'|",
    r"| |        \ \        | |",
    r": :         \ \       : :",
    r". .          `'       . ."]
    
    ]
    
    # Adiciona partes do boneco baseado no número de erros (6 - tentativas_restantes)
    erros = 6 - tentativas_restantes
    
    # Garante que o índice não exceda o tamanho da lista
    if erros < 0:
        erros = 0
    if erros >= len(estagios_forca):
        erros = len(estagios_forca) - 1
        
    for linha in estagios_forca[erros]:
        print(linha)

def jogar_forca():
    print(r"    __________  ____  _________    __")
    print(r"   / ____/ __ \/ __ \/ ____/   |  / /")
    print(r"  / /_  / / / / /_/ / /   / /| | / /")
    print(r" / __/ / /_/ / _, _/ /___/ ___ |/_/")
    print(r"/_/    \____/_/ |_|\____/_/  |_(_)")
    
    # Lista de palavras embutida no código
    palavras = [
        "banana", "abacaxi", "laranja", "morango", "uva",
        "computador", "python", "programacao", "algoritmo",
        "jogos", "desenvolvimento", "teclado", "internet",
        "software", "hardware", "monitor", "memoria"
    ]
    
    palavra_secreta = random.choice(palavras).upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    letras_erradas = []
    tentativas = 6
    
    # Mostra a forca vazia no início
    desenhar_forca(tentativas)
    print("\nPalavra:", " ".join(letras_acertadas))
    print(f"Você tem {tentativas} tentativas")
    
    while True:
        chute = input("\nDigite uma letra: ").strip().upper()
        
        if len(chute) != 1 or not chute.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue
            
        if chute in letras_acertadas or chute in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue
            
        if chute in palavra_secreta:
            for i, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_acertadas[i] = letra
            print("\nAcertou!")
        else:
            letras_erradas.append(chute)
            tentativas -= 1
            print("\nErrou! Letras erradas:", " ".join(letras_erradas))
            print(f"Tentativas restantes: {tentativas}")
        
        # Desenha a forca com o boneco atualizado
        print()
        desenhar_forca(tentativas)
        print("\nPalavra:", " ".join(letras_acertadas))
        
        # Verifica se ganhou
        if "_" not in letras_acertadas:
            print(r" __  __      __                                __")
            print(r"/\ \/\ \  __/\ \__                __          /\ \ ")
            print(r"\ \ \ \ \/\_\ \ ,_\   ___   _ __ /\_\     __  \ \ \ ")
            print(r" \ \ \ \ \/\ \ \ \/  / __`\/\`'__\/\ \  /'__`\ \ \ \ ")
            print(r"  \ \ \_/ \ \ \ \ \_/\ \L\ \ \ \/ \ \ \/\ \L\.\_\ \_\ ")
            print(r"   \ `\___/\ \_\ \__\ \____/\ \_\  \ \_\ \__/.\_\\/\_\ ")
            print(r"    `\/__/  \/_/\/__/\/___/  \/_/   \/_/\/__/\/_/ \/_/ ")
            print("")
            print(f"A palavra era: {palavra_secreta}")
            break
            
        # Verifica se perdeu
        if tentativas == 0:
            print(r" ____                                __                       _ ")
            print(r"/\  _`\                             /\ \__                  /' \ ")
            print(r"\ \ \/\ \     __   _ __   _ __   ___\ \ ,_\    __       __ /\ ,/' ")
            print(r" \ \ \ \ \  /'__`\/\`'__\/\`'__\/ __`\ \ \/  /'__`\    /\_\\ \ \ ")
            print(r"  \ \ \_\ \/\  __/\ \ \/ \ \ \//\ \L\ \ \ \_/\ \L\.\_  \/_/_\ \ `\ ")
            print(r"   \ \____/\ \____\\ \_\  \ \_\\ \____/\ \__\ \__/.\_\   /\_\\ `\__\ ")
            print(r"    \/___/  \/____/ \/_/   \/_/ \/___/  \/__/\/__/\/_/   \/_/ `\/_/ ")
            print("")
            print(f"A palavra era: {palavra_secreta}")
            break

# Pede se o jogador quer jogar novamente
if __name__ == "__main__":
    while True:
        jogar_forca()
        jogar_novamente = input("\nDeseja jogar novamente? (S/N): ").strip().upper()
        if jogar_novamente != "S":
            print("\nObrigado por jogar! Até mais!")
            break