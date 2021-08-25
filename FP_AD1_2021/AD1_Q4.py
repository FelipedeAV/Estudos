import math

def lista_pontos(p):
    coord = p.split()
    pontos.append(coord)
    return pontos

def centroide(v_pontos):
    c = []
    xs = []
    ys = []
    x = 0
    y = 0
    for p in pontos:
        xs.append(p[0])
        ys.append(p[1])
    for item in xs:
        x = x + int(item)
    media_x = x / len(xs)
    for item in ys:
        y = y + int(item)
    media_y = y / len(ys)
    c.append(media_x)
    c.append(media_y)
    return c

def calcula_distancia(c, p2, distancias):
    d = math.sqrt((int(p2[0])-c[0])**2+(int(p2[1])-c[1])**2)
    distancias.append([p2, d])
    return distancias

def acha_menor_d(distancias):
    menor_d = distancias[0][1]
    menor_p_d = distancias[0]
    for k in range(len(distancias)):
        if distancias[k][1] < menor_d:
            menor_d = distancias[k][1]
            menor_p_d = distancias[k]
    return menor_p_d

def acha_maoir_d(distancias):
    maior_d = distancias[0][1]
    maior_p_d = distancias[0]
    for k in range(len(distancias)):
        if distancias[k][1] > maior_d:
            maior_d = distancias[k][1]
            maior_p_d = distancias[k]
    return maior_p_d

ponto = input()
if ponto == " ":
    print("Nenhum ponto lido. Portanto, não há centróide.")
pontos = []
distancias = []
while ponto != "":
    lista_pontos(ponto)
    ponto = input()

c = centroide(pontos)
for p in pontos:
    distancias = calcula_distancia(c,p, distancias)

me_d = acha_menor_d(distancias)
ma_d = acha_maoir_d(distancias)

print("-------------------------")
print("Centróide: (", c[0], ", ", c[1], ")")
print("Ponto mais próximo do Centróide: (", me_d[0][0],",",me_d[0][1],")")
print("Ponto mais próximo do Centróide: (", ma_d[0][0],",",ma_d[0][1],")")
print("-------------------------")