import string

from pydantic import BaseModel


class ImageBase(BaseModel):
    path_IPFS: str


class ImageCreate(ImageBase):
    pass


class Image(ImageBase):
    id: int

    class Config:
        orm_mode = True
