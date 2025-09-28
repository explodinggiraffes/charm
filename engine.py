from typing import Any, Iterable, Set

import tcod
from tcod.context import Context
from tcod.map import compute_fov
from tcod.tileset import Tileset

from constants import WINDOW_HEIGHT, WINDOW_WIDTH
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler


class Engine:
    def __init__(self, game_map: GameMap, tileset: Tileset, entities: Set[Entity], player: Entity):
        self.entities = entities
        self.game_map = game_map
        self.tileset = tileset
        self.player = player

        self.console = tcod.console.Console(WINDOW_WIDTH, WINDOW_HEIGHT, order="F")

        self.event_handler = EventHandler()

        self.update_fov()
        self.handle_game_loop()

    def handle_game_loop(self) -> None:
        """ Create a window, then handle events and rendering."""
        with tcod.context.new(
            columns=self.console.width, rows=self.console.height, tileset=self.tileset, title="Charm", vsync=True
        ) as context:
            while True:
                self.render(context=context)

                # For a non-blocking event loop replace `tcod.event.wait` with `tcod.event.get`.
                events = tcod.event.wait()
                self.handle_events(events)

    def handle_events(self, events: Iterable[Any]) -> None:
        """Handle game events and update the player's FOV."""
        for event in events:
            action = self.event_handler.dispatch(event)
            if action is None:
                continue
            action.perform(self, self.player)

            self.update_fov()  # Update the FOV before the player's next action.

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8,
        )
        # If a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible

    def render(self, context: Context) -> None:
        """Render the game map and entities within the player's FOV."""
        self.game_map.render(self.console)

        for entity in self.entities:
            # Only render entities that are in the FOV.
            if self.game_map.visible[entity.x, entity.y]:
                self.console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(self.console)
        self.console.clear()
