def birthdayCakeCandles(candles):
  c = 0
  v = 1
  count = []
  candles.sort()
  for c in range(c,len(candles)):
    for v in range(v,len(candles)):
     if(candles[c] < candles[v]):
      c = v
      v+=1
  for i in range(0,len(candles)):
    if(candles[i] == candles[c]):
      count.append(candles[i])
  return(len(count))

birthdayCakeCandles([82, 49, 82, 82, 41, 82, 15, 63, 38, 25])