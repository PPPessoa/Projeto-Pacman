import pygame
from constantes_pacman import (EIXO_X, EIXO_Y,
                               VELOCIDADE)
from movivel import Movivel
from caracteristicas import CaracteristicasPacman
from desenhando_pacman import desenhar_pacman
pygame.init()

# criando a tela do jogo

# criando um tipo de fonte para escrever
# <tipo de fonte>, tamanho, bold, itaclico


class Pacman(CaracteristicasPacman, Movivel):
    def __init__(self, tamanho) -> None:
        self.coluna: int = 1
        self.linha: int = 1
        self.centro_x:  int = EIXO_X//2
        self.centro_y: int = EIXO_Y//2
        self.tamanho: float = tamanho
        self.raio: float = self.tamanho//2
        self.velocidade_x: int = 0
        self.velocidade_y: int = 0
        self.coluna_intencao: int = self.coluna
        self.linha_intencao: int = self.linha
        self.abertura: int = 0
        self.velocidade_abertura = 2

    def calcular_movimentos(self) -> None:
        self.coluna_intencao = self.coluna + self.velocidade_x
        self.linha_intencao = self.linha + self.velocidade_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

    def desenhar(self, tela) -> None:
        # Desenhando o corpo do pacman
        desenhar = desenhar_pacman()
        self.abertura += self.velocidade_abertura
        if self.abertura >= self.raio:
            self.velocidade_abertura = -2
        if self.abertura <= 0:
            self.velocidade_abertura = 2
        desenhar.desenhar(tela, self.centro_x,
                          self.centro_y, self.raio, self.abertura)

    def processar_cliques_teclado(self, eventos):
        # Detectando se alguma tecla foi pressionada
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = VELOCIDADE
                elif e.key == pygame.K_LEFT:
                    self.velocidade_x = -VELOCIDADE
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y = VELOCIDADE
                elif e.key == pygame.K_UP:
                    self.velocidade_y = -VELOCIDADE
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = 0
                elif e.key == pygame.K_LEFT:
                    self.velocidade_x = 0
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y = 0
                elif e.key == pygame.K_UP:
                    self.velocidade_y = 0

    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao

    def esquina(self, direcoes):
        pass

    # para o fantasma precisa dessa def pois ele movimenta sozinho
    def recusar_movimento(self, direcoes):
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna

    # somente para conhecimento pois nao sera usado nesse jogo
    # def processar_cliques_mouse(self, evento):
    #     delay = 50
    #     for e in eventos:
    #         if e.type == pygame.MOUSEMOTION:
    #             mouse_x, mouse_y = e.pos
    #             self.coluna = mouse_x / delay
    #             self.linha = mouse_y / delay
