from typing import Tuple

# Note:
# - Subclasses of Entity will be implemented here.
# - Graphical block characters used in roguelikes:
#   https://www.reddit.com/r/roguelikedev/comments/2fxaks/a_compendium_of_ascii_characters_across_roguelikes/


class Entity:
    """A generic object to represent players, enemies, items, etc."""
    def __init__(self, char: str, color: Tuple[int, int, int], x: int, y: int):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy
