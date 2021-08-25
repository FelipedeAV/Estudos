#Subprogramas

#Função para criar os conjuntos (set) de cada tipo de medalha
def criaMedalhas(arquivo):
    medalhaOuro = set()
    medalhaPrata = set()
    medalhaBronze = set()
    texto = open(arquivo, "r", encoding='utf-8')
    for linha in texto:
        pais, cor, esporte = linha.strip().split('#')

        # Separando um set para cada tipo de medalha
        if cor == 'ouro':
            medalhaOuro.add(pais)

        if cor == 'prata':
            medalhaPrata.add(pais)

        if cor == 'bronze':
            medalhaBronze.add(pais)
    texto.close()
    return medalhaOuro, medalhaPrata, medalhaBronze

#Imprimir todos os resultados
def imprima(medalhaOuro, medalhaPrata, medalhaBronze, peloMenosUm,todasMedalhas):
    print("Países com Ouro(s):")
    for elemento in medalhaOuro:
        print("       ", elemento)
    print()

    print("Países com Prata(s):")
    for elemento in medalhaPrata:
        print("       ", elemento)
    print()

    print("Países com Bronze(s):")
    for elemento in medalhaBronze:
        print("       ", elemento)
    print()

    print("Países com pelo menos uma medalha:")
    for elemento in peloMenosUm:
        print("         ", elemento)
    print()

    print("País(es) com pelo menos uma Medalha de cada Tipo:")
    for elemento in todasMedalhas:
        print("        ", elemento)

#Fazendo união de todos os países com medalhas
def peloMenos(medalhaOuro, medalhaPrata, medalhaBronze):
    peloMenosUm = medalhaOuro.union(medalhaPrata, medalhaBronze)
    return peloMenosUm

#Fazendo a intersecção dos países que possuem todas das medalhas
def todosTipos(medalhaOuro, medalhaPrata, medalhaBronze):
    todasMedalhas = medalhaOuro.intersection(medalhaBronze,medalhaPrata)
    return todasMedalhas

#Programa Principal
arquivo = input("Escreva o nome do arquivo: " ) + '.txt'

medalhaOuro, medalhaPrata, medalhaBronze = criaMedalhas(arquivo)
peloMenosUm = peloMenos(medalhaOuro, medalhaPrata, medalhaBronze)
todasMedalhas = todosTipos(medalhaOuro, medalhaPrata, medalhaBronze)
imprima(medalhaOuro, medalhaPrata, medalhaBronze, peloMenosUm,todasMedalhas)