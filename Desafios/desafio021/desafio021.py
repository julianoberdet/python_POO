from rich import print
class Caneta:
    def __init__(self,cor):
        self.cor = cor
        self.tampa_caneta = True


    def destampar(self):
        self.tampa_caneta = False



    def escrever(self,texto):
        if not self.tampa_caneta:
            if self.cor == "azul":
                print(f"[blue]{texto}[/]",end='')
            elif self.cor == "vermelha":
                print(f"[red]{texto}[/]",end='')
            elif self.cor == "verde":
                print(f"[green]{texto}[/]",end='')
        else:
            print(":prohibited: A [blue]caneta[/] está tampada")



    def quebra_linha(self,qtd):
        for c in range(0,qtd):
            print(f"\n",end='')


c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")


c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem?")
c1.quebra_linha(2)
c2.escrever("Olá Gafanhoto! ")
c3.escrever("Vamos exercitar!")
