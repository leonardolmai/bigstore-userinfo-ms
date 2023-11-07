from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.database.settings.db_connection import get_db
from src.presentation.composers.create_address_composer import (
    create_address_composer,
)
from src.presentation.composers.delete_address_composer import (
    delete_address_composer,
)
from src.presentation.composers.get_address_composer import (
    get_address_composer,
)
from src.presentation.composers.list_addresses_composer import (
    list_addresses_composer,
)
from src.presentation.composers.update_address_composer import (
    update_address_composer,
)
from src.presentation.schemas.address import (
    AddressCreate,
    AddressOut,
    AddressUpdate,
)

router = APIRouter(prefix="/addresses", tags=["addresses"])


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=AddressOut)
def get_address(
    id: int,
    session: Session = Depends(get_db),
):
    address = get_address_composer(session, id)
    if address:
        return address
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="get-address for id, not found."
    )


@router.get(
    "/list/{user_id}", status_code=status.HTTP_200_OK, response_model=list[AddressOut]
)
def list_addresses(user_id: int, session: Session = Depends(get_db)):
    address = list_addresses_composer(user_id, session)
    print(address)
    if address:
        return address
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="List addresses not found."
    )


@router.post(
    "/{user_id}", status_code=status.HTTP_201_CREATED, response_model=AddressOut
)
def create_address(
    user_id: int, address: AddressCreate, session: Session = Depends(get_db)
):
    address = create_address_composer(session, address, user_id)
    if address:
        return address
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Address already exists or not found.",
    )


@router.patch("/update/{id}", status_code=status.HTTP_200_OK, response_model=AddressOut)
def update_address(id: int, address: AddressUpdate, session: Session = Depends(get_db)):
    address = address.model_dump(exclude_unset=True)
    address = update_address_composer(session, id, address)
    if address:
        return address
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Update Address, not found."
    )


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_address(
    id: int,
    session: Session = Depends(get_db),
):
    address = delete_address_composer(session, id)
    if address:
        return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Delete address not found."
    )
