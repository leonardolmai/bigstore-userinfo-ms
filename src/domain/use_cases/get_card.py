from abc import ABC, abstractmethod

from src.domain.entities.card import Card


class GetCardUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, id: Card) -> Card | None:
        pass
