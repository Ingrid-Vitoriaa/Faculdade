Class graph:
  def __init__(self, vertices):
    #Fazer uma contagem do meu número de vertices
    self.V = vertices #numero total de vertices
    #Celula = casas [u] [v] (Capacidade)
    self.graph = ([0 for _ in range(vertices)] for _ in range(vertices))
  def add_edge(self, u, v, capacidade):
    #Adicinar a nossa aresta direcional/especifica
    self.graph[u][v] = capacidade
    '''
    u = inicio da aresta
    v = fim da aresta
    capacidade = "contagem" das arestas
    '''
  def bfs(self, source, sink, parent)
    #busca por largura
    '''
    source = vertice fonte (caixa d' água)
    sink = vertice somidouro (caixa de água reserva)
    parent = lista de armazenamento para o melhor caminho
    '''
    #Inicializar todos os vertices não visitados
    visited = [False] * self.V
    #cria uma fila para o nosso BFS
    queue = []
    queue.append(source)
    visited[source] = True

   #loop BFS
    while queue:
      u = queue.pop(0)

      for ind, val in enumerate(self.graph[u]):
        if not visited[ind] and val > 0:
          queue.append(ind)
          visited[ind] = True
          parent[ind] = u
      return visted[sink]
    def dfs(self, source, sink, parent):
      visited = [False] * self.V

      stack = [source]
      visited[source] = True

      while stack:
        u = stack.pop(0)

        for ind, val in enumerate(self.graph[u]):
          if not visited[ind] and val > 0:
            stack.append(ind)
            visited[ind] = True
            parent[ind] = u
          if ind == sink:
            return True
      return visted[sink]

    def ford_fulkerson(self, source, sink):
      residual_graph = [row[i] for row in self.graph]
      parent = [-1] * self.V
      # inicio fluxo maximo
      max_flow = 0

      while self.dfs(source, sink, parent):
          path_flow = float("Inf")
          s = sink
          while s != source;
          #atualizar o caminho (fluxo minimo)
          path_flow = min(path_flow, residual_graph[parent[s]][s])
          s = parent[s]
          max_flow += path_flow
          v = sink
          while v != source:
            u = parent[v]
           # Rduzir a capacidade direta do fluxo
           residual_graph[u][v] -= path_flow
           # Aumentar a capacidade reversa
           residual_graph[v][u] += path_flow
           v = parent[v]
      return max_flow

