from server.modules.base import Board
from server.modules.object import Player, Enemy, Bullet, Beam


class PlayBoard(Board):
    def __init__(self, height, width):
        super().__init__(height, width)

        self.player: Player = Player(self.h, self.w)
        self.bullet: list[Bullet] = []
        self.enemy: Enemy = Enemy(self.h, self.w)
        self.beam: Beam | None = None

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

        # 生存確認
        self.bullet = [b for b in self.bullet if not b.is_dead()]
        if self.beam is not None and self.beam.is_dead():
            self.beam = None

        # 敵の攻撃確認
        if self.beam is None:
            self.beam = Beam(self.h, self.w, self.enemy.position)

        # 発射
        if command == "k":
            b = Bullet(self.h, self.w, self.player.position)
            self.bullet.append(b)

        # move
        self.player.move(command)
        self.enemy.move()
        for b in self.bullet:
            b.move()
        self.beam.move()

        # set
        self._set_object(self.player.position, self.player.symbol)
        self._set_object(self.enemy.position, self.enemy.symbol)
        for b in self.bullet:
            self._set_object(b.position, b.symbol)
        self._set_object(self.beam.position, self.beam.symbol)

    def get_board_state(self) -> dict:
        return {"field": self.field}
