from collections import OrderedDict
#Subprogramas
#função que cria o dicionário
def dicCovid(nomeArquivo,cepaDesejada):
    dicionario = {}

    with open(nomeArquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            cpf, cepa, data, cidade, estado = linha.strip().split('#')
            #totalInfectados = countInfect(cidade)
            dia, mes, ano = data.split('/')
            if cepa == cepaDesejada:
                if estado in dicionario:
                    if cidade in dicionario[estado]:
                        #Se a Cidade estiver no dicionário, atualiza os valores da chave cidade

                        novoValor = dicionario[estado][cidade]
                        novoValor.append([ano, mes])
                        dicionario[estado].update({cidade: novoValor})
                    else:
                        #Se a Cidade não estiver, adiciona
                        dicionario[estado].update({cidade:[[ano,mes]]})
                else:
                    #Se o Estado não estiver no dicionário, adiciona
                    dicionario.update({estado:{cidade:[[ano,mes]]}})
    return dicionario

def imprimeSaida(dici,cepaDesejada):
    totalInfects = 0

    print("Tipo da Cepa: ",cepaDesejada)
    #acessar todas chaves do dicionario
    for chave in dici:

        print(chave)
        #acessa o valor da chave anterior
        for valor in dici[chave]: #valor é chave
            listAux = []
            print(" ",valor) #imprime a chave do dicionario cidade
            #print("   ",dici[chave][valor]) #testar se está imprimendo os valores da chave cidade que é uma lista
            for lista in dici[chave][valor]:
                aparece = dici[chave][valor].count(lista) #quantas vezes a lista aparece
                #print("aparece: ", aparece) #imprime o valor de aparece como forma de controle
                #adicionar os valores numa lista auxiliar
                listAux.append(lista[0])
                listAux.append(lista[1])
                listAux.append(aparece)

            #print(listAux) #print de controle da lista auxuliar
            novaLista = separaLista(listAux,3)
            novaListaUnica = retiraDuplicatas(novaLista)
            #print(dici[chave][valor])
            #acessa cada elemento da lista de valores de cada chave do dicionario cidade
            for elem in novaListaUnica:
                print("    Ano:",elem[0]," Mês:",elem[1]," Infectados:",elem[2])
                totalInfects = totalInfects + elem[2]
    print()
    print("Total Geral: ",totalInfects)

#Função para fazer lista de lista
def separaLista(lista,n):
    for i in range(0,len(lista),n):
        yield lista[i:i+n]
    return lista

#função para retirar duplicatas
def retiraDuplicatas(lista):
    nova_lista = []
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
    return nova_lista

#Programa Principal
arquivo = input("Escreva o nome do arquivo: " ) + '.txt'
cepaDesejada = input("Informe a cepa desejada: ")

dicionario = dicCovid(arquivo,cepaDesejada)
dici = OrderedDict(sorted(dicionario.items(), reverse=False))
#imprime minha saida
imprimeSaida(dici,cepaDesejada)