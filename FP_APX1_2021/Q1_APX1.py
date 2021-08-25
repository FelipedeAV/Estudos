#Iniciando as variaveis do programa
ultimo = 1
penultimo = 0
contador = 1

#Perguntando para interface quantos degraus tem a escada
degraus = int(input(" "))

#Programa
#A quantidade de maneiras de subir uma escada de n degraus com as condições determinadas obdece uma parte da sequência de Fibonacci.
#Se a quantidade de degraus for menor que zero, não tem escada. Então não entra no programa
if degraus > 0:
      #condição de parada do laço é o contador ser maior que a quantidade de degraus, significa que a pessoa já subiu a escada
      while contador <= degraus:
        maneiras = ultimo + penultimo
        penultimo = ultimo
        ultimo = maneiras
        contador = contador + 1
print("Posso subir a escada de ", degraus, "degraus de ", maneiras, "formas")