from random import randint

from server.modules.base import GameObject


class Player(GameObject):
    def __init__(self, height, width):
        super().__init__(height, width)
        self._init_position()

    def _init_position(self) -> None:
        if self._x is None or self._y is None:
            self._x = self.w // 2
            self._y = self.h - 1

    @property
    def symbol(self) -> str:
        return "P"

    def move(self, command: str):
        match command:
            case "j":
                self.move_x(-1)
            case "l":
                self.move_x(1)


class Enemy(GameObject):
    def __init__(self, height, width):
        super().__init__(height, width)
        self._init_position()

    def _init_position(self) -> None:
        if self._x is None or self._y is None:
            self._x = self.w // 2
            self._y = 0

    @property
    def symbol(self) -> str:
        return "E"

    def move(self):
        random_x = randint(-2, 2)
        self.move_x(random_x)


class Bullet(GameObject):
    """Playerが発射するもの"""

    def __init__(self, height, width):
        super().__init__(height, width)
        self._init_position()

    def _init_position(self, position: dict) -> None:
        player_x = position["x"]
        player_y = position["y"]
        if self._x is None or self._y is None:
            self._x = player_x
            self._y = player_y - 1

    @property
    def symbol(self) -> str:
        return "*"

    def is_dead(self):
        if self._y == 0:
            return True
        return False

    def move(self):
        self.move_y(-1)
