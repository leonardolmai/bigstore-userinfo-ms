from abc import ABC, abstractmethod

from src.domain.entities.address import Address


class GetAddressUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, id: Address) -> Address | None:
        pass
