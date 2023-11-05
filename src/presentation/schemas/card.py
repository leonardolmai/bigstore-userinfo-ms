from pydantic import BaseModel


class CardCreate(BaseModel):
    user_id: int
    postal_code: str
    name: str
    number: str
    expiration_month: str
    expiration_year: str
    cvc: str


class CardUpdate(BaseModel):
    user_id: int | None = None
    postal_code: str | None = None
    name: str | None = None
    number: str | None = None
    expiration_month: str | None = None
    expiration_year: str | None = None
    cvc: str | None = None


class CardOut(BaseModel):
    id: int
    user_id: int
    postal_code: str
    name: str
    number: str
    expiration_month: str
    expiration_year: str
    cvc: str
