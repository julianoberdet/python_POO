class ContaBancaria:
    """
    =============================================================
    Sistema para ver saldo da conta e realizar depósitos e saques
    =============================================================
    """
    def __init__(self,id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo


    def __str__(self):
        return f"A conta {self.id} do titular {self.titular} tem R${self.saldo:.2f} de saldo"


    def depositar(self,valor):
        self.saldo += valor
        print(f"Depósito na conta {self.id} de R${valor:.2f}  realizado com sucesso")


    def sacar(self,valor):
        if valor > self.saldo:
            print(f"Saque NEGADO de R${valor:.2f}, SALDO INSUFICIENTE")
        else:
            print(f"Saque de R${valor:.2f} na conta {self.id} realizado com sucesso")
            self.saldo -= valor


c1 = ContaBancaria(112, "Juliano", 3000)
print('=' * 30)
print('BANCO FICTICIO'.center(30))
print('=' * 30)
while True:
    print("""Escolha uma opção abaixo:
[1] Ver saldo da conta
[2] Depositar
[3] Sacar
[4] Sair
""")
    print('=' * 30)
    opc = int(input('Qual opção? '))
    if opc == 1:
        print(c1)
    if opc == 2:
         c1.depositar(float(input('Qual valor deseja depositar? ')))
    if opc == 3:
        c1.sacar(float(input('Qual valor deseja sacar? ')))
    if opc == 4:
        print('Muito Obrigado! Volte sempre')
        break
    print('=' * 30)