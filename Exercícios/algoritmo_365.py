num = []
valor = []
destino = []
data = []

for i in range(20):
    k = str(input("\nNúmero do cheque: "))
    num.append(k)
    
    k = str(input("\nValor do cheque: "))
    valor.append(k)
    
    k = str(input("\nData do cheque ddmmaa: "))
    data.append(k)
    
    k = str(input("\nDestino do cheque: "))
    destino.append(k)

print("\nRelação dos Cheques")

for i,(cheque1,cheque2,cheque3,cheque4) in enumerate(zip(num,valor,destino,data)):
    print(f"\nNúmero do cheque: {cheque1}")
    print(f"Valor do cheque: {cheque2}")
    print(f"Data do cheque: {cheque3}")
    print(f"Destino do cheque: {cheque4}")
    


