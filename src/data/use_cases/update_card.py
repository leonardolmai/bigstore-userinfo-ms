from typing import Any

from src.data.repositories.card_repository import CardRepositoryInterface
from src.domain.entities.card import Card
from src.domain.use_cases.update_card import UpdateCardUseCaseInterface


class UpdateCardUseCase(UpdateCardUseCaseInterface):
    def __init__(self, card_repository: CardRepositoryInterface) -> None:
        self.__card_repository = card_repository

    def execute(self, id, update_fields: dict[str, Any]) -> Card | None:
        card = self.__card_repository.update_card(id, update_fields)
        return card
