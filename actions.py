from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_map import GameMap
    from actors.entity import Entity


class Action:
    """Base class for all actions using the Command pattern.

    Actions decouple input from behavior and have access to the game_map
    for validation and state changes.
    """
    def perform(self, game_map: GameMap, entity: Entity) -> None:
        """Perform this action with the objects needed to determine its scope.
        This method must be overridden by Action subclasses.

        Args:
            game_map: The game map this action is being performed in.
            entity: The object performing the action.
        """
        raise NotImplementedError()

class MovementAction(Action):
    """Action for moving an entity by a relative offset.

    Validates that the destination is in bounds and walkable before
    performing the move. If validation fails, the action does nothing.
    """
    def __init__(self, dx: int, dy: int):
        super().__init__()
        self.__dx = dx
        self.__dy = dy

    def perform(self, game_map: GameMap, entity: Entity) -> None:
        dest_x = entity.x + self.__dx
        dest_y = entity.y + self.__dy

        if not game_map.in_bounds(dest_x, dest_y):
            return  # Destination is out of bounds
        if not game_map.tiles["walkable"][dest_x, dest_y]:
            return  # Destination is blocked by a tile

        entity.move(self.__dx, self.__dy)

class EscapeAction(Action):
    """Action for exiting the game.

    Raises SystemExit to terminate the application when performed.
    """
    def perform(self, game_map: GameMap, entity: Entity) -> None:
        raise SystemExit()
