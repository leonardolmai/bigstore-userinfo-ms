from random import random

from factory import Factory, Faker

from src.infrastructure.database.models.card import Card


class CardFactory(Factory):
    class Meta:
        model = Card

    name = Faker("name")
    card_number = Faker("credit_card_number")
    card_number = "".join(str(random.randint(0, 9)) for _ in range(16))
    expiration_month = str(random.randint(1, 12)).zfill(2)
    expiration_year = str(random.randint(2023, 2030))
    cvc = Faker("credit_card_security_code")
