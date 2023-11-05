from abc import ABC, abstractmethod
from typing import Any

from src.domain.entities.card import Card


class CardRepositoryInterface(ABC):
    @abstractmethod
    def list_cards(self) -> list[Card] | None:
        pass

    @abstractmethod
    def get_card(self, id: int) -> Card | None:
        pass

    @abstractmethod
    def create_card(self, card: Card) -> Card | None:
        pass

    @abstractmethod
    def update_card(self, id: int, update_fields: dict[str, Any]) -> Card | None:
        pass

    @abstractmethod
    def delete_card(self, id: int) -> bool:
        pass
