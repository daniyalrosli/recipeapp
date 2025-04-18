from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    ingredients = Column(Text)
    instructions = Column(Text)
    cooking_time = Column(Integer)
    servings = Column(Integer)
    image_url = Column(String, nullable=True)  # For storing image URL

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="recipes")
    comments = relationship("Comment", back_populates="recipe")