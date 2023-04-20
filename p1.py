minutos = int(input("Digite a quantidade de minutos"))
if minutos <200:
    conta =0.2*minutos 
    print("f2:", conta)

elif minutos <400:
    conta =0.18 *minutos
    print("f3:", conta)

else:
     conta = 0.15 *minutos
     print("f4:", conta)