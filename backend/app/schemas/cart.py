from pydantic import BaseModel, Field


class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Cart item id")
    quantity: int = Field(..., gt=0, description="Item quantity(must be greater than 0)")


# корзина сессионная перекинута во фронтенд
class CartItemCreate(CartItemBase):
    pass


class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="Cart item id")
    quantity: int = Field(..., gt=0, description="Item new quantity(must be greater than 0)")


class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="Product name")
    price: float = Field(..., description="Product price")
    quantity: int = Field(..., description="Quantity in cart")
    subtotal: int = Field(..., description="Total price for this item (price * quantity)")
    image_url: str | None = Field(None, description="Product image URL")


class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="List of items in cart")
    total: float = Field(..., description="Total cart price")
    items_count: int = Field(..., description="Total number of items in cart")
