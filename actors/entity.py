from typing import Tuple

# NOTE: Subclasses of Entity will be implemented here.


class Entity:
    """A generic object to represent players, enemies, items, etc."""
    def __init__(self, *, char: str, color: Tuple[int, int, int], x: int, y: int):
        """Initialize an Entity with a visual representation and map position.

        Args:
            char: The character used to represent this entity on the map.
            color: The RGB color tuple used to render the entity's character.
            x: The initial column position of the entity on the map.
            y: The initial row position of the entity on the map.
        """
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, *, dx: int, dy: int) -> None:
        """Move the entity by a relative offset.

        Args:
            dx: The number of columns to move (positive = right, negative = left).
            dy: The number of rows to move (positive = down, negative = up).
        """
        self.x += dx
        self.y += dy
