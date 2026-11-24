from rich import print
from rich.panel import Panel
class Produto:
    def __init__(self,nome, preco=0):
        self.nome = nome
        self.preco = preco


    def etiqueta(self):
        etiq = Panel(f"{self.nome.center(30)}\n{'-'*30} R${self.preco:.^28.2f}",title = "Produto",width=35)
        print(etiq)

c1 = Produto("Iphone Pro Max 17",23_000.89)
c2 = Produto("Notebook Gamer",8_000)

c1.etiqueta()
c2.etiqueta()