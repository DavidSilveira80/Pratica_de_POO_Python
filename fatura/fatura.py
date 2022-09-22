class Fatura:
    def __init__(self, numero_do_item: str, descricao: str, quantidade_item: int, preco_unitario: float) -> None:

        self.numero_do_item = numero_do_item
        self. descricao = descricao
        if quantidade_item < 0:
            self.quantidade_item = 0
        if preco_unitario < 0:
            self.preco_unitario = 0.0
        else:
            self.quantidade_item = quantidade_item
            self.preco_unitario = preco_unitario

    def calcula_fatura(self) -> float:
        total = self.quantidade_item * self.preco_unitario
        return total

    def emitir_fatura(self) -> str:
        fatura = f'Produto Nº: {self.numero_do_item}.\nDescrição: ' \
                 f'{self.descricao}.\nQuantidade: ' \
                 f'{self.quantidade_item}.\nPreço unitário: R$ ' \
                 f'{self.preco_unitario:.2f}.\nTotal: R$ ' \
                 f'{self.calcula_fatura():.2f}.'
        return fatura
