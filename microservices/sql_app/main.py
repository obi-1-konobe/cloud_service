from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/")
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.post("/items/{item_id}/indicators", response_model=schemas.Indicator)
def create_indicator_for_item(
    item_id: int, indicator: schemas.IndicatorCreate, db: Session = Depends(get_db)
):
    return crud.create_item_indicator(db=db, indicator=indicator, item_id=item_id)


@app.get("/indicators/", response_model=List[schemas.Indicator])
def read_indicators(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    indicators = crud.get_indicators(db, skip=skip, limit=limit)
    return indicators


@app.get('/items/{item_id}/indicators', response_model=List[schemas.Indicator])
def get_item_indicators(item_id: int, db: Session = Depends(get_db)):
    indicators = crud.get_item_indicators(db=db, item_id=item_id)
    if indicators is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return indicators
