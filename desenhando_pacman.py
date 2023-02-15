import pygame
from constantes_pacman import PRETO, AMARELO


class desenhar_pacman:

    def desenhar(self, tela, centro_x, centro_y, raio, abertura) -> None:
        pygame.draw.circle(
            tela, AMARELO, (centro_x, centro_y), raio, 0)
        # Desenhando boca do pacman
        canto_boca: tuple = (centro_x, centro_y)
        labio_superior: tuple = (centro_x+raio, centro_y-abertura)
        labio_inferior: tuple = (centro_x + raio, centro_y+abertura)
        pontos: list = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)

        # Desenhando olho do pacman
        olho_x: int = int(centro_x+raio/6)
        olho_y: int = int(centro_y-raio*0.6)
        olho_raio: int = int(raio/10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)
