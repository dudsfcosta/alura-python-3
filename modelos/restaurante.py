from modelos.avaliacao import Avaliacao
from modelos.cardapio.itemCardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() # .title mantém a primeira letra como maiúscula
        self._categoria = categoria
        self._ativo = False # o atributo é protegido, mas não é privado
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)}| {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._name.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)}| {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        else:
            sum_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            qtd_notas = len(self._avaliacao)
            avg_notas = round(sum_notas/qtd_notas, 1)
            return avg_notas

    # def adicionar_bebida_no_cardapio(self, bebida):
        # self._cardapio.append(bebida)

    # def adicionar_prato_no_cardapio(self, prato):
        # self._cardapio.append(prato)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio,start=1):
            # print(item)
            # print(type(item))
            # if hasattr(item, '_descricao'):
                # print(item._descricao)
            if hasattr(item,'_descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item._descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)
