from abc import ABCMeta, abstractmethod


class CaracteristicasPacman(metaclass=ABCMeta):

    @abstractmethod
    def desenhar(self, tela):
        pass

    @abstractmethod
    def calcular_movimentos(self):
        pass

    @abstractmethod
    def processar_cliques_teclado(self, eventos):
        pass
