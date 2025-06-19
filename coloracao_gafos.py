def toGrid(n):
  return (n // 9, n % 9)
def toV(g):
  return g[0] * 9 + g[1]
def conect(v1, v2):
  g1 = toGrid(v1)
  g2 = toGrid(v2)
  if g1[0] == g2[0] or g1[1] == g2[1]:
    return True
  if g1[0] // 3 == g2[0] // 3 and g1[1] // 3 == g2[1] // 3:
    return True
  return False
V = [i for i in range(81)]
L = {i: [] for i in range(81)}
for i in range(80):
  for j in range(i+1, 81):
    if conect(i, j):
      L[i].append(j)
      L[j].append(i)
print(L)
cor = [0] * 81
cor[toV((0, 3))] = 7
cor[toV((0, 4))] = 9
cor[toV((0, 5))] = 8
cor[toV((0, 7))] = 4
cor[toV((0, 8))] = 2
cor[toV((1, 1))] = 7
cor[toV((1, 2))] = 8
cor[toV((1, 6))] = 6
cor[toV((1, 8))] = 3
cor[toV((2, 0))] = 1
cor[toV((2, 1))] = 4
cor[toV((2, 4))] = 6
cor[toV((2, 5))] = 3
cor[toV((2, 7))] = 7
cor[toV((2, 8))] = 8
cor[toV((3, 0))] = 5
cor[toV((3, 1))] = 6
cor[toV((3, 2))] = 4
cor[toV((3, 4))] = 8
cor[toV((3, 7))] = 3
cor[toV((3, 8))] = 1
cor[toV((4, 0))] = 8
cor[toV((4, 4))] = 2
cor[toV((4, 5))] = 1
cor[toV((4, 6))] = 5
cor[toV((4, 8))] = 4
cor[toV((5, 3))] = 6
cor[toV((5, 5))] = 4
cor[toV((5, 7))] = 9
cor[toV((6, 0))] = 3
cor[toV((6, 2))] = 5
cor[toV((6, 3))] = 2
cor[toV((6, 6))] = 7
cor[toV((7, 0))] = 4
cor[toV((7, 2))] = 6
cor[toV((7, 3))] = 8
cor[toV((7, 4))] = 7
cor[toV((7, 5))] = 9
cor[toV((7, 7))] = 1
cor[toV((8, 0))] = 7
cor[toV((8, 1))] = 8
cor[toV((8, 3))] = 1
cor[toV((8, 4))] = 3
cor[toV((8, 6))] = 4
cor[toV((8, 7))] = 2
cor[toV((8, 8))] = 6
def printSuduku(cor):
  for i in range(9):
    print("+-" * 9 + "+")
    for j in range(9):
      print("|", end = "")
      if cor[toV((i, j))] > 0:
        print(cor[toV((i, j))], end = "")
      else:
        print(" ", end = "")
    print("|")
  print("+-" * 9 + "+")

def greedy(cor):
  for i in range(9):
    for j in range(9):
      if cor[toV((i, j))] == 0:
        k = 1
        vizinhos = L[toV((i, j))]
        valores_vizinhos = [cor[i] for i in vizinhos]

        while k in valores_vizinhos:
          k += 1

        cor[toV((i, j))] = k

  return cor

cor = greedy(cor)
printSuduku(cor)