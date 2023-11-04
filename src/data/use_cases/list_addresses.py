from src.data.repositories.address_repository import AddressRepositoryInterface
from src.domain.entities.address import Address
from src.domain.use_cases.list_addresses import ListAddressesUseCaseInterface


class ListAddressessUseCase(ListAddressesUseCaseInterface):
    def __init__(self, user_repository: AddressRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def execute(self) -> list[Address] | None:
        users = self.__user_repository.list_address()
        return users
