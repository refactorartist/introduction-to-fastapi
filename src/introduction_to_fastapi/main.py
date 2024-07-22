from typing import Any
from uuid import UUID
from fastapi import FastAPI, HTTPException, status

from introduction_to_fastapi.models import (
    Item,
    ItemCreate,
    ItemListResponse,
    ItemReplace,
    ItemResponse,
    ItemUpdate,
)
from introduction_to_fastapi.data import item_repository

app = FastAPI(
    title="Introduction to FastAPI",
    description="This is a simple FastAPI application.",
    version="0.1",
)


@app.get("/")
def root() -> dict[str, Any]:
    return {"message": "Hello, World!"}


@app.get("/items", response_model=ItemListResponse)
def read_items() -> ItemListResponse:
    return ItemListResponse(
        items=item_repository.read_all(), total=item_repository.count()
    )


@app.get("/items/{id}", response_model=ItemResponse)
def read_item(id: UUID) -> Item:
    item = item_repository.read(id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

@app.post("/items", response_model=ItemResponse)
def create_item(item_create: ItemCreate) -> Item:
    item = item_repository.create(item_create)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Item already exists"
        )
    return item

@app.put("/items/{id}", response_model=ItemResponse)
def replace_item(id: UUID, item_replace: ItemReplace) -> Item:
    item = item_repository.replace(id, item_replace)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return item

@app.patch("/items/{id}", response_model=ItemResponse)
def update_item(id: UUID, item_update: ItemUpdate) -> Item:
    item = item_repository.update(id, item_update)

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    
    return item

@app.delete("/items/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id: UUID) -> None:
    is_item_deleted = item_repository.delete(id)

    if not is_item_deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )

    return None
