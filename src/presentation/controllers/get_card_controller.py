from src.domain.use_cases.get_card import GetCardUseCaseInterface
from src.presentation.schemas.card import CardOut


class GetCardController:
    def __init__(self, use_case: GetCardUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, id: int) -> CardOut | None:
        response = self.__use_case.execute(id)
        return response
