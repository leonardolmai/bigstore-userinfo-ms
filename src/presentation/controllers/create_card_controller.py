from src.domain.use_cases.create_card import CreateCardUseCaseInterface
from src.presentation.schemas.card import CardOut


class CreateCardController:
    def __init__(self, use_case: CreateCardUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, card) -> CardOut | None:
        response = self.__use_case.execute(card)
        return response
