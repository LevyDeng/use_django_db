class a():
    def __init__(self):
        print self.__class__
        self.x=1
        self.y=2
        self.c=3

    #c=3





    #def set(self, key, value):
      #  setattr(self.__class__,key,value)

aa=a()
print aa.x,aa.y
#aa.set('z',4)
#print aa.z
setattr(aa,'z',6)
print aa.z
print aa.c
