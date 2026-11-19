from rich import print
from rich.panel import Panel
class Produto:
    def __init__(self,nome, preco=0):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        caixa  = Panel(f"{self.nome.center(30)} \n{'-' * 30}\n..........R${self.preco:.2f}.........."
                       ,title = "Produto",width=35)
        print(caixa)

p1 = Produto("Iphone Pro Max",25_000.85)
p2 = Produto("Notebook Gamer",8_000)

p1.etiqueta()
p2.etiqueta()