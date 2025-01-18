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
        self.base = np.delete(self.base, -1)
        self.out_base = np.append(self.path[0].map["index"], self.out_base)
        self.path[0].map["rocks"].append("red")
        self.path[0].map["num_rocks"] += 1

    # index المصفوفة
    def return_rock_to_base(self, index):
        rocks_list = self.path[index].map["rocks"]
        for item in range(len(rocks_list)):
            self.path[index].map["rocks"].pop()
            self.base = np.append(1, self.base)
        self.path[index].map["num_rocks"] = 0
        self.out_base = self.out_base[self.out_base != self.path[index].map["index"]]
        # self.out_base=np.unique(self.out_base)
        # self.out_base=np.delete(self.out_base,self.path[index].map["index"])


a = player(70, "red")
print(a.base)
print(a.out_base)
a.get_rock_from_base()
a.get_rock_from_base()
print("@" * 100)
print(a.base)
print(a.out_base)
# for item in a.path:
#     print(
#         f"{item.map["type"]}"
#         + "*****************"
#         + f"{item.map["index"]}"
#         + f"{item.map["rocks"]}"
#         + f"{item.map["num_rocks"]}"
#     )
#     print("#" * 100)


a.return_rock_to_base(0)

for item in a.path:
    print(
        f"{item.map["type"]}"
        + "*****************"
        + f"{item.map["index"]}"
        + f"{item.map["rocks"]}"
        + f"{item.map["num_rocks"]}"
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
print("@" * 100)
print(a.base)
print(a.out_base)
a.get_rock_from_base()
print("@" * 100)
print(a.base)
print(a.out_base)
