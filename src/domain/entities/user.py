class Constraint:
    def __init__(
        self,
        id: int,
        user_id: int,
    ) -> None:
        self.id = id
        self.user_id = user_id


class User:
    def __init__(
        self,
        id: int,
        user_id: int,
        name: str,
        email: str,
        password: str,
        phone: str | None = None,
        cpf: str | None = None,
        is_active: bool = True,
    ) -> None:
        super().__init__(id, user_id)
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.cpf = cpf
        self.is_active = is_active
