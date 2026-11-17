class ContaBancaria:
    """
    =============================================================
    Crie uma conta bancária que permite fazer saques e depósitos
    =============================================================
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo


    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo"


    def depositar(self,valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} na conta {self.id} Realizado com sucesso")


    def sacar(self,valor):
        if valor > self.saldo:
            print(f"Saque NEGADO de R${valor:,.2f} na conta {self.id} , Saldo INSUFICIENTE")
        else:
            print(f"Saque de R${valor:.2f} realizado com sucesso na conta {self.id}")
            self.saldo -= valor


c1 = ContaBancaria(833, "Augusto", 3000)
print(c1.__doc__)
c1.depositar(float(input('Qual valor que quer depositar? ')))
print('-' * 40)
c1.sacar(float(input('Qual valor deseja sacar? ')))
print(c1)
