from datetime import datetime
from pydantic import BaseModel, Field

from .category import CategoryResponse


class ProductBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=200, description="Product's name")
    description: str | None = Field(None, max_length=300, description="Product's description")
    price: float = Field(..., gt=0, description="Product's price(must be greater than 0)")
    category_id: int = Field(..., description="Category's id")
    image_url: str | None = Field(None, description="Product's image url")


class ProductCreate(ProductBase):
    pass


class ProductResponse(BaseModel):
    id: int = Field(..., description="Unique product identifier")
    description: str | None
    price: float
    category_id: int
    created_at: datetime
    category: CategoryResponse = Field(..., description="Product category details")

    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    total: int = Field(..., description="Total number of products")
