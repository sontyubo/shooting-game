from server.modules.base import Board
from server.modules.object import Player, Enemy


class PlayBoard(Board):
    def __init__(self, height, width):
        super().__init__(height, width)

        self.player: Player = Player(self.h, self.w)
        self.enemy: Enemy = Enemy(self.h, self.w)

        self._init_set()

    def _init_set(self) -> None:
        self._set_object(self.player.position, self.player.symbol)
        self._set_object(self.enemy.position, self.enemy.symbol)

    def _set_object(self, position: dict, symbol: str) -> None:
        x = position["x"]
        y = position["y"]
        self.field[y][x] = symbol

    def update(self, command):
        # fieldの初期化
        self._init_field()

        # move
        self.player.move(command)
        self.enemy.move()

        # set
        self._set_object(self.player.position, self.player.symbol)
        self._set_object(self.enemy.position, self.enemy.symbol)

    def get_board_state(self) -> dict:
        return {"field": self.field}
