import curses
import time
import random
from util.coordinate import Coordinate
from model.game_object import GameObject
from util.map import Map

class MapWrapper:
    def __init__(self, map_object: Map, viewport_size: int = 30):
        """
        Wrapper around the Map class for interactive display.
        
        :param map_object: The Map instance to wrap.
        :type map_object: Map
        :param viewport_size: Size of the viewport to display.
        :type viewport_size: int
        """
        self.map = map_object
        self.viewport_size = viewport_size
        self.size = map_object.get_size()
        self.top_left = Coordinate(0, 0)

    def display(self):
        """
        Generate a string representation of the current viewport.
        """
        x_start = self.top_left.get_x()
        y_start = self.top_left.get_y()

        x_end = min(self.size - 1, x_start + self.viewport_size - 1)
        y_end = min(self.size - 1, y_start + self.viewport_size - 1)

        view_map = self.map.get_map_from_to(Coordinate(x_start, y_start), Coordinate(x_end, y_end))
        grid = f"Viewport Coordinates: ({x_start}, {y_start})\n"

        for x in range(x_start, x_end + 1):
            row = []
            for y in range(y_start, y_end + 1):
                obj = view_map.get(Coordinate(x, y), None)
                row.append(f"{obj.get_letter() if obj else '.'}")
            grid += " ".join(row) + "\n"
        return grid

    def move_viewport(self, dx: int, dy: int):
        """
        Move the viewport by the specified deltas.
        
        :param dx: Change in x-coordinate.
        :param dy: Change in y-coordinate.
        """
        new_x = max(0, min(self.size - self.viewport_size, self.top_left.get_x() + dx))
        new_y = max(0, min(self.size - self.viewport_size, self.top_left.get_y() + dy))
        self.top_left = Coordinate(new_x, new_y)


def display_interactive_map(stdscr, wrapper: MapWrapper, fps: int = 20):
    """
    Interactive display of the map using curses.
    
    :param stdscr: Curses standard screen object.
    :param wrapper: MapWrapper instance for map interaction.
    :param fps: Frames per second for rendering.
    """
    frame_time = 1 / fps
    curses.curs_set(0)
    stdscr.timeout(100)

    try:
        while True:
            stdscr.clear()
            stdscr.addstr(wrapper.display())

            key = stdscr.getch()
            if key == ord('w') or key == curses.KEY_UP:
                wrapper.move_viewport(-1, 0)
            elif key == ord('s') or key == curses.KEY_DOWN:
                wrapper.move_viewport(1, 0)
            elif key == ord('a') or key == curses.KEY_LEFT:
                wrapper.move_viewport(0, -1)
            elif key == ord('d') or key == curses.KEY_RIGHT:
                wrapper.move_viewport(0, 1)

            stdscr.refresh()
            time.sleep(frame_time)

    except KeyboardInterrupt:
        stdscr.addstr("\nProgram stopped by user.\n")
        stdscr.refresh()
        time.sleep(1)


map_instance = Map(160)

# Add random GameObjects for testing
for _ in range(50):
    x = random.randint(0, 159)
    y = random.randint(0, 159)
    obj = GameObject("oui", 'T', 1)
    if map_instance.check_placement(obj, Coordinate(x, y)):
        map_instance.add(obj, Coordinate(x, y))

wrapper = MapWrapper(map_instance, viewport_size=30)
curses.wrapper(display_interactive_map, wrapper, fps=20)
