#input direto
k = 3
s = "ACGTAG"
t = "ACGGATCGGCATCGT"


print("As substrings com distância no máximo ", k, " do mofit e as posições são:")
print()

posicoes = []
for t_i in range(len(t)-(len(s))+1):
    cont_dif = 0
    pos_i = [t_i+1]
    for s_i in range(len(s)):
        if t[t_i+s_i] != s[s_i]:
            cont_dif += 1
            pos_i.append(s_i+1)
    if cont_dif <= 3:
        posicoes.append(pos_i)

for i in posicoes:
    for k in i:
        print(k, end=" ")
    print()



