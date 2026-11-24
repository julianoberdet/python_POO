from rich import print
from rich.panel import Panel
class Funcionario:
    """
    =========================================================
    Aqui vejo cadastro de pessoas, seus cargos e seus setores
    =========================================================
    """
    #Atributo de classe
    empresa = "Curso em Vídeo"
    def __init__(self, nome, setor, cargo):
        #Atributo de Intância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    #Metodo de Intância
    def apresentacao(self) -> str:
        return (f":handshake: Olá, sou [blue]{self.nome}[/] se sou {self.cargo} do setor de {self.setor}"
                f" na empresa {Funcionario.empresa}")


    #Estado
    def __getstate__(self):
        pessoa = Panel(f"Nome = [blue]{self.nome}[/]\nSetor = [blue]{self.setor}[/]\n"
                       f"Cargo = [blue]{self.cargo}[/]\nEmpresa = [blue]{Funcionario.empresa}[/]",
                       width=35,style="green", title= "Cadastro de funcionário")
        return pessoa


c1 = Funcionario("Maria","Administração","Diretora")
print(Funcionario.__doc__)
print(c1.apresentacao())


c2 = Funcionario("Cláudio","Ti","Programador senior")
print(c2.apresentacao())
print()
print(c1.__getstate__())
print(c2.__getstate__())
