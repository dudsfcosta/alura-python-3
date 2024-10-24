from modelos.cardapio.itemCardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
        self._descricao = descricao

    def aplicar_desconto(self):
        pass

    def __str__(self):
        return self._nome
