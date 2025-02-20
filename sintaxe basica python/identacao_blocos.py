def sacar(valor):
  saldo = 500
  if saldo >= valor:
    print("valor sacado!")
    

def depositar(valor):
  saldo = 500
  valor += saldo
  print(valor)
  print("Adicionado ao seu banco")


depositar(100)

sacar(100)