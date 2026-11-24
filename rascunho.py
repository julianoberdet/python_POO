from rich import print
from rich.panel import Panel
class Churrasco:
    def __init__(self,titulo,qtd):
        self.qtd = qtd
        self.titulo = titulo


    def __str__(self):
        return f"No total são {self.qtd} pessoas"


    def analisar(self):
        precocarne = 82.40
        pessoas_comem = 0.40
        qtd_carne = pessoas_comem * self.qtd
        pagamento_por_pessoa = (precocarne * qtd_carne) / self.qtd
        custo_total = precocarne * qtd_carne
        texto = f"Analisando o [green]{self.titulo}[/] com [blue]{self.qtd} convidados[/]"
        texto += f"\nCada participante comerá {pessoas_comem:.2f}kg e cada kg custa R${precocarne:.2f}"
        texto += f"\nRecomendo [blue]comprar {qtd_carne:.2f}Kg[/] de carne"
        texto += f"\nO custo total será de [green]R${custo_total:.2f}[/]"
        texto += f"\nCada pessoa pagará [yellow]R${pagamento_por_pessoa:.2f}[/] para participar"
        com = Panel(texto,title=f"{self.titulo}",width=70)
        print(com)


c1 = Churrasco("Churras dos Amigos", 5)
c1.analisar()