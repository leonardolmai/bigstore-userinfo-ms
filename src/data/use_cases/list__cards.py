from src.data.repositories.card_repository import CardRepositoryInterface
from src.domain.entities.card import Card
from src.domain.use_cases.list_cards import ListCardsUseCaseInterface


class ListCardsUseCase(ListCardsUseCaseInterface):
    def __init__(self, card_repository: CardRepositoryInterface) -> None:
        self.__card_repository = card_repository

    def execute(self) -> list[Card] | None:
        users = self.__card_repository.list_cards()
        return users
