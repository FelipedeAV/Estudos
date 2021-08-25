# Função para remover os nomes intermidiários
def RemoveNome(ListaNomes):
    for nome in ListaNomes:
        # Usei .lower() para fazer a comparação de palavras todas em minúsculo, evitar problema tipo DaS
        if (nome.lower() == 'da') or (nome.lower() == 'das') or (nome.lower() == 'de') or (nome.lower() == 'des') \
                or (nome.lower() == 'di') or (nome.lower() == 'dis') or (nome.lower() == 'do') or (
                nome.lower() == 'dos') \
                or (nome.lower() == 'du') or (nome.lower() == 'dus') or (nome.lower() == 'a') or (nome.lower() == 'as') \
                or (nome.lower() == 'e') or (nome.lower() == 'es') or (nome.lower() == 'i') or (nome.lower() == 'is') \
                or (nome.lower() == 'o') or (nome.lower() == 'os') or (nome.lower() == 'u') or (nome.lower() == 'us'):
            ListaNomes.remove(nome)
    return ListaNomes


# Função para abreviar os nomes intermediários
def AbreviaSobrenomes(ListaNomes):
    for i in range(1, len(ListaNomes) - 1):
        ListaNomes[i] = ListaNomes[i][0] + "."
    return ListaNomes


# Função para imprimir os nomes da lista
def ImprimaNome(ListaNomes):
    for i in range(len(ListaNomes)):
        print(ListaNomes[i], end=' ')


# Inicio do programa
#Digitar um nome completo
nomecompleto = input()
Vazio = []
ListaNomesCompleto = []
# Verifica se o usuário não digitou nome
if nomecompleto == Vazio:
    print("Não digitou nome algum")
else:
    # Digitando nomes e completar a lista
    while nomecompleto != "":
        ListaNomesCompleto.append(nomecompleto)
        nomecompleto = input()

for nome in ListaNomesCompleto:
    ListaNomes = nome.split()
    RemoveNome(ListaNomes)
    AbreviaSobrenomes(ListaNomes)
    print(" ")
    ImprimaNome(ListaNomes)