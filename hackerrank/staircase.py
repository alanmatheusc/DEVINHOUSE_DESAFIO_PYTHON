def staircase(n):
  for i in range(n + 1):
    s = "#" * i
    print(s.rjust(n))
staircase(4)