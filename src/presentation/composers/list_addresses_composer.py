from src.data.use_cases.list_addresses import ListAddressessUseCase
from src.infrastructure.database.repositories.address_repository import (
    AddressRepository,
)
from src.presentation.controllers.list_addresses_controller import (
    ListAddressesController,
)
from src.presentation.schemas.address import AddressOut


def list_addresses_composer(session) -> list[AddressOut] | None:
    repository = AddressRepository(session)
    use_case = ListAddressessUseCase(repository)
    controller = ListAddressesController(use_case)
    addresses = controller.handle()
    return addresses
