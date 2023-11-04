from src.data.use_cases.delete_address import DeleteAddressUseCase
from src.infrastructure.database.repositories.address_repository import (
    AddressRepository,
)
from src.presentation.controllers.create_address_controller import (
    CreateAddressController,
)
from src.presentation.schemas.address import AddressOut


def delete_address_composer(session, address) -> AddressOut | None:
    repository = AddressRepository(session)
    use_case = DeleteAddressUseCase(repository)
    controller = CreateAddressController(use_case)
    address = controller.handle(address)
    return address
