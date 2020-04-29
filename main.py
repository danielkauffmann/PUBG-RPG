# PlayerUnknown's BattleGrounds - RPG
# Criado e idealizado por Daniel Henrique Venna Kauffmann


import math
import random
import time
import sys



# -------------
# | PUBG LOGO |
# -------------



def logo():
    print('')
    print('')
    print('             `.....................```......`............``....................``````  ` `          ')
    print('            .////////////////////////://////////////////////////////////////////////:` ``.`         ')
    print('            .////::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::://///.              ')
    print('            .////`  ``````````````` `` ```      `````````````````````````````````////-              ')
    print('           `.////`                                                               :///- `            ')
    print('         -:::///:`    .:::::::---`  `:---   .---`  `:::::::::-`  `-::::::::-`    :////:::`          ')
    print('         :///////`    -//////////-  `////`  :///-  `//////////.  -/////////:.    :///////.          ')
    print('         `..-////`    -///:``:///:  `:///`  :///-  `////``:///.  -///:``.///.    :///:..`           ')
    print('            .////`    -///:  :///-  `////`  -///-  `////  :///.  -///:   :::.    :///-              ')
    print('            .////.    -///:  :///-  `////`  -///-  `///:  :///`  -///:           :///:              ')
    print('            .////.    -///:  :///:  `////`  -///:  `////  :///.  .///:           :///:              ')
    print('            .////`    :///-``-///-  `////`  :///:  ://///:///:`  .///: .///:-    :///:              ')
    print('            .////`   `///////////-  `////`  -///:  ://///////:`  .///: .////:    :///:              ')
    print('            .////`   `:////::::::`  `////`  -///:  .////``:///-  .///:  -///:    :///:              ')
    print('            .////`    -///:         `////`  -///-  `////  :///-  -///:  -///:    :///:              ')
    print('            .////`    .///:         .////`  -///-  `////  :///-  -///:  -///:    :///:              ')
    print('            .////`    -///:         .////`  :///-  `////  -///-  -///:  .://-    :///:              ')
    print('         `..-////`    -///:         .////..`:///-  `///:``:///-  -///:.`.///-    :///:..`           ')
    print('         ://////:`    -///:         .///////////.  `//////////-  .//////////-    :///////.          ')
    print('         -//////:`    .:::-          -----------   `---------.    .----:::--`    :////:/:`          ')
    print('          ``.///:`                                                               -///:``            ')
    print('            .////.`````     `````````````````` ``````````````````````````````````:///:`             ')
    print('            ./////:::::::::::::::::::::::::::::::::::::::::::::::::/:://:::::/:::////:`             ')
    print('            `:///////////////////////////:///////////////////////////////////////////-              ')
    print('             ``````...................``````.``.``...........``````..........`.....``               ')
    print('')
    print('')

logo()



# -------------------------------
# | Regras e Explicação do Jogo |
# -------------------------------



print("Seja muito bem-vindo ao PlayerUnknown's BattleGrounds (PUBG) - RPG")
print('')
time.sleep(1)

print('O jogo consiste em ser o último sobrevivente entre os 100 participantes!')
time.sleep(5)

print('Seu objetivo é lootear armas, equipamentos e cura para batalhar com os inimigos.')
time.sleep(5)

print('Além das batalhas, para movimentar os jogadores, existe o gás que irá avançar no decorrer da partida.')
time.sleep(6)

print('Ele tem o formato de círculo e irá fechar cada vez mais em função do tempo da partida.')
time.sleep(5)

print('Também, precisará tomar cuidado com a zona vermelha, na qual é escolhida aleatoriamente no mapa, onde cairão bombas do céu.')
time.sleep(7)

print('Você será avisado antes de ambas acontecerem.')
time.sleep(3)

print('Você será avaliado no final da partida diante da sua colocação e tempo permanecido vivo.')
time.sleep(7)

print('Inicialmente, terá de escolher em qual cidade quer cair de paraquedas do avião, no qual todos estarão dentro.')
print('')
time.sleep(7)

print('A ilha em que você sobreviverá será a Ilha de Erangel, possui 6km por 4km de área e cinco principais cidades.')
time.sleep(5)

print('Aqui estão as cidades com suas respectivas características:')
time.sleep(3)

print('')
print('                           Georgopol')
print('Localizada no noroeste da ilha, a cidade de Georgopol é um porto de cargas e possui muitos containers.')
print('Tem alguns galpões com loot, porém a maioria do loot fica em cima dos containers.')
print('Tome cuidado pois em cima dos containers não há proteção e esconderijos.')
print('Pode subir nos guindastes para pegar inimigos de longe ou lá de cima, é uma posição overpower.')
print('')
time.sleep(20)

print('                        Yasnya Polyana')
print('Ao lado da nascente do Rio Rangel, Polyana fica no nordeste e é a maior cidade da ilha, contando com a grande maioria de casas, cerca de 6 prédios e alguns galpões.')
print('Seu loot é bem espalhado e demorado para se equipar totalmente, por outro lado, há muita proteção dentro das construções e mais chances de permanecer vivo.')
print('É uma cidade com altas chances de possuir carros na rua ou nas garagens que existem na cidade. Pode utilizar ao seu favor caso precisar!')
print('Se der sorte, a zona segura pode fechar lá e quem sabe vencer o jogo!')
print('')
time.sleep(20)

print('                            Pochinki')
print('Pochinki fica no centro da ilha e é a principal cidade pois todas principais estradas passam por ela.')
print('Possui um loot um pouco melhor do que as cidades anteriores e consiste em apenas casas com uma igreja no morro ao lado da cidade.')
print('Mesmo tendo bastante proteção para batalhas, é bem menor que Polyana e seus combates são mais rápidos.')
print('Com certeza tem no mínimo um carro na cidade e rotas de fuga com facilidade no acesso.')
print('')
time.sleep(20)

print('                            Primorsk')
print('Localizada na parte sudoeste da ilha, Primorsk também é representada por grande parte de casas e 3 galpões na beira do mar.')
print('Tem altas chances de ter carros e barcos, porém fica muito distante das outras cidades. Precisa de um carro para sair de lá.')
print('Se o gás não for favorável, precisará sair rápido de lá. Em contraponto seu loot é bom mas espalhado.')
print('Com barcos, consegue chegar rapidamente em Georgopol, na ponte oeste e na Base Militar caso precise.')
print('')
time.sleep(20)

print('                             Mylta')
print('Mylta fica no sudeste, bem próximo da ponte leste que liga a Base Militar. Formada por apenas casas, possui um loot mais fraco e espalhado.')
print('Porém, é a cidade ideal para marcar jogadores que saem da Base Militar pela ponte. Essa estratégia é muito frequente e conhecida por muitos.')
print('Possui acesso a estrada que dá direto em Pochinki e beira a costa também.')
print('Barcos e carros são comuns na área e muito úteis para se movimentar por ali e montar estratégias.')
print('')
time.sleep(20)



# --------------
# | Preparado? |
# --------------



pronto = input('Você está pronto? ')
pronto = pronto.lower()

if pronto == 'sim' or pronto == 's':
    print('Boa! Esse é o espírito!! Vamos começar em breve...')
    print('')
elif pronto == 'não' or pronto == 'nao' or pronto == 'n':
    lerdnv = input('Não tem problema... vai conseguir! Quer um tempo a mais para ler as informações anteriores? ')
    lerdnv = lerdnv.lower()
    if lerdnv == 'sim' or lerdnv == 's':
        print('Beleza, vou dar mais dois minutos para ler as coisas de novo!')
        time.sleep(120)
    else:
        print('Tudo bem então, vamos começar em breve!')
else:
    print('Eu entendo a indecisão... mas digo para confiar em você! Vai conseguir parceiro!')

time.sleep(5)



# -------------------
# | Função do Final |
# -------------------


def final():
    second_time = time.time() #final do contador de tempo
    diferenca_tempo = second_time - first_time
    tempo = diferenca_tempo/60
    print('')
    print('Tempo vivo:.................',format(tempo,'.2f'),'minutos')
    print('Abates:.....................',kills)
    print('Fugas de combates:..........',fugir)
    print('Fuga de Zona Vermelha:......',fugir_zm)
    print('')

    classi = (kills - fugir - fugir_zm)*tempo
    
    if classi > 20:
        print('Sua classificação final foi de Sobrevivente Experiente! Incrível!')
    elif classi > 14:
        print('Sua classificação final foi de Sobrevivente Mediano!')
    elif classi > 0:
        print('Sua classificação final foi de Sobrevivente Iniciante!')
    elif classi < 0:
        print('Sua classificação final foi de Quase Sobrevivente!')
    else:
        print('Sua classificação final foi de Super Iniciante! Precisa treinar mais...')
    print('')
    sys.exit()



# ----------------------
# | Início da gameplay |
# ----------------------


#variáveis mapas
georgopol_ir = 0
polyana_ir = 0
pochinki_ir = 0
primorsk_ir = 0
mylta_ir = 0
#fim variaveis

print('')
print('')
print('')
print('')
print('')
print('Você embarcou no avião C-130 em direção à Ilha de Erangel com outras 99 pessoas.')
print('')
time.sleep(3)

print('Há escoteiros, prisioneiros, lutadores, corredores, todos os tipos de pessoas.')
print('')
time.sleep(3)

print('Cada um tem uma habilidade que pode usar ao seu favor, porém, as armas são um diferencial.')
print('')
time.sleep(4)

print('Sua escolha é sábia e faz parte da sua estratégia para ganhar!')
print('')
time.sleep(2)

print('Estamos nos aproximando da ilha, em minutos passaremos pelas primeiras cidades.')
print('')
time.sleep(6)

print('')
print('...')
print('')
time.sleep(4)

print('Piloto: Muito bom dia sobreviventes! Em cerca de um minuto passaremos por Georgopol e Polyana.')
print('')
time.sleep(5)

print('Piloto: Estamos vindo do norte da ilha, vocês terão 30 segundos para escolher em pular ou esperar.')
print('')
time.sleep(6)

print('...')
print('')
time.sleep(3)

print('Você: Ali, estou vendo o porto de Georgopol!!')
print('')
time.sleep(3)

print('Piloto: Passageiros, chegou a hora!, voces tem a opção de pular agora e escolherem entre Georgopol e Polyana.')
print('')
time.sleep(6)

print('Piloto: A partir de agora, 15 segundos para fazerem as decisões!')
print('')


first_time = time.time() #início do contador de tempo

pular_norte = input('Você deseja pular de paraquedas agora? ')
pular_norte = pular_norte.lower()

if pular_norte == 'sim' or pular_norte == 's':
    geor_poly = input('Demais! Quer ir para Georgopol ou Polyana? ')
    geor_poly = geor_poly.lower()
    if geor_poly == 'georgopol':
        print('Então vamos para Georgopol! Chegamos em 30 segundos lá!')
        georgopol_ir = 1
    else:
        print('Então vamos para Yasnya Polyana! Chegamos em 30 segundos lá!')
        polyana_ir = 1
else:
    print('Sem problemas! Já já aproximaremos da próxima cidade, jovem!')

time.sleep(10)

if georgopol_ir == 1:
        arma_pri = '.'
        kills = 0
        fugir = 0
        fugir_zm = 0
        granada_frag = 0
        print('Estamos caindo nos containers!')
        time.sleep(5)

        print('')
        print('Aterrissamos!')
        time.sleep(1)
        print('Você: Caramba, esses containers machucam mesmo...')
        time.sleep(4)
        print('... looteando ...')
        print('')
        time.sleep(6)
        

        colete = random.randint(1,9)
        if colete == 1 or colete == 2 or colete == 3 or colete == 4:
            print('Você achou um colete nível 1 em cima dos containers!')
            colete_eq = 1
            time.sleep(3)
        elif colete == 5 or colete == 6 or colete == 7:
            print('Você achou um colete nível 2 em cima dos containers!')
            colete_eq = 2
            time.sleep(3)
        else:
            print('Você achou um colete nível 3 em cima dos containers!')
            colete_eq = 3
            time.sleep(3)
        
        print('')

        capacete = random.randint(1,9)
        if capacete == 1 or capacete == 2 or capacete == 3 or capacete == 4:
            print('Encontrou um capacete nível 1 ao lado também!')
            capacete_eq = 1
            time.sleep(3)
        elif capacete == 5 or capacete == 6 or capacete == 7:
            print('Encontrou um capacete nível 2 ao lado também!')
            capacete_eq = 2
            time.sleep(3)
        else:
            print('Encontrou um capacete nível 3 ao lado também!')
            capacete_eq = 3
            time.sleep(3)

        print('')

        arma = random.randint(1,7)
        if arma == 1 or arma == 2 or arma == 3 or arma == 4:
            m4a4ouAK47 = random.randint(1,2)
            if m4a4ouAK47 == 1:
                print('Dentro de um container havia uma M416, um poderoso rifle automático para curta/média distância, será sua arma principal!')
                time.sleep(2)
                print('Veio com 120 munições 5.56mm e sua arma possui controle de recoil fácil comparado com a AK-47')
                arma_eq = 1
                time.sleep(5)
            else:
                print('Dentro de um container havia uma AK-47, ótimo para curta distância, será sua arma principal!')
                time.sleep(2)
                print('Veio com 120 munições 7.62mm e possui alto recoil mas seu dano é o maior entre todos rifles automáticos')
                arma_eq = 2
                time.sleep(5)
        elif arma == 5 or arma == 6:
            print('Dentro de um container você achou uma Kar-98, uma sniper poderosa para média/longa distâncias')
            time.sleep(2)
            print('Ela é sua arma principal enquanto não achar um rifle ou pistola, tome cuidado com os combates')
            time.sleep(2)
            print('Veio com 60 munições 7.62mm e uma mira de 8x na qual pode regular o zoom dela.')
            arma_eq = 3
            time.sleep(5)
        else:
            print('Dentro de um container você achou uma P92, uma pistola semi automática boa para combates de curta distância')
            time.sleep(2)
            print('Veio com 60 munições 9mm e uma mira laser, por enquanto é sua arma principal!')
            arma_eq = 4
            time.sleep(5)

        print('')

        georgopol_casa = input('Pelo visto acabou o loot por aqui, você quer ir para umas casas ao lado? ')
        georgopol_casa = georgopol_casa.lower()
        print('')
        if georgopol_casa == 'sim' or georgopol_casa == 's':
            time.sleep(5)
            mochila = random.randint(1,9)
            if mochila == 1 or mochila == 2 or mochila == 3:
                print('Na primeira casa você acha uma mochila nível 1 para guardar munições e outras coisas que precisar!')
            elif mochila == 4 or mochila == 5 or mochila == 6:
                print('Na primeira casa você acha uma mochila nível 2 para guardar munições e outras coisas que precisar!')
            else:
                print('Na primeira casa você acha uma mochila nível 3 para guardar munições e outras coisas que precisar!')
                
            print('')
            time.sleep(5)

            if arma_eq == 3:
                print('Em um dos cômodos encontra também uma submetralhadora UMP45 automática, boa para combates de curta distância!')
                time.sleep(2)
                print('Veio com 120 munições .45 ACP e será sua arma primária juntamente com a Kar98 como secundária.')
                time.sleep(5)
                arma_eq = 5
            elif arma_eq == 4:
                print('Em um dos cômodos encontra também uma submetralhadora UMP45, boa para combates de curta distância!')
                time.sleep(2)
                print('Veio com 120 munições .45 ACP e será sua arma primária juntamente com a P92 como secundária.')
                time.sleep(5)
                arma_eq = 6

            print('')

            if arma_eq == 1:
                arma_pri = 'M416'
            elif arma_eq == 2:
                arma_pri = 'AK47'
            elif arma_eq == 5 or arma_pri == 6:
                arma_pri = 'UMP'


            print('Passos! Você escuta alguém se aproximando da casa que está!')
            time.sleep(1)
            combate1 = input('Pode pular pela janela ou enfrentar ele. Deseja enfrentar ou fugir?')
            combate1 = combate1.lower()
            print('')
            time.sleep(1)
            if combate1 == 'enfrentar':
                print('Há um armário no quarto que está, você se posiciona atrás dele mirado na porta')
                time.sleep(2)
                print('Você espera pacientemente pelo inimigo entrar e treme um pouco a mira pois está nervoso')
                time.sleep(2)
                print('Escuta passos de escadas e parece que ele está se aproximando. Prende a respiração e concentra-se.')
                time.sleep(4)

                inimigo1 = random.randint(1,10)
                if inimigo1 != 1:
                    print('POW PA PA PUM TUM TUM')
                    time.sleep(1)
                    print('Você dispara vários tiros contra ele com sua',arma_pri,' e acaba com o inimigo sem ele nem te ver!')
                    time.sleep(3)
                    print('')
                    kills += 1
                    if arma_eq == 5:
                        print('Em seu loot, acha uma granada de fragmentação e uma M16A4 com bastante munições!')
                        time.sleep(2)
                        print('É um rifle semi automático que pode ser usado para méidas e curtas distâncias')
                        arma_eq = 7
                        time.sleep(2)
                        print('Equipa sua arma e guarda o que achou na mochila para sair da casa,')
                        time.sleep(4)

                        if arma_eq == 7:
                            arma_pri = 'M416'

                    elif arma_eq == 6:
                        print('Em seu loot, acha uma granada de fragmentação e uma M16A4 com bastante munições!')
                        time.sleep(2)
                        print('É um rifle semi automático que pode ser usado para méidas e curtas distâncias')
                        arma_eq = 7
                        time.sleep(2)
                        print('Equipa sua arma e guarda o que achou na mochila para sair da casa,')
                        time.sleep(4)

                        if arma_eq == 8:
                            arma_pri = 'M416'
                        
                    else:
                        print('Em seu loot, encontra uma granada de fragmentação e mais munições')
                        time.sleep(2)
                        print('Guarda na mochila o que achou e sai da casa.')
                        time.sleep(3)

                    granada_frag += 1
                    print('')
                    
                else:
                    print('POW PA PA PUM TUM TUM')
                    time.sleep(1)
                    print('Ele, suspeitando de alguém estar lá, logo reage ao seu tiro na perna saindo da frente da porta')
                    time.sleep(2)
                    print('Você, meio sem saber o que fazer, continua na mesma posição e esperando que ele apareceça')
                    time.sleep(2)
                    print('Ele então, joga uma granada de fragmentação no quarto, que logo explode e você morre.')
                    time.sleep(6)
                    final()

                print('Na rua que passa enfrente as casas encontra um Dacia amarelo')
                time.sleep(3)
                print('Pega o carro e segue a rua, saindo de Georgopol.')
                time.sleep(6)
                print('')

            else:
                print('Rapidamente você pula pela janela e cai da casa de mal jeito')
                time.sleep(2)
                print('Corta seu braço com o estilhasso do vidro e machuca sua perna por conta da altura')
                time.sleep(3)
                print('Mesmo assim, com medo, você força a correr e encontra um Dacia cinza na rua')
                time.sleep(3)
                print('Logo pega o carro e sai de Georgopol sem pensar duas vezes.')
                fugir += 1
                print('')

        else:
            time.sleep(3)

            if arma_eq == 1:
                arma_pri = 'M416'
            elif arma_eq == 2:
                arma_pri = 'AK47'
            elif arma_eq == 3:
                arma_pri = 'Kar98'
            elif arma_eq == 4 :
                arma_pri = 'P92'

            print('')
            
            print('Enquanto estava saindo dos containers, escuta passos se aproximando')
            time.sleep(2)
            print('Parece que vem da frente. Sem saber onde mirar, segue o som do inimigo com os olhos')
            time.sleep(4)
            print('Pega sua',arma_pri,'e mira onde possivelmente ele irá aparecer')
            time.sleep(2)
            print('Você prende a respiração para parar de tremer a mira mas não escuta mais os passos dele...')
            time.sleep(3)

            if arma_eq == 1 or arma_eq == 2:
                combate1 = random.randint(1,7)
                if combate1 != 1:
                    kills += 1
                    print('Ele então aparece na sua mira e você dá um tiro certeiro na cabeça, matando-o')
                    time.sleep(4)
                    print('Preocupado por chamar a atenção, decide pegar a mochila nível 1 dele e sair logo de lá')
                    time.sleep(6)

                else:
                    print('Ele então aparece na sua mira aos poucos e desesperado, você logo atira na perna dele')
                    time.slee(3)
                    print('Como reação, o inimigo vira e acerta um tiro certeiro na sua cabeça.')
                    time.sleep(6)
                    final()
            
            elif arma_eq == 3:
                combate1 = random.randint(1,4)
                if combate1 != 1:
                    kills += 1
                    print('Ele então aparece na sua mira e incrivelmente você acerta o tiro de sniper nele, matando-o')
                    time.sleep(4)
                    print('Preocupado por chamar a atenção, decide pegar a mochila nível 1 dele e a P92 que tinha para sair logo')
                    time.sleep(4)

                else:
                    print('Ele então aparece na sua mira aos poucos e desesperado, você logo atira na perna dele de sniper')
                    time.slee(3)
                    print('Como reação, o inimigo vira e acerta um tiro certeiro na sua cabeça.')
                    time.sleep(6)
                    final()
            
            else:
                combate1 = random.randint(1,5)
                if combate1 != 1:
                    kills += 1
                    print('Ele então aparece na sua mira e você acerta um tiro certeiro na cabeça, matando-o')
                    time.sleep(4)
                    print('Preocupado por chamar a atenção, decide pegar a mochila nível 1 dele e sair logo de lá')
                    time.sleep(6)

                else:
                    print('Ele então aparece na sua mira aos poucos e desesperado, você logo atira na perna dele de pistola')
                    time.slee(3)
                    print('Como reação, o inimigo vira e acerta um tiro certeiro na sua cabeça.')
                    time.sleep(6)
                    final()

            print('')
            print('Na rua que passa por perto, acha um Dacia vermelho')
            time.sleep(2)
            print('Entra no carro e sai de Georgopol, evitando mais possíveis combates.')
            time.sleep(6)

        print('')
        print('A Zona de Gás fechou e você precisa ir para a zona segura')
        time.sleep(3)
        print('Porém, há uma Zona Vermelha no caminho, mas o gás está vindo')
        time.sleep(3)
        print('Precisa decidir se quer passar por lá ou dar uma volta grande e fugir de uma possível explosão')
        time.sleep(5)

        zona_verm1 = input('Quer fugir ou passar pela zona vermelha? ')
        zona_verm1 = zona_verm1.lower()
        print('')
        time.sleep(4)
        if zona_verm1 == 'fugir':
            fugir_zm += 1
            print('Você então vira seu carro para a direita e começa a contornar a Zona Vermelha')
            time.sleep(3)
            print('Porém não há estrada por onde passa, vai ter que segurar firme e forte no volante!')
            time.sleep(4)
            print('O carro está passando por uma plantação de trigo e várias valetas')
            time.sleep(4)
            print('Você: Ai minha cabeça! Deviam ter colocado um amortecedor nesse teto!')
            time.sleep(5)
            print('Agora, passará por uma área de morros e precisa tomar cuidado com a velocidade!')
            time.sleep(5)
            print('Você: Caramba, dá pra ver as bombas caíndo e explodindo bem perto!')
            time.sleep(3)
            print('Você: AAAAA!! Quase que eu bato na árvore! Preciso me concentrar...')
            time.sleep(4)
            print('As bombas pararam de cair mas precisa achar um lugar bom para ficar protegido')
            time.sleep(4)
            print('Você: Ali, em cima do morro! Tem uma casa que parece ser boa para ficar')
            time.sleep(3)
            print('Você então sobe o morro e estaciona seu Dacia')
            time.sleep(3)
            print('Entra na casa e começa a vasculhar por algum loot.')
            time.sleep(7)

            print('')

            if fugir > 0:
                print('Em cima de uma mesa, encontra 5 bandagens')
                time.sleep(2)
                print('Você então as usa para cuidar dos cortes de vidro e no pé por conta da queda.')
                time.sleep(6)
                print('')


            if arma_eq == 7 or arma_eq == 3:
                print('Quando terminou de ver as casas, viu da janela um inimigo correndo no campo aberto')
                time.sleep(4)
                print('Pega então sua Kar98 e mira nele')
                time.sleep(2)
                print('Percebe que está correndo em linha reta e logo mira a frente para acertar o tiro')
                time.sleep(3)
                print('De primeira não acerta, ele continua a fugir e você tenta novamente')
                time.sleep(3)
                print('Acerta o tiro só que na perna, fazendo com que o inimigo caia no chão')
                time.sleep(3)
                print('Rapidamente, você atira na cabeça para finalizá-lo e mata-o!')
                time.sleep(4)
                print('Você: Eu sou um Deus da Sniper!')
                kills += 1
                time.sleep(6)
            
            else:
                print('Quando terminou de ver as casas, escutou um barulho de moto')
                time.sleep(3)
                print('Sai da casa e ve uma moto passando no campo')
                time.sleep(2)
                print('Ve que não estava muito rápida e não muito longe')
                time.sleep(2)
                print('Pega a sua',arma_pri,'e começa a atirar nele para tentar matá-lo')
                time.sleep(3)
                print('Sem saber controlar a arma direito, acerta a roda traseira da moto')
                time.sleep(3)
                print('Faz o inimigo perder controle e cair da moto, matando-o')
                time.sleep(4)
                print('Você: Eu sou um Deus da',arma_pri,'!')
                kills += 1
                time.sleep(6)

            print('')
        
        else:
            print('Você então acelera ao máximo o Dacia e entra na Zona Vermelha')
            time.sleep(3)
            print('Muitas bombas caem do céu de todas direções e explodem muito perto do seu carro!')
            time.sleep(2)
            print('Você desvia das que consegue ver mas muitas caem aleatóriamente!')
            time.sleep(2)
            print('Você: Isso é insanoo!!! Acho que vou morrer!')
            time.sleep(2)

            zona1 = random.randint(1,5)
            if zona1 != 1:
                print('Uma bomba atinge uma árvore que começa a cair na sua frente!')
                time.sleep(2)
                print('Você acelera e ela quase acerta o teto, amassa um pouco a traseira mas você sai vivo!')
                time.sleep(3)
                print('Em seguida as bombas param de cair e você percebe que passou intacto!')
                time.sleep(3)
                print('Você: UHUULL!! Isso que é sobrevivência!!')
                time.sleep(4)
                print('Para dar uma respirada você para em umas casas num morro')
                time.sleep(4)
                print('Deixa seu carro e entra pra ver se há algum loot.')
                time.sleep(7)
                print('Encontra em um banheiro uma AUG A3, um rifle melhor do que a sua',arma_pri,'!')
                time.sleep(4)
                print('Pega as 120 munições 5.56mm e equipa como arma principal')
                arma_pri = 'AUG'
                time.sleep(6)

                print('')

                if fugir > 0:
                    print('Em cima de uma mesa, encontra 5 bandagens')
                    time.sleep(2)
                    print('Você então as usa para cuidar dos cortes de vidro e no pé por conta da queda.')
                    time.sleep(6)
                    print('')

                if arma_eq == 7 or arma_eq == 3:
                    print('Quando terminou de ver as casas, viu da janela um inimigo correndo na rua')
                    time.sleep(4)
                    print('Pega então sua Kar98 e mira nele')
                    time.sleep(2)
                    print('Percebe que está correndo em linha reta e logo mira a frente para acertar o tiro')
                    time.sleep(3)
                    print('De primeira não acerta, ele continua a fugir e você tenta novamente')
                    time.sleep(3)
                    print('Acerta o tiro só que na perna, fazendo com que o inimigo caia no chão')
                    time.sleep(3)
                    print('Rapidamente, você atira na cabeça para finalizá-lo e mata-o!')
                    time.sleep(4)
                    print('Você: Eu sou um Deus da Sniper!')
                    kills += 1
                    time.sleep(6)
            
                else:
                    print('Quando terminou de ver as casas, escutou um barulho de moto')
                    time.sleep(3)
                    print('Sai da casa e ve uma moto passando na rua')
                    time.sleep(2)
                    print('Ve que não estava muito rápida e não muito longe')
                    time.sleep(2)
                    print('Pega a sua',arma_pri,'e começa a atirar nele para tentar matá-lo')
                    time.sleep(3)
                    print('Sem saber controlar a arma direito, acerta a roda traseira da moto')
                    time.sleep(3)
                    print('Faz o inimigo perder controle e cair da moto, matando-o')
                    time.sleep(4)
                    print('Você: Eu sou um Deus da',arma_pri,'!')
                    kills += 1
                    time.sleep(6)

                print('')


            else:
                print('Uma bomba cai perto do pneu traseiro e faz com que ele exploda!')
                time.sleep(2)
                print('Sem ter controle, você tenta continuar dirigindo mas o carro derrapa para a direita')
                time.sleep(3)
                print('Não consegue segurar o carro e ele bate em alta velocidade numa árvore grande')
                time.sleep(4)
                print('Por estar muito rápido, o cinto não te segura e você voa para fora do carro, morrendo.')
                time.sleep(6)
                final()

        print('')
        print('A Zona de Gás fechou novamente menor ainda! Precisa sair daí logo!')
        time.sleep(3)
        print('Por estar um pouco perto, você vai correndo em direção a área segura.')
        time.sleep(10)
        print('')
        print('---------------------------------')
        print('| Você está no Top 5 jogadores! |')
        print('---------------------------------')
        print('')
        time.sleep(4)
        print('Finalmente chega na área segura e logo se posiciona em um lugar alto')
        time.sleep(3)
        print('Fica olhando para todos os lados e com muito medo')
        time.sleep(2)
        print('Escuta muitos tiros próximos e você se esconde deles')
        time.sleep(2)
        print('Percebe que sobrou apenas dois sobreviventes vivos')
        time.sleep(2)
        print('Vai precisar matá-lo para ganhar!')
        time.sleep(2)
        print('A Zona de Gás diminui mais um pouco de tal forma que vocês se encontrem')
        time.sleep(3)
        print('Você se reposiciona e escuta barulhos próximos...')
        time.sleep(3)

        if granada_frag == 1:
            print('Vê um vulto passando para uma árvore na direita')
            time.sleep(2)
            print('Lembra que tinha uma granada de fragmentação guardada e pega ela da mochila')
            time.sleep(4)
            print('Com ela em mãos, vê o inimigo indo para trás de uma árvore')
            time.sleep(3)
            print('Percebe que fica parado lá e prepara a granada')
            time.sleep(2)
            print('Quando puxa o pino, ele escuta e corre para a esquerda')
            time.sleep(2)
            print('Você rapidamente prevê onde ele está indo e joga a granada')
            time.sleep(3)
            print('BOOM! Ela explode e mata o inimigo certeiramente!!')
            time.sleep(3)
            print('Você: EU GANHEI!! EU GANHEI!!')
            time.sleep(3)
            print('')
            print('')
            print('WINNER WINNER CHICKEN DINNER!')
            time.sleep(2)
            print('Você ganhou! Parabéns sobrevivente!!')
            time.sleep(2)
            print('Aqui estão seus resultados finais:')
            print('')
            final()

        elif arma_pri == 'AUG':
            print('Você vê o inimigo deitado e rastejando pelos arbustos')
            time.sleep(2)
            print('Pega logo sua AUG e posiciona a mira sem ele te ver')
            time.sleep(3)

            inimigo2 = random.randint(1,20)
            if inimigo2 != 1:
                kills += 1
                print('Prende a respiração e atira contra ele')
                time.sleep(2)
                print('Sem ver da onde e sem reações, o inimigo morre quase instantaneamente para você!')
                time.sleep(4)
                print('Você: EU GANHEI!! EU GANHEI!!')
                time.sleep(3)
                print('')
                print('')
                print('WINNER WINNER CHICKEN DINNER!')
                time.sleep(2)
                print('Você ganhou! Parabéns sobrevivente!!')
                time.sleep(2)
                print('Aqui estão seus resultados finais:')
                print('')
                final()
            
            else:
                print('Esqueçe de prender a respiração mas mesmo assim atira contra ele')
                time.sleep(3)
                print('Sem ver da onde e sem reações, o inimigo toma tiros mas logo esquiva-se')
                time.sleep(3)
                print('Ele estava atento e consegue pegar uma proteção da árvore')
                time.sleep(2)
                print('Você escuta um barulho de pino mas não entende e quando menos percebe...')
                time.sleep(3)
                print('BOOM! Uma granada vem contudo em você, morrendo para ela na hora.')
                time.sleep(6)
                final()
        
        else:
            print('Você vê o inimigo deitado e rastejando pelos arbustos')
            time.sleep(2)
            print('Pega logo sua',arma_pri,'e posiciona a mira sem ele te ver')
            time.sleep(3)

            inimigo2 = random.randint(1,7)
            if inimigo2 != 1:
                kills += 1
                print('Prende a respiração e atira contra ele')
                time.sleep(2)
                print('Sem ver da onde e sem reações, o inimigo morre quase instantaneamente para você!')
                time.sleep(4)
                print('Você: EU GANHEI!! EU GANHEI!!')
                time.sleep(3)
                print('')
                print('')
                print('WINNER WINNER CHICKEN DINNER!')
                time.sleep(2)
                print('Você ganhou! Parabéns sobrevivente!!')
                time.sleep(2)
                print('Aqui estão seus resultados finais:')
                print('')
                final()
            
            else:
                print('Esqueçe de prender a respiração mas mesmo assim atira contra ele')
                time.sleep(3)
                print('Sem ver da onde e sem reações, o inimigo toma tiros mas logo esquiva-se')
                time.sleep(3)
                print('Ele estava atento e consegue pegar uma proteção da árvore')
                time.sleep(2)
                print('Você escuta um barulho de pino mas não entende e quando menos percebe...')
                time.sleep(3)
                print('BOOM! Uma granada vem contudo em você, morrendo para ela na hora.')
                time.sleep(6)
                final()
elif polyana_ir == 1:
        arma_pri = '.'
        kills = 0
        fugir = 0
        fugir_zm = 0
        granada_frag = 0
        print('Você: shhh... O ventshhh está muito fortshhhh ...')
        time.sleep(3)
        print('Estamos caindo nos prédios!')
        time.sleep(5)

        print('')
        print('Aterrissamos!')
        print('Voce: Caramba, por pouco que erro o prédio...')
        time.sleep(4)
        print('... looteando ...')
        print('')
        time.sleep(6)

        colete = random.randint(1,9)
        if colete == 1 or colete == 2 or colete == 3 or colete == 4:
            print('Você achou um colete nível 1 em um dos apartamentos!')
            colete_eq = 1
            time.sleep(3)
        elif colete == 5 or colete == 6 or colete == 7:
            print('Você achou um colete nível 2 em um dos apartamentos!')
            colete_eq = 2
            time.sleep(3)
        else:
            print('Você achou um colete nível 3 em um dos apartamentos!')
            colete_eq = 3
            time.sleep(3)

        print('')

        capacete = random.randint(1,9)
        if capacete == 1 or capacete == 2 or capacete == 3 or capacete == 4:
            print('Encontrou um capacete nível 1 ao lado também!')
            capacete_eq = 1
            time.sleep(3)
        elif capacete == 5 or capacete == 6 or capacete == 7:
            print('Encontrou um capacete nível 2 ao lado também!')
            capacete_eq = 2
            time.sleep(3)
        else:
            print('Encontrou um capacete nível 3 ao lado também!')
            capacete_eq = 3
            time.sleep(3)

        print('')

        arma = random.randint(1,7)
        if arma == 1 or arma == 2 or arma == 3 or arma == 4:
            m4a4ouAK47 = random.randint(1,2)
            if m4a4ouAK47 == 1:
                print('Dentro de um quarto havia uma M416, um poderoso rifle automático para curta/média distância, será sua arma principal!')
                time.sleep(2)
                print('Veio com 120 munições 5.56mm e sua arma possui controle de recoil fácil comparado com a AK-47')
                arma_eq = 1
                time.sleep(5)
            else:
                print('Dentro de um quarto havia uma AK-47, ótimo para curta distância, será sua arma principal!')
                time.sleep(2)
                print('Veio com 120 munições 7.62mm e possui alto recoil mas seu dano é o maior entre todos rifles automáticos')
                arma_eq = 2
                time.sleep(5)
        elif arma == 5 or arma == 6:
            print('Dentro de um quarto você achou uma Kar-98, uma sniper poderosa para média/longa distâncias')
            time.sleep(2)
            print('Ela é sua arma principal enquanto não achar um rifle ou pistola, tome cuidado com os combates')
            time.sleep(2)
            print('Veio com 60 munições 7.62mm e uma mira de 8x na qual pode regular o zoom dela.')
            arma_eq = 3
            time.sleep(5)
        else:
            print('Dentro de um quarto você achou uma P92, uma pistola semi automática boa para combates de curta distância')
            time.sleep(2)
            print('Veio com 60 munições 9mm e uma mira laser, por enquanto é sua arma principal!')
            arma_eq = 4
            time.sleep(5)

        print('')
        polyana_predio = input('Pelo visto acabou o loot por aqui, você quer ir para o prédio ao lado? ')
        polyana_predio = polyana_predio.lower()
        if polyana_predio == 'sim' or polyana_predio == 's':
            time.sleep(5)
            mochila = random.randint(1,9)
            if mochila == 1 or mochila == 2 or mochila == 3:
                print('No primeiro andar você acha uma mochila nível 1 para guardar munições e outras coisas que precisar!')
            elif mochila == 4 or mochila == 5 or mochila == 6:
                print('No primeiro andar você acha uma mochila nível 2 para guardar munições e outras coisas que precisar!')
            else:
                print('No primeiro andar você acha uma mochila nível 3 para guardar munições e outras coisas que precisar!')
                
            time.sleep(5)

            if arma_eq == 3:
                print('Em um dos cômodos encontra também uma submetralhadora UMP45 automática, boa para combates de curta distância!')
                time.sleep(2)
                print('Veio com 120 munições .45 ACP e será sua arma primária juntamente com a Kar98 como secundária.')
                time.sleep(5)
                arma_eq = 5
            elif arma_eq == 4:
                print('Em um dos cômodos encontra também uma submetralhadora UMP45, boa para combates de curta distância!')
                time.sleep(2)
                print('Veio com 120 munições .45 ACP e será sua arma primária juntamente com a P92 como secundária.')
                time.sleep(5)
                arma_eq = 6

            if arma_eq == 1:
                arma_pri = 'M416'
            elif arma_eq == 2:
                arma_pri = 'AK47'
            elif arma_eq == 5 or arma_pri == 6:
                arma_pri = 'UMP'

            print('')
            print('Passos! Você escuta alguém se aproximando do prédio que está!')
            time.sleep(1)
            combate1 = input('Pode pular pela janela e ou enfrentar ele. Deseja enfrentar ou fugir?')
            combate1 = combate1.lower()
            time.sleep(1)
            if combate1 == 'enfrentar':
                print('Você agacha atrás da cama e posiciona sua mira na porta')
                time.sleep(2)
                print('Espera pacientemente pelo inimigo entrar e treme um pouco a mira pois está nervoso')
                time.sleep(2)
                print('Escuta passos de escadas e parece que ele está se aproximando. Prende a respiração e concentra-se.')
                time.sleep(4)

                inimigo1 = random.randint(1,10)
                if inimigo1 != 1:
                    print('POW PA PA PUM TUM TUM')
                    time.sleep(1)
                    print('Você dispara vários tiros contra ele com sua',arma_pri,' e acaba com o inimigo sem ele nem te ver!')
                    time.sleep(3)
                    kills += 1
                    if arma_eq == 5 or arma_eq == 6:
                        print('Em seu loot, acha uma granada de fragmentação e uma M16A4 com bastante munições!')
                        time.sleep(2)
                        print('É um rifle semi automático que pode ser usado para méidas e curtas distâncias')
                        arma_eq = 7
                        time.sleep(2)
                        print('Equipa sua arma e guarda o que achou na mochila para sair do prédio,')
                        time.sleep(4)

                        if arma_eq == 7:
                            arma_pri = 'M416'

                    elif arma_eq == 6:
                        print('Em seu loot, acha uma granada de fragmentação e uma M16A4 com bastante munições!')
                        time.sleep(2)
                        print('É um rifle semi automático que pode ser usado para méidas e curtas distâncias')
                        arma_eq = 7
                        time.sleep(2)
                        print('Equipa sua arma e guarda o que achou na mochila para sair da casa,')
                        time.sleep(4)

                        if arma_eq == 8:
                            arma_pri = 'M416'
                    else:
                        print('Em seu loot, encontra uma granada de fragmentação e mais munições')
                        time.sleep(2)
                        print('Guarda na mochila o que achou e sai do prédio.')
                        time.sleep(3)
                        print('')

                    granada_frag += 1
                    print('')
                    
                else:
                    print('POW PA PA PUM TUM TUM')
                    time.sleep(1)
                    print('Ele, suspeitando de alguém estar lá, logo reage ao seu tiro na perna saindo da frente da porta')
                    time.sleep(2)
                    print('Você, meio sem saber o que fazer, continua na mesma posição e esperando que ele apareceça')
                    time.sleep(2)
                    print('Ele então, joga uma granada de fragmentação no quarto, que logo explode e você morre.')
                    time.sleep(6)
                    final()

                print('Na rua que passa enfrente as casas encontra um jipe UAZ de teto fechado')
                time.sleep(3)
                print('Pega o carro e segue a rua, saindo de Polyana.')
                time.sleep(6)

            else:
                fugir += 1
                print('Rapidamente você pula pela janela e cai da casa de mal jeito')
                time.sleep(2)
                print('Bate a cabeça no ferro da janela e machuca sua perna por conta da altura')
                time.sleep(3)
                print('Mesmo assim, com medo, você força a correr e encontra um jipe UAZ de teto aberto na rua')
                time.sleep(3)
                print('Logo pega o carro e sai de Polyana sem pensar duas vezes.')
                print('')

        else:
            time.sleep(3)

            if arma_eq == 1:
                arma_pri = 'M416'
            elif arma_eq == 2:
                arma_pri = 'AK47'
            elif arma_eq == 3:
                arma_pri = 'Kar98'
            elif arma_eq == 4 :
                arma_pri = 'P92'
            
            print('')
            print('Enquanto estava saindo do prédio, escuta passos se aproximando')
            time.sleep(2)
            print('Parece que vem da frente. Sem saber onde mirar, segue o som do inimigo com os olhos')
            time.sleep(4)
            print('Pega sua',arma_pri,'e mira onde possivelmente ele irá aparecer')
            time.sleep(2)
            print('Você prende a respiração para parar de tremer a mira mas não escuta mais os passos dele...')
            time.sleep(3)

            if arma_eq == 1 or arma_eq == 2:
                combate1 = random.randint(1,7)
                if combate1 != 1:
                    kills += 1
                    print('Ele então aparece na sua mira e você dá um tiro certeiro na cabeça, matando-o')
                    time.sleep(4)
                    print('Preocupado por chamar a atenção, decide pegar a mochila nível 1 dele e sair logo de lá')
                    time.sleep(6)

                else:
                    print('Ele então aparece na sua mira aos poucos e desesperado, você logo atira na perna dele')
                    time.slee(3)
                    print('Como reação, o inimigo vira e acerta um tiro certeiro na sua cabeça.')
                    time.sleep(6)
                    final()
            
            elif arma_eq == 3:
                combate1 = random.randint(1,4)
                if combate1 != 1:
                    kills += 1
                    print('Ele então aparece na sua mira e incrivelmente você acerta o tiro de sniper nele, matando-o')
                    time.sleep(4)
                    print('Preocupado por chamar a atenção, decide pegar a mochila nível 1 dele e a P92 que tinha para sair logo')
                    time.sleep(4)

                else:
                    print('Ele então aparece na sua mira aos poucos e desesperado, você logo atira na perna dele de sniper')
                    time.slee(3)
                    print('Como reação, o inimigo vira e acerta um tiro certeiro na sua cabeça.')
                    time.sleep(6)
                    final()
            
            else:
                combate1 = random.randint(1,5)
                if combate1 != 1:
                    kills += 1
                    print('Ele então aparece na sua mira e você acerta um tiro certeiro na cabeça, matando-o')
                    time.sleep(4)
                    print('Preocupado por chamar a atenção, decide pegar a mochila nível 1 dele e sair logo de lá')
                    time.sleep(6)

                else:
                    print('Ele então aparece na sua mira aos poucos e desesperado, você logo atira na perna dele de pistola')
                    time.slee(3)
                    print('Como reação, o inimigo vira e acerta um tiro certeiro na sua cabeça.')
                    time.sleep(6)
                    final()

            print('')
            print('Na rua que passa por perto, acha um jipe UAZ de teto aberto')
            time.sleep(2)
            print('Entra no carro e sai de Georgopol, evitando mais possíveis combates.')
            time.sleep(6)

        print('')
        print('A Zona de Gás fechou e você precisa ir para a zona segura')
        time.sleep(3)
        print('Porém, há uma Zona Vermelha no caminho, mas o gás está vindo')
        time.sleep(3)
        print('Precisa decidir se quer passar por lá ou dar uma volta grande e fugir de uma possível explosão')
        time.sleep(5)

        zona_verm1 = input('Quer fugir ou passar pela zona vermelha? ')
        zona_verm1 = zona_verm1.lower()
        time.sleep(4)
        print('')
        if zona_verm1 == 'fugir':
            fugir_zm += 1
            print('Você então vira seu carro para a direita e começa a contornar a Zona Vermelha')
            time.sleep(3)
            print('Porém não há estrada por onde passa, vai ter que segurar firme e forte no volante!')
            time.sleep(4)
            print('O carro está passando por uma plantação de milho cheio de obstáculos')
            time.sleep(4)
            print('Você: Segura pião! Esses negócios são difíceis de desviar!')
            time.sleep(5)
            print('Agora, passará por uma área de morros e precisa tomar cuidado com a velocidade!')
            time.sleep(5)
            print('Você: Caramba, dá pra ver as bombas caíndo e explodindo bem perto!')
            time.sleep(3)
            print('Você: AAAAA!! Quase que eu bato no poste da rua! Preciso me concentrar...')
            time.sleep(4)
            print('As bombas pararam de cair mas precisa achar um lugar bom para ficar protegido')
            time.sleep(4)
            print('Você: Ali, tem um bunker! Parece um lugar seguro')
            time.sleep(3)
            print('Você então se aproxima e estaciona seu jipe fora')
            time.sleep(3)
            print('Entra lá dentro e começa a vasculhar por algum loot.')
            time.sleep(7)
            print('')

            if fugir > 0:
                print('Em cima de uma caixa, encontra 5 bandagens')
                time.sleep(2)
                print('Você então as usa para cuidar do ferimento na cabeça e no pé por conta da queda.')
                time.sleep(6)
                print('')

            if arma_eq == 7 or arma_eq == 3:
                print('Quando terminou de ver o bunker, subiu e viu um inimigo correndo no campo aberto')
                time.sleep(4)
                print('Pega então sua Kar98 e mira nele')
                time.sleep(2)
                print('Percebe que está correndo em linha reta e logo mira a frente para acertar o tiro')
                time.sleep(3)
                print('De primeira não acerta, ele continua a fugir e você tenta novamente')
                time.sleep(3)
                print('Acerta o tiro só que na perna, fazendo com que o inimigo caia no chão')
                time.sleep(3)
                print('Rapidamente, você atira na cabeça para finalizá-lo e mata-o!')
                time.sleep(4)
                print('Você: Eu sou um Deus da Sniper!')
                kills += 1
                time.sleep(6)
                print('')
            
            else:
                print('Quando terminou de ver lá embaixo, escutou um barulho de Buggy e logo subiu')
                time.sleep(3)
                print('Sai da casa e ve um Buggy passando no campo')
                time.sleep(2)
                print('Ve que não estava muito rápida e não muito longe')
                time.sleep(2)
                print('Pega a sua',arma_pri,'e começa a atirar nele para tentar matá-lo')
                time.sleep(3)
                print('Sem saber controlar a arma direito, acerta a roda traseira do Buggy')
                time.sleep(3)
                print('Faz o inimigo perder controle e cair do Buggy, matando-o')
                time.sleep(4)
                print('Você: Eu sou um Deus da',arma_pri,'!')
                kills += 1
                time.sleep(6)
                print('')
        
        else:
            print('Você então acelera ao máximo seu jipe e entra na Zona Vermelha')
            time.sleep(3)
            print('Muitas bombas caem do céu de todas direções e explodem muito perto do seu carro!')
            time.sleep(2)
            print('Você desvia das que consegue ver mas muitas caem aleatóriamente!')
            time.sleep(2)
            print('Você: Isso é insanoo!!! Acho que vou morrer!')
            time.sleep(2)

            zona1 = random.randint(1,5)
            if zona1 != 1:
                print('Uma bomba atinge uma árvore que começa a cair na sua frente!')
                time.sleep(2)
                print('Você acelera e ela quase acerta o teto, amassa um pouco a traseira mas você sai vivo!')
                time.sleep(3)
                print('Em seguida as bombas param de cair e você percebe que passou intacto!')
                time.sleep(3)
                print('Você: UHUULL!! Isso que é sobrevivência!!')
                time.sleep(4)
                print('Para dar uma respirada você para em uma escola abandonada')
                time.sleep(4)
                print('Deixa seu carro e entra pra ver se há algum loot.')
                time.sleep(7)
                print('Encontra em uma sala uma Groza, um rifle melhor do que a sua',arma_pri,'!')
                time.sleep(4)
                print('Pega as 120 munições 7.62mm e equipa como arma principal')
                arma_pri = 'Groza'
                time.sleep(6)
                print('')

                if fugir > 0:
                    print('Em cima de uma mesa, encontra 5 bandagens')
                    time.sleep(2)
                    print('Você então as usa para cuidar do ferimento na cabeça e no pé por conta da queda.')
                    time.sleep(6)
                    print('')

                if arma_eq == 7 or arma_eq == 3:
                    print('Quando terminou de ver o bunker, subiu e viu um inimigo correndo na estrada')
                    time.sleep(4)
                    print('Pega então sua Kar98 e mira nele')
                    time.sleep(2)
                    print('Percebe que está correndo em linha reta e logo mira a frente para acertar o tiro')
                    time.sleep(3)
                    print('De primeira não acerta, ele continua a fugir e você tenta novamente')
                    time.sleep(3)
                    print('Acerta o tiro só que na perna, fazendo com que o inimigo caia no chão')
                    time.sleep(3)
                    print('Rapidamente, você atira na cabeça para finalizá-lo e mata-o!')
                    time.sleep(4)
                    print('Você: Eu sou um Deus da Sniper!')
                    kills += 1
                    time.sleep(6)
                    print('')
            
                else:
                    print('Quando terminou lá embaixo, escutou um barulho de Buggy')
                    time.sleep(3)
                    print('Sai da casa e ve um Buggy passando na rua')
                    time.sleep(2)
                    print('Ve que não estava muito rápida e não muito longe')
                    time.sleep(2)
                    print('Pega a sua',arma_pri,'e começa a atirar nele para tentar matá-lo')
                    time.sleep(3)
                    print('Sem saber controlar a arma direito, acerta a roda traseira do Buggy')
                    time.sleep(3)
                    print('Faz o inimigo perder controle e cair do Buggy, matando-o')
                    time.sleep(4)
                    print('Você: Eu sou um Deus da',arma_pri,'!')
                    kills += 1
                    time.sleep(6)
                    print('')


            else:
                print('Uma bomba cai perto do pneu traseiro e faz com que ele exploda!')
                time.sleep(2)
                print('Sem ter controle, você tenta continuar dirigindo mas o carro derrapa para a direita')
                time.sleep(3)
                print('Não consegue segurar o carro e ele bate em alta velocidade numa árvore grande')
                time.sleep(4)
                print('Por estar muito rápido, o cinto não te segura e você voa para fora do carro, morrendo.')
                time.sleep(6)
                final()

        print('')
        print('A Zona de Gás fechou novamente menor ainda! Precisa sair daí logo!')
        time.sleep(3)
        print('Por estar um pouco perto, você vai correndo em direção a área segura.')
        time.sleep(10)
        print('')
        print('---------------------------------')
        print('| Você está no Top 5 jogadores! |')
        print('---------------------------------')
        print('')
        time.sleep(4)
        print('Finalmente chega na área segura e logo se posiciona dentro de uma guarita')
        time.sleep(3)
        print('Fica olhando para todos os lados e com muito medo')
        time.sleep(2)
        print('Escuta muitos tiros próximos e você se esconde deles')
        time.sleep(2)
        print('Percebe que sobrou apenas dois sobreviventes vivos')
        time.sleep(2)
        print('Vai precisar matá-lo para ganhar!')
        time.sleep(2)
        print('A Zona de Gás diminui mais um pouco de tal forma que vocês se encontrem')
        time.sleep(3)
        print('Você se reposiciona e escuta barulhos próximos...')
        time.sleep(3)

        if granada_frag == 1:
            print('Vê um vulto passando para uma guarita na esquerda')
            time.sleep(2)
            print('Lembra que tinha uma granada de fragmentação guardada e pega ela da mochila')
            time.sleep(4)
            print('Com ela em mãos, vê o inimigo entrando na guarita')
            time.sleep(3)
            print('Percebe que fica parado lá e prepara a granada')
            time.sleep(2)
            print('Quando puxa o pino, ele escuta e sai correndo de lá')
            time.sleep(2)
            print('Você rapidamente prevê onde ele está indo e joga a granada')
            time.sleep(3)
            print('BOOM! Ela explode e mata o inimigo certeiramente!!')
            time.sleep(3)
            print('Você: EU GANHEI!! EU GANHEI!!')
            time.sleep(3)
            print('')
            print('')
            print('WINNER WINNER CHICKEN DINNER!')
            time.sleep(2)
            print('Você ganhou! Parabéns sobrevivente!!')
            time.sleep(2)
            print('Aqui estão seus resultados finais:')
            print('')
            final()

        elif arma_pri == 'Groza':
            print('Você vê o inimigo agachado atrás da árvore')
            time.sleep(2)
            print('Consegue ver apenas a perna dele')
            time.sleep(2)
            print('Então se posiciona mais para a esquerda e consegue vê-lo mehlor')
            time.sleep(3)
            print('Pega logo sua Groza e posiciona a mira sem ele te ver')
            time.sleep(3)

            inimigo2 = random.randint(1,20)
            if inimigo2 != 1:
                kills += 1
                print('Prende a respiração e atira contra ele')
                time.sleep(2)
                print('Sem ver da onde e sem reações, o inimigo morre quase instantaneamente para você!')
                time.sleep(4)
                print('Você: EU GANHEI!! EU GANHEI!!')
                time.sleep(3)
                print('')
                print('')
                print('WINNER WINNER CHICKEN DINNER!')
                time.sleep(2)
                print('Você ganhou! Parabéns sobrevivente!!')
                time.sleep(2)
                print('Aqui estão seus resultados finais:')
                print('')
                final()
            
            else:
                print('Esqueçe de prender a respiração mas mesmo assim atira contra ele')
                time.sleep(3)
                print('Sem ver da onde e sem reações, o inimigo toma tiros mas logo se esconde para a direita')
                time.sleep(3)
                print('Ele estava atento e consegue pegar uma proteção da árvore')
                time.sleep(2)
                print('Você escuta um barulho de pino mas não entende e quando menos percebe...')
                time.sleep(3)
                print('BOOM! Uma granada vem contudo em você, morrendo para ela na hora.')
                time.sleep(6)
                final()
        
        else:
            print('Você vê o inimigo agachado atrás da árvore')
            time.sleep(2)
            print('Pega logo sua',arma_pri,'e posiciona a mira sem ele te ver')
            time.sleep(3)

            inimigo2 = random.randint(1,7)
            if inimigo2 != 1:
                kills += 1
                print('Prende a respiração e atira contra ele')
                time.sleep(2)
                print('Sem ver da onde e sem reações, o inimigo morre quase instantaneamente para você!')
                time.sleep(4)
                print('Você: EU GANHEI!! EU GANHEI!!')
                time.sleep(3)
                print('')
                print('')
                print('WINNER WINNER CHICKEN DINNER!')
                time.sleep(2)
                print('Você ganhou! Parabéns sobrevivente!!')
                time.sleep(2)
                print('Aqui estão seus resultados finais:')
                print('')
                final()
            
            else:
                print('Esqueçe de prender a respiração mas mesmo assim atira contra ele')
                time.sleep(3)
                print('Sem ver da onde e sem reações, o inimigo toma tiros mas logo se esconde para a direita')
                time.sleep(3)
                print('Ele estava atento e consegue pegar uma proteção da árvore')
                time.sleep(2)
                print('Você escuta um barulho de pino mas não entende e quando menos percebe...')
                time.sleep(3)
                print('BOOM! Uma granada vem contudo em você, morrendo para ela na hora.')
                time.sleep(6)
                final()
else:
    time.sleep(2)


print('')
print('Piloto: Nossa próxima parada é Pochinki! Iremos passar exatamente em cima!')
time.sleep(6)

print('')
print('Piloto: Preparem-se quem for pular, vocês terão 20 segundos para decidir!')
print('')

pular_centro = input('Você deseja pular de paraquedas para Pochinki agora? ')
pular_centro = pular_centro.lower()

if pular_centro == 'sim' or pular_centro == 's':
    print('Incrível! Chegará em Pochinki por volta de 20 segundos! Boa sorte!')
    pochinki_ir = 1
else:
    print('Tudo bem sobrevivente! Vamos para a próxima parada!')

time.sleep(12)


if pochinki_ir == 1:
        arma_pri = '.'
        kills = 0
        fugir = 0
        fugir_zm = 0
        granada_frag = 0
        print('Você: shhh... O ventshhh está muito fortshhhh ...')
        time.sleep(3)
        print('')

        print('Estamos quase chegando! Vamos cair nas casas!')
        time.sleep(5)

        print('')
        print('Aterrissamos!')
        time.sleep(1)
        print('Voce: Caramba, que altura! Minha perna tá até doendo...')
        time.sleep(4)
        print('... looteando ...')
        print('')
        time.sleep(6)

        colete = random.randint(1,9)
        if colete == 1 or colete == 2 or colete == 3 or colete == 4:
            print('Você achou um colete nível 1 na sala de uma casa!')
            colete_eq = 1
            time.sleep(3)
        elif colete == 5 or colete == 6 or colete == 7:
            print('Você achou um colete nível 2 na sala de uma casa!')
            colete_eq = 2
            time.sleep(3)
        else:
            print('Você achou um colete nível 3 na sala de uma casa!')
            colete_eq = 3
            time.sleep(3)

        print('')

        capacete = random.randint(1,9)
        if capacete == 1 or capacete == 2 or capacete == 3 or capacete == 4:
            print('Encontrou um capacete nível 1 ao lado também!')
            capacete_eq = 1
            time.sleep(3)
        elif capacete == 5 or capacete == 6 or capacete == 7:
            print('Encontrou um capacete nível 2 ao lado também!')
            capacete_eq = 2
            time.sleep(3)
        else:
            print('Encontrou um capacete nível 3 ao lado também!')
            capacete_eq = 3
            time.sleep(3)

        print('')

        arma = random.randint(1,7)
        if arma == 1 or arma == 2 or arma == 3 or arma == 4:
            m4a4ouAK47 = random.randint(1,2)
            if m4a4ouAK47 == 1:
                print('Dentro de um banheiro havia uma M416, um poderoso rifle automático para curta/média distância, será sua arma principal!')
                time.sleep(2)
                print('Veio com 120 munições 5.56mm e sua arma possui controle de recoil fácil comparado com a AK-47')
                arma_eq = 1
                time.sleep(5)
            else:
                print('Dentro de um banheiro havia uma AK-47, ótimo para curta distância, será sua arma principal!')
                time.sleep(2)
                print('Veio com 120 munições 7.62mm e possui alto recoil mas seu dano é o maior entre todos rifles automáticos')
                arma_eq = 2
                time.sleep(5)
        elif arma == 5 or arma == 6:
            print('Dentro de um banheiro você achou uma Kar-98, uma sniper poderosa para média/longa distâncias')
            time.sleep(2)
            print('Ela é sua arma principal enquanto não achar um rifle ou pistola, tome cuidado com os combates')
            time.sleep(2)
            print('Veio com 60 munições 7.62mm e uma mira de 8x na qual pode regular o zoom dela.')
            arma_eq = 3
            time.sleep(5)
        else:
            print('Dentro de um banheiro você achou uma P92, uma pistola semi automática boa para combates de curta distância')
            time.sleep(2)
            print('Veio com 60 munições 9mm e uma mira laser, por enquanto é sua arma principal!')
            arma_eq = 4
            time.sleep(5)

        print('')
        pochinki_ingreja = input('Pelo visto acabou o loot por aqui, você quer ir para a ingreja no morro? ')
        pochinki_ingreja = pochinki_ingreja.lower()
        if pochinki_ingreja == 'sim' or pochinki_ingreja == 's':
            time.sleep(5)
            mochila = random.randint(1,9)
            if mochila == 1 or mochila == 2 or mochila == 3:
                print('De cara você acha uma mochila nível 1 para guardar munições e outras coisas que precisar!')
            elif mochila == 4 or mochila == 5 or mochila == 6:
                print('De cara você acha uma mochila nível 2 para guardar munições e outras coisas que precisar!')
            else:
                print('De cara você acha uma mochila nível 3 para guardar munições e outras coisas que precisar!')
                
            time.sleep(5)
            print('')

            if arma_eq == 3:
                print('Atrás de um pilar você encontra também uma submetralhadora UMP45 automática, boa para combates de curta distância!')
                time.sleep(2)
                print('Veio com 120 munições .45 ACP e será sua arma primária juntamente com a Kar98 como secundária.')
                time.sleep(5)
                arma_eq = 5
            elif arma_eq == 4:
                print('Atrás de um pilar você encontra também uma submetralhadora UMP45, boa para combates de curta distância!')
                time.sleep(2)
                print('Veio com 120 munições .45 ACP e será sua arma primária juntamente com a P92 como secundária.')
                time.sleep(5)
                arma_eq = 6

            if arma_eq == 1:
                arma_pri = 'M416'
            elif arma_eq == 2:
                arma_pri = 'AK47'
            elif arma_eq == 5 or arma_pri == 6:
                arma_pri = 'UMP'

            print('')
            print('Passos! Você escuta alguém se aproximando da igreja!')
            time.sleep(1)
            combate1 = input('Pode sair por trás ou enfrentar ele. Deseja enfrentar ou fugir?')
            combate1 = combate1.lower()
            time.sleep(1)
            if combate1 == 'enfrentar':
                print('Você se esconde atrás do altar e posiciona sua mira na entrada da igreja')
                time.sleep(2)
                print('Espera pacientemente pelo inimigo entrar e treme um pouco a mira pois está nervoso')
                time.sleep(2)
                print('Escuta passos lá de fora e parece que ele está se aproximando. Prende a respiração e concentra-se.')
                time.sleep(4)

                inimigo1 = random.randint(1,10)
                if inimigo1 != 1:
                    print('POW PA PA PUM TUM TUM')
                    time.sleep(1)
                    print('Você dispara vários tiros contra ele com sua',arma_pri,' e acaba com o inimigo sem ele nem te ver!')
                    time.sleep(3)
                    kills = 1
                    if arma_eq == 5 or arma_eq == 6:
                        print('Em seu loot, acha uma granada de fragmentação e uma M16A4 com bastante munições!')
                        time.sleep(2)
                        print('É um rifle semi automático que pode ser usado para méidas e curtas distâncias')
                        arma_eq = 7
                        time.sleep(2)
                        print('Equipa sua arma e guarda o que achou na mochila para sair da casa,')
                        time.sleep(4)

                        if arma_eq == 7:
                            arma_pri = 'M416'

                    elif arma_eq == 6:
                        print('Em seu loot, acha uma granada de fragmentação e uma M16A4 com bastante munições!')
                        time.sleep(2)
                        print('É um rifle semi automático que pode ser usado para méidas e curtas distâncias')
                        arma_eq = 7
                        time.sleep(2)
                        print('Equipa sua arma e guarda o que achou na mochila para sair da casa,')
                        time.sleep(4)

                        if arma_eq == 8:
                            arma_pri = 'M416'

                    else:
                        print('Em seu loot, encontra uma granada de fragmentação e mais munições')
                        time.sleep(2)
                        print('Guarda na mochila o que achou e sai da casa.')
                        time.sleep(3)

                    granada_frag += 1
                    print('')
                    
                else:
                    print('POW PA PA PUM TUM TUM')
                    time.sleep(1)
                    print('Ele, suspeitando de alguém estar lá, logo reage ao seu tiro na perna saindo da frente da entrada')
                    time.sleep(2)
                    print('Você, meio sem saber o que fazer, continua na mesma posição e esperando que ele apareceça')
                    time.sleep(2)
                    print('Ele então, da a volta na igreja e joga uma granada de fragmentação dentro, que logo explode e você morre.')
                    time.sleep(6)
                    final()

                print('Na rua que passa enfrente a igreja encontra um Buggy')
                time.sleep(3)
                print('Pega o Buggy e segue a rua, saindo de Pochinki.')
                time.sleep(6)
                print('')

            else:
                fugir = 1
                print('Rapidamente você corre para trás mas tropeça e cai do morro ao sair')
                time.sleep(2)
                print('Rola o morro todo, ralando seu braço, pernas e rosto')
                time.sleep(3)
                print('Mesmo assim, com medo, você força a correr e encontra um Buggy na rua')
                time.sleep(3)
                print('Logo pega o Buggy e sai de Pochinki sem pensar duas vezes.')
                time.sleep(6)
                print('')

        else:
            time.sleep(3)

            if arma_eq == 1:
                arma_pri = 'M416'
            elif arma_eq == 2:
                arma_pri = 'AK47'
            elif arma_eq == 3:
                arma_pri = 'Kar98'
            elif arma_eq == 4 :
                arma_pri = 'P92'
            
            print('Enquanto estava saindo das casas, escuta passos se aproximando')
            time.sleep(2)
            print('Parece que vem de trás. Sem saber onde mirar, segue o som do inimigo com os olhos')
            time.sleep(4)
            print('Pega sua',arma_pri,'e mira onde possivelmente ele irá aparecer')
            time.sleep(2)
            print('Você prende a respiração para parar de tremer a mira mas não escuta mais os passos dele...')
            time.sleep(3)

            if arma_eq == 1 or arma_eq == 2:
                combate1 = random.randint(1,7)
                if combate1 != 1:
                    kills += 1
                    print('Ele então aparece na sua mira e você dá um tiro certeiro na cabeça, matando-o')
                    time.sleep(4)
                    print('Preocupado por chamar a atenção, decide pegar a mochila nível 1 dele e sair logo de lá')
                    time.sleep(6)

                else:
                    print('Ele então aparece na sua mira aos poucos e desesperado, você logo atira na perna dele')
                    time.slee(3)
                    print('Como reação, o inimigo vira e acerta um tiro certeiro na sua cabeça.')
                    time.sleep(6)
                    final()
            
            elif arma_eq == 3:
                combate1 = random.randint(1,4)
                if combate1 != 1:
                    kills += 1
                    print('Ele então aparece na sua mira e incrivelmente você acerta o tiro de sniper nele, matando-o')
                    time.sleep(4)
                    print('Preocupado por chamar a atenção, decide pegar a mochila nível 1 dele e a P92 que tinha para sair logo')
                    time.sleep(4)

                else:
                    print('Ele então aparece na sua mira aos poucos e desesperado, você logo atira na perna dele de sniper')
                    time.slee(3)
                    print('Como reação, o inimigo vira e acerta um tiro certeiro na sua cabeça.')
                    time.sleep(6)
                    final()
            
            else:
                combate1 = random.randint(1,5)
                if combate1 != 1:
                    kills += 1
                    print('Ele então aparece na sua mira e você acerta um tiro certeiro na cabeça, matando-o')
                    time.sleep(4)
                    print('Preocupado por chamar a atenção, decide pegar a mochila nível 1 dele e sair logo de lá')
                    time.sleep(6)

                else:
                    print('Ele então aparece na sua mira aos poucos e desesperado, você logo atira na perna dele de pistola')
                    time.slee(3)
                    print('Como reação, o inimigo vira e acerta um tiro certeiro na sua cabeça.')
                    time.sleep(6)
                    final()

            print('')
            print('Na rua que passa ao lado, acha um Buggy')
            time.sleep(2)
            print('Entra nele e sai de Pochinki, evitando mais possíveis combates.')
            time.sleep(6)

        print('')
        print('A Zona de Gás fechou e você precisa ir para a zona segura')
        time.sleep(3)
        print('Porém, há uma Zona Vermelha no caminho, mas o gás está vindo')
        time.sleep(3)
        print('Precisa decidir se quer passar por lá ou dar uma volta grande e fugir de uma possível explosão')
        time.sleep(5)

        zona_verm1 = input('Quer fugir ou passar pela zona vermelha? ')
        zona_verm1 = zona_verm1.lower()
        time.sleep(4)
        print('')
        if zona_verm1 == 'fugir':
            fugir_zm += 1
            print('Você então vira seu Buggy para a direita e começa a contornar a Zona Vermelha')
            time.sleep(3)
            print('Porém não há estrada por onde passa, vai ter que segurar firme e forte no volante!')
            time.sleep(4)
            print('O carro está passando por uma plantação de batatas que estavam molhadas!')
            time.sleep(4)
            print('Você: Esse Buggy tá derrapando demais! Não consigo controlar direito!')
            time.sleep(5)
            print('Por pouco que não cai, mas se depara com canas-de-açúcar!')
            time.sleep(5)
            print('Você: Caramba, dá pra ver as bombas caíndo e explodindo bem perto!')
            time.sleep(3)
            print('Você: AAAAA!! Quase que eu caio num buraco! Preciso me concentrar...')
            time.sleep(4)
            print('As bombas pararam de cair mas precisa achar um lugar bom para ficar protegido')
            time.sleep(4)
            print('Você: Ali, tem umas casas na beira do mar! Parece ter uma visão boa da ilha!')
            time.sleep(3)
            print('Você então chega até as casas e para o Buggy')
            time.sleep(3)
            print('Entra na primeira casa e começa a vasculhar por algum loot.')
            time.sleep(7)
            print('')

            if fugir > 0:
                print('Em cima de uma mesa, encontra 5 bandagens')
                time.sleep(2)
                print('Você então as usa para cuidar das raladas em todo o corpo.')
                time.sleep(6)
                print('')

            if arma_eq == 7 or arma_eq == 3:
                print('Quando terminou de ver as casas, viu da janela um inimigo passando de barco no mar!')
                time.sleep(4)
                print('Pega então sua Kar98 e mira nele')
                time.sleep(2)
                print('Percebe que está navegando em linha reta e logo mira a frente para acertar o tiro')
                time.sleep(3)
                print('De primeira não acerta, ele continua a dirigir e você tenta novamente')
                time.sleep(3)
                print('Acerta um incrível tiro na cabeça dele, matando-o')
                time.sleep(4)
                print('Você: Eu sou um Deus da Sniper!')
                kills += 1
                time.sleep(6)
                print('')
            
            else:
                print('Quando terminou de ver as casas, escutou um barulho de moto')
                time.sleep(3)
                print('Sai da casa e ve um triciculo passando no campo')
                time.sleep(2)
                print('Ve que não estava muito rápida e não muito longe')
                time.sleep(2)
                print('Pega a sua',arma_pri,'e começa a atirar nele para tentar matá-lo')
                time.sleep(3)
                print('Sem saber controlar a arma direito, acerta a roda traseira da moto')
                time.sleep(3)
                print('Faz o inimigo perder controle e cair da moto, matando-o')
                time.sleep(4)
                print('Você: Eu sou um Deus da',arma_pri,'!')
                kills += 1
                time.sleep(6)
                print('')
        
        else:
            print('Você então acelera ao máximo o Buggy e entra na Zona Vermelha')
            time.sleep(3)
            print('Muitas bombas caem do céu de todas direções e explodem muito perto do seu Buggy!')
            time.sleep(2)
            print('Você desvia das que consegue ver mas muitas caem aleatóriamente!')
            time.sleep(2)
            print('Você: Isso é insanoo!!! Acho que vou morrer!')
            time.sleep(2)

            zona1 = random.randint(1,5)
            if zona1 != 1:
                print('Uma bomba atinge um poste que começa a cair na sua frente!')
                time.sleep(2)
                print('Você acelera e ele quase acerta capô, amassa um pouco o teto mas você sai vivo!')
                time.sleep(3)
                print('Em seguida as bombas param de cair e você percebe que passou intacto!')
                time.sleep(3)
                print('Você: UHUULL!! Isso que é sobrevivência!!')
                time.sleep(4)
                print('Para dar uma respirada você para em uma madereira')
                time.sleep(4)
                print('Deixa seu carro e procura no terreno por loot.')
                time.sleep(7)
                print('Encontra entre uns troncos uma SCAR-L, um rifle melhor do que a sua',arma_pri,'!')
                time.sleep(4)
                print('Pega as 120 munições 5.56mm e equipa como arma principal')
                arma_pri = 'SCAR'
                time.sleep(6)
                print('')

                if fugir > 0:
                    print('Em cima de uma mesa, encontra 5 bandagens')
                    time.sleep(2)
                    print('Você então as usa para cuidar das raladas em todo o corpo.')
                    time.sleep(6)
                    print('')

                if arma_eq == 7 or arma_eq == 3:
                    print('Quando terminou de ver as casas, viu da janela um inimigo passando de barco no mar!')
                    time.sleep(4)
                    print('Pega então sua Kar98 e mira nele')
                    time.sleep(2)
                    print('Percebe que está navegando em linha reta e logo mira a frente para acertar o tiro')
                    time.sleep(3)
                    print('De primeira não acerta, ele continua a dirigir e você tenta novamente')
                    time.sleep(3)
                    print('Acerta um incrível tiro na cabeça dele, matando-o')
                    time.sleep(4)
                    print('Você: Eu sou um Deus da Sniper!')
                    kills += 1
                    time.sleep(6)
                    print('')
            
                else:
                    print('Quando terminou de ver as casas, escutou um barulho de moto')
                    time.sleep(3)
                    print('Sai da casa e ve um triciculo passando no campo')
                    time.sleep(2)
                    print('Ve que não estava muito rápida e não muito longe')
                    time.sleep(2)
                    print('Pega a sua',arma_pri,'e começa a atirar nele para tentar matá-lo')
                    time.sleep(3)
                    print('Sem saber controlar a arma direito, acerta a roda traseira da moto')
                    time.sleep(3)
                    print('Faz o inimigo perder controle e cair da moto, matando-o')
                    time.sleep(4)
                    print('Você: Eu sou um Deus da',arma_pri,'!')
                    kills += 1
                    time.sleep(6)
                    print('')


            else:
                print('Uma bomba cai perto do pneu traseiro e faz com que ele exploda!')
                time.sleep(2)
                print('Sem ter controle, você tenta continuar dirigindo mas o carro derrapa para a esquerda')
                time.sleep(3)
                print('Não consegue segurar o Buggy e ele passa por um buraco grande, voando por muitos metros')
                time.sleep(4)
                print('Capota dezenas de vezes e você não aguenta, morrendo dolorosamente.')
                time.sleep(6)
                final()

        print('')
        print('A Zona de Gás fechou novamente menor ainda! Precisa sair daí logo!')
        time.sleep(3)
        print('Por estar um pouco perto, você vai correndo em direção a área segura.')
        time.sleep(10)
        print('')
        print('---------------------------------')
        print('| Você está no Top 5 jogadores! |')
        print('---------------------------------')
        print('')
        time.sleep(4)
        print('Finalmente chega na área segura e logo se posiciona numa casa de 1 andar')
        time.sleep(3)
        print('Fica olhando para todas janelas com muito medo')
        time.sleep(2)
        print('Escuta muitos tiros próximos e você se esconde deles')
        time.sleep(2)
        print('Percebe que sobrou apenas dois sobreviventes vivos')
        time.sleep(2)
        print('Vai precisar matá-lo para ganhar!')
        time.sleep(2)
        print('A Zona de Gás diminui mais um pouco de tal forma que vocês se encontrem')
        time.sleep(3)
        print('Você se reposiciona e escuta barulhos próximos...')
        time.sleep(3)

        if granada_frag == 1:
            print('Vê um vulto passando para uma árvore na esquerda')
            time.sleep(2)
            print('Lembra que tinha uma granada de fragmentação guardada e pega ela da mochila')
            time.sleep(4)
            print('Com ela em mãos, vê o inimigo descendo do morro entre as árvores')
            time.sleep(3)
            print('Quando puxa o pino, ele escuta e corre para a outra direção')
            time.sleep(2)
            print('Você rapidamente prevê onde ele está indo e joga a granada')
            time.sleep(3)
            print('BOOM! Ela explode e mata o inimigo certeiramente!!')
            time.sleep(3)
            print('Você: EU GANHEI!! EU GANHEI!!')
            time.sleep(3)
            print('')
            print('')
            print('WINNER WINNER CHICKEN DINNER!')
            time.sleep(2)
            print('Você ganhou! Parabéns sobrevivente!!')
            time.sleep(2)
            print('Aqui estão seus resultados finais:')
            print('')
            final()

        elif arma_pri == 'SCAR':
            print('Você vê o inimigo entrando numa pequena casa de dois andares')
            time.sleep(2)
            print('Pega logo sua SCAR-L e espera ele sair de lá')
            time.sleep(3)

            inimigo2 = random.randint(1,20)
            if inimigo2 != 1:
                kills += 1
                print('Prende a respiração e atira contra ele na hora que abre a porta')
                time.sleep(2)
                print('Sem ver da onde e sem reações, o inimigo morre quase instantaneamente para você!')
                time.sleep(4)
                print('Você: EU GANHEI!! EU GANHEI!!')
                time.sleep(3)
                print('')
                print('')
                print('WINNER WINNER CHICKEN DINNER!')
                time.sleep(2)
                print('Você ganhou! Parabéns sobrevivente!!')
                time.sleep(2)
                print('Aqui estão seus resultados finais:')
                print('')
                final()
            
            else:
                print('Esqueçe de prender a respiração mas mesmo assim atira contra ele')
                time.sleep(3)
                print('Sem ver da onde e sem reações, o inimigo toma tiros mas logo volta para dentro')
                time.sleep(3)
                print('Ele estava atento e consegue pegar uma proteção da casa')
                time.sleep(2)
                print('Você escuta um barulho de pino mas não entende e quando menos percebe...')
                time.sleep(3)
                print('BOOM! Uma granada vem contudo em você, morrendo para ela na hora.')
                time.sleep(6)
                final()
        
        else:
            print('Você vê o inimigo entrando numa pequena casa de dois andares')
            time.sleep(2)
            print('Pega logo sua',arma_pri,'e espera ele sair de lá')
            time.sleep(3)

            inimigo2 = random.randint(1,7)
            if inimigo2 != 1:
                kills += 1
                print('Prende a respiração e atira contra ele na hora que abre a porta')
                time.sleep(2)
                print('Sem ver da onde e sem reações, o inimigo morre quase instantaneamente para você!')
                time.sleep(4)
                print('Você: EU GANHEI!! EU GANHEI!!')
                time.sleep(3)
                print('')
                print('')
                print('WINNER WINNER CHICKEN DINNER!')
                time.sleep(2)
                print('Você ganhou! Parabéns sobrevivente!!')
                time.sleep(2)
                print('Aqui estão seus resultados finais:')
                print('')
                final()
            
            else:
                print('Esqueçe de prender a respiração mas mesmo assim atira contra ele')
                time.sleep(3)
                print('Sem ver da onde e sem reações, o inimigo toma tiros mas logo volta para dentro')
                time.sleep(3)
                print('Ele estava atento e consegue pegar uma proteção da casa')
                time.sleep(2)
                print('Você escuta um barulho de pino mas não entende e quando menos percebe...')
                time.sleep(3)
                print('BOOM! Uma granada vem contudo em você, morrendo para ela na hora.')
                time.sleep(6)
                final()


print('')
print('Piloto: Passaremos em breve nas últimas duas cidades, Primorsk e Mylta!')
time.sleep(6)

print('')
print('Piloto: Preparados? Façam suas decisões! 15 segundos para fazê-las!')
print('')

pular_sul = input('Você deseja pular de paraquedas agora? ')
pular_sul = pular_sul.lower()

if pular_sul == 'sim' or pular_sul == 's':
    prim_mylt = input('Beleza! Você quer ir para Primorsk ou Mylta? ')
    prim_mylt = prim_mylt.lower()
    if prim_mylt == 'primorsk' or prim_mylt == 'primosk':
        print('Então vamos para Primorsk! Chegamos em 30 segundos!')
        primorsk_ir = 1
    else:
        print('Então vamos para Mylta! Chegamos em 30 segundos!')
        mylta_ir = 1
else:
    print('Você não escolheu uma das duas, cairá em Primorsk.')
    primorsk_ir = 1

time.sleep(10)


if primorsk_ir == 1:
        arma_pri = '.'
        kills = 0
        fugir = 0
        fugir_zm = 0
        granada_frag = 0
        print('Você: shhh... O ventshhh está muito fortshhhh ...')
        time.sleep(3)
        print('Estamos caindo nos galpões!')
        time.sleep(5)

        print('')
        print('Aterrissamos!')
        time.sleep(1)
        print('Voce: Caramba, quase caio no mar...')
        time.sleep(4)
        print('... looteando ...')
        print('')
        time.sleep(6)

        colete = random.randint(1,9)
        if colete == 1 or colete == 2 or colete == 3 or colete == 4:
            print('Você achou um colete nível 1 no canto do galpão!')
            colete_eq = 1
            time.sleep(3)
        elif colete == 5 or colete == 6 or colete == 7:
            print('Você achou um colete nível 2 no canto do galpão!!')
            colete_eq = 2
            time.sleep(3)
        else:
            print('Você achou um colete nível 3 no canto do galpão!!')
            colete_eq = 3
            time.sleep(3)

        print('')

        capacete = random.randint(1,9)
        if capacete == 1 or capacete == 2 or capacete == 3 or capacete == 4:
            print('Encontrou um capacete nível 1 ao lado também!')
            capacete_eq = 1
            time.sleep(3)
        elif capacete == 5 or capacete == 6 or capacete == 7:
            print('Encontrou um capacete nível 2 ao lado também!')
            capacete_eq = 2
            time.sleep(3)
        else:
            print('Encontrou um capacete nível 3 ao lado também!')
            capacete_eq = 3
            time.sleep(3)

        print('')

        arma = random.randint(1,7)
        if arma == 1 or arma == 2 or arma == 3 or arma == 4:
            m4a4ouAK47 = random.randint(1,2)
            if m4a4ouAK47 == 1:
                print('Em uma caixa havia uma M416, um poderoso rifle automático para curta/média distância, será sua arma principal!')
                time.sleep(2)
                print('Veio com 120 munições 5.56mm e sua arma possui controle de recoil fácil comparado com a AK-47')
                arma_eq = 1
                time.sleep(5)
            else:
                print('Em uma caixa havia uma AK-47, ótimo para curta distância, será sua arma principal!')
                time.sleep(2)
                print('Veio com 120 munições 7.62mm e possui alto recoil mas seu dano é o maior entre todos rifles automáticos')
                arma_eq = 2
                time.sleep(5)
        elif arma == 5 or arma == 6:
            print('Em uma caixa você achou uma Kar-98, uma sniper poderosa para média/longa distâncias')
            time.sleep(2)
            print('Ela é sua arma principal enquanto não achar um rifle ou pistola, tome cuidado com os combates')
            time.sleep(2)
            print('Veio com 60 munições 7.62mm e uma mira de 8x na qual pode regular o zoom dela.')
            arma_eq = 3
            time.sleep(5)
        else:
            print('Em uma caixa você achou uma P92, uma pistola semi automática boa para combates de curta distância')
            time.sleep(2)
            print('Veio com 60 munições 9mm e uma mira laser, por enquanto é sua arma principal!')
            arma_eq = 4
            time.sleep(5)


        print('')
        primorsk_casas = input('Pelo visto acabou o loot por aqui, você quer ir para as casas ao lado? ')
        primorsk_casas = primorsk_casas.lower()
        if primorsk_casas == 'sim' or primorsk_casas == 's':
            time.sleep(5)
            mochila = random.randint(1,9)
            if mochila == 1 or mochila == 2 or mochila == 3:
                print('De cara você acha uma mochila nível 1 para guardar munições e outras coisas que precisar!')
            elif mochila == 4 or mochila == 5 or mochila == 6:
                print('De cara você acha uma mochila nível 2 para guardar munições e outras coisas que precisar!')
            else:
                print('De cara você acha uma mochila nível 3 para guardar munições e outras coisas que precisar!')
                
            time.sleep(5)
            print('')

            if arma_eq == 3:
                print('Na cozinha você encontra também uma submetralhadora UMP45 automática, boa para combates de curta distância!')
                time.sleep(2)
                print('Veio com 120 munições .45 ACP e será sua arma primária juntamente com a Kar98 como secundária.')
                time.sleep(5)
                arma_eq = 5
            elif arma_eq == 4:
                print('Na cozinha você encontra também uma submetralhadora UMP45, boa para combates de curta distância!')
                time.sleep(2)
                print('Veio com 120 munições .45 ACP e será sua arma primária juntamente com a P92 como secundária.')
                time.sleep(5)
                arma_eq = 6

            if arma_eq == 1:
                arma_pri = 'M416'
            elif arma_eq == 2:
                arma_pri = 'AK47'
            elif arma_eq == 5 or arma_pri == 6:
                arma_pri = 'UMP'

            print('')
            print('Passos! Você escuta alguém se aproximando da sua casas!')
            time.sleep(1)
            combate1 = input('Pode pular pela janela ou enfrentar ele. Deseja enfrentar ou fugir?')
            combate1 = combate1.lower()
            time.sleep(1)
            if combate1 == 'enfrentar':
                print('Há um armário no quarto que está, você se posiciona atrás dele mirado na porta')
                time.sleep(2)
                print('Você espera pacientemente pelo inimigo entrar e treme um pouco a mira pois está nervoso')
                time.sleep(2)
                print('Escuta passos de escadas e parece que ele está se aproximando. Prende a respiração e concentra-se.')
                time.sleep(4)

                inimigo1 = random.randint(1,10)
                if inimigo1 != 1:
                    print('POW PA PA PUM TUM TUM')
                    time.sleep(1)
                    print('Você dispara vários tiros contra ele com sua',arma_pri,' e acaba com o inimigo sem ele nem te ver!')
                    time.sleep(3)
                    kills += 1
                    if arma_eq == 5 or arma_eq == 6:
                        print('Em seu loot, acha uma granada de fragmentação e uma M16A4 com bastante munições!')
                        time.sleep(2)
                        print('É um rifle semi automático que pode ser usado para méidas e curtas distâncias')
                        arma_eq = 7
                        time.sleep(2)
                        print('Equipa sua arma e guarda o que achou na mochila para sair da casa,')
                        time.sleep(4)

                        if arma_eq == 7:
                            arma_pri = 'M416'

                    elif arma_eq == 6:
                        print('Em seu loot, acha uma granada de fragmentação e uma M16A4 com bastante munições!')
                        time.sleep(2)
                        print('É um rifle semi automático que pode ser usado para méidas e curtas distâncias')
                        arma_eq = 7
                        time.sleep(2)
                        print('Equipa sua arma e guarda o que achou na mochila para sair da casa,')
                        time.sleep(4)

                        if arma_eq == 8:
                            arma_pri = 'M416'
                        
                    else:
                        print('Em seu loot, encontra uma granada de fragmentação e mais munições')
                        time.sleep(2)
                        print('Guarda na mochila o que achou e sai da casa.')
                        time.sleep(3)

                    print('')
                    granada_frag += 1
                    
                else:
                    print('POW PA PA PUM TUM TUM')
                    time.sleep(1)
                    print('Ele, suspeitando de alguém estar lá, logo reage ao seu tiro na perna saindo da frente da porta')
                    time.sleep(2)
                    print('Você, meio sem saber o que fazer, continua na mesma posição e esperando que ele apareceça')
                    time.sleep(2)
                    print('Ele então, joga uma granada de fragmentação na cozinha, que logo explode e você morre.')
                    time.sleep(6)
                    final()

                print('Na praia, avista uma lancha estacionada lá')
                time.sleep(3)
                print('Pega a lancha e segue na costa, saindo de Primorsk.')
                time.sleep(6)
                print('')

            else:
                fugir += 1
                print('Rapidamente você pula pela janela e corta seu braço com o estilhasso do vidro')
                time.sleep(3)
                print('Mesmo assim, com medo, você força a correr e encontra uma lancha na praia')
                time.sleep(3)
                print('Logo pega ela e sai de Pochinki sem pensar duas vezes.')
                time.sleep(6)
                print('')

        else:
            time.sleep(3)

            if arma_eq == 1:
                arma_pri = 'M416'
            elif arma_eq == 2:
                arma_pri = 'AK47'
            elif arma_eq == 3:
                arma_pri = 'Kar98'
            elif arma_eq == 4 :
                arma_pri = 'P92'
            
            print('Enquanto estava saindo das casas, escuta passos se aproximando')
            time.sleep(2)
            print('Parece que vem da frente. Sem saber onde mirar, segue o som do inimigo com os olhos')
            time.sleep(4)
            print('Pega sua',arma_pri,'e mira onde possivelmente ele irá aparecer')
            time.sleep(2)
            print('Você prende a respiração para parar de tremer a mira mas não escuta mais os passos dele...')
            time.sleep(3)

            if arma_eq == 1 or arma_eq == 2:
                combate1 = random.randint(1,7)
                if combate1 != 1:
                    kills += 1
                    print('Ele então aparece na sua mira e você dá um tiro certeiro na cabeça, matando-o')
                    time.sleep(4)
                    print('Preocupado por chamar a atenção, decide pegar a mochila nível 1 dele e sair logo de lá')
                    time.sleep(6)

                else:
                    print('Ele então aparece na sua mira aos poucos e desesperado, você logo atira na perna dele')
                    time.slee(3)
                    print('Como reação, o inimigo vira e acerta um tiro certeiro na sua cabeça.')
                    time.sleep(6)
                    final()
            
            elif arma_eq == 3:
                combate1 = random.randint(1,4)
                if combate1 != 1:
                    kills += 1
                    print('Ele então aparece na sua mira e incrivelmente você acerta o tiro de sniper nele, matando-o')
                    time.sleep(4)
                    print('Preocupado por chamar a atenção, decide pegar a mochila nível 1 dele e a P92 que tinha para sair logo')
                    time.sleep(4)

                else:
                    print('Ele então aparece na sua mira aos poucos e desesperado, você logo atira na perna dele de sniper')
                    time.slee(3)
                    print('Como reação, o inimigo vira e acerta um tiro certeiro na sua cabeça.')
                    time.sleep(6)
                    final()
            
            else:
                combate1 = random.randint(1,5)
                if combate1 != 1:
                    kills += 1
                    print('Ele então aparece na sua mira e você acerta um tiro certeiro na cabeça, matando-o')
                    time.sleep(4)
                    print('Preocupado por chamar a atenção, decide pegar a mochila nível 1 dele e sair logo de lá')
                    time.sleep(6)

                else:
                    print('Ele então aparece na sua mira aos poucos e desesperado, você logo atira na perna dele de pistola')
                    time.slee(3)
                    print('Como reação, o inimigo vira e acerta um tiro certeiro na sua cabeça.')
                    time.sleep(6)
                    final()

            print('')
            print('Na praia da cidade você avista uma lancha parada')
            time.sleep(2)
            print('Entra nela e sai de Pochinki, evitando mais possíveis combates.')
            time.sleep(6)

        print('')
        print('A Zona de Gás fechou e você precisa ir para a zona segura')
        time.sleep(3)
        print('Porém, há uma Zona Vermelha no caminho, mas o gás está vindo')
        time.sleep(3)
        print('Precisa decidir se quer passar por lá ou dar uma volta grande e fugir de uma possível explosão')
        time.sleep(5)

        zona_verm1 = input('Quer fugir ou passar pela zona vermelha? ')
        zona_verm1 = zona_verm1.lower()
        time.sleep(4)
        print('')
        if zona_verm1 == 'fugir':
            fugir_zm += 1
            print('Você então vira a lancha para a direita e começa a contornar a Zona Vermelha pelo mar')
            time.sleep(3)
            print('Você tenta desviar das várias bombas que caem na água')
            time.sleep(4)
            print('Você: Tô todo molhado! Deviam ter fechado essa lancha!')
            time.sleep(5)
            print('Você: Caramba, dá pra ver as bombas caíndo e explodindo bem perto!')
            time.sleep(3)
            print('Você: AAAAA!! Quase que eu bato numa rocha! Preciso me concentrar...')
            time.sleep(4)
            print('As bombas pararam de cair mas precisa achar um lugar bom para ficar protegido')
            time.sleep(4)
            print('Você: Ali, perto da praia! Tem um casarão bem grande!')
            time.sleep(3)
            print('Você então encalha a lancha na praia e vai até o casarão')
            time.sleep(3)
            print('Entra no casarão e começa a vasculhar por algum loot.')
            time.sleep(7)
            print('')

            if fugir > 0:
                print('Em cima de uma mesa, encontra 5 bandagens')
                time.sleep(2)
                print('Você então as usa para cuidar dos cortes de vidro de quando fugiu.')
                time.sleep(6)
                print('')

            if arma_eq == 7 or arma_eq == 3:
                print('Quando terminou de ver a casa, viu da janela um inimigo correndo no campo aberto')
                time.sleep(4)
                print('Pega então sua Kar98 e mira nele')
                time.sleep(2)
                print('Percebe que está correndo em linha reta e logo mira a frente para acertar o tiro')
                time.sleep(3)
                print('De primeira não acerta, ele continua a fugir e você tenta novamente')
                time.sleep(3)
                print('Acerta o tiro só que na perna, fazendo com que o inimigo caia no chão')
                time.sleep(3)
                print('Rapidamente, você atira na cabeça para finalizá-lo e mata-o!')
                time.sleep(4)
                print('Você: Eu sou um Deus da Sniper!')
                kills += 1
                time.sleep(6)
                print('')
            
            else:
                print('Quando terminou de ver as casas, escutou um barulho de moto')
                time.sleep(3)
                print('Sai da casa e ve uma moto passando no campo')
                time.sleep(2)
                print('Ve que não estava muito rápida e não muito longe')
                time.sleep(2)
                print('Pega a sua',arma_pri,'e começa a atirar nele para tentar matá-lo')
                time.sleep(3)
                print('Sem saber controlar a arma direito, acerta a roda traseira da moto')
                time.sleep(3)
                print('Faz o inimigo perder controle e cair da moto, matando-o')
                time.sleep(4)
                print('Você: Eu sou um Deus da',arma_pri,'!')
                kills += 1
                time.sleep(6)
                print('')
        
        else:
            print('Você então acelera ao máximo a lancha e entra na Zona Vermelha')
            time.sleep(3)
            print('Muitas bombas caem do céu de todas direções e explodem muito perto da sua lancha!')
            time.sleep(2)
            print('Você desvia das que consegue ver mas muitas caem aleatóriamente!')
            time.sleep(2)
            print('Você: Isso é insanoo!!! Acho que vou morrer!')
            time.sleep(2)

            zona1 = random.randint(1,5)
            if zona1 != 1:
                print('Uma bomba gigante faz cair muita água no barco!')
                time.sleep(2)
                print('Você acelera e ela afunda um pouco o barco, mas você sai vivo!')
                time.sleep(3)
                print('Em seguida as bombas param de cair e você percebe que passou intacto!')
                time.sleep(3)
                print('Você: UHUULL!! Isso que é sobrevivência!!')
                time.sleep(4)
                print('Para dar uma respirada você para em umas casas na beira da praia')
                time.sleep(4)
                print('Deixa sua lancha na areia e entra pra ver se há algum loot.')
                time.sleep(7)
                print('Encontra em um banheiro uma AUG A3, um rifle melhor do que a sua',arma_pri,'!')
                time.sleep(4)
                print('Pega as 120 munições 5.56mm e equipa como arma principal')
                arma_pri = 'AUG'
                time.sleep(6)
                print('')

                if fugir > 0:
                    print('Em cima de uma mesa, encontra 5 bandagens')
                    time.sleep(2)
                    print('Você então as usa para cuidar dos cortes de vidro de quando fugiu.')
                    time.sleep(6)
                    print('')

                if arma_eq == 7 or arma_eq == 3:
                    print('Quando terminou de ver a casa, viu da janela um inimigo correndo no campo aberto')
                    time.sleep(4)
                    print('Pega então sua Kar98 e mira nele')
                    time.sleep(2)
                    print('Percebe que está correndo em linha reta e logo mira a frente para acertar o tiro')
                    time.sleep(3)
                    print('De primeira não acerta, ele continua a fugir e você tenta novamente')
                    time.sleep(3)
                    print('Acerta o tiro só que na perna, fazendo com que o inimigo caia no chão')
                    time.sleep(3)
                    print('Rapidamente, você atira na cabeça para finalizá-lo e mata-o!')
                    time.sleep(4)
                    print('Você: Eu sou um Deus da Sniper!')
                    kills += 1
                    time.sleep(6)
                    print('')
            
                else:
                    print('Quando terminou de ver as casas, escutou um barulho de moto')
                    time.sleep(3)
                    print('Sai da casa e ve uma moto passando no campo')
                    time.sleep(2)
                    print('Ve que não estava muito rápida e não muito longe')
                    time.sleep(2)
                    print('Pega a sua',arma_pri,'e começa a atirar nele para tentar matá-lo')
                    time.sleep(3)
                    print('Sem saber controlar a arma direito, acerta a roda traseira da moto')
                    time.sleep(3)
                    print('Faz o inimigo perder controle e cair da moto, matando-o')
                    time.sleep(4)
                    print('Você: Eu sou um Deus da',arma_pri,'!')
                    kills += 1
                    time.sleep(6)
                    print('')


            else:
                print('Uma bomba cai perto muito perto do barco!')
                time.sleep(2)
                print('Ela faz com a lancha vire e você caia na água')
                time.sleep(3)
                print('Não consegue aguentar tantas bombas explodindo por perto e morre')
                time.sleep(6)
                final()

        print('')
        print('A Zona de Gás fechou novamente menor ainda! Precisa sair daí logo!')
        time.sleep(3)
        print('Por estar um pouco perto, você vai correndo em direção a área segura.')
        time.sleep(10)
        print('')
        print('---------------------------------')
        print('| Você está no Top 5 jogadores! |')
        print('---------------------------------')
        print('')
        time.sleep(4)
        print('Finalmente chega na área segura e logo se posiciona entre umas pedras grandes')
        time.sleep(4)
        print('Fica olhando para todos os lados e com muito medo')
        time.sleep(2)
        print('Escuta muitos tiros atrás e você se esconde deles')
        time.sleep(2)
        print('Percebe que sobrou apenas dois sobreviventes vivos')
        time.sleep(2)
        print('Vai precisar matá-lo para ganhar!')
        time.sleep(2)
        print('A Zona de Gás diminui mais um pouco de tal forma que vocês se encontrem')
        time.sleep(3)
        print('Você se reposiciona e escuta barulhos próximos...')
        time.sleep(3)

        if granada_frag == 1:
            print('Vê um vulto passando para uma pedra na direita')
            time.sleep(2)
            print('Lembra que tinha uma granada de fragmentação guardada e pega ela da mochila')
            time.sleep(4)
            print('Com ela em mãos, vê o inimigo indo para trás de uma pedra')
            time.sleep(3)
            print('Percebe que fica parado lá e prepara a granada')
            time.sleep(2)
            print('Quando puxa o pino, ele escuta e corre para a esquerda')
            time.sleep(2)
            print('Você rapidamente prevê onde ele está indo e joga a granada')
            time.sleep(3)
            print('BOOM! Ela explode e mata o inimigo certeiramente!!')
            time.sleep(3)
            print('Você: EU GANHEI!! EU GANHEI!!')
            time.sleep(3)
            print('')
            print('')
            print('WINNER WINNER CHICKEN DINNER!')
            time.sleep(2)
            print('Você ganhou! Parabéns sobrevivente!!')
            time.sleep(2)
            print('Aqui estão seus resultados finais:')
            print('')
            final()

        elif arma_pri == 'AUG':
            print('Você vê o inimigo deitando dentro de uma canoa abandonada')
            time.sleep(2)
            print('Pega logo sua AUG e posiciona-se atrás dele')
            time.sleep(3)

            inimigo2 = random.randint(1,20)
            if inimigo2 != 1:
                kills += 1
                print('Prende a respiração e atira contra ele')
                time.sleep(2)
                print('Sem ver da onde e sem reações, o inimigo morre quase instantaneamente para você!')
                time.sleep(4)
                print('Você: EU GANHEI!! EU GANHEI!!')
                time.sleep(3)
                print('')
                print('')
                print('WINNER WINNER CHICKEN DINNER!')
                time.sleep(2)
                print('Você ganhou! Parabéns sobrevivente!!')
                time.sleep(2)
                print('Aqui estão seus resultados finais:')
                print('')
                final()
            
            else:
                print('Esqueçe de prender a respiração mas mesmo assim atira contra ele')
                time.sleep(3)
                print('Sem ver da onde e sem reações, o inimigo toma tiros mas logo vira-se')
                time.sleep(3)
                print('Ele estava atento e consegue atirar rapidamente contra você')
                time.sleep(3)
                print('Acerta um tiro no ombro e você cai no chão, te finalizando.')
                time.sleep(6)
                final()
        
        else:
            print('Você vê o inimigo deitando dentro de uma canoa abandonada')
            time.sleep(2)
            print('Pega logo sua',arma_pri,'e posiciona-se atrás dele')
            time.sleep(3)

            inimigo2 = random.randint(1,7)
            if inimigo2 != 1:
                kills += 1
                print('Prende a respiração e atira contra ele')
                time.sleep(2)
                print('Sem ver da onde e sem reações, o inimigo morre quase instantaneamente para você!')
                time.sleep(4)
                print('Você: EU GANHEI!! EU GANHEI!!')
                time.sleep(3)
                print('')
                print('')
                print('WINNER WINNER CHICKEN DINNER!')
                time.sleep(2)
                print('Você ganhou! Parabéns sobrevivente!!')
                time.sleep(2)
                print('Aqui estão seus resultados finais:')
                print('')
                final()
            
            else:
                print('Esqueçe de prender a respiração mas mesmo assim atira contra ele')
                time.sleep(3)
                print('Sem ver da onde e sem reações, o inimigo toma tiros mas logo vira-se')
                time.sleep(3)
                print('Ele estava atento e consegue atirar rapidamente contra você')
                time.sleep(3)
                print('Acerta um tiro no ombro e você cai no chão, te finalizando.')
                time.sleep(6)
                final()
elif mylta_ir == 1:
        arma_pri = '.'
        kills = 0
        fugir = 0
        fugir_zm = 0
        granada_frag = 0
        print('Você: shhh... O ventshhh está muito fortshhhh ...')
        time.sleep(3)
        print('')

        print('Estamos quase chegando! Vamos cair nas casas!')
        time.sleep(5)

        print('')
        print('Aterrissamos!')
        time.sleep(1)
        print('Voce: Caramba, que altura! Minha perna tá até doendo...')
        print('Deu pra ver a ponte que liga na base militar, lá é gigante!')
        time.sleep(4)
        print('... looteando ...')
        print('')
        time.sleep(6)

        colete = random.randint(1,9)
        if colete == 1 or colete == 2 or colete == 3 or colete == 4:
            print('Você achou um colete nível 1 no quarto da casa!')
            colete_eq = 1
            time.sleep(3)
        elif colete == 5 or colete == 6 or colete == 7:
            print('Você achou um colete nível 2 no quarto da casa!')
            colete_eq = 2
            time.sleep(3)
        else:
            print('Você achou um colete nível 3 no quarto da casa!')
            colete_eq = 3
            time.sleep(3)

        print('')

        capacete = random.randint(1,9)
        if capacete == 1 or capacete == 2 or capacete == 3 or capacete == 4:
            print('Encontrou um capacete nível 1 ao lado também!')
            capacete_eq = 1
            time.sleep(3)
        elif capacete == 5 or capacete == 6 or capacete == 7:
            print('Encontrou um capacete nível 2 ao lado também!')
            capacete_eq = 2
            time.sleep(3)
        else:
            print('Encontrou um capacete nível 3 ao lado também!')
            capacete_eq = 3
            time.sleep(3)

        print('')

        arma = random.randint(1,7)
        if arma == 1 or arma == 2 or arma == 3 or arma == 4:
            m4a4ouAK47 = random.randint(1,2)
            if m4a4ouAK47 == 1:
                print('Na sala havia uma M416, um poderoso rifle automático para curta/média distância, será sua arma principal!')
                time.sleep(2)
                print('Veio com 120 munições 5.56mm e sua arma possui controle de recoil fácil comparado com a AK-47')
                arma_eq = 1
                time.sleep(5)
            else:
                print('Na sala havia uma AK-47, ótimo para curta distância, será sua arma principal!')
                time.sleep(2)
                print('Veio com 120 munições 7.62mm e possui alto recoil mas seu dano é o maior entre todos rifles automáticos')
                arma_eq = 2
                time.sleep(5)
        elif arma == 5 or arma == 6:
            print('Na sala você achou uma Kar-98, uma sniper poderosa para média/longa distâncias')
            time.sleep(2)
            print('Ela é sua arma principal enquanto não achar um rifle ou pistola, tome cuidado com os combates')
            time.sleep(2)
            print('Veio com 60 munições 7.62mm e uma mira de 8x na qual pode regular o zoom dela.')
            arma_eq = 3
            time.sleep(5)
        else:
            print('Na sala você achou uma P92, uma pistola semi automática boa para combates de curta distância')
            time.sleep(2)
            print('Veio com 60 munições 9mm e uma mira laser, por enquanto é sua arma principal!')
            arma_eq = 4
            time.sleep(5)

        print('')
        mylta_ponte = input('Pelo visto acabou o loot por aqui, você quer ir para as casas ao lado? ')
        mylta_ponte = mylta_ponte.lower()
        if mylta_ponte == 'sim' or mylta_ponte == 's':
            time.sleep(5)
            mochila = random.randint(1,9)
            if mochila == 1 or mochila == 2 or mochila == 3:
                print('Na entrada você acha uma mochila nível 1 para guardar munições e outras coisas que precisar!')
            elif mochila == 4 or mochila == 5 or mochila == 6:
                print('Na entrada você acha uma mochila nível 2 para guardar munições e outras coisas que precisar!')
            else:
                print('Na entrada você acha uma mochila nível 3 para guardar munições e outras coisas que precisar!')
                
            time.sleep(5)
            print('')

            if arma_eq == 3:
                print('No quarto de cima você encontra também uma submetralhadora UMP45 automática, boa para combates de curta distância!')
                time.sleep(2)
                print('Veio com 120 munições .45 ACP e será sua arma primária juntamente com a Kar98 como secundária.')
                time.sleep(5)
                arma_eq = 5
            elif arma_eq == 4:
                print('No quarto de cima você encontra também uma submetralhadora UMP45, boa para combates de curta distância!')
                time.sleep(2)
                print('Veio com 120 munições .45 ACP e será sua arma primária juntamente com a P92 como secundária.')
                time.sleep(5)
                arma_eq = 6

            if arma_eq == 1:
                arma_pri = 'M416'
            elif arma_eq == 2:
                arma_pri = 'AK47'
            elif arma_eq == 5 or arma_pri == 6:
                arma_pri = 'UMP'

            print('')
            print('Passos! Você escuta alguém se aproximando da sua casas!')
            time.sleep(1)
            combate1 = input('Pode pular pela janela ou enfrentar ele. Deseja enfrentar ou fugir?')
            combate1 = combate1.lower()
            time.sleep(1)
            if combate1 == 'enfrentar':
                print('Há um armário no quarto que está, você se posiciona atrás dele mirado na porta')
                time.sleep(2)
                print('Você espera pacientemente pelo inimigo entrar e treme um pouco a mira pois está nervoso')
                time.sleep(2)
                print('Escuta passos de escadas e parece que ele está se aproximando. Prende a respiração e concentra-se.')
                time.sleep(4)

                inimigo1 = random.randint(1,10)
                if inimigo1 != 1:
                    print('POW PA PA PUM TUM TUM')
                    time.sleep(1)
                    print('Você dispara vários tiros contra ele com sua',arma_pri,' e acaba com o inimigo sem ele nem te ver!')
                    time.sleep(3)
                    kills += 1
                    if arma_eq == 5 or arma_eq == 6:
                        print('Em seu loot, acha uma granada de fragmentação e uma M16A4 com bastante munições!')
                        time.sleep(2)
                        print('É um rifle semi automático que pode ser usado para méidas e curtas distâncias')
                        arma_eq = 7
                        time.sleep(2)
                        print('Equipa sua arma e guarda o que achou na mochila para sair da casa,')
                        time.sleep(4)

                        if arma_eq == 7:
                            arma_pri = 'M416'

                    elif arma_eq == 6:
                        print('Em seu loot, acha uma granada de fragmentação e uma M16A4 com bastante munições!')
                        time.sleep(2)
                        print('É um rifle semi automático que pode ser usado para méidas e curtas distâncias')
                        arma_eq = 7
                        time.sleep(2)
                        print('Equipa sua arma e guarda o que achou na mochila para sair da casa,')
                        time.sleep(4)

                        if arma_eq == 8:
                            arma_pri = 'M416'

                    else:
                        print('Em seu loot, encontra uma granada de fragmentação e mais munições')
                        time.sleep(2)
                        print('Guarda na mochila o que achou e sai da casa.')
                        time.sleep(3)

                    granada_frag += 1
                    print('')
                    
                else:
                    print('POW PA PA PUM TUM TUM')
                    time.sleep(1)
                    print('Ele, suspeitando de alguém estar lá, logo reage ao seu tiro na perna saindo da frente da porta')
                    time.sleep(2)
                    print('Você, meio sem saber o que fazer, continua na mesma posição e esperando que ele apareceça')
                    time.sleep(2)
                    print('Ele então, joga uma granada de fragmentação na cozinha, que logo explode e você morre.')
                    time.sleep(6)
                    final()

                print('Decide se posicionar na ponte e esperar por alguem vir')
                time.sleep(3)
                print('Vai correndo e se esconde atrás de caixas na ponte, saindo de Primorsk.')
                time.sleep(7)
                print('')

            else:
                fugir += 1
                print('Rapidamente você pula pela janela e corta seu braço com o estilhasso do vidro')
                time.sleep(3)
                print('Mesmo assim, com medo, você força a correr e vai em direção a ponte')
                time.sleep(3)
                print('Se esconde atrás de caixas e fica lá.')
                time.sleep(7)
                print('')

        else:
            time.sleep(3)

            if arma_eq == 1:
                arma_pri = 'M416'
            elif arma_eq == 2:
                arma_pri = 'AK47'
            elif arma_eq == 3:
                arma_pri = 'Kar98'
            elif arma_eq == 4 :
                arma_pri = 'P92'
            
            print('Enquanto estava saindo das casas, escuta passos se aproximando')
            time.sleep(2)
            print('Parece que vem da frente. Sem saber onde mirar, segue o som do inimigo com os olhos')
            time.sleep(4)
            print('Pega sua',arma_pri,'e mira onde possivelmente ele irá aparecer')
            time.sleep(2)
            print('Você prende a respiração para parar de tremer a mira mas não escuta mais os passos dele...')
            time.sleep(3)

            if arma_eq == 1 or arma_eq == 2:
                combate1 = random.randint(1,7)
                if combate1 != 1:
                    kills += 1
                    print('Ele então aparece na sua mira e você dá um tiro certeiro na cabeça, matando-o')
                    time.sleep(4)
                    print('Preocupado por chamar a atenção, decide pegar a mochila nível 1 dele e sair logo de lá')
                    time.sleep(6)

                else:
                    print('Ele então aparece na sua mira aos poucos e desesperado, você logo atira na perna dele')
                    time.slee(3)
                    print('Como reação, o inimigo vira e acerta um tiro certeiro na sua cabeça.')
                    time.sleep(6)
                    final()
            
            elif arma_eq == 3:
                combate1 = random.randint(1,4)
                if combate1 != 1:
                    kills += 1
                    print('Ele então aparece na sua mira e incrivelmente você acerta o tiro de sniper nele, matando-o')
                    time.sleep(4)
                    print('Preocupado por chamar a atenção, decide pegar a mochila nível 1 dele e a P92 que tinha para sair logo')
                    time.sleep(4)

                else:
                    print('Ele então aparece na sua mira aos poucos e desesperado, você logo atira na perna dele de sniper')
                    time.slee(3)
                    print('Como reação, o inimigo vira e acerta um tiro certeiro na sua cabeça.')
                    time.sleep(6)
                    final()
            
            else:
                combate1 = random.randint(1,5)
                if combate1 != 1:
                    kills += 1
                    print('Ele então aparece na sua mira e você acerta um tiro certeiro na cabeça, matando-o')
                    time.sleep(4)
                    print('Preocupado por chamar a atenção, decide pegar a mochila nível 1 dele e sair logo de lá')
                    time.sleep(6)

                else:
                    print('Ele então aparece na sua mira aos poucos e desesperado, você logo atira na perna dele de pistola')
                    time.slee(3)
                    print('Como reação, o inimigo vira e acerta um tiro certeiro na sua cabeça.')
                    time.sleep(6)
                    final()

            print('')
            print('Decide se posicionar na ponte e esperar por alguem vir')
            time.sleep(3)
            print('Vai correndo e se esconde atrás de caixas na ponte, saindo de Primorsk.')
            time.sleep(7)

        print('')
        print('A Zona de Gás fechou e você precisa ir para a zona segura')
        time.sleep(3)
        print('Porém, escuta um carro vindo na ponte')
        time.sleep(2)
        print('Decide então aparecer e atirar contra ele com sua',arma_pri)
        time.sleep(3)
        combate2 = random.randint(1,6)
        if combate2 != 1:
            kills += 1
            print('Acerta vários tiros no carro mas estava um pouco longe')
            time.sleep(3)
            print('Ele vem se aproximando e você consegue acertar no peito dele enquanto dirige, matando-o')
            time.sleep(4)
            print('Rapidamente pula para o lado das caixas para o carro não atropelar')
            time.sleep(3)
            print('Sem muito tempo, apenas pega o carro e sai da ponte super rápido.')
            print('')
        
        else:
            print('Acerta muitos disparos no carro e não no inimigo')
            time.sleep(2)
            print('Você se esconde para recarregar mas quando aparece de novo...')
            time.sleep(3)
            print('Ele vem em alta velocidade e te atropela.')
            time.sleep(6)
            final()

        print('No caminho se depara com uma Zona vermelha')
        time.sleep(3)
        print('Precisa decidir se quer passar por lá ou dar uma volta grande e fugir de uma possível explosão')
        time.sleep(5)

        zona_verm1 = input('Quer fugir ou passar pela zona vermelha? ')
        zona_verm1 = zona_verm1.lower()
        time.sleep(4)
        print('')
        if zona_verm1 == 'fugir':
            fugir_zm += 1
            print('Você então vira o carro para a esquerda e começa a contornar a Zona Vermelha')
            time.sleep(3)
            print('Você tenta desviar das várias bombas que do lado do carro')
            time.sleep(4)
            print('Você: Não consigo ver direito! O parabrisa não funciona!')
            time.sleep(5)
            print('Você: Caramba, dá pra ver as bombas caíndo e explodindo bem perto!')
            time.sleep(3)
            print('Você: AAAAA!! Quase que eu numa árvore! Preciso me concentrar...')
            time.sleep(4)
            print('As bombas pararam de cair mas precisa achar um lugar bom para ficar protegido')
            time.sleep(4)
            print('Você: Ali, na beira da rua! Tem um posto de gasolina!')
            time.sleep(3)
            print('Você então estaciona o carro e vai até o posto')
            time.sleep(3)
            print('Entra no posto e começa a vasculhar por algum loot.')
            time.sleep(7)

            if fugir > 0:
                print('Em cima de uma mesa, encontra 5 bandagens')
                time.sleep(2)
                print('Você então as usa para cuidar dos cortes de vidro de quando fugiu.')
                time.sleep(6)
                print('')

            if arma_eq == 7 or arma_eq == 3:
                print('Quando terminou de ver o posto, viu lá fora um inimigo nadando na água')
                time.sleep(4)
                print('Pega então sua Kar98 e mira nele')
                time.sleep(2)
                print('Percebe que está nadando em linha reta e logo mira a frente para acertar o tiro')
                time.sleep(3)
                print('De primeira não acerta, ele continua a nadar e você tenta novamente')
                time.sleep(3)
                print('Acerta o tiro só que no braço, fazendo com que o inimigo fique mais lento')
                time.sleep(3)
                print('Rapidamente, você atira na cabeça para finalizá-lo e mata-o!')
                time.sleep(4)
                print('Você: Eu sou um Deus da Sniper!')
                kills += 1
                time.sleep(6)
                print('')
            
            else:
                print('Quando terminou de ver o posto, escutou um barulho de jipe')
                time.sleep(3)
                print('Sai da casa e ve um jipe passando na estrada em frente')
                time.sleep(2)
                print('Ve que não estava muito rápida e não muito longe')
                time.sleep(2)
                print('Pega a sua',arma_pri,'e começa a atirar nele para tentar matá-lo')
                time.sleep(3)
                print('Sem saber controlar a arma direito, acerta as rodas traseiras do jipe')
                time.sleep(3)
                print('Faz o inimigo perder controle e bater num poste, matando-o')
                time.sleep(4)
                print('Você: Eu sou um Deus da',arma_pri,'!')
                kills += 1
                time.sleep(6)
                print('')
        
        else:
            print('Você então acelera ao máximo o carro e entra na Zona Vermelha')
            time.sleep(3)
            print('Muitas bombas caem do céu de todas direções e explodem muito perto de seu carro!')
            time.sleep(2)
            print('Você desvia das que consegue ver mas muitas caem aleatóriamente!')
            time.sleep(2)
            print('Você: Isso é insanoo!!! Acho que vou morrer!')
            time.sleep(2)

            zona1 = random.randint(1,5)
            if zona1 != 1:
                print('Uma bomba faz voar terra no vidro da frente e você não enxerga nada!')
                time.sleep(2)
                print('Você acelera e o vento empurra a terra, você sai vivo!')
                time.sleep(3)
                print('Em seguida as bombas param de cair e você percebe que passou intacto!')
                time.sleep(3)
                print('Você: UHUULL!! Isso que é sobrevivência!!')
                time.sleep(4)
                print('Para dar uma respirada você para em uma casa de praia')
                time.sleep(4)
                print('Deixa seu carro na areia e entra pra ver se há algum loot.')
                time.sleep(7)
                print('Encontra em um banheiro uma SCAR-L, um rifle melhor do que a sua',arma_pri,'!')
                time.sleep(4)
                print('Pega as 120 munições 5.56mm e equipa como arma principal')
                arma_pri = 'SCAR'
                time.sleep(6)
                print('')

                if fugir > 0:
                    print('Em cima de uma mesa, encontra 5 bandagens')
                    time.sleep(2)
                    print('Você então as usa para cuidar dos cortes de vidro de quando fugiu.')
                    time.sleep(6)
                    print('')

                if arma_eq == 7 or arma_eq == 3:
                    print('Quando terminou de ver a casa, viu lá fora um inimigo nadando na água')
                    time.sleep(4)
                    print('Pega então sua Kar98 e mira nele')
                    time.sleep(2)
                    print('Percebe que está nadando em linha reta e logo mira a frente para acertar o tiro')
                    time.sleep(3)
                    print('De primeira não acerta, ele continua a nadar e você tenta novamente')
                    time.sleep(3)
                    print('Acerta o tiro só que no braço, fazendo com que o inimigo fique mais lento')
                    time.sleep(3)
                    print('Rapidamente, você atira na cabeça para finalizá-lo e mata-o!')
                    time.sleep(4)
                    print('Você: Eu sou um Deus da Sniper!')
                    kills += 1
                    time.sleep(6)
                    print('')
            
                else:
                    print('Quando terminou de ver a casa, escutou um barulho de jipe')
                    time.sleep(3)
                    print('Sai da casa e ve um jipe passando na estrada de trás')
                    time.sleep(2)
                    print('Ve que não estava muito rápida e não muito longe')
                    time.sleep(2)
                    print('Pega a sua',arma_pri,'e começa a atirar nele para tentar matá-lo')
                    time.sleep(3)
                    print('Sem saber controlar a arma direito, acerta as rodas traseiras do jipe')
                    time.sleep(3)
                    print('Faz o inimigo perder controle e bater num poste, matando-o')
                    time.sleep(4)
                    print('Você: Eu sou um Deus da',arma_pri,'!')
                    kills += 1
                    time.sleep(6)
                    print('')


            else:
                print('Uma bomba cai perto muito do carro!')
                time.sleep(2)
                print('Ela faz com que você perca o pneu frontal')
                time.sleep(2)
                print('Sem controle do carro, você vira o volante e começa a capotar')
                time.sleep(3)
                print('Não aguenta as pancadas por conta da velocidade e morre.')
                time.sleep(6)
                final()


        print('')
        print('A Zona de Gás fechou novamente menor ainda! Precisa sair daí logo!')
        time.sleep(3)
        print('Por estar um pouco perto, você vai correndo em direção a área segura.')
        time.sleep(10)
        print('')
        print('---------------------------------')
        print('| Você está no Top 5 jogadores! |')
        print('---------------------------------')
        print('')
        time.sleep(4)
        print('Finalmente chega na área segura e logo se posiciona grandes fenos num campo')
        time.sleep(4)
        print('Fica olhando para todos os lados e com muito medo')
        time.sleep(2)
        print('Escuta muitos tiros na frente e você se esconde deles')
        time.sleep(2)
        print('Percebe que sobrou apenas dois sobreviventes vivos')
        time.sleep(2)
        print('Vai precisar matá-lo para ganhar!')
        time.sleep(2)
        print('A Zona de Gás diminui mais um pouco de tal forma que vocês se encontrem')
        time.sleep(3)
        print('Você se reposiciona e escuta barulhos próximos...')
        time.sleep(3)

        if granada_frag == 1:
            print('Vê um vulto passando para um bloco de feno')
            time.sleep(2)
            print('Lembra que tinha uma granada de fragmentação guardada e pega ela da mochila')
            time.sleep(4)
            print('Com ela em mãos, vê o inimigo indo para trás de outro feno')
            time.sleep(3)
            print('Percebe que fica parado lá e prepara a granada')
            time.sleep(2)
            print('Quando puxa o pino, ele escuta e corre para a direita')
            time.sleep(2)
            print('Você rapidamente prevê onde ele está indo e joga a granada')
            time.sleep(3)
            print('BOOM! Ela explode e mata o inimigo certeiramente!!')
            time.sleep(3)
            print('Você: EU GANHEI!! EU GANHEI!!')
            time.sleep(3)
            print('')
            print('')
            print('WINNER WINNER CHICKEN DINNER!')
            time.sleep(2)
            print('Você ganhou! Parabéns sobrevivente!!')
            time.sleep(2)
            print('Aqui estão seus resultados finais:')
            print('')
            final()

        elif arma_pri == 'SCAR':
            print('Você vê o inimigo rastegando para trás de um feno')
            time.sleep(2)
            print('Pega logo sua SCAR-L e abre para o lado para vê-lo melhor')
            time.sleep(3)

            inimigo2 = random.randint(1,20)
            if inimigo2 != 1:
                kills += 1
                print('Prende a respiração e atira contra ele')
                time.sleep(2)
                print('Sem ver da onde e sem reações, o inimigo morre quase instantaneamente para você!')
                time.sleep(4)
                print('Você: EU GANHEI!! EU GANHEI!!')
                time.sleep(3)
                print('')
                print('')
                print('WINNER WINNER CHICKEN DINNER!')
                time.sleep(2)
                print('Você ganhou! Parabéns sobrevivente!!')
                time.sleep(2)
                print('Aqui estão seus resultados finais:')
                print('')
                final()
            
            else:
                print('Esqueçe de prender a respiração mas mesmo assim atira contra ele')
                time.sleep(3)
                print('Sem ver da onde e sem reações, o inimigo toma tiros mas logo vai para o lado')
                time.sleep(3)
                print('Ele estava atento e consegue se esconder')
                time.sleep(3)
                print('Escuta um barulho de pino mas não entende')
                time.sleep(3)
                print('Quando percebe, uma granada vinha em sua direção e explode em seguida, morrendo.')
                time.sleep(6)
                final()
        
        else:
            print('Você vê o inimigo rastegando para trás de um feno')
            time.sleep(2)
            print('Pega logo sua',arma_pri,'e abre para o lado para vê-lo melhor')
            time.sleep(3)

            inimigo2 = random.randint(1,7)
            if inimigo2 != 1:
                kills += 1
                print('Prende a respiração e atira contra ele')
                time.sleep(2)
                print('Sem ver da onde e sem reações, o inimigo morre quase instantaneamente para você!')
                time.sleep(4)
                print('Você: EU GANHEI!! EU GANHEI!!')
                time.sleep(3)
                print('')
                print('')
                print('WINNER WINNER CHICKEN DINNER!')
                time.sleep(2)
                print('Você ganhou! Parabéns sobrevivente!!')
                time.sleep(2)
                print('Aqui estão seus resultados finais:')
                print('')
                final()
            
            else:
                print('Esqueçe de prender a respiração mas mesmo assim atira contra ele')
                time.sleep(3)
                print('Sem ver da onde e sem reações, o inimigo toma tiros mas logo vai para o lado')
                time.sleep(3)
                print('Ele estava atento e consegue se esconder')
                time.sleep(3)
                print('Escuta um barulho de pino mas não entende')
                time.sleep(3)
                print('Quando percebe, uma granada vinha em sua direção e explode em seguida, morrendo.')
                time.sleep(6)
                final()