class SumList(object):
    def __init__(self, this_list):
        self.mylist = this_list

    def __add__(self, other):
        new_List = [x + y for x, y in zip(self.mylist, other.mylist)]
        return SumList(new_List)

    def __repr__(self): #called implicity
        return str(self.mylist)

cc = SumList([1, 2, 3, 4, 4])
dd = SumList([100, 200, 300, 400, 500])

ee = cc + dd
print(ee)
