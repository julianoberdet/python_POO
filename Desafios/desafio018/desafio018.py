from rich import print
from rich.panel import Panel
class Churrasco:
    def __init__(self,titulo, qnt=0):
        self.titulo = titulo
        self.qnt = qnt

    def analisar(self):
        consumo = 0.400
        preco = 82.40
        consumo_total = self.qnt * consumo
        total = consumo_total * preco
        pagamento_pessoa = total / self.qnt
        caixa = Panel(f"Analisando [green]{self.titulo}[/] com [blue]{self.qnt} convidados[/]\nCada "
                      f"Participante comerá {consumo}Kg e cada Kg custa R${preco:.2f}\nRecomendo [blue]comprar {consumo_total}Kg[/] de carne"
                      f"\nO custo total será de [green]R${total:.2f}[/]"
                      f"\nCada pessoa pagará [yellow]R${pagamento_pessoa}[/] para participar",
                      title = f"{self.titulo}",width=70)

        print(caixa)


c1 = Churrasco("Churras dos Amigos", 100)
c1.analisar()