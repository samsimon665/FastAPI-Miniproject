from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.crud import user as user_crud


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db, user)


@router.get(
    "/",
    response_model=List[UserResponse]
)
def get_users(db: Session = Depends(get_db)):
    return user_crud.get_users(db)


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_crud.get_user_by_id(db, user_id)


@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    return user_crud.update_user(db, user_id, user_update)


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_crud.delete_user(db, user_id)
    return None
