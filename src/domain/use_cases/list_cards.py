from abc import ABC, abstractmethod

from src.domain.entities.card import Card


class ListCardsUseCaseInterface(ABC):
    @abstractmethod
    def execute(self) -> list[Card] | None:
        pass
