from src.domain.use_cases.list_cards import ListCardsUseCaseInterface
from src.presentation.schemas.card import CardOut


class ListCardController:
    def __init__(self, use_case: ListCardsUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self) -> list[CardOut] | None:
        response = self.__use_case.execute()
        return response
