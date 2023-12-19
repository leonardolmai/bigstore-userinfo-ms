from src.data.use_cases.delete_address import DeleteAddressUseCase
from src.infrastructure.database.repositories.address_repository import (
    AddressRepository,
)
from src.presentation.controllers.delete_address_controller import (
    DeleteAddressController,
)
from src.presentation.schemas.address import AddressOut


def delete_address_composer(session, id: int) -> AddressOut | None:
    repository = AddressRepository(session)
    use_case = DeleteAddressUseCase(repository)
    controller = DeleteAddressController(use_case)
    address = controller.handle(id)
    return address
