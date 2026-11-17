#Declaração de classe
class Gafanhoto:
    def __init__(self):
        #Atributos de instância
        self.nome = ""
        self.idade = 0

    #Métodos de intância
    def Aniversario(self):
        self.idade += 1


    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade"


#Declaração de objetos
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade = 17
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Mauro"
g2.idade = 53
g2.Aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())