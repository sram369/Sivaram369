from abc import ABC, abstractmethod

class A(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass
class B:
    def siva(self):
        print("Hi")
class C:
    def Ram(self):
        print("Where")

class D(A):
    def sound(self):
        return "Bow Bow"

d =D("Chingchang")
print(d.sound())
print(d.name)