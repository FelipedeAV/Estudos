from itertools import product

# Insere as letras para o alfabeto
entrada = input(' ')
alfabeto = entrada.split(' ')

# Guarda a quantidade de letras digitadas na variável n
n = len(alfabeto)

# Cria uma lista para receber as permutações
listafinal = []

# cria as permutações e incrementa na lista
for i in range(1, len(alfabeto) + 1):
    Listapermutacaoi = [''.join(str(j) for j in x) for x in product(alfabeto, repeat=i)]
    listafinal = listafinal + Listapermutacaoi

print("As palavras do alfabeto", entrada, "são", listafinal)