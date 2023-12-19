import factory
from factory import Faker
from src.infrastructure.database.models.address import Address
from src.infrastructure.database.settings.db_connection import get_db


class AddressFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Address
        sqlalchemy_session = get_db
        sqlalchemy_get_or_create = (
            "postal_coode",
            "uf",
            "city",
            "neighborhood",
            "street",
            "number",
            "complement",
        )

    id = Faker("random_number")
    user_id = Faker("random_number")
    postal_code = Faker("zipcode")
    uf = Faker(
        "random_element",
        elements=(
            "AL",
            "AP",
            "AM",
            "BA",
            "CE",
            "DF",
            "ES",
            "GO",
            "MA",
            "MT",
            "MS",
            "MG",
            "PA",
            "PB",
            "PR",
            "PE",
            "PI",
            "RJ",
            "RN",
            "RS",
            "RO",
            "RR",
            "SC",
            "SP",
            "SE",
            "TO",
        ),
    )
    city = Faker("city")
    neighborhood = Faker("word")
    street = Faker("street_name")
    number = Faker("random_number")
    complement = Faker("sentence")
