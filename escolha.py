def preludio():
    print("Prelúdio: ")


def celeiro():
    Preludio()
    x = "WWW"
    print("Entrar no celeiro?\nS / N")
    while True:
        x = input()
        if x.capitalize() == 'S' or x.capitalize() == 'N':
            break
    if x is 's' or x is 'S':
        print("\nDentro do celeiro há uma escada para o patamar. Subir?\nS / N")
        while True:
            x = input()
            if x.capitalize() == 'S':
                break
        if x.capitalize() == 'S':
            print("\nPela janela do segundo andar você vê um homem segurando um machado indo rumo ao celeiro.")
            print("Fugir ou Esconder-se?\nF / E")
            
            while True:
                x = input()
                if x.capitalize() == 'F':
                    break
            if x.capitalize() == 'F':
                print("\nVocê desce a escada e vai para a porta dos fundos. Ela não abre de primeira.\nTentar com mais força ou procurar uma alternativa?\nT / A?")
                
                while True:
                    x = input()
                    if x.capitalize() == 'T':
                        break
                if x.capitalize() == 'T':
                    print("\nA porta range, mas não abre; atrás de você à entrada do celeiro o homem do machado\nte observa. Ao notar que você não tem saída, avança!")
                    print("Há uma pá no feno próximo a você. Você a pega. O que fazer: atacar a fechadura da porta e tentar fugir ou preparar para lutar?\nP / L")
                    
                    while True:
                        x = input()
                        if x.capitalize() == 'P':
                            break
                    if x.capitalize() == 'P':
                        print("O trinco se rompe e a porta abre o homem acelera, mas você foge.")
                        return 3
        else:
            print("\nVocê precisa se proteger o homem com machado está vindo te matar. Você pode tirar um cavalo do celeiro e fugir mesmo sem saber\ncomo cavalgar ou pode se esconder por entre o monte de palha. Fugir ou Esconder? F / E")
            
            while True:
                x = input()
                if x.capitalize() == 'F':
                    break
            if x.capitalize() is 'F':
                print("\nO cavalo está sem cela. Montar sem cela ou procurar a cela? S / C")
            
                while True:
                    x = input()
                    if x.capitalize() == 'S':
                        break
                if x.capitalize() is 'S':
                    print("\nO cavalo se irrita, relincha e empina, você se afasta e esbarra no Homem com o Machado,\nele move o machado para te atacar. Você abaixa ou pula para trás? B / P")

                    while True:
                        x = input()
                        if x.capitalize() == 'B':
                            break
                        if x.capitalize() is 'B':
                            print("Você desvia e se esgueira para fora. O cavalo irritadiço faz o Homem deixar o machado cair. Você aproveita o momento para...\nAtacar ou Fugir? A / F")

                            while True:
                                x = input()
                                if x.capitalize() == 'A':
                                    break
                            if x.capitalize() is 'A':
                                print("Ao avançar em sua direção o Homem olha para você e mesmo por baixo da máscara os olhos dele fixos em você te deixam congelado.")
                                return "Medo"
                else:
                    print("A cela está sobre a divisória, você a joga por cima do cavalo apressadamente e sobe no cavalo\nsem jeito você tenta fazer o cavalo andar, mas nada acontece.")
                    print("O Homem com o Machado entra no celeiro e você bate com força no dorso do cavalo que sai disparado.\nO Homem com o Machado atinge o cavalo que cai com um som agudo de dor. Você está bem apesar de tudo.")
                    print("Você continua a correr sem olhar para trás? S / N")

                    while True:
                        x = input()
                        if x.capitalize() == 'S':
                            print("Ops! Sua perna foi quebrada na queda. O Homem com o Machado se aproxima e corta sua cabeça.")
                            return "Decaptação"
                        elif x.capitalize() == 'N':
                            print("Sem escolha você decide confrontá-lo; o machado dele ficou preso ao cavalo, você pega o machado ou vai no X-1? M / X")

                            while True:
                                x = input()
                                if x.capitalize() == 'M':
                                    print("O cavalo ainda vivo e com dor reage por reflexo quando você puxa o machado\nele te dá um coice que te derruba.")
                                    return "Inconsciênte"
                                elif x.capitalize() == 'X':
                                    print("Você se põe em posição o seu oponente não se move, apenas te observa. Dá um passo para trás e some dentro do celeiro.")
                                    return "Sobrevivente"
            
    else:
        x = "WWW"
        print("\nVocê dá a volta no celeiro e vê três pessoas encapuzadas esfaqueando alguém que berra incontrolavelmente.\nVocê salva a pessoa ou a ignora?\nS / I")
        while x.capitalize() != 'S' or x.capitalize() != 'I':
            x = input()
        if x.capitalize() == 'S':
            print("\nVocê corre para cima deles saltando nas costas do indivíduo mais próximo,\nderrubando sua faca e fazendo os outros dois pararem de esquear a vítima.\nVocê pega a faca dele e...")
            print("Continua atacando o mesmo indivíduo, defende-se daquele tenta te atacar ou desvia dele e parte para cima do terceiro?\nIndivíduo: 1, 2 ou 3")
            i = 10
            
            while i > 3:
                i = int(input())
            if i == 1:
                print("\nVocê corta a garganta dele e é pego pelo braço enquanto o outro te acerta na barriga.\nVocê dá uma cabeçada em quem te segura e consegue se livrar e se ajoelha no chão com dor.")
                print("Olhando para o lado você nota que a vítima é na realidade um porco e é chutado na cara,\ncaído no chão o outro levanta a faca para fincá-la em você. Rolar para esquerda ou direta? E / D")
                
                while x.capitalize() != 'E' or x.capitalize() != 'D':
                    x = input()
                if x == 'E':
                    print("Você esbarra no cadáver que você matou e é atingido no peito pela faca e morre")
                    return "Esfaqueado"


print(celeiro().upper())

