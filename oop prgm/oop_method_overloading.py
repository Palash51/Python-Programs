import abc

class GetSetParent(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self, value):
        set_val = 0

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val

    @abc.abstractmethod
    def showdoc(self):
        return

class GetSetInt(GetSetParent):
    def set_val(self, value):
        if not isinstance(value, int):  #check value if it is integer 
            value = 0
        super(GetSetInt, self).set_val(value) #look for super class of getsetint 

    def showdoc(self):
        print('GetSetInt object ({0}), only accepts '
              'integer values'.format(id(self)))

class GetSetList(GetSetParent):
    def __init__(self, value=0):
        self.vallist = [value]

    def get_val(self):
        return self.vallist[-1]

    def get_vals(self):
        return self.vallist

    def set_val(self, value):
        self.vallist.append(value)
        
    def showdoc(self):
        print('GetSetList object, len {0}, stores '
              'history of values set'.format(len(self.vallist)))
        

x = GetSetInt(3)
x.set_val(5)
print(x.get_val())
x.showdoc()

gsl = GetSetList(5)
gsl.set_val(10)
gsl.set_val(20)
print("\n\n")
print(gsl.get_val())
print(gsl.get_vals())
gsl.showdoc()

