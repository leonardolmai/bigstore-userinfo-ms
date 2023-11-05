# pylint: disable=abstract-class-instantiated
from src.data.use_cases.list__cards import ListCardsUseCase
from src.infrastructure.database.repositories.card_repository import (
    CardRepository,
)
from src.presentation.controllers.list_card_controller import (
    ListCardController,
)
from src.presentation.schemas.card import CardOut


def list_cards_composer(session) -> list[CardOut] | None:
    repository = CardRepository(session)
    use_case = ListCardsUseCase(repository)
    controller = ListCardController(use_case)
    cards = controller.handle()
    return cards
