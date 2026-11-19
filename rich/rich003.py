from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preços")

tabela.add_column("Nome",justify="center", style="bold blue")
tabela.add_column("Preço",justify="center", style="bold yellow")

tabela.add_row("Lápiz","R$1,50",)
tabela.add_row("Borracha","R$5,00")

print(tabela)