from factory import Factory, Faker
import random

from src.infrastructure.database.models.address import Address


class AddressFactory(Factory):
    class Meta:
        model = Address

    name = Faker("name")

    # Generate random address-related fields
    postal_code = "".join(str(random.randint(0, 9)) for _ in range(8))
    uf = Faker("state_abbr")
    city = Faker("city")
    neighborhood = Faker("city_suffix")
    street = Faker("street_name")
    number = Faker("building_number")
    complement = Faker("secondary_address")
