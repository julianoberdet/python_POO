#Declaração de classe
class Gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade
    Para criar uma nova pessoa use:
    variavel = gafanhoto(nome, idade)
    """
    def __init__(self, n = "", i = 0):
        #Atributos de instância
        self.nome = n
        self.idade = i

    #Métodos de intância
    def Aniversario(self):
        self.idade += 1


    def __str__(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade"


    def __getstate__(self):
        return f"Estado: nome = {self.nome}, idade {self.idade} "


#Declaração de objetos
g1 = Gafanhoto("Maria",17)
g1.Aniversario()
#print(g1)
print(g1.__dict__) #Dunder Attribute
print(g1.__getstate__()) #Dunder Method
print(g1.__class__) # Mostrar a classe do objeto
print(g1.__doc__) #Para ver as docstrings, ou seja, a documentação de como usar o código
