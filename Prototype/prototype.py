from abc import ABC
from copy import deepcopy


class Prototype(ABC):
    def clone(self):
        pass


class Knight(Prototype):
    def __init__(self, level):
        self.unit_type = "Knight"
        # read from knight data file not implemented

    def __str__(self):
        return f"Type: {self.unit_type}"

    def clone(self):
        return deepcopy(self)


class Archer(Prototype):
    def __init__(self, level):
        self.unit_type = "Archer"
        # read from archer data file not implemented

    def __str__(self):
        return f"Type: {self.unit_type}"

    def clone(self):
        return deepcopy(self)


class Barracks:
    def __init__(self):
        self.units = {
            "knight": {1: Knight(1), 2: Knight(2)},
            "archer": {1: Archer(1), 2: Archer(2)},
        }

    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()


if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.build_unit("knight", 1)
    archer1 = barracks.build_unit("archer", 2)
    print(f"[knight1]: {knight1}")
    print(f"[archer1]: {archer1}")
