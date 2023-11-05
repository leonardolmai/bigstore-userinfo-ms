from src.data.repositories.card_repository import CardRepositoryInterface
from src.domain.entities.card import Card
from src.domain.use_cases.create_card import CreateCardUseCaseInterface


class CreateCardUseCase(CreateCardUseCaseInterface):
    def __init__(self, card_repository: CardRepositoryInterface) -> None:
        self.__card_repository = card_repository

    def execute(self, card: Card) -> Card | None:
        card = self.__card_repository.create_card(card)
        return card
