# Subprograma

def abrir(arq,arqSaida1,arqSaida2,arqSaida3,arqSaida4,arqSaida5,arqSaida6,arqSaida7):

    openFile = open(arq,'r')
    qtdeDoseTotal = open(arqSaida1,'w+')

    for line in openFile:
        print(line, end="")
        dados = line.strip().split('#')
        nome = dados[0]
        qtd = int(dados[2])
        
        if qtd == 1:
        
            if dados[1] == 'Coronavac':
                with open(arqSaida2,'w') as unicaCoronavac:
                    unicaCoronavac.write(nome + '\n')
        
            if dados[1] == 'Oxford':
                with open(arqSaida3,'w') as unicaOxford:
                    unicaOxford.write(nome + '\n')

            if dados[1] == 'Pfizer':
                with open(arqSaida4,'w') as unicaPfizer:
                    unicaPfizer.write(nome + '\n')

            if dados[1] == 'Sputnik':
                with open(arqSaida5,'w') as unicaSputnik:
                    unicaSputnik.write(nome + '\n')
            
            if dados[1] == 'Covax':
               with open(arqSaida6,'w') as  unicaCovax:
                unicaCovax.write(nome + '\n')
        
            if dados[1] == 'Jansen':
                with open(arqSaida7,'w') as unicaJansen:
                    unicaJansen.write(nome + '\n')

        if qtd > 1:
            qtdeDoseTotal.write(nome + '#' + dados[1] + '\n')


    qtdeDoseTotal.close()
    openFile.close()



def mostra(result):

    file = open(result,'r')
    for item in file:
        print(item,end='')
    print()



#Programa Principal

arquivo = input( ) + '.txt'
doseTotal = 'qtdeDoseTotal.txt'
Coronavac = 'Coronavac.txt'
Oxford = 'Oxford.txt'
Pfizer = 'Pfizer.txt'
Sputnik = 'Sputnik.txt'
Covax = 'Covax.txt'
Jansen = 'Jansen.txt'

abrir(arquivo,doseTotal,Coronavac,Oxford,Pfizer,Sputnik,Covax,Jansen)

print('Vacinados com duas doses em Teste1:')
mostra(doseTotal)

print('Vacinados com uma dose da Coronavac em Teste1:')
mostra(Coronavac)

print('Vacinados com uma dose da Oxford em Teste1:')
mostra(Oxford)

print('Vacinados com uma dose da Pfizer em Teste1:')
mostra(Pfizer)

print('Vacinados com uma dose da Sputnik em Teste1:')
mostra(Sputnik)

print('Vacinados com uma dose da Covax em Teste1:')
mostra(Covax)

print('Vacinados com uma dose da Jansen em Teste1:')
mostra(Jansen)