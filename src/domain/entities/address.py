from dataclasses import dataclass


class Constraint:
    def __init__(
        self,
        id: int,
        user_id: int,
    ) -> None:
        self.id: id
        self.user_id: user_id


@dataclass
class Address(Constraint):
    postal_code: str
    uf: str
    city: str
    neighborhood: str
    street: str
    number: str
    complement: str
