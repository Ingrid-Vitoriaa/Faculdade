from collections import deque


def BFS(Cr, s, t, n):
    F = deque([s])
    p = [-1] * n
    p[s] = s
    while len(F) > 0:
        v = F.popleft()
        for w in range(n):
            if Cr[v][w] > 0 and p[w] == -1:
                p[w] = v
                if w == t:
                    return p
                F.append(w)
    return p

def fulkerson(C, s, t, n):
    f = [[0] * n for _ in range(n)]
    Cr = [[C[i][j] for j in range(n)] for i in range(n)]
    F = 0


    p = BFS(Cr, s, t, n)


    while p[t] != -1:

        r = float('inf')
        v = t
        while v != s:
            u = p[v]
            r = min(r, Cr[u][v])
            v = u


        F += r


        v = t
        while v != s:
            u = p[v]
            f[u][v] += r
            Cr[u][v] -= r
            f[v][u] -= r
            Cr[v][u] += r
            v = u


        p = BFS(Cr, s, t, n)

    return F, f

n = 6
C = [[0, 16, 13, 0, 0, 0],
     [0, 0, 10, 12, 0, 0],
     [0, 4, 0, 0, 14, 0],
     [0, 0, 9, 0, 0, 20],
     [0, 0, 0, 7, 0, 4],
     [0, 0, 0, 0, 0, 0]]


F, f = fulkerson(C, 0, 5, n)


print("Fluxo máximo:", F)

# crie a matriz adjacência do grafo acima e use o programa para imprimir o fluxo máximo
n = 8
C = [
    #s  #2  #3  #4  #5   #6  #7  #t
    [0, 10, 5,  15,  0,  0,  0,  0], #s
    [0,  0,  4,  0,  9,  15,  0,  0], #2
    [0,  0,  0,  4,  0,  8,  6,  0], #3
    [0,  0,  0,  0,  0,  0,  30,  0], #4
    [0,  0,  0,  0,  0,  0,  15,  10], #5
    [0,  0,  0,  0,  0,  0,  15,  10], #6
    [0,  0,  6,  0,  0,  0,  0,  10], #7
    [0,  0,  0,  0,  0,  0,  0,  0]  #8
  ]
(F, f) = fulkerson(C, 0, 7, n)
print("Fluxo máximo:",F)