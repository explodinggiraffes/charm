"""Container for player and NPC entities."""

from typing import List

from actors import Entity


class Pawns:
    """A container that holds the player and NPC entities.

    This class provides a structured alternative to a plain list for
    managing the entities returned by the spawn functions in the
    proc_gen module.

    Attributes:
        player: The player character entity.
        npcs: A list of non-player character entities.
    """

    def __init__(self, player: Entity, npcs: List[Entity]):
        """Initialize Pawns with a player and a list of NPC entities.

        Args:
            player: The entity representing the player character.
            npcs: A list of entities representing non-player characters.
        """
        self._player = player
        self._npcs = npcs

    @property
    def player(self) -> Entity:
        """Get the player character entity."""
        return self._player

    @player.setter
    def player(self, value: Entity) -> None:
        self._player = value
