MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("informe sua idade: "))

if idade >= MAIOR_IDADE:
  print("Maior de idade, pode tirar sua CNH")

if idade < MAIOR_IDADE:
  print("Ainda nao pode tirar a CNH")


if idade >= MAIOR_IDADE:
  print("Maior de idade, pode tirar sua CNH")
else: 
  print("Ainda nao pode tirar a CNH")


if idade >= MAIOR_IDADE:
  print("Maior de idade, pode tirar sua CNH")
elif idade == IDADE_ESPECIAL:
  print("Pode fazer a aula teorica mas nao pode fazer a aula pratica")
else: 
  print("Ainda nao pode tirar a CNH")


