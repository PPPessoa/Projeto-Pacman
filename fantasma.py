from caracteristicas import CaracteristicasPacman
from movivel import Movivel
from matriz_cenario import Matriz
from constantes_pacman import (
    P_ESQUERDA, P_BAIXO, P_CIMA, P_DIREITA, VELOCIDADE)
import random
from desenhando_fantasma import Desenhar_fantasma


class Fantasma(CaracteristicasPacman, Movivel):
    def __init__(self, cor, tamanho, linha, coluna) -> None:
        self.cor: tuple = cor
        self.tamanho: int = tamanho
        self.coluna: int = coluna
        self.linha: int = linha
        self.velocidade: int = VELOCIDADE
        self.direcao: int = 0
        self.cenario: Matriz = Matriz()
        self.linha_intencao: int = self.linha
        self.coluna_intencao: int = self.coluna

    def desenhar(self, tela) -> None:
        desenho = Desenhar_fantasma()
        desenho.desenhar(tela, self.cor, self.coluna, self.linha, self.tamanho)

    def calcular_movimentos(self) -> None:
        if self.direcao == P_CIMA:
            self.linha_intencao -= self.velocidade
        if self.direcao == P_BAIXO:
            self.linha_intencao += self.velocidade
        if self.direcao == P_ESQUERDA:
            self.coluna_intencao -= self.velocidade
        if self.direcao == P_DIREITA:
            self.coluna_intencao += self.velocidade

    def processar_cliques_teclado(self, eventos) -> None:
        pass

    def mudar_direcao(self, direcoes) -> None:
        self.direcao = random.choice(direcoes)

    def esquina(self, direcoes) -> None:
        self.mudar_direcao(direcoes)

    def aceitar_movimento(self) -> None:
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao

    # para o fantasma precisa dessa def pois ele movimenta sozinho
    def recusar_movimento(self, direcoes) -> None:
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.mudar_direcao(direcoes)
