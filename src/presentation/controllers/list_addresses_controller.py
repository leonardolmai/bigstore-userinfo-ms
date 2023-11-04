from src.domain.use_cases.list_addresses import ListAddressesUseCaseInterface
from src.presentation.schemas.address import AddressOut


class ListAddressesController:
    def __init__(self, use_case: ListAddressesUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self) -> list[AddressOut] | None:
        response = self.__use_case.execute()
        return response
