import numpy as np
import square as sq
from path import path as pth


class player:

    def __init__(self, start_path, color):

        # end = start+56
        # اخر 6 مسار ملون للعالب نفسو
        self.base = np.ones(4, int)
        self.out_base = np.array([], int)
        self.path = pth(start_path).path

    def get_rock_from_base(self):
        self.base = np.delete(a.base, -1)
        self.out_base = np.append(0, self.out_base)
        self.path[0].map["rocks"].append("red")


a = player(1, "red")
print(a.base)
print(a.out_base)
a.get_rock()
print("@" * 100)
print(a.base)
print(a.out_base)
for item in a.path:
    print(
        f"{item.map["type"]}"
        + "*****************"
        + f"{item.map["index"]}"
        + f"{item.map["rocks"]}"
    )
    print("#" * 100)


# a.base=np.delete(a.base,-1)
# a.base=np.delete(a.base,-1)
# a.base=np.delete(a.base,-1)
# a.base=np.delete(a.base,-1)
# print(a.base)
# if(a.base.size!=0):
#  a.base=np.delete(a.base,-1)
#  print(a.base)
