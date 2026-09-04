from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.models.product import Product
from app.dependencies.database import get_db

#prefix="/api/products"

#means that any endpoint we create in this router will start with:

#/api/products


#tags=["Products"]
#will group these endpoints under Products in Swagger.

router = APIRouter(
    prefix="/api/products",
    tags=["Products"]
)

@router.post("/",response_model=ProductResponse)
def create_product(
    product:ProductCreate,
    db: Session= Depends(get_db)
):
    new_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        discount_price=product.discount_price,
        stock=product.stock,
        image_url=product.image_url,
        is_active=product.is_active
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

@router.get("/",response_model=list[ProductResponse])
def get_products(
    db: Session = Depends(get_db)
):
    products = db.query(Product).all()

    return products

@router.get("/{product_id}",response_model=ProductResponse)
def get_product_by_id(product_id : int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product

@router.put("/{product_id}",response_model=ProductResponse)
def update_product(product_id : int, product : ProductUpdate, db : Session = Depends(get_db)):
    existing_product = db.query(Product).filter(Product.id == product_id).first()

    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")

    update_data = product.model_dump(exclude_unset=True)#Give me only the fields the user actually sent.

    for field, value in update_data.items():
        setattr(existing_product, field, value)

    db.commit()
    db.refresh(existing_product)

    return existing_product


@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    db.delete(product)
    db.commit()

    return {
        "message": "Product deleted successfully"
    }