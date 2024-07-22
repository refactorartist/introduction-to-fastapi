from uuid import UUID

from introduction_to_fastapi.models import Item, ItemCreate, ItemReplace, ItemUpdate


class ItemRepository:
    """
    Simulated data source for managing items.
    This is an overly simplified implementation for demonstration purposes.
    """

    def __init__(self) -> None:
        # This is a dictionary that will store items by their ID
        # The key is the ID of the item and the value is the item itself
        # This should make it easier to retrieve items by their ID

        self.items: dict[UUID, Item] = {}

    # The following methods are used to interact with the data source

    def create(self, item_create: ItemCreate) -> Item:
        """
        Create a new item in the data source.

        Args:
            item (Item): The item to be created.

        Returns:
            Item: The created item if successful
        """

        item = Item(
            **item_create.model_dump()
        )  # Create a new item with the provided values

        self.items[item.id] = item  # Add the item to the data source

        return item

    def read(self, id: UUID) -> Item | None:
        """
        Read an item from the data source.

        Args:
            id (UUID): The ID of the item to be read.

        Returns:
            Item | None: The item if found, None if the item does not exist.
        """
        if not self.exists(id):
            return None

        return self.items[id]

    def read_all(self) -> list[Item]:
        """
        Read all items from the data source.

        Returns:
            list[Item]: A list of all items in the data source.
        """
        return list(self.items.values())

    def update(self, id: UUID, item_update: ItemUpdate) -> Item | None:
        """
        Update an item in the data source.

        Args:
            id (UUID): The ID of the item to be updated.
            item_update (ItemUpdate): The updated values for the item.

        Returns:
            Item | None: The updated item if successful, None if the item does not exist.
        """
        item = self.read(id)  # Retrieve the item

        if item is None:  # Check if the item exists
            return None

        # Update the `item` with the new values
        # This will only update the values that have been set in the `item_update` object

        self.items[id] = item.model_copy(  # Copy the item with the updated values
            update=item_update.model_dump(  # Dump the update values
                exclude_unset=True  # Exclude any value which does not have a value
            )
        )

        return item

    def replace(self, id: UUID, item_replace: ItemReplace) -> Item | None:
        """
        Replace an item in the data source.

        Args:
            id (UUID): The ID of the item to be replaced.
            item (ItemReplace): The new item to replace the existing item.

        Returns:
            Item | None: The replaced item if successful, None if the item does not exist.
        """
        if not self.exists(id):  # Check if the item exists
            return None

        item = Item(id=id, **item_replace.model_dump())

        self.items[id] = item  # Replace the item

        return item

    def delete(self, id: UUID) -> bool:
        """
        Delete an item from the data source.

        Args:
            id (UUID): The ID of the item to be deleted.

        Returns:
            bool: Return True if the item was deleted, False if the item does not exist
        """
        if not self.exists(id):  # Check if the item exists
            return False

        del self.items[id]  # Delete the item
        return True

    def count(self) -> int:
        """
        Get the count of items in the data source.

        Returns:
            int: The count of items in the data source.
        """
        return len(self.items)

    def exists(self, id: UUID) -> bool:
        """
        Check if an item exists in the data source.

        Args:
            id (UUID): The ID of the item to check.

        Returns:
            bool: True if the item exists, False otherwise.
        """
        return id in self.items


# This is a singleton instance of the ItemRepository class
# It will be shared across the entire application
# This is a simple way to manage data in memory
# In a real-world application, you would typically use a database
# This is not a recommended approach for production applications

item_repository = ItemRepository()
