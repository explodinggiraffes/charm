from typing import Any, Iterable

import tcod
from tcod.context import Context
from tcod.map import compute_fov

from constants import WINDOW_HEIGHT, WINDOW_WIDTH
from graphical_block_characters import GraphicalBlockCharacters as Graphics
from input_handlers import EventHandler
from world import World


class Engine:
    """The main game loop and controller.

    On initialization, the Engine:
    1. Creates the graphics system (tileset loading)
    2. Sets up the console and event handler
    3. Creates a World instance
    4. Creates the dungeon via the World instance (which spawns entities and positions the player)
    5. Handles the game loop: event processing, FOV updates, and rendering
    """
    def __init__(self):
        self._graphics = Graphics()
        self._console = tcod.console.Console(WINDOW_WIDTH, WINDOW_HEIGHT, order="F")
        self._event_handler = EventHandler()

        self._world = World()
        self._world.create_dungeon()

        self.update_fov()
        self.handle_game_loop()

    def handle_game_loop(self) -> None:
        """ Create a window, then handle events and rendering."""
        with tcod.context.new(
            columns=self._console.width, rows=self._console.height, tileset=self._graphics.tileset, title="Charm", vsync=True
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
            action.perform(self._world.current_map, self._world.current_map.player)

            self.update_fov()  # Update the FOV before the player's next action.

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        self._world.current_map.visible[:] = compute_fov(
            self._world.current_map.tiles["transparent"],
            (self._world.current_map.player.x, self._world.current_map.player.y),
            radius=8,
        )
        # If a tile is "visible" it should be added to "explored".
        self._world.current_map.explored |= self._world.current_map.visible

    def render(self, context: Context) -> None:
        """Render the game map and entities within the player's FOV."""
        self._world.current_map.render(self._console)

        for entity in self._world.current_map.entities:
            # Only render entities that are in the FOV.
            #if self._world.current_map.visible[entity.x, entity.y]:  # Re-add this if statement when entities are debugged
            self._console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(self._console)
        self._console.clear()
