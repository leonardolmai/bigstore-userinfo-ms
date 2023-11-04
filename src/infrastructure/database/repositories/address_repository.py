from typing import Any

from sqlalchemy.orm import Session

from src.data.repositories.address_repository import AddressRepositoryInterface
from src.domain.entities.address import Address
from src.infrastructure.database.models.address import Address as AddressModel


class AddressRepository(AddressRepositoryInterface):
    def __init__(self, session: Session):
        self.session: Session = session

    def list_address(self) -> list[Address] | None:
        try:
            return self.session.query(AddressModel).all()
        except:
            return None

    def get_address(self, id: int) -> Address | None:
        try:
            return (
                self.session.query(Address).filter(AddressModel.id == id).one_or_none()
            )
        except:
            return None

    def create_address(self, address: Address) -> Address | None:
        try:
            address_data = {
                "user_id": address.user_id,
                "postal_code": address.postal_code,
                "uf": address.uf,
                "city": address.city,
                "neighborhood": address.neighborhood,
                "number": address.number,
                "complement": address.complement,
            }
            address_model = AddressModel(**address_data)

            self.session.add(address_model)
            self.session.commit()

            return address_model
        except:
            return None

    def update_address(self, id: int, update_fields: dict[str, Any]) -> Address | None:
        try:
            self.session.query(AddressModel).filter(AddressModel.id == id).update(
                update_fields
            )
            self.session.commit()
            user_updated = self.get_address(id)

            return user_updated
        except:
            return None

    def delete_address(self, id: int) -> bool:
        try:
            self.session.query(AddressModel).filter(AddressModel.id == id).delete()
            self.session.commit()
            return True
        except:
            return False
