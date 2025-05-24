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

    def __init__(self, height, width, position):
        super().__init__(height, width)
        self._init_position(position)

    def _init_position(self, player_pos: dict) -> None:
        player_x = player_pos["x"]
        player_y = player_pos["y"]
        if self._x is None or self._y is None:
            self._x = player_x
            self._y = player_y

    @property
    def symbol(self) -> str:
        return "*"

    def is_dead(self):
        if self._y == 0:
            return True
        return False

    def move(self):
        self.move_y(-1)


class Beam(GameObject):
    """Enemyが発射するもの"""

    def __init__(self, height, width, position):
        super().__init__(height, width)
        self.direct_flag: bool = True
        self._init_position(position)

    def _init_position(self, enemy_pos: dict) -> None:
        enemy_x = enemy_pos["x"]
        enemy_y = enemy_pos["y"]
        if self._x is None or self._y is None:
            self._x = enemy_x
            self._y = enemy_y

    @property
    def symbol(self) -> str:
        return "@"

    def is_dead(self):
        if self._y == (self.h - 1):
            return True
        return False

    def _is_turn(self):
        if self._x == 0 or self._x == (self.w - 1):
            return True
        return False

    def move(self):
        if self._is_turn():
            self.direct_flag = not self.direct_flag

        if self.direct_flag:
            self.move_x(1)
            self.move_y(1)
        else:
            self.move_x(-1)
            self.move_y(1)
