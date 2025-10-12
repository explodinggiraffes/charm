from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from actors.entity import Entity


class Action:
    def perform(self, engine: Engine, entity: Entity) -> None:
        """Perform this action with the objects needed to determine its scope.
        This method must be overridden by Action subclasses.

        Args:
          engine: The scope this action is being performed in.
          entity: The object performing the action.
        """
        raise NotImplementedError()

class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()
        self.__dx = dx
        self.__dy = dy

    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.__dx
        dest_y = entity.y + self.__dy

        if not engine.game_map.in_bounds(dest_x, dest_y):
            return  # Destination is out of bounds
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return  # Destination is blocked by a tile

        entity.move(self.__dx, self.__dy)

class EscapeAction(Action):
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()
