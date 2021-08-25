#Subprogramas
def abrir(arquivo):
    apostas = open(arquivo, "r")
    print("Conteúdo do Arquivo de Apostas Teste2:")
    for linha in apostas:
        print(linha, end="")
    print()
    print("---- Fim do Arquivo de Apostas ----")
    apostas.close()

def contApostas(arquivo):
    apostas = open(arquivo, "r")
    quantidade = 0
    for linha in apostas:
        quantidade = quantidade + 1
    print("Total de Apostas: ", quantidade)
    apostas.close()

def percorrer(numerosSorteados,conteudo):
    count = 0
    listaNumerosSorteados = list(numerosSorteados)
    valor = conteudo[1:]
    for item in valor:
        for numero in listaNumerosSorteados:
            if item == numero:
                count = count + 1
    return count

def montaDicionario(arquivo):
    dicionario = dict()
    apostas = open(arquivo, "r")
    for linha in apostas:
        conteudo = linha.strip().split("#")
        acertos = percorrer(numerosSorteados,conteudo)
        dicionario[conteudo[0]] = acertos
    apostas.close()
    return dicionario
    #print(dicionario)

def ordemNome(ganhadores):
    ganhadores.sort()
    return ganhadores

def imprimirDicionario(dicionario):
    ganhadores = []
    for chave, valor in dicionario.items():
        if valor == 8:
            ganhadores.append(chave)
            qtdGanhadores = len(ganhadores)
    if ganhadores == []:
        print("Ninguém Acertou 8 Números!!!")
    else:
        print("Foi(ram)", qtdGanhadores, "Ganhador(es) com 8 Acertos:")
        ordemNome(ganhadores)
        for nome in ganhadores:
            print("     ", nome)

    ganhadores = []
    for chave, valor in dicionario.items():
        if valor == 7:
            ganhadores.append(chave)
            qtdGanhadores = len(ganhadores)
    if ganhadores == []:
        print("Ninguém Acertou 7 Números!!!")
    else:
        print("Foi(ram)", qtdGanhadores, "Ganhador(es) com 7 Acertos:")
        ordemNome(ganhadores)
        for nome in ganhadores:
            print("     ", nome)

    ganhadores = []
    for chave, valor in dicionario.items():
        if valor == 6:
            ganhadores.append(chave)
            qtdGanhadores = len(ganhadores)
    if ganhadores == []:
        print("Ninguém Acertou 6 Números!!!")
    else:
        print("Foi(ram)", qtdGanhadores, "Ganhador(es) com 6 Acertos:")
        ordemNome(ganhadores)
        for nome in ganhadores:
            print("     ", nome)

    ganhadores = []
    for chave, valor in dicionario.items():
        if valor == 5:
            ganhadores.append(chave)
            qtdGanhadores = len(ganhadores)
    if ganhadores == []:
        print("Ninguém Acertou 5 Números!!!")
    else:
        print("Foi(ram)", qtdGanhadores, "Ganhador(es) com 5 Acertos:")
        ordemNome(ganhadores)
        for nome in ganhadores:
            print("     ", nome)

    ganhadores = []
    for chave, valor in dicionario.items():
        if valor == 4:
            ganhadores.append(chave)
            qtdGanhadores = len(ganhadores)
    if ganhadores == []:
        print("Ninguém Acertou 4 Números!!!")
    else:
        print("Foi(ram)", qtdGanhadores, "Ganhador(es) com 4 Acertos:")
        ordemNome(ganhadores)
        for nome in ganhadores:
            print("     ", nome)

    ganhadores = []
    for chave, valor in dicionario.items():
        if valor == 3:
            ganhadores.append(chave)
            qtdGanhadores = len(ganhadores)
    if ganhadores == []:
        print("ACUMULOU TUDO")
    else:
        print("Foi(ram)", qtdGanhadores, "Ganhador(es) com 3 Acertos:")
        ordemNome(ganhadores)
        for nome in ganhadores:
            print("     ", nome)

    ganhadores = []
    for chave, valor in dicionario.items():
        if valor < 3:
            ganhadores.append(chave)
            qtdGanhadores = len(ganhadores)
    if ganhadores != []:
        print("ACUMULOU TUDO")

#Programa Principal
arquivo = input( ) + ".txt"
numerosSorteados = set(input().split())
abrir(arquivo)
contApostas(arquivo)
dicionario = montaDicionario(arquivo)
imprimirDicionario(dicionario)

