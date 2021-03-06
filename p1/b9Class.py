
class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0
    def __init__(self, name,height,weight,sound):
        self.__name = name
        self.__height= height
        self.__weight = weight
        self.__sound = sound

    def set_name(self,name):
        self.__name = name
    def get_name (self):
        return self.__name

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilogram and say {}".format\
            (self.__name,
             self.__height,
             self.__weight,
             self.__sound)

cat = Animal('Whiskers', 33, 10, 'Meow')
print(cat.toString())

class Dog(Animal):
    __owner = ""
    def __init__(self,name,height,weight,sound,owner):
        self.__owner = owner
        super(Dog,self).__init__(name,height,weight,sound)
    def set_owner(self,owner):
        self.__owner = owner
    def __get_owner(self):
        return self.__owner
    def get_type(self):
        print("Dog")
    def toString(self):
        return "{} is {} cm tall and {} kilogram and say {} owner is {}".format(self.__name,
                                                                                 self.__height,
                                                                                 self.__weight,
                                                                                 self.__sound,
                                                                                self.__owner)

    def multiple_sounds(self,how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)

spot = Dog("Spot", 53,27,"Ruff" , "malik")
print(spot.toString())