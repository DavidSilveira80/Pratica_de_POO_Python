class ContaCorrente:
    def __init__(self, numero_conta: str, nome_correntista: str, saldo: float) -> None:
        self.__numero_conta = numero_conta
        self.__nome_correntista = nome_correntista
        self.__saldo = saldo

    def get_nome_correntista(self) -> str:
        return self.__nome_correntista

    def set_nome_correntista(self, nome) -> None:
        self.__nome_correntista = nome

    def get_numero_conta(self) -> str:
        return self.__numero_conta

    def set_numero_conta(self, numero_conta: str) -> None:
        self.__numero_conta = numero_conta

    def get_saldo(self) -> float:
        return self.__saldo

    def set_saldo(self, saldo: float) -> None:
        self.__saldo = saldo

    def alterar_nome(self, nome: str) -> None:
        self.set_nome_correntista(nome)

    def alterar_numero_conta(self, numero: str) -> None:
        self.set_numero_conta(numero)

    def depositar(self, valor: float) -> None:
        self.__saldo += valor

    def sacar(self, valor: float) -> None:

        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")

    def emitir_extrato(self) -> None:
        print(f'Conta N°: {self.get_numero_conta()}')
        print(f'Correntista: {self.get_nome_correntista()}')
        print(f'Saldo: R$ {self.get_saldo():.2f}.\n')
