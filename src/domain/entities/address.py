from dataclasses import dataclass


@dataclass
class Constraint:
    id: int
    user_id: int


@dataclass
class Address(Constraint):
    postal_code: str
    uf: str
    city: str
    neighborhood: str
    street: str
    number: str
    complement: str
