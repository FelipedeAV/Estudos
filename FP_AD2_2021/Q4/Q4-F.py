import struct
TAM = 17

#Subprogramas

def criaLista(arquivo):
    lista = []
    with open('frete.bin', 'rb') as arquivo:
        for i in range(6):
            arquivo.seek(i * TAM)
            CEP, loja, valorFrete = lerBin(arquivo)
            lista.append([CEP, loja, valorFrete])
    return lista

def lerBin(arq):
    CEP = arq.read(8).decode("iso8859-1")
    loja = arq.read(5).decode("iso8859-1").rstrip(chr(0))
    valorFrete = struct.unpack("f", arq.read(4))[0]
    return CEP, loja, valorFrete

def procuraLojaFrete(lista):
    listLojaFrete = []
    menorFrete = 999999999999
    for entrada in lista:
        if cepProcurado == entrada[0]:
            auxFrete = entrada[2]
            auxLoja = entrada[1]
            if auxFrete < menorFrete:
                menorFrete = auxFrete
                nomeLoja = auxLoja
    listLojaFrete.append(nomeLoja)
    listLojaFrete.append(menorFrete)
    return listLojaFrete

def contaFinal(produto,listaLojaFrete):
    arq = open(produto, "r")
    lista = []
    for linha in arq:
        info = linha.strip().split()
        lista.append(info)
    listAux = lista[2:5]
    for i in range(len(listAux)):
        if listaLojaFrete[0] == listAux[i][0]:
            melhorLoja = listaLojaFrete[0]
            precoProduto = float(listAux[i][1])
            valorFrete = float(listaLojaFrete[1])
            resultado = precoProduto + valorFrete
    arq.close()
    return resultado, melhorLoja

#Limpar o CEP
def limpaCEP(frase, para_remover):
    nova_frase = frase
    for x in para_remover:
        nova_frase = nova_frase.replace(x, '')
    return nova_frase

#Programa Principal
arquivoBinario = input( ) + ".bin"
produto = input( ) + ".txt"
cep = str(input( ))
cepProcurado = limpaCEP(cep, ".-")
lista = criaLista(arquivoBinario)
listaLojaFrete = procuraLojaFrete(lista)
precoTotal, melhorLoja = contaFinal(produto, listaLojaFrete)
resposta = "A melhor loja do produto 1 para o CEP " + cepProcurado + " é a " +melhorLoja + ", com o valor total de R$"
print(resposta, "%.2f" %precoTotal,".")