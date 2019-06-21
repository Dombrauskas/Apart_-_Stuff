"""
 " 
 " autor Maurício
 " 
 " 
"""

import os
import random

#os.system('clear') or None # Limpa a tela do console.

def preludio():
    print("Prelúdio: ")

def continua():
    x = input("\n\nPrecione ENTER para continuar...")
    print(x)


def celeiro():
    preludio()
    x = "WWW"
    print("Entrar no celeiro?\nS / N")
    
    # Celeiro
    while True:
        x = input()
        if x.capitalize() == 'S' or x.capitalize() == 'N':
            break
    # Dentro do Celeiro
    if x is 's' or x is 'S':
        print("\nDentro do celeiro há uma escada para o patamar. Subir?\nS / N")
        while True:
            x = input()
            if x.capitalize() == 'S':
                break
            elif x.capitalize() == 'N':
                break
        # No segundo andar
        if x.capitalize() == 'S':
            print("\nPela janela do segundo andar você vê um homem segurando um machado indo rumo ao celeiro.")
            print("Fugir ou Esconder-se?\nF / E")
            
            while True:
                x = input()
                if x.capitalize() == 'F' or x.capitalize() == 'E':
                    break
            # Fuga do Celeiro
            if x.capitalize() == 'F':
                print("\nVocê desce a escada e vai para a porta dos fundos. Ela não abre de primeira.\nTentar com mais força ou procurar uma alternativa?\nT / A?")
                
                while True:
                    x = input()
                    if x.capitalize() == 'T' or x.capitalize() == 'A':
                        break
                # Forçar a porta
                if x.capitalize() == 'T':
                    print("\nA porta range, mas não abre; atrás de você à entrada do celeiro o homem do machado\nte observa. Ao notar que você não tem saída, avança!")
                    print("Há uma pá no feno próximo a você. Você a pega. O que fazer: atacar a fechadura da porta e tentar fugir ou preparar para lutar?\nP / L")
                    
                    while True:
                        x = input()
                        if x.capitalize() == 'P' or x.capitalize() == 'L':
                            break
                    # Quebrar a porta do Celeiro
                    if x.capitalize() == 'P':
                        print("\nO trinco se rompe e a porta abre o homem acelera, mas você foge.")
                        continua()
                        return "Fugitivo"
                    # Lutando com a pá
                    else:
                        print("\nVocê pega a pá enquanto o Homem com o Machado se aproxima. Ele ataca, mas você desvia e contra-golpeia.")
                        print("Ele sangra e se zanga; em fúria extrema ele afunda o machado em seu peito\ncom tanta força que suas costelas saem pelas costas.")
                        continua()
                        return "Fatality"
                # Escolha da porta
                else:
                    print("\nPróximo a você a um monte de feno que você pode se esconder. Há também uma janela no alto,\ntalvez você possa alcançá-la e fugir por lá.\nFeno ou Janela? F / J")

                    while True:
                        x = input()
                        if x.capitalize() == 'F' or x.capitalize() == 'J':
                            break
                    # No palheiro
                    if x.capitalize() == 'F':
                        print("\nVocê se joga no monte de feno e espeta a mão. Você achou uma agulha no palheiro.")
                        continua()
                        return "Vencedor"
                    # Na janela
                    else:
                        print("\nVocê tenta e não alcança, mas ainda tem esperança. Tenta mais vez e consegue pela ponta dos dedos.\nCom esforço se levanta para a passagem, porém você não cabe nela, você se debate e se esforça;")
                        print("Logo você sente o frio metal do machado passando por você, o sabor do sangue lhe vem a boca e\nvocê tem certeza...")
                        continua()
                        return "Morri"
            # Esconde
            else:
                print("\nVocê olha ao redor e vê uma caminhonete e mais afastado uma sala que parece ser uma oficina.\nPara onde você vai? C / O")

                while True:
                    x = input()
                    if x.capitalize() == 'C' or x.capitalize() == 'O':
                        break
                    # Na caminhonete
                    if x.capitalize() == 'C':
                        print("\nVocê se entra na caçamba da caminhonete e põe a capa por cima.\nO Homem com o Machado está por perto e você olha na caçamba por algo para se defender se preciso.")
                        print("Sem querer você chuta a lateral da caminhote e o alarme dispara\no machado penetra a caçamba, mas não te acerta. Então a capa é rasgada e novamente você escapa.")
                        print("Saltar para fora ou ficar na caminhonete? S / F")

                        while True:
                            x = input()
                            if x.capitalize() == 'S' or x.capitalize() == 'F':
                                break
                            # Saindo...
                            if x.capitalize() == 'S':
                                print("No desespero você salta para fora o que surpreende o Homem com o Machado e vai rumo a oficina.\nNão há saída lá, então você pega uma enxada.")
                                print("O machado vai em sua direção e você interpõe a enxada no reflexo de defesa.\nA enxada se quebra e o Homem com o Machado te acerta com o cabo e você desmaia.")
                                continua()
                                return "Desmaio"
                            # Fique na caçamba
                            else:
                                print("A próxima machadada é certeira")
                                continua()
                                return "Alarmado"
                    
                    
                    # Na Oficina ???
                    else:
                        print("\nVocê corre para a pequena sala no canto, sobre a " +
                        "mesa há um martelo e uma serra, na parede oposta há pistola " +
                        "de pregos. O que você pega; martelo, serra ou pistola de " + 
                        "pregos?\nM / S / P")

                        while True:
                            x = input()
                            if x.capitalize() == 'M' or x.capitalize() == 'S' or x.capitalize() == 'P':
                                break
                        if x.capitalize() == 'M':
                            print("\n'Um martelo contra um machado?' - você pensa. " +
                            "Decidido a trocar pela pistola. Mas já era tarde, seu " +
                            "braço foi cortado fora, enquanto você grita de dor leva " +
                            "outra machadada na perna. Conforme seu corpo diminui sua dor aumenta.")
                            continua()
                            return "Desmembrado"
                        elif x.capitalize() == 'S':
                            print()
                        else:
                            print()

        # No primeiro andar
        else:
            print("\nVocê precisa se proteger o homem com machado está vindo te matar. Você pode tirar " +
            "um cavalo do celeiro e fugir mesmo sem saber como cavalgar ou pode se esconder por entre o " +
            "monte de palha. Fugir ou Esconder? F / e - Sem")
            
            while True:
                x = input()
                if x.capitalize() == 'F':
                    break
            # Pé-de-Pano meu amigo
            if x.capitalize() == 'F':
                print("\nO cavalo está sem cela. Montar sem cela ou procurar a cela? S / c - Sem")
            
                while True:
                    x = input()
                    if x.capitalize() == 'S':
                        break
                # Para quê serve a cela?!
                if x.capitalize() == 'S':
                    print("\nO cavalo se irrita, relincha e empina, você se afasta e esbarra no Homem com o Machado,\nele move o machado para te atacar. Você abaixa ou pula para trás? B / p - Sem")

                    while True:
                        x = input()
                        if x.capitalize() == 'B':
                            break
                    # Desviando do Machado
                    if x.capitalize() == 'B':
                        print("Você desvia e se esgueira para fora. O cavalo irritadiço faz o Homem deixar o machado cair. Você aproveita o momento para...\nAtacar ou Fugir? A / f - Sem")

                        while True:
                            x = input()
                            if x.capitalize() == 'A':
                                break
                        # Vou Lutar
                        if x.capitalize() == 'A':
                            print("Ao avançar em sua direção o Homem olha para você e mesmo por baixo da máscara os olhos dele fixos em você te deixam congelado.")
                            continua()
                            return "Medo"
                # Caindo do cavalo
                else:
                    print("A cela está sobre a divisória, você a joga por cima do cavalo apressadamente e sobe no cavalo\nsem jeito você tenta fazer o cavalo andar, mas nada acontece.")
                    print("O Homem com o Machado entra no celeiro e você bate com força no dorso do cavalo que sai disparado.\nO Homem com o Machado atinge o cavalo que cai com um som agudo de dor. Você está bem apesar de tudo.")
                    print("Você continua a correr sem olhar para trás? S / N")

                    while True:
                        x = input()
                        if x.capitalize() == 'S':
                            print("Ops! Sua perna foi quebrada na queda. O Homem com o Machado se aproxima e corta sua cabeça.")
                            continua()
                            return "Decaptação"
                        elif x.capitalize() == 'N':
                            print("Sem escolha você decide confrontá-lo; o machado dele ficou preso ao cavalo, você pega o machado ou vai no X-1? M / X")
                            x = input()
                            if x.capitalize() == 'M' or x.capitalize() == 'X':
                                break
                    # O machado é meu
                    if x.capitalize() == 'M':      
                        print("O cavalo ainda vivo e com dor reage por reflexo quando você puxa o machado\nele te dá um coice que te derruba.")
                        continua()
                        return "Inconsciênte"
                    elif x.capitalize() == 'X':
                        print("Você se põe em posição o seu oponente não se move, apenas te observa. Dá um passo para trás e some dentro do celeiro.")
                        continua()
                        return "Sobrevivente"
            
    # Fora do Celeiro
    else:
        x = "WWW"
        print("\nVocê dá a volta no celeiro e vê três pessoas encapuzadas esfaqueando alguém que berra " +
        "incontrolavelmente.\nVocê salva a pessoa ou a ignora?\nS / i - Sem")

        while True:
            x = input()
            if x.capitalize() == 'S':
                break
        # Bom Samaritano
        if x.capitalize() == 'S':
            print("\nVocê corre para cima deles saltando nas costas do indivíduo mais próximo, derrubando " + 
            "sua faca e fazendo os outros dois pararem de esquear a vítima.\nVocê pega a faca dele e...")
            print("Continua atacando o mesmo indivíduo, defende-se daquele tenta te atacar ou desvia dele e " + 
            "parte para cima do terceiro?\nIndivíduo: 1, 2 ou 3")
            
            i = 0
            while i > 3 or i < 1:
                i = int(input())
            # Terminando o serviço
            if i == 1:
                print("\nVocê corta a garganta dele e é pego pelo braço enquanto o outro te acerta na barriga. " +
                "Você dá uma cabeçada em quem te segura e consegue se livrar e se ajoelha no chão com dor. " +
                "Olhando para o lado você nota que a vítima é na realidade um porco e é chutado na cara, caído " + 
                "no chão o outro levanta a faca para fincá-la em você. Rolar para esquerda ou direta? E / d - Sem")
                
                while True:
                    x = input()
                    if x.capitalize() == 'E':
                        break
                # Dois cadáveres
                if x.capitalize() == 'E':
                    print("\nVocê esbarra no cadáver que você matou e é atingido no peito pela faca e morre")
                    continua()
                    return "Esfaqueado"

                
l = list()
r = {}
n = 0
while n <= 0 or n > 10:
    n = int(input("Quantas pessoas vão jogar? "))

for j in range(n):
    l.append(input())

random.shuffle(l, random=None)
os.system('clear') or None

print("Vez de ", end="")
for e in range(n):
    print(l[e])
    r[l[e]] = celeiro().upper()
    os.system('clear') or None
    
# Os elementos da lista serão o conteúdo do dicionário.
#dic = { 1: l[0], 2: l[1] }

for k in r:
  print(k, r[k])

