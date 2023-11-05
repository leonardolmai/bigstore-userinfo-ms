from src.domain.use_cases.update_card import UpdateCardUseCaseInterface
from src.presentation.schemas.card import CardOut


class UpdateCardController:
    def __init__(self, use_case: UpdateCardUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, id, address) -> CardOut | None:
        response = self.__use_case.execute(id, address)
        return response
