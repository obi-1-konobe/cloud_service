from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User.id, models.User.email).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item.id,
                    models.Item.title,
                    models.Item.description,
                    models.Item.owner_id).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_item_indicator(db: Session, indicator: schemas.IndicatorCreate, item_id: int):
    db_indicator = models.Indicators(**indicator.dict(), device_id=item_id)
    db.add(db_indicator)
    db.commit()
    db.refresh(db_indicator)
    return db_indicator


def get_indicators(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Indicators).offset(skip).limit(limit).all()


def get_item_indicators(db: Session, item_id: int):
    res = db.query(models.Indicators).filter(models.Indicators.device_id == item_id).all()
    return res
