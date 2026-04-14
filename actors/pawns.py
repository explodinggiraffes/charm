"""Container for player and NPC entities."""

from typing import List

from actors import Entity


class Pawns:
    """A container that holds the player and NPC entities."""

    def __init__(self):
        """Initialize Pawns with default values."""
        self._player = None
        self._npcs = []

    @property
    def player(self) -> Entity:
        """Get the player character entity."""
        return self._player

    @player.setter
    def player(self, value: Entity) -> None:
        self._player = value

    @property
    def npcs(self) -> List[Entity]:
        """Get the list of non-player character entities."""
        return self._npcs

    def add_npc(self, npc: Entity) -> None:
        """Add a non-player character entity to the list of NPCs.

        Args:
            npc: The entity to add to the NPC list.
        """
        self._npcs.append(npc)

    def remove_npc(self, npc: Entity) -> None:
        """Remove a non-player character entity from the list of NPCs.

        If the supplied entity does not exist in the list of NPCs, no action is taken.

        Args:
            npc: The entity to remove from the NPC list.
        """
        try:
            self._npcs.remove(npc)
        except ValueError:
            pass
