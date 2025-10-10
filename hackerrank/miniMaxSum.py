def miniMaxSum(arr):
  min = 0
  max = 0
  for i in range(1,len(arr)):
    max += arr[i]
  for i in range(0,len(arr) - 1):
    print(arr[i])
    min += arr[i]
  print(min,max)

abc([1,2,3,4,5])