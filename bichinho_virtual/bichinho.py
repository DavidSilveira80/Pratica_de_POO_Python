# TODO inplementar classe Tamagushi
"""
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade
b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
Obs: Existe mais uma informação que devemos levar em consideração,
o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde,
ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação
por que ela pode ser calculada a qualquer momento.
"""

class Tamagushi:
    def __init__(self, nome: str, fome: int, saude: int, idade: int) -> None:
        self.nome = nome
        self.fome = fome
        self. saude = saude
        self.idade = idade

    def alterar_nome(self, nome):
        self.nome = nome

    def alterar_fome(self, fome):
        self.fome = fome

    def alterar_saude(self, saude):
        self.saude = saude

    def alterar_idade(self, idade):
        self.idade = idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade
