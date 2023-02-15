import pygame
from constantes_pacman import BRANCO, PRETO


class Desenhar_fantasma:
    def desenhar(self, tela, cor, coluna, linha, tamanho) -> None:
        # a fatia significa cada quadrado dividido pelo tamanho
        fatia: int = tamanho // 8
        # px == pixel x
        px: int = int(coluna * tamanho)
        # py == pixel y
        py: int = int(linha * tamanho)
        # fazendo o contorno do fantasman com todos os pontos
        contorno: list[tuple] = [(px, py + tamanho),
                                 (px + fatia, py + fatia * 2),
                                 (px + fatia * 2, py + fatia // 2),
                                 (px + fatia * 3, py),
                                 (px + fatia * 5, py),
                                 (px + fatia * 6, py + fatia // 2),
                                 (px + fatia * 7, py + fatia * 2),
                                 (px + tamanho, py + tamanho)]
        pygame.draw.polygon(tela, cor, contorno, 0)

        raio_olho_contorno: int = fatia
        raio_olho_bolinha: int = fatia // 2

        # olho esquerdo
        olho_e_x: int = int(px + fatia * 2.5)
        olho_e_y: int = int(py + fatia * 2.5)
        # olho direito
        olho_d_x: int = int(px + fatia * 5.5)
        olho_d_y: int = int(py + fatia * 2.5)

        # desenhando os olhos
        # olho esquerdo
        pygame.draw.circle(tela, BRANCO, (olho_e_x, olho_e_y),
                           raio_olho_contorno, 0)
        pygame.draw.circle(tela, PRETO, (olho_e_x, olho_e_y),
                           raio_olho_bolinha, 0)

        # olho direito
        pygame.draw.circle(tela, BRANCO, (olho_d_x, olho_d_y),
                           raio_olho_contorno, 0)
        pygame.draw.circle(tela, PRETO, (olho_d_x, olho_d_y),
                           raio_olho_bolinha, 0)
