from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.database.settings.db_connection import get_db
from src.presentation.composers.create_card_composer import (
    create_card_composer,
)
from src.presentation.composers.delete_card_composer import (
    delete_card_composer,
)
from src.presentation.composers.list_cards_composer import list_cards_composer
from src.presentation.composers.update_card_composer import (
    update_card_composer,
)
from src.presentation.schemas.card import CardCreate, CardOut, CardUpdate

router = APIRouter(prefix="/cards", tags=["cards"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[CardOut])
def list_cards(session: Session = Depends(get_db)):
    cards = list_cards_composer(session)
    if cards:
        return [cards]
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="List cards not found."
    )


@router.get("/me/{id}", status_code=status.HTTP_200_OK, response_model=CardOut)
def get_card(
    id: int,
    session: Session = Depends(get_db),
):
    card = get_card(id, session)
    if card:
        return card
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="get-card for id, not found."
    )


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CardOut)
def create_card(card: CardCreate, session: Session = Depends(get_db)):
    card = create_card_composer(session, card)

    if card:
        return card
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT, detail="Card already exists."
    )


@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=CardOut)
def update_card(id: int, card: CardUpdate, session: Session = Depends(get_db)):
    card = update_card_composer(session, id, card)
    if card:
        return card
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Update Card, not found."
    )


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_card(
    id: int,
    session: Session = Depends(get_db),
):
    card = delete_card_composer(session, id)
    if card:
        return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Delete Card not found."
    )
