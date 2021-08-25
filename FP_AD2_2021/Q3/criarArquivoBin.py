import struct
TAM = 40

#Subprogramas

def escrever(arq, ano, modelo, AlcoolKMCidade, GasolinaKMCidade, AlcoolKMEstrada, GasolinaKMEstrada, tanque):
    arq.write(ano.encode("utf-8"))
    arq.write(modelo[:16].ljust(16,chr(0)).encode("utf-8"))
    arq.write(struct.pack("f",AlcoolKMCidade))
    arq.write(struct.pack("f", GasolinaKMCidade))
    arq.write(struct.pack("f", AlcoolKMEstrada))
    arq.write(struct.pack("f", GasolinaKMEstrada))
    arq.write(struct.pack("f", tanque))

def ler(arq):
    ano = arq.read(4).decode("utf-8")
    modelo = arq.read(16).decode("utf-8").rstrip(chr(0))
    AlcoolKMCidade = struct.unpack("f", arq.read(4))[0]
    GasolinaKMCidade = struct.unpack("f", arq.read(4))[0]
    AlcoolKMEstrada = struct.unpack("f", arq.read(4))[0]
    GasolinaKMEstrada = struct.unpack("f", arq.read(4))[0]
    tanque = struct.unpack("f", arq.read(4))[0]
    return ano, modelo, AlcoolKMCidade, GasolinaKMCidade, AlcoolKMEstrada, GasolinaKMEstrada, tanque

#Programa Principal
with open("carros2.bin", "w+b") as arq:
    escrever(arq, "2017", "Duster", 7, 7, 10, 11, 50) #chave0
    escrever(arq, "2018", "Kwid", 7, 9, 12, 13, 48)  #chave1
    escrever(arq, "2017", "Aircross", 7, 8, 11, 12, 50)  # chave3
    escrever(arq, "2018", "Stepway", 8, 12, 10, 14, 50)  # chave4
    arq.seek(0*TAM)
    ano, modelo, AlcoolKMCidade, GasolinaKMCidade, AlcoolKMEstrada, GasolinaKMEstrada, tanque = ler(arq)
    print(ano, modelo, "%.2f" %AlcoolKMCidade, "%.2f" %GasolinaKMCidade, "%.2f" %AlcoolKMEstrada, "%.2f" %GasolinaKMEstrada, "%.2f" %tanque)