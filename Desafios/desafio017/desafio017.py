from rich import print
from rich.panel import Panel


class Produto:
    def __init__(self,nome, preco=0):
        self.nome = nome
        self.preco = preco


    def __str__(self):
        return f"Produto {self.nome} custa R${self.preco:,.2f}"


    def etiqueta(self):
        precof = f"R${self.preco:,.2f}"
        comando = f"{self.nome.center(30," ")}"
        comando += f"{"-" * 30}"
        comando += f"{precof.center(30, '.')}"
        etiqueta = Panel(comando,title ="Produto",width=34,style="blue bold")
        print(etiqueta)

p1 = Produto("Iphone Pro Max 17",23_000.89)
p2 = Produto("Notebook Gamer",8_000)

p1.etiqueta()
p2.etiqueta()