N = int(input())
for i in range(1, 2 ** N):
  sequence = []
  for j in range(N):
    if i & (1 << j):
      sequence.append(j + 1)
  print(" ".join(str(x) for x in sequence))


