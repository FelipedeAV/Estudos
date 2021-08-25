import struct
TAM = 40
#Subprogramas

#Função para produzir a saída .txt
def escritaTXT(anoConsulta, kmTotal, melhorModeloGasolina, melhorModeloAlcool, tanqueTGasolina, tanqueTAlcool, gastoTAlcool, gastoTGasolina):
    carroEconomico = open("carro_mais_economico.txt", "w")
    carroEconomico.write("No ano de " + anoConsulta + ", os carros mais" + "\n")
    carroEconomico.write("econômicos para andar " + str(kmTotal) + " km à"+"\n")
    carroEconomico.write("gasolina e a álcool são " + melhorModeloGasolina + " e" + "\n")
    carroEconomico.write(melhorModeloAlcool + ", respectivamente." + "\n")
    carroEconomico.write("À gasolina, para andar " + str(kmTotal) + " km"+"\n")
    carroEconomico.write("utilizaremos " + str(tanqueTGasolina) + " tanques e" + "\n")
    carroEconomico.write("gastaremos R$ " + str(gastoTGasolina) + "." + "\n")
    carroEconomico.write("À álcool, para andar " + str(kmTotal) + " km" + "\n")
    carroEconomico.write("utilizaremos " + str(tanqueTAlcool) + " tanques e" + "\n")
    carroEconomico.write("gastaremos R$ " + str(gastoTAlcool) + ".")
    carroEconomico.close()

#Função para criar uma lista com o arquivo binário
def criaLista(arquivo):
    lista = []
    with open(arquivoCarros, 'rb') as arquivo:
        for i in range(4):
            arquivo.seek(i * TAM)
            ano, modelo, AlcoolKMCidade, GasolinaKMCidade, AlcoolKMEstrada, GasolinaKMEstrada, tanque = lerBin(arquivo)
            lista.append([ano, modelo, AlcoolKMCidade, GasolinaKMCidade, AlcoolKMEstrada, GasolinaKMEstrada, tanque])
    return lista

#Função para ler o arquivo binário
def lerBin(arqC):
    ano = arqC.read(4).decode("iso8859-1")
    modelo = arqC.read(16).decode("iso8859-1").rstrip(chr(0))
    AlcoolKMCidade = struct.unpack("f", arqC.read(4))[0]
    GasolinaKMCidade = struct.unpack("f", arqC.read(4))[0]
    AlcoolKMEstrada = struct.unpack("f", arqC.read(4))[0]
    GasolinaKMEstrada = struct.unpack("f", arqC.read(4))[0]
    tanque = struct.unpack("f", arqC.read(4))[0]

    return ano, modelo, AlcoolKMCidade, GasolinaKMCidade, AlcoolKMEstrada, GasolinaKMEstrada, tanque

#Função para criar uma lista com as informações do modelo e a quantidade de litros utilizados
def consultaLitros(listCarrosBin, anoConsulta, kmCidade, kmEstrada):
    listAux = []
    listLitros = []
    for i in range(len(listCarrosBin)):
        if anoConsulta == listCarrosBin[i][0]:
            modelo = listCarrosBin[i][1]
            litrosAlcool = (kmCidade/listCarrosBin[i][2])+(kmEstrada/listCarrosBin[i][4])
            litrosGasolina = (kmCidade/listCarrosBin[i][3])+(kmEstrada/listCarrosBin[i][5])
            listAux.append(modelo)
            listAux.append(litrosAlcool)
            listAux.append(litrosGasolina)
    #organizando a lista
    listLitros = list(separaLista(listAux,3))
    return listLitros

#Função para fazer lista de lista
def separaLista(lista,n):
    for i in range(0,len(lista),n):
        yield lista[i:i+n]
    return lista

#Função para identificar qual o melhor modelo de carro de acordo com o tipo de combustível e seu gasto em litros
def economico(listaLitros):
    menorAlcool = 99999999999
    menorGasolina = 99999999999
    for lista in listaLitros:
        auxMenorAlcool = lista[1]
        ModeloAlcool = lista[0]
        auxMenorGasolina = lista[2]
        ModeloGasolina = lista[0]
        if auxMenorAlcool < menorAlcool:
            menorAlcool = auxMenorAlcool
            melhorModeloAlcool = ModeloAlcool
        if auxMenorGasolina < menorGasolina:
            menorGasolina = auxMenorGasolina
            melhorModeloGasolina = ModeloGasolina
    return melhorModeloAlcool, menorAlcool, melhorModeloGasolina, menorGasolina

#Função para truncar números de acordo com a quantidade de casas decimais desejadas
def truncar(num,n):
    numTruncado = int(num*(10**n))/(10**n)
    return numTruncado

#Função para calcular quanto sobrou no tanque de cada tipo de combustível
def tanqueUsado(listCarrosBin,melhorModeloAlcool, menorAlcool, melhorModeloGasolina, menorGasolina):
    for lista in listCarrosBin:
        if melhorModeloAlcool == lista[1]:
            tanqueAlcool = menorAlcool/lista[6]
        if melhorModeloGasolina == lista[1]:
            tanqueGasolina = menorGasolina/lista[6]
    return tanqueAlcool, tanqueGasolina

#Função para calcular o gasto de cada tipo de combustível
def calculaGasto(arquivoPrecos, menorGasolina, menorAlcool):
    precos = open(arquivoPrecos, 'r')
    for linha in precos:
        dados = linha.strip().split(' ')
        precoAlcool = float(dados[0])
        precoGasolina = float(dados[1])
    gastoAlcool = precoAlcool * menorAlcool
    gastoGasolina = precoGasolina * menorGasolina
    precos.close()
    return gastoAlcool, gastoGasolina

#Programa Principal
#Entra com o arquivo binário
arquivoCarros = input( ) + ".bin"

#Entra com o arquivo txt
arquivoPrecos = input( ) + ".txt"

#Entra com o valor do ano para consulta
anoConsulta = input( )

#Entra com os quilômetros utilizados na Cidade para consulta
kmCidade = float(input( ))

#Entra com os quilômetros utilizados na Estrada para consulta
kmEstrada = float(input( ))

#Calcula a quilometragem total para ser inserida na saída .txt, converti para inteiro para facilitar
kmTotal = int(kmCidade + kmEstrada)

#Cria uma lista com as informações do arquivo binário
listCarrosBin = criaLista(arquivoCarros)

#Cria uma lista com os modelos consultados e a quantidade de litros utilizados com álcool e gasolina, respectivamente
listaLitros = consultaLitros(listCarrosBin, anoConsulta, kmCidade, kmEstrada)

#O melhor modelo para cada tipo de combustível e a quantidade de litros utilizada para cada combustível em litros
melhorModeloAlcool, menorAlcool, melhorModeloGasolina, menorGasolina = economico(listaLitros)

#a quantidade de litros que sobrou em cada tanque de acordo com o combustível
tanqueAlcool, tanqueGasolina = tanqueUsado(listCarrosBin,melhorModeloAlcool, menorAlcool, melhorModeloGasolina, menorGasolina)

#valores truncados da quantidade de cada tanque calculados anteriormente
tanqueTGasolina = truncar(tanqueGasolina,2)
tanqueTAlcool = truncar(tanqueAlcool,2)

#a quantidade em reais gasta em cada tipo de combustível
gastoAlcool, gastoGasolina = calculaGasto(arquivoPrecos, menorGasolina, menorAlcool)

#valores truncados em reais de cada tipo de combustível informados anteriormente
gastoTAlcool = truncar(gastoAlcool,2)
gastoTGasolina = truncar(gastoGasolina,2)

#Escrita da saída .txt
escritaTXT(anoConsulta, kmTotal, melhorModeloGasolina, melhorModeloAlcool, tanqueTGasolina, tanqueTAlcool, gastoTAlcool, gastoTGasolina)