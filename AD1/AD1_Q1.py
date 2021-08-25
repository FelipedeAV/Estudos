import math

distancia = 120000;
distancia_cm = distancia * 10**5;
diametro = 50;
pi = round(math.pi, 3)
#Comprimento da Roda
roda = (2 * pi * (diametro/2))
#Quantidade de voltas que a roda dá
voltas = distancia_cm / roda

mantissa = 0
expoente = 0

#Dividir sucessivamente a quantidade de voltas para descobrir o expoente da potência 10
while voltas > 10 :
    voltas = voltas/10
    mantissa = voltas
    expoente = expoente + 1

if mantissa > 3.16 :
    expoente = expoente + 1

print("Distância percorrida: ", distancia, " km")
print("Diâmetro da roda: ", diametro, " cm")
print("Ordem de grandeza da quantidade de voltas efetuadas: 10 elevado a ", expoente)
#print("Ordem de grandeza da quantidade de voltas efetuadas: ", , "elevado a", )