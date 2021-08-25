#Biblioteca para gerar itens aleatórios
import random

#Função para achar o menos valor de um vetor desconsiderando o primeiro item que é o nome do produto
def menor_valor(v):
    menor = v[1]
    loja_indice = 0
    for i in range(len(v)-1):
        if menor > v[i+1]:
            menor = v[i+1]
            loja_indice = i
    menor_loja = [loja_indice, menor]
    return menor_loja

l = int(input())
p = int(input())
#Lista de lojas
lojas = []
#Lista de Produtos
produtos = []
#Ínicio e final do intervalo para gerar um número aleatório
produtos_limites = []
#Lista com o produtos e os preçcs das lojas [[nome prod 1, preço loja 1, preço loja 2, ...], [nome prod 2, preço loja 1, preço loja 2, ...]]
produtos_precos = []
#Matriz geral com loja e os preços [[loja 1, preço prod 1, preço prod 2, ...],[loja 1, preço prod 1, preço prod 2,...]]
lojas_geral = []
#Variável usada para calculo do valor total gasto
total = 0

#Gera a lista de lojas
for k in range(l):
    lojas.append(input())

#Gera a lista de produtos e a de produtos com os preços
for i in range(p):
    produto_precos = []
    texto = input().split()
    produto_precos.append(texto[0])
    produtos.append(texto[0])
    x = round(random.uniform(int(texto[1]),int(texto[2])),2)
    y = round(random.uniform(int(texto[1]),int(texto[2])),2)
    produto_precos.append(x)
    produto_precos.append(y)
    produtos_precos.append(produto_precos)

#Gera a lista com a loja e os preços
for n in range(len(lojas)):
    loja_produtos_precos = [lojas[n]]
    for m in range(p):
        loja_produtos_precos.append(produtos_precos[m][n+1])
    lojas_geral.append(loja_produtos_precos)


print("--------------------------")
print("Resultado da pesquisa:")
#O :15s fixa o tamanho usado como 15 caracteres independente de quantos a palavra tenha, isso faz com que a matriz seja impressa com os mesmos espaços
#O end=" " faz com que o próximo item printado seja colocado ao lado do item anterios ao invés de quebrar a linha
print('{:15s}'.format(""), end=" ")
for produto in produtos:
    print('{:15s}'.format(produto), end=" ")
#Quebra de linha
print()

for loja in lojas_geral:
    for i in range(len(loja)):
        print('{:15s}'.format(str(loja[i])), end=" ")
    print()
print()
print("Menores preços: ")
for g in produtos_precos:
    x = menor_valor(g)
    total = total + x[1]
    print(g[0], "  ", lojas[x[0]])
print()
print("Valor total: ")
print("R$ ",round(total, 2))
print("--------------------------")