def extraLongFactorials(n):
  if n > 100 or n < 1:
    return
  elif n == 1:
    print(numero)
  numero = 0
  j = n - 1
  while(j >= 0):
    if(numero == 0):
        numero += n * j
        j = j - 1
    elif(j != 0):
        numero *= j
        j = j - 1
    else:
      print(numero)
      break

extraLongFactorials(25)