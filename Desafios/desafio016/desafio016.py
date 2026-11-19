from rich import print
from rich import inspect

class Funcionario:
    #Atributos de classe
    empresa = "Curso em Video"
    def __init__(self,nome, setor, cargo):
        #Atributos de Instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def apresentacao(self) -> str:
        return (f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} no setor de {self.setor} na empresa"
                f" {self.__class__.empresa}")


c1 = Funcionario("Maria","Administração", "Diretora")
print(c1.apresentacao())
inspect(c1)

c2 = Funcionario("Pedro","TI","Programador")
print(c2.apresentacao())
inspect(c2)

inspect(Funcionario)