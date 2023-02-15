from abc import abstractmethod


class Movivel:
    @abstractmethod
    def esquina(self, direcoes) -> None:
        pass

    @abstractmethod
    def aceitar_movimento(self) -> None:
        pass

    @abstractmethod
    def recusar_movimento(self, direcoes) -> None:
        pass
