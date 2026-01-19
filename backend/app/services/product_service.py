from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..repositories.category_repository import CategoryRepository
from ..repositories.product_repository import ProductRepository
from ..schemas.product import ProductResponse, ProductListResponse


class ProductService:
    def __init__(self, db: Session):
        self.product_repository = ProductRepository(db)
        self.category_repository = CategoryRepository(db)

    def get_all_products(self) -> ProductListResponse | None:
        products = self.product_repository.get_all()
        if not products:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No product has been added yet"
            )
        products_response = [ProductResponse.model_validate(product) for product in products]
        return ProductListResponse(products=products_response, total=len(products_response))

    def get_product_by_id(self, product_id: int) -> ProductResponse | None:
        product = self.product_repository.get_by_id(product_id)

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {product} not found"
            )
        return ProductResponse.model_validate(product)

    def get_products_by_category(self, category_id) -> ProductListResponse | None:
        category = self.category_repository.get_by_id(category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Category with id {category_id} not found"
            )
        products = self.product_repository.get_by_category(category_id)
        products_response = [ProductResponse.model_validate(product) for product in products]
        return ProductListResponse(products=products_response, total=len(products_response))

    def create_product(self, product_data: ProductResponse) -> ProductResponse:
        product = self.product_repository.create(**product_data.model_dump())
        return ProductResponse.model_validate(product)

    def get_multiple_products_by_ids(self, product_ids: List[int]) -> ProductListResponse:
        products = self.product_repository.get_multiple_by_ids(product_ids)
        products_response = [ProductResponse.model_validate(product) for product in products]
        return ProductListResponse(products=products_response, total=len(products_response))
