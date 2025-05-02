from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from dependencies.auth import (
    get_user,
    get_db,
    authenticate_user,
    get_current_user,
)
from models.token import Token, TokenData
from utils.utils import generate_hash_password
from models.user import UserCreate, UserBase, UserResponse
from models.auth_model import Auths

auth_router = APIRouter()


@auth_router.post("/token", response_model=Token)
def handle_login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username  or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = generate_hash_password(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.post("/signup", response_model=UserResponse)
def handle_signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    hashed_password = generate_hash_password(user.password)
    db_user = Auths(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
