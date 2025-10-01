from typing import Any, Iterable, Set

import tcod
from tcod.context import Context
from tcod.map import compute_fov

from constants import WINDOW_HEIGHT, WINDOW_WIDTH
from entity import Entity
from game_map import GameMap
from graphical_block_characters import GraphicalBlockCharacters
from input_handlers import EventHandler


class Engine:
    def __init__(self, game_map: GameMap, entities: Set[Entity], player: Entity):
        self.game_map = game_map  # Public so Actions can access the GameMap and its attributes

        self._entities = entities
        self._player = player

        self._char_graphics = GraphicalBlockCharacters()
        self._console = tcod.console.Console(WINDOW_WIDTH, WINDOW_HEIGHT, order="F")
        self._event_handler = EventHandler()

        self.update_fov()
        self.handle_game_loop()

    def handle_game_loop(self) -> None:
        """ Create a window, then handle events and rendering."""
        with tcod.context.new(
            columns=self._console.width, rows=self._console.height, tileset=self._char_graphics.tileset, title="Charm", vsync=True
        ) as context:
            while True:
                self.render(context=context)

                # For a non-blocking event loop replace `tcod.event.wait` with `tcod.event.get`.
                events = tcod.event.wait()
                self.handle_events(events)

    def handle_events(self, events: Iterable[Any]) -> None:
        """Handle game events and update the player's FOV."""
        for event in events:
            action = self._event_handler.dispatch(event)
            if action is None:
                continue
            action.perform(self, self._player)

            self.update_fov()  # Update the FOV before the player's next action.

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self._player.x, self._player.y),
            radius=8,
        )
        # If a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible

    def render(self, context: Context) -> None:
        """Render the game map and entities within the player's FOV."""
        self.game_map.render(self._console)

        for entity in self._entities:
            # Only render entities that are in the FOV.
            if self.game_map.visible[entity.x, entity.y]:
                self._console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(self._console)
        self._console.clear()
