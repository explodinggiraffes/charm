# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Charm is a roguelike game built with Python using the TCOD library. The game features dungeon generation, field of view (FOV) calculations, and entity management using a traditional roguelike architecture.

## Development Setup

### Prerequisites (macOS)
```bash
# Install SDL2 libraries
brew install SDL2 SDL2_image SDL2_ttf

# Update shell resource file
export LD_LIBRARY_PATH=/opt/homebrew/lib:$LD_LIBRARY_PATH
```

### Virtual Environment Setup
```bash
# Create and activate virtual environment
python3 -m venv .venv
source ./.venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt

# Update dependencies
pip3 install --upgrade -r requirements.txt
```

### Running the Game
```bash
python3 main.py
```

## Architecture

### Core Systems

**Engine (`engine.py`)**: The main game loop and controller. On initialization, it:
1. Creates the graphics system (tileset loading)
2. Sets up the console and event handler
3. Creates a World instance (stored as a private attribute)
4. Calls `World.create_dungeon()` to populate the World's `current_map` attribute
5. Handles the game loop: event processing, FOV updates, and rendering

The Engine does not maintain its own reference to the GameMap. It accesses the current map, entities, and player through `self._world.current_map`, `self._world.current_map.entities`, and `self._world.current_map.player`.

**World (`world.py`)**: Container for game levels/maps. Manages the current active map:
- `current_map`: Public attribute holding the currently active GameMap instance
- `create_dungeon()`: Instance method that generates a new dungeon and populates `self.current_map` by:
  1. Calling `proc_gen.generate_dungeon()` with default parameters from `constants.py`, which returns a `(GameMap, Pawns, starting_position)` tuple
  2. Building `current_map.entities` from `[pawns.player] + pawns.npcs` and setting `current_map.player`
  3. Positioning the player at the starting location returned by `generate_dungeon()`
- The Engine creates and maintains a World instance as a private attribute and accesses the game map through it

**Procedural Generation (`proc_gen` module)**: A module containing procedural generation logic organized in two files:
- **`proc_gen/dungeon_map_gen.py`**: Map generation functions
  - `generate_dungeon()`: Creates a GameMap, generates non-overlapping rooms connected by L-shaped tunnels, populates the `GameMap.rooms` attribute, spawns entities via `DungeonEntitySpawner().spawn_pawns()`, and returns a tuple of (GameMap, Pawns, starting_position)
  - `tunnel_between()`: Creates L-shaped corridors using Bresenham's line algorithm
- **`proc_gen/dungeon_spawn_gen.py`**: Entity spawning functions encapsulated in `DungeonEntitySpawner`:
  - `spawn_pawns()`: Instantiates `_pawns`, populates it with the player and all NPCs, and returns the `Pawns` instance
  - `spawn_player_actor()`: Creates the player entity (@) at position (0, 0)
  - `spawn_npc_actor()`: Creates an NPC (O) with hardcoded position
- Only `DungeonEntitySpawner` is re-exported via `proc_gen/__init__.py`

**RectangularRoom (`rectangular_room.py`)**: A data structure for room representation with properties:
- `center`: Returns the center coordinates of the room
- `inner`: Returns a 2D array slice for the room's inner area
- `intersects()`: Checks if this room overlaps with another room

**GameMap (`game_map.py`)**: Stores map tiles, visibility state, rooms, and entities:
- `width`, `height`: Map dimensions
- `rooms`: List of RectangularRoom objects, populated during dungeon generation
- `tiles`: NumPy array of tile data (walkable, transparent, graphics)
- `visible`: Currently visible tiles (FOV)
- `explored`: Previously seen tiles (persistent)
- `entities`: List of all entities (player and NPCs), initialized to `None` in `__init__()`
- `player`: Reference to the player entity (always `entities[0]`), initialized to `None` in `__init__()`
- Uses NumPy's `np.select()` for efficient rendering of visible/explored/shroud states

### Entity-Component System

**Entity (`actors/entity.py`)**: Generic container for all game objects (players, NPCs, items). Has position (x, y), visual representation (char, color), and a `move()` method. All parameters in `__init__()` and `move()` are keyword-only. Subclasses planned but not yet implemented. Re-exported via `actors/__init__.py` for convenient importing.

**Pawns (`actors/pawns.py`)**: Container for player and NPC entities. Provides a structured alternative to a plain list:
- `player`: Property (with setter) for the player entity
- `npcs`: Property returning the list of NPC entities
- `add_npc(npc)`: Adds an NPC to the list
- `remove_npc(npc)`: Removes an NPC (no-op if not found)
- Re-exported via `actors/__init__.py`

**Actions (`actions.py`)**: Command pattern for all game behaviors:
- `Action`: Base class with `perform(game_map, entity)` signature
- `MovementAction`: Validates destination (bounds + walkability) before moving. Stores offset as `_dx`/`_dy` (single underscore, protected).
- `GameExitAction`: Exits the game

Actions decouple input from behavior and receive the `game_map` for validation and state changes.

### Input & Rendering

**EventHandler (`input_handlers.py`)**: Translates TCOD events to Actions. Supports arrow keys, numpad, and vi-keys for 8-directional movement. Also includes no-op handlers for `ev_pixelsizechanged` and `ev_clipboardupdate` to suppress TCOD runtime warnings.

**Graphics (`graphical_block_characters.py`)**:
- Loads the tileset (`Alloy_curses_12x12.png` from assets/)
- Defines tile structures using NumPy dtypes for efficient memory layout
- Provides `floor_tile()` and `wall_tile()` factory methods
- Tiles have both "dark" (explored but not visible) and "light" (currently visible) color schemes

## Constants

Key configuration values in `constants.py`:
- `WINDOW_WIDTH/HEIGHT`: Console size (80x50)
- `MAP_WIDTH/HEIGHT`: Dungeon size (80x45)
- `ROOM_SIZE_MIN/MAX`: Room dimensions (6-10)
- `ROOMS_MAX`: Maximum room attempts (30)

## Code Patterns

- Uses `TYPE_CHECKING` imports to avoid circular dependencies
- NumPy arrays use Fortran order ("F") for column-major layout
- Private attributes use single underscore prefix (`_attribute`)
- FOV radius hardcoded to 8 in `Engine.update_fov()`
- Pylint configured to disable C0114 (missing module docstrings), C0116 (missing function docstrings), C0301 (line too long), R0913 (too many arguments), R0917 (too many positional arguments)

## Coding Style

**Python**:

Python code should follow **PEP 8** conventions when possible.
  - Use clear, descriptive variable and function names.
  - Follow standard indentation (4 spaces).
  - Limit lines to 120 characters where practical.
  - Use snake_case for variables and functions, CamelCase for classes.
  - Include docstrings for public functions, classes, and modules.
  - Prefer readability and clarity over clever or compact code.
