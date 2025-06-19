class Categorias:
    def __init__(self, nome, eh_categoria = True):
        self.nome = nome
        self.eh_categoria = eh_categoria
        self.sub_categorias = []

    def adicionar_sub_categoria(self, sub_categoria):
        self.sub_categorias.append(sub_categoria)

    def exibir_estrutura(self, nivel=0):
      espaco = "     " *  nivel

      print(f"{espaco}{self.nome}/" if self.eh_categoria else f"{espaco}{self.nome}")

      for sub_categoria in self.sub_categorias:
          sub_categoria.exibir_estrutura(nivel + 1)

    def remover_sub_categoria(self, nome_sub_categoria):
        self.sub_categorias = [sub_categoria for sub_categoria in self.sub_categorias if sub_categoria.nome != nome_sub_categoria]

    def buscar_sub_categoria(self, nome_sub_categoria):
        for sub_categoria in self.sub_categorias:
            if sub_categoria.nome == nome_sub_categoria:
                return sub_categoria
        return None

    def listar_sub_categorias(self):
        return [sub_categoria.nome for sub_categoria in self.sub_categorias]

raiz = Categorias("Raiz", True)
cosmeticos = Categorias("Cosméticos", True)
eletrodomesticos = Categorias("Eletrodomésticos", True)
papelaria = Categorias("Papelaria", True)
comida = Categorias("Comida", True)

cosmeticos1 = Categorias("Perfume", False)
eletrodomesticos1 = Categorias("Fogao", False)
eletrodomesticos2 = Categorias("Filtro de Água", False)
eletrodomesticos3 = Categorias("Microondas", False)
papelaria1 = Categorias("Caderno", False)
papelaria2 = Categorias("Lápis", False)
papelaria3 = Categorias("Borracha", False)
comida1 = Categorias("Hambúrger", False)

raiz.adicionar_sub_categoria(cosmeticos)
raiz.adicionar_sub_categoria(eletrodomesticos)
raiz.adicionar_sub_categoria(papelaria)
raiz.adicionar_sub_categoria(comida)

cosmeticos.adicionar_sub_categoria(cosmeticos1)
eletrodomesticos.adicionar_sub_categoria(eletrodomesticos1)
eletrodomesticos.adicionar_sub_categoria(eletrodomesticos2)
eletrodomesticos.adicionar_sub_categoria(eletrodomesticos3)
papelaria.adicionar_sub_categoria(papelaria1)
papelaria.adicionar_sub_categoria(papelaria2)
papelaria.adicionar_sub_categoria(papelaria3)
comida.adicionar_sub_categoria(comida1)

raiz.exibir_estrutura()