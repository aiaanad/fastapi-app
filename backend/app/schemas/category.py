from datetime import datetime
from pydantic import BaseModel, Field
from typing import Annotated


class CategoryBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100, description="Category name")
    slug: str = Field(..., min_length=5, max_length=100, description="Category slug")


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int = Field(..., description="Unique category identifier")

    class Config:
        form_attributes = True
