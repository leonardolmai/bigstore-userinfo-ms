from src.data.repositories.address_repository import AddressRepositoryInterface
from src.domain.entities.address import Address
from src.domain.use_cases.get_address import GetAddressUseCaseInterface


class GetAddressUseCase(GetAddressUseCaseInterface):
    def __init__(self, user_repository: AddressRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def execute(self, id: str) -> Address | None:
        user = self.__user_repository.get_address(id)
        return user
