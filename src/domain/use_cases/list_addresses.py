from abc import ABC, abstractmethod

from src.domain.entities.address import Address


class ListAddressesUseCaseInterface(ABC):
    @abstractmethod
    def execute(self) -> list[Address] | None:
        pass
