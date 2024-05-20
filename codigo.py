
# Resolução Exercício 1 - com for

andar = 0
for i in range(21):
  andar = andar + 1
  if(andar == 13):
    continue
  if(andar == 21):
    break
  print(andar)

# Resolução Exercício 2

andar = 1
while(andar < 21):
  if(andar != 13):
    print(andar)
  andar = andar + 1

# Resolução desafio imprimir em order decrescente:

# usando for
andar = 21
for i in range(21):
  andar = andar - 1
  if(andar == 13):
    continue
  if(andar == 21):
    break
  print(andar)

# usando while
andar = 20
while(andar > 0):
  if(andar != 13):
    print(andar)
  andar = andar - 1

