from abc import ABC, abstractmethod

from pydantic import BaseModel


class Position(BaseModel):
    x: int
    y: int


class GameObject(ABC):
    def __init__(self, height, width):
        self.__h: int = height
        self.__w: int = width
        self._x: int | None = None
        self._y: int | None = None

    @property
    def h(self) -> int:
        return self.__h

    @property
    def w(self) -> int:
        return self.__w

    @property
    def position(self) -> dict:
        p = Position(x=self._x, y=self._y)
        return p.model_dump()

    @property
    @abstractmethod
    def symbol(self) -> str:
        pass

    def move_x(self, value: int) -> None:
        if self._x is not None:
            if not isinstance(value, int):
                raise ValueError("引数はint型です:", value)

            if value >= 0 and (self._x + value) <= (self.w - 1):
                self._x += value

            if value < 0 and (self._x + value) >= 0:
                self._x += value

    def move_y(self, value: int) -> None:
        if self._y is not None:
            if not isinstance(value, int):
                raise ValueError("引数はint型です:", value)

            if value >= 0 and (self._y + value) <= (self.h - 1):
                self._y += value

            if value < 0 and (self._y + value) >= 0:
                self._y += value

    @property
    @abstractmethod
    def move(self):
        pass


class Board(ABC):
    def __init__(self, height: int, width: int):
        self.h: int = height
        self.w: int = width
        self.field: list[str] | None = None

        self._init_field()

    def _init_field(self):
        self.field = [[" " for _ in range(self.w)] for _ in range(self.h)]
        for i in range(self.h):
            for j in range(self.w):
                if i % (self.h - 1) == 0 and j % (self.w - 1) == 0:
                    self.field[i][j] = "+"
                elif i == 0 or i == (self.h - 1):
                    self.field[i][j] = "-"
                elif j == 0 or j == (self.w - 1):
                    self.field[i][j] = "|"

    # TODO デバッグ用
    def show_field(self):
        for line in self.field:
            print(*line)

    @abstractmethod
    def update(self, command: str):
        pass


def main():
    B = Board()
    B.show_field()


if __name__ == "__main__":
    main()
