
class Conta: #construindo um objeto

    def __init__(self,nome,saldo,limite):
        self._nome = nome
        self._saldo = saldo
        self._limite = limite
      #criando os métodos
    def extrato(self):
       print(f"O saldo do titular {self._nome} foi de {self._saldo}")
    def depositar(self,valor):
        if (valor > self._limite):
            print("Depósito não autorizando, Ultrapassou o limite da conta")
        else:
            print("deposito autorizado\n")
            self._saldo += valor

    def sacar(self,valor):
       if(valor > 0 and valor <= self._saldo):
           self._saldo -= valor
           print("Saque autorizado")

       else:
           print("Nao pudemos efetuar seu saque")