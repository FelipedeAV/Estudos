import math
#Função para Converter as informações em float
def converte(partes):
    numeros = []
    for item in partes:
        numeros.append(float(item))
    return numeros

#Função para calcular a distância entre dois pontos, onde um ponto é percorrido na lista e o outro é o ponto referência
def calculaDistancia(listaPontos):
    somatorio = 0
    distancia = 0
    for i in range(5):                                                   #acessa os pontos
        somatorio = 0
        for j in range(3):                                               #acessa as coordenadas dos pontos
            auxSomatorio = (listaPontos[i][j] - listaPontos[5][j]) ** 2
            somatorio = somatorio + auxSomatorio
        raizdoSomatorio = math.sqrt(somatorio)
        distancia = distancia + raizdoSomatorio
    return distancia

#Função para calcular tudo do ciclo. Calcular a nova lista de pontos e após a distância desejada
def calculaCicloN(listaPontos):
    for a in range(ciclo):
        numCiclo = a +1
        for i in range(4):
            for j in range(2):
                listaPontos[i][j] = listaPontos[i][j] - listaPontos[7][0]
            listaPontos[i][2] = listaPontos[i][2] + listaPontos[7][0]
        for z in range(2):
            listaPontos[4][z] = listaPontos[4][z] - listaPontos[7][0]
        #calculando a distancia da lista atual
        distancia = calculaDistancia(listaPontos)

        #imprimir a saída
        print("Listagem de Pontos no Cilco", numCiclo, "com Delta de Deslocamento", listaPontos[7][0],":")
        print("   ", tuple(listaPontos[0]))
        print("   ", tuple(listaPontos[1]))
        print("   ", tuple(listaPontos[2]))
        print("   ", tuple(listaPontos[3]))
        print("   ", tuple(listaPontos[4]))
        print("Soma das Distâncias para o Ponto ", tuple(listaPontos[5]), ":","%1.2f" %distancia)
        print()
    return None

#def converteFloat(listaPontos):
#    for i in range(6):
#        for j in range(3):
#            listaPontos[i][j] = "%.2f" % listaPontos[i][j]
#    listaPontos[6][0] = "%.2f" % listaPontos[6][0]
#    listaPontos[7][0] ="%.2f" % listaPontos[7][0]
#
#    return listaPontos

#Início do programa
listaPontos = []
ponto = input()
while ponto != "":
    pontoFloat = converte(ponto.split())
    listaPontos.append(pontoFloat)  # minha lista com todas as informações
    ponto = input()

#Converte os valores da lista para duas casas decimais à direita da vírgula
#converteFloat(listaPontos)

#Guarda o valor do cálculo da distância entre dois pontos
distancia = calculaDistancia(listaPontos)

#Guarda o valor da quantidade de ciclo
ciclo = int(listaPontos[6][0])

#Área de Impressão
print("Pontos Originais:")
print("   ", tuple(listaPontos[0]))
print("   ", tuple(listaPontos[1]))
print("   ", tuple(listaPontos[2]))
print("   ", tuple(listaPontos[3]))
print("   ", tuple(listaPontos[4]))
print("Soma das Distâncias para o Ponto ", tuple(listaPontos[5]), ":", "%1.2f" %distancia)
print()
calculaCicloN(listaPontos)