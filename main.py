import pygame
from cenario import Cenario
from pacman import Pacman
from fantasma import Fantasma
from constantes_pacman import (PRETO, EIXO_X, EIXO_Y, AMARELO, VERMELHO,
                               ROSA, CIANO)


tela = pygame.display.set_mode((EIXO_X, EIXO_Y), 0)

if __name__ == "__main__":
    tamanho: int = EIXO_Y//30  # dividindo pela quantidade de casas
    pacman: Pacman = Pacman(tamanho)
    fantasma1: Fantasma = Fantasma(AMARELO, tamanho, 15, 12)
    fantasma2: Fantasma = Fantasma(VERMELHO, tamanho, 15, 15)
    fantasma3: Fantasma = Fantasma(ROSA, tamanho, 15, 14)
    fantasma4: Fantasma = Fantasma(CIANO, tamanho, 15, 13)
    cenario: Cenario = Cenario(tamanho, pacman)
    cenario.adiocionar_moviveis(pacman)
    cenario.adiocionar_moviveis(fantasma1)
    cenario.adiocionar_moviveis(fantasma2)
    cenario.adiocionar_moviveis(fantasma3)
    cenario.adiocionar_moviveis(fantasma4)
    while True:
        # limpando o fundo com preto
        tela.fill(PRETO)

        # Calcula as regras (movimentação)
        pacman.calcular_movimentos()
        cenario.calcular_movimentos()
        fantasma1.calcular_movimentos()
        fantasma2.calcular_movimentos()
        fantasma3.calcular_movimentos()
        fantasma4.calcular_movimentos()

        # Pintar a tela

        cenario.desenhar(tela)
        pacman.desenhar(tela)
        fantasma1.desenhar(tela)
        fantasma2.desenhar(tela)
        fantasma3.desenhar(tela)
        fantasma4.desenhar(tela)
        pygame.display.update()
        pygame.time.delay(100)
        # Captura os eventos (cliques)
        eventos = pygame.event.get()
        cenario.processar_cliques_teclado(eventos)
        # Detectando se alguma tecla foi pressionada
        pacman.processar_cliques_teclado(eventos)
        # pacman.processar_cliques_mouse(eventos)
