class Pessoa:
    def __init__(self, nome: str, ano_nasc: int, altura: float) -> None:
        self.__nome = nome
        self.__ano_nasc = ano_nasc
        self.__altura = altura

    def get_nome(self)-> str:
        return self.__nome

    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def get_ano_nasc(self) -> int:
        return self.__ano_nasc

    def set_ano_nasc(self, ano_nasc: int) -> None:
        self.__ano_nasc = ano_nasc

    def get_altura(self) -> float:
        return self.__altura

    def set_altura(self, altura: float) -> None:
        self.__altura = altura

    def imprimir_dados(self) -> None:
        print(self.get_nome())
        print(self.get_ano_nasc())
        print(self.get_altura())

    def calcular_idade(self, ano_atual: int) -> int:
        return ano_atual - self.__ano_nasc
