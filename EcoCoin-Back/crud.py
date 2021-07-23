from sqlalchemy.orm import Session
import models
import schemas


def get_image(db: Session, image_id: int):
    return db.query(models.Image_db).filter(models.Image_db.id == image_id).first()


def get_images(db: Session, limit: int = 100, skip: int = 0):
    return db.query(models.Image_db).offset(skip).limit(limit).all()


def create_image(db: Session, image: schemas.ImageCreate):
    db_image = models.Image_db(path_IPFS=image.path_IPFS)  # TODO ligne de l'erreur
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image
