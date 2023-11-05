from abc import ABC, abstractmethod

from src.domain.entities.card import Card


class UpdateCardUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, id, update_fields: dict[str, any]) -> Card | None:
        pass
