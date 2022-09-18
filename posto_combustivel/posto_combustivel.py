class BombaCombustivel:
    def __init__(self, tipo_de_combustivel: str, valor_por_litro: float,
                 quantidade_de_combustivel: float) -> None:
        self.__tipo_de_combustivel = tipo_de_combustivel
        self.__valor_por_litro = valor_por_litro
        self.__quantidade_de_combustivel = quantidade_de_combustivel

    def abastecer_por_litro(self, litro: float) -> None:
        self.__quantidade_de_combustivel -= litro

    def abastecer_por_valor(self, valor: float) -> None:
        litros = valor / self.__valor_por_litro
        self.abastecer_por_litro(litros)

    def alterar_valor_por_litro(self, valor: float) -> None:
        self.__valor_por_litro = valor

    def alterar_quantidade_combustivel(self, quantidade: float) -> None:
        self.__quantidade_de_combustivel = quantidade

    def alterar_combustivel(self, combustivel: str) -> None:
        self.__tipo_de_combustivel = combustivel

    def mostrar_status_da_bomba(self) -> None:
        print(self.__tipo_de_combustivel)
        print(self.__valor_por_litro)
        print(self.__quantidade_de_combustivel)
