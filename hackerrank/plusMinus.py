def plusMinus(arr):
  positivo = 0.0
  negativo = 0.0
  zero = 0.0
  for v in arr:
    if v > 0:
      positivo += 1.0
    elif v < 0:
      negativo += 1.0
    else:
      zero += 1.0
  print("{:.5f} \n{:.5f} \n{:.5f}".format(positivo/len(arr),negativo/len(arr),zero/len(arr)))
plusMinus(arr = [1,1,0,-1,-1])