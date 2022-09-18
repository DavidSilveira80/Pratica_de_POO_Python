class Elevador:
    def __init__(self, andar=0, numero_de_andares=7, capacidade_do_elevador=10, pessoas_no_elevador=0) -> None:
        self.andar = andar
        self.numero_de_andares = numero_de_andares
        self.capacidade_do_elevador = capacidade_do_elevador
        self.pessoas_no_elevador = pessoas_no_elevador

    def inicializa(self) -> None:
        self.andar = 0
        self.pessoas_no_elevador = 0

    def entra(self, pessoas: int) -> None:
        if self.verifica_espaco_no_elevador(pessoas):
            self.pessoas_no_elevador += pessoas
        else:
            print("Não há lugar no elevador.")

    def verifica_espaco_no_elevador(self, pessoas: int) -> bool:
        if pessoas < self.pessoas_no_elevador and self.pessoas_no_elevador < self.capacidade_do_elevador:
            espaco = True
        else:
            espaco = False
        return espaco
