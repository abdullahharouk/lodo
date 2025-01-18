import numpy as np
from square import square as sq


class path:

    def __init__(self, start):
        self.path = [sq(0, rows) for rows in range(start, start + 57)]
        self.path[8].map["type"] = 1
        self.path[21].map["type"] = 1
        self.path[34].map["type"] = 1
        self.path[47].map["type"] = 1

        self.path[-1].map["type"] = 3
        self.path[-2].map["type"] = 3
        self.path[-3].map["type"] = 3
        self.path[-4].map["type"] = 3
        self.path[-5].map["type"] = 3
        self.path[-6].map["type"] = 3


a = path(14)
for item in a.path:
    print(
        f"{item.map["type"]}"
        + "*****************"
        + f"{item.map["index"]}"
        + f"{item.map["rocks"]}"
    )
    print("#" * 100)
