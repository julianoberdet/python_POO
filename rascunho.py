from rich import print
from rich.panel import Panel
class Funcionario:
    """
    =========================================================
    Aqui vejo cadastro de pessoas, seus cargos e seus setores
    =========================================================
    """
    empresa = "Curso em Vídeo"
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f":handshake: Olá, sou [blue]{self.nome}[/] se sou {self.cargo} do setor de {self.setor} na empresa {Funcionario.empresa}"


    def __getstate__(self):
        pessoa = Panel(f"[blue]Nome = {self.nome}\nSetor = {self.setor}\nCargo = {self.cargo}\nEmpresa = {Funcionario.empresa}[/]",width=49,style="green", title= "Cadastro de funcionário")
        return pessoa



c1 = Funcionario("Maria","Administração","Diretora")
print(Funcionario.__doc__)
print(c1.apresentacao())

c2 = Funcionario("Cláudio","Ti","Programador senior")
print(c2.apresentacao())
print(c1.__getstate__())
print(c2.__getstate__())
