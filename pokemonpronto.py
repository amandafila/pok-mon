# ***********************é necessário baixar a biblioteca TQDM***********************
# por algum motivo só funciona direito no pycharm!!
import random
from tqdm import tqdm
import time
result = 0
sair = 1
contTentativas = 0
escolhidocaverna = 0
escolhidomato = 0
contpokemon = -1
pokemons = list()
pokcaverna = ["Geodude", "Zubat", "Sandshrew", "Sandslash", "Golbat", "Diglet", "Dugtrio", "Meowth", "Machop", "Gravler"]
pokmato = ["Evee", "Vulpix", "Caterpie", "Metapod", "Pidgey", "Weedle", "Ekans", "Spearow", "Arbok", "Pikachu", "Nidoran"]
# for i in tqdm(range(10000000)):
#     result += i
print("Olá! Sou o Professor Carvalho, um pesquisador Pokémon.")
nome = input("Antes de começarmos nossa jornada qual é o seu nome? ")
genero = input("Qual é o seu gênero? (m/f) ")
if genero == "m":
    print(f"Ótimo! Então você é o {nome}! Prepare-se para uma aventura emocionante no mundo dos Pokémons!")
if genero == "f":
    print(f"Ótimo! Então você é a {nome}! Prepare-se para uma aventura emocionante no mundo dos Pokémons!")
while sair != 0 and contTentativas < 3:
    print("OPÇÕES")
    time.sleep(0.5)
    print("1 - Entrar na caverna")
    time.sleep(0.5)
    print("2 - Entrar no mato")
    time.sleep(0.5)
    print("3 - Listar Pokémon")
    time.sleep(0.5)
    print("4 - Sair")
    op = int(input(f"{nome}, digite o número da opção escolhida: "))
    print('.', end='')
    time.sleep(0.3)
    print('.', end='')
    time.sleep(0.3)
    print('.', end='')
    time.sleep(0.3)
    if op == 1:
        caverna = random.randint(0, 9)
        escolhidocaverna = (pokcaverna[caverna])
        print("\nVocê está na Caverna! ")
        print(f"Você encontrou o {escolhidocaverna}!")
        sn = input("Deseja tentar capturá-lo? (s/n) ")
        if sn == "s": #colocar while aqui, eu acho kkkkkkk. Só aumentar o contador de tentativas quando o pokemon não for capturado
            for i in tqdm(range(10000000)):
                result += i
            while contTentativas < 3:
                probabilidadecaverna = random.randint(0, 100)
                if probabilidadecaverna > 0 and probabilidadecaverna<= 35:
                    if escolhidocaverna in pokemons:
                        print("Pokémon já capturado.")
                        break
                    else: 
                        print(f"{escolhidocaverna} capturado com sucesso!")
                        contpokemon += 1
                        pokemons.insert(contpokemon, escolhidocaverna)
                        break
                else:
                    print ("O Pokémon não foi capturado!")
                    novTentativa = input("Deseja tentar novamente?(s/n) ")
                    if novTentativa == "s":
                        contTentativas += 1
                    if novTentativa == "n":
                        break
                        #continue
                #print("Suas tentativas acabaram")
                        #isso aqui não tá funcionando. Arrumar (provavelmente tem que por um while)
    if op == 2:
        print("\nVocê está no Mato! ")
        mato = random.randint(0,9)
        escolhidomato = (pokmato[mato])
        print("\nVocê encontrou o {}".format(escolhidomato))
        sn = input("Deseja tentar capturá-lo? (s/n) ")
        if sn == "s":
            for i in tqdm(range(10000000)):
                result += i
            while contTentativas < 3:
                probabilidademato = random.randint(0, 100)
                if probabilidademato > 0 and probabilidademato <= 50:
                    if escolhidomato in pokemons:
                        print("Pokémon já capturado.")
                        break
                    else: 
                        print(f"{escolhidomato} capturado com sucesso!")
                        contpokemon += 1
                        pokemons.insert(contpokemon, escolhidomato)
                        break
                    # print(f"{escolhidomato} capturado com sucesso!")
                    # contpokemon += 1
                    # # if escolhidomato in pokemons:
                    # #     print("Pokémon já capturado.")
                    # #     break
                    # pokemons.insert(contpokemon, escolhidomato)
                    # break
                else:
                    print("O Pokémon não foi capturado!")
                    novTentativa = input("Deseja tentar novamente?(s/n) ")
                    #print(contTentativas)
                    if novTentativa == "s":
                        contTentativas += 1
                    if novTentativa == "n":
                        break
                    #break
            # if contTentativas > 3:
            #     print("Suas tentativas acabaram. O jogo encerra aqui.\nAté a próxima! :)")
            #     sair == 0
                #break
    elif op == 4:
        break
    elif op == 3:
        a = len(pokemons)
        for c in range (0,a):
            print("\n- ", pokemons[c])
        #print("\nPokémon capturados: ", pokemons)
        #print("Pokémon capturados da caverna: ", escolhidocaverna)
if contTentativas >= 3:
    print("Suas tentativas acabaram.", end=' ')
    #print ("Pokémon capturados: ", pokemons)
print("\nA sua jornada encerra aqui. Até a próxima! :)")
#if contTentativas > 3:
#print("Suas tentativas acabaram. O jogo encerra aqui.\nAté a próxima! :)")
#print(escolhidocaverna)
