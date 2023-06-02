class ContaBancaria:
    def __init__(self,num_conta,saldo,status,nome,tipo):
        self.conta = num_conta
        self.saldo = saldo
        self.status = True
        self.nome = nome
        self.tipo = tipo

    def depositar(self, valor):
        if self.status == True:
            self.saldo += valor
            print(f"O valor foi depositado no valor de {valor} ")
        else:
            print("A conta está desativada")

    def sacar (self,valor):
        if self.status == True:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque realizado com sucesso no valor de {valor}")
            else:
                print("Saque nao realizado, valor maior que o saldo")
        else:
            print("A conta está desativada")

    def verif_saldo(self):
        if self.status == True:
            print(f"O saldo da conta é {self.saldo}")
        else:
            print(f"A conta está desativada")

    def ativar_conta(self):
        if self.saldo > 0:
            self.status = True
            print("Conta ativada, seu saldo é positivo")
        else:
            print(f"Sua conta deve está zerada")

    def desativar_conta(self):
        if self.saldo == 0:
            self.status = False
            print(f"Conta desativada")
        else:
            print(f"A conta possui saldo, para desativar ela precisa está zerada")


conta1 = ContaBancaria("1234", 100, True, "João Silva", "Corrente")

conta1.desativar_conta()