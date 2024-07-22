from decimal import Decimal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Item(BaseModel):
    id: UUID = Field(default_factory=uuid4)  # This will generate a random UUID when an object is created
    name: str
    description: str | None = None  # You can also use Optional[str]
    price: Decimal = Field(..., gt=0, decimal_places=2)  # This will ensure that the price is greater than 0


class ItemUpdate(BaseModel):
    name: str | None = None  # You can also use Optional[str]
    description: str | None = None  # You can also use Optional[str]
    price: Decimal | None = Field(None, gt=0, decimal_places=2)  # This will ensure that the price is greater than 0 with 2 decimal places, otherwise it will be none


class ItemCreate(BaseModel):
    name: str
    description: str | None = None  # You can also use Optional[str]
    price: Decimal = Field(..., gt=0, decimal_places=2)  # This will ensure that the price is greater than 0

# This model is used to replace an existing item
# It does not have an ID field because the ID is provided in the path
# We could have simply used `ItemCreate` here, but we are using a separate model for clarity
class ItemReplace(BaseModel):
    name: str
    description: str | None = None  # You can also use Optional[str]
    price: Decimal = Field(..., gt=0, decimal_places=2)  # This will ensure that the price is greater than 0


class ItemResponse(Item):
    ... # This will inherit all the fields from the Item model
        # You can also add more fields if needed


class ItemListResponse(BaseModel):
    items: list[Item]
    total: int


