# pylint: disable=abstract-class-instantiated
from src.data.use_cases.update_card import UpdateCardUseCase
from src.infrastructure.database.repositories.card_repository import (
    CardRepository,
)
from src.presentation.controllers.update_card_controller import (
    UpdateCardController,
)
from src.presentation.schemas.card import CardOut


def update_card_composer(session, id, card) -> CardOut | None:
    repository = CardRepository(session)
    use_case = UpdateCardUseCase(repository)
    controller = UpdateCardController(use_case)
    card = controller.handle(id, card)
    return card
