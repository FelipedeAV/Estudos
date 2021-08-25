# :rocket: AD2-Fundamentos-da-Programação
:computer: AD2 de Fundamentos da Programação de 2021.1

## 📌Questão 01

( )

Faça um programa, contendo subprogramas, que leia da entrada padrão o nome de um arquivo do tipo texto contendo informações sobre a vacinação da Covid. Mostre inicialmente seu conteúdo. Cada linha possui as seguintes três informações:

nome#vacina#dose

Onde vacina pode ser uma das seis opções a seguir: “Oxford”, “Coronavac”, “Pfizer”, “Sputnik”, “Covax” ou “Jansen”. Produza sete arquivos, sendo que o primeiro deve conter em cada linha os nomes dos cidadãos que receberam duas doses, no formato nome#vacina. Os outros seis arquivos devem conter apenas os nomes dos cidadãos, um por linha, que receberam apenas
uma vacina daquele tipo. Ao final, mostre conteúdo dos sete arquivos produzidos. Suponha que o arquivo original seja consistente e que ninguém tenha tomado uma dose de uma vacina e uma dose de outra. Além disso, ninguém toma a segunda sem ter tomado a primeira vacina.

**Restrição:** Está proibido o uso de listas para manter nomes de pessoas e vacinas, etc. Suas eventuais listas devem possuir no máximo sete elementos. Caso esta restrição não seja respeitada, sua solução perderá 50% do valor da questão. Isto é, toda a massa de informações deve residir em arquivo do tipo texto.

**Teste:**
![Alt text](?raw=true "Optional title")



# 📌Questão 02

(Q2-F)

Faça um programa, contendo subprogramas, que leia da entrada padrão o nome de um arquivo do tipo texto contendo em cada linha o nome de um apostador e oito números diferentes escolhidos por ele no intervalo 0 a 99. Suponha que cada item seja separado pelo caractere “#”. Ou seja:

nome do apostador#n1#n2#n3#n4#n5#n6#n7#n8

Mostre seu conteúdo na saída padrão. Em seguida, leia da entrada padrão uma linha contendo o resultado do sorteio de oito números diferentes, separador por espaço em branco. Ou seja:

res1 res2 res3 res4 res5 res6 res7 res8

Suponha que no arquivo ninguém possa fazer mais que uma aposta.

Processe o arquivo e produza um dicionário (tipo “dict”) onde a chave é o número de acertos 8, 7, 6, 5, 4 ou 3, e o valor é um conjunto (tipo “set”) dos nomes de todos os apostadores com aquele total de acertos.

Caso nenhuma aposta esteja contida no arquivo, escreva a mensagem “Nenhuma Aposta!!!”. Caso contrário, escreva na saída padrão o total de apostas no arquivo e de acertadores de
cada grupo, iniciando com 8 acertos e finalizando com 3 acertos e seus respectivos nomes, ordenados alfabeticamente de forma crescente. Caso ninguém tenha acertado 3 ou mais números, escreva a mensagem “ACUMULOU TUDO”.

**Teste:**
![Alt text](?raw=true "Optional title")



# 📌Questão 03

(Q3-F)

Escreva um programa que faça análises sobre consumos de carros movidos a álcool e a gasolina. Seu programa deve avaliar com carro mais econômico no ano desejado, de acordo
com a quilometragem desejada do carro andar na cidade e na estrada. Segue abaixo todos os detalhes a serem feitos.

A entrada é dada por: (1) um arquivo binário, (2) um arquivo texto e (3) três inteiros, com as seguintes exigências:
(1) Um arquivo binário:
O arquivo binário de nome “carros.bin” é composto por uma sequência de registros formados por duas strings, dois pares de dois pontos flutuantes de precisão dupla e um ponto flutuante de precisão dupla:
Duas strings, onde a primeira ocupa 4 bytes e a segunda ocupa 16 bytes. A primeira string se refere ao ano do carro e a segunda ao modelo do carro;
O primeiro par de pontos flutuantes associa a quantidade de KM por L rodados pelo carro à álcool e a gasolina, respectivamente, na cidade;
O segundo par de pontos flutuantes associa a quantidade de KM por L rodados pelo carro à álcool e a gasolina, respectivamente, na estrada;
O terceiro ponto flutuante associa a quantos litros que há no tanque do carro.

(2) Um arquivo texto:
O arquivo texto de nome “precos_combustiveis.txt” é composto por um par de pontos flutuantes de precisões tripla com os preços do álcool e da gasolina, respectivamente.

(3) Três inteiros:
O primeiro inteiro será o ano referente a consulta a ser feita;
O segundo inteiro será a quilometragem do carro na cidade a ser avaliada;
O terceiro inteiro será a quilometragem do carro na estrada a ser avaliada.

A saída deverá ser em um arquivo “carro_mais_economico.txt” e deve possuir as seguintes informações:

Ano avaliado, o carro mais econômico utilizando somente gasolina e somente álcool no ano desejado, juntamente com o quanto do tanque foi utilizado e o valor gasto para a quilometragem.

**Teste:**
![Alt text](?raw=true "Optional title")

**Obs.: O arquivo .bin aparece no exemplo dessa forma para melhor compreensão da questão.**

**Obs.: Os valores apresentados são meramente ilustrativos. Pode não haver nenhum grande reflexo com a realidade.**


# 📌Questão 04

(Q4-F)

Escreva um programa que computa os preços de um determinado produto juntamente com o frete do mesmo. A entrada contém dois arquivos e uma string: (1) "frete.bin", que consiste de
CEP's, 8 bytes, juntamente do valor do frete do produto; (2) "produto.txt", que consiste das lojas juntamente do valor do produto desejado; (3) string que consiste do CEP onde deseja-se a entrega, que pode estar do formato xx.xxx-xxx, xx.xxx.xxx ou xxxxxxxx.

A saída deve ter na tela a loja que possui o menor preço com o frete e o preço total desse produto. Caso o CEP não exista em frete.bin, então a saída deve ser: "O produto desejado não pode ser entregue neste frete".

**Exemplo**
![Alt text](?raw=true "Optional title")
