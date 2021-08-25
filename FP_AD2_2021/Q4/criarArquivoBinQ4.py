import struct
TAM = 17

#Subprogramas

def escrever(arq, CEP, loja, frete):
    arq.write(CEP.encode("iso8859-1"))
    arq.write(loja[:5].ljust(5,chr(0)).encode("iso8859-1"))
    arq.write(struct.pack("f",frete))

def ler(arq):
    CEP = arq.read(8).decode("iso8859-1")
    loja = arq.read(5).decode("iso8859-1").rstrip(chr(0))
    frete = struct.unpack("f", arq.read(4))[0]
    return CEP, loja, frete

#Programa Principal
with open("frete.bin", "w+b") as arq:
    escrever(arq, "00000990", "loja1", 78.90) #chave0
    escrever(arq, "00000990", "loja2", 48.90)  #chave1
    escrever(arq, "00000990", "loja3", 100.20)  # chave2
    escrever(arq, "12300990", "loja1", 78.90)  # chave3
    escrever(arq, "12300990", "loja2", 50.88)  # chave4
    escrever(arq, "12300990", "loja3", 21.90)  # chave5
    arq.seek(5*TAM)
    CEP, loja, frete = ler(arq)
    print(CEP, loja, "%.2f" %frete)