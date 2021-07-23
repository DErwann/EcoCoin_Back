from sqlalchemy import Column, Integer, String

from database import Base


class Image_db(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)

    path_IPFS = Column(String, nullable=False)
    positive_review = Column(Integer, nullable= True)
    negative_review = Column(Integer, nullable= True)
