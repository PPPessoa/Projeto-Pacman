import pygame
from constantes_pacman import (
    AZUL, PRETO, AMARELO, P_ESQUERDA, P_BAIXO, P_CIMA, P_DIREITA)
from matriz_cenario import Matriz
from caracteristicas import CaracteristicasPacman
from pacman import Pacman
from fantasma import Fantasma
pygame.init()
fonte: pygame.font.Font = pygame.font.SysFont("arial", 26, True, False)


class Cenario(CaracteristicasPacman):
    def __init__(self, tamanho, pacboy) -> None:
        self.tamanho: int = tamanho
        self.moviveis: list[Pacman] = []
        self.pontos: int = 0
        self.vidas: int = 3
        self.estado: str = "JOGANDO"
        self.pacman: Pacman = pacboy
        self.cenario: Matriz = Matriz()

    def desenhar_infos(self, tela) -> None:
        # quantidades de colunas * tamanho de cada coluna
        pontos_x: int = 30 * self.tamanho
        txt_pontos = fonte.render(
            "Score: {}".format(self.pontos), True, AMARELO)
        tela.blit(txt_pontos, (pontos_x, 50))
        txt_vidas = fonte.render(
            "Vidas: {}".format(self.vidas), True, AMARELO)
        tela.blit(txt_vidas, (pontos_x, 90))

    def pintar_linha(self, tela, numero_linha, linha) -> None:
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna*self.tamanho
            y = numero_linha*self.tamanho
            metade: int = self.tamanho//2
            cor = PRETO
            if coluna == 2:
                cor = AZUL
            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
            if coluna == 1:
                pygame.draw.circle(
                    tela, AMARELO, (x+metade, y+metade), self.tamanho//10, 0)

    def adiocionar_moviveis(self, mov) -> None:
        self.moviveis.append(mov)

    def desenhar(self, tela) -> None:
        if self.estado == "JOGANDO":
            self.desenhar_jogando(tela)
        elif self.estado == "PAUSADO":
            self.desenhar_jogando(tela)
            self.desenhar_pausado(tela)
        elif self.estado == "GAMEOVER":
            self.desenhar_jogando(tela)
            self.desenhar_gameover(tela)
        elif self.estado == "VITORIA":
            self.desenhar_jogando(tela)
            self.desenhar_vitoria(tela)

    def desenhar_vitoria(self, tela) -> None:
        self.desenhar_texto_info(tela, "V I T O R I A")

    def desenhar_pausado(self, tela) -> None:
        self.desenhar_texto_info(tela, "P A U S A D O")

    def desenhar_gameover(self, tela) -> None:
        self.desenhar_texto_info(tela, "G A M E   O V E R")

    def desenhar_texto_info(self, tela, texto) -> None:
        texto_pausa = fonte.render(texto, True, AMARELO)
        texto_x = (tela.get_width() - texto_pausa.get_width())//2
        texto_y = (tela.get_height() - texto_pausa.get_height())//2
        tela.blit(texto_pausa, (texto_x, texto_y))

    def desenhar_jogando(self, tela) -> None:
        for numero_linha, linha in enumerate(self.cenario.matriz):
            self.pintar_linha(tela, numero_linha, linha)
        self.desenhar_infos(tela)

    def defenifir_direcoes(self, linha, coluna) -> list:
        direcoes: list[int] = []
        if self.cenario.matriz[int(linha-1)][int(coluna)] != 2:
            direcoes.append(P_CIMA)
        if self.cenario.matriz[int(linha+1)][int(coluna)] != 2:
            direcoes.append(P_BAIXO)
        if self.cenario.matriz[int(linha)][int(coluna+1)] != 2:
            direcoes.append(P_DIREITA)
        if self.cenario.matriz[int(linha)][int(coluna-1)] != 2:
            direcoes.append(P_ESQUERDA)
        return direcoes

    def calcular_movimentos(self) -> None:
        if self.vidas == 0:
            self.estado = "GAMEOVER"
        if self.estado == "JOGANDO":
            self.calcular_movimentos_jogando()
        elif self.estado == "PAUSADO":
            self.tela_pause()
        elif self.estado == "GAMEOVER":
            self.tela_gameover()

    def tela_gameover(self) -> None:
        pass

    def tela_pause(self) -> None:
        pass

    def calcular_movimentos_jogando(self) -> None:
        for movivel in self.moviveis:
            lin: int = int(movivel.linha)
            col: int = int(movivel.coluna)
            lin_intencao: int = int(movivel.linha_intencao)
            col_intencao: int = int(movivel.coluna_intencao)
            direcoes = self.defenifir_direcoes(lin, col)

            if len(direcoes) >= 3:
                movivel.esquina(direcoes)
            if isinstance(movivel, Fantasma) and movivel.linha == \
                    self.pacman.linha and movivel.coluna == self.pacman.coluna:
                self.vidas -= 1
                self.pacman.coluna = 1
                self.pacman.linha = 1
            if 0 <= col_intencao < 28 and 0 <= lin_intencao < 29 and \
                    self.cenario.matriz[lin_intencao][col_intencao] != 2:
                movivel.aceitar_movimento()
                # vendo se o tipo do movivel é pacman para comer a bolinha
                # para os fantasmas nao comerem as bolinhas
                if isinstance(movivel, Pacman) and \
                        self.cenario.matriz[lin][col] == 1:
                    self.pontos += 1
                    self.cenario.matriz[lin][col] = 0
                    if self.pontos >= 306:
                        self.estado = "VITORIA"
            else:
                movivel.recusar_movimento(direcoes)

    def processar_cliques_teclado(self, eventos) -> None:
        for e in eventos:
            # Detectando se clicou no X para fechar
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    if self.estado == "JOGANDO":
                        self.estado = "PAUSADO"
                    elif self.estado == "PAUSADO":
                        self.estado = "JOGANDO"
