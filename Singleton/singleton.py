class Singleton:
    class __Singleton:
        def __init__(self):
            self.val = None

        def __str__(self):
            return f"{id(self)} {self.val}"

    instance = None

    def __new__(cls):
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton()

        return Singleton.instance

    # def __getattr__(self, name):
    #     return getattr(self.instance, name)
    #
    # def __setattr__(self, name):
    #     return setattr(self.instance, name)


obj1 = Singleton()
obj1.val = "obj val 1"
print(obj1)

obj2 = Singleton()
obj2.val = "obj val 2"
print(obj2)

assert obj1 is obj2
