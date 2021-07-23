from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
from database import SessionLocal, engine, Base

# models.Base.metadata.create_all(bind=engine)
Base.metadata.create_all(bind=engine)
app = FastAPI()


# TODO Check pour quoi on a un typeError: 'path_ipfs' is an invalid keyword for Image

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/new_image/", response_model=schemas.Image)
async def create_image(image_in: schemas.ImageCreate, db: Session = Depends(get_db)):
    return crud.create_image(db=db, image=image_in)


@app.get("/images", response_model=List[schemas.Image])
async def read_images(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    images = crud.get_images(db, skip=skip, limit=limit)
    return images


@app.get("/images/{image_id}", response_model=schemas.Image)
async def read_image(image_id: int, db: Session = Depends(get_db)):
    db_image = crud.get_image(db=db, image_id=image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return db_image
