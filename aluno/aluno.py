class Aluno:

    def __init__(self, matricula: str, nome: str, nota1: float,
                 nota2: float, nota_trabalho: float, media_escolar: float) -> None:
        self.matricula: matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota_trabalho = nota_trabalho
        self.media_escolar = media_escolar

    def media(self) -> float:
        media = ((self.nota1 * 2.5) + (self.nota2 * 2.5) +
                 (self.nota_trabalho * 2)) / (2.5 + 2.5 + 2)
        return media

    def final(self) -> float:
        final = self.media_escolar - self.media()
        return final
