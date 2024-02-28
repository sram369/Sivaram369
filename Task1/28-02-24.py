# *********   Encapsulation.   *********

class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        print("Your account is XYZ credited ",self.balance)

    def _withdraw(self, amount):
        self.balance -= amount
    def __show_balance(self):
        print("Your Balance is ",self.balance)

    def if_you_are_auth(self):
        User_Pin_In_Data = "3690"
        Pin = input("Enter your Pin:")
        if Pin == User_Pin_In_Data:
            self.__show_balance()
        else:
            print("Invalid User Pin , Please Enter valid Pin ")

    def do_with_by_bank_manager(self,amount):
        self._withdraw(amount=amount)
        print("Your account is XYZ Debited ", amount)

User = BankAccount()
User.deposit(5000)
User.do_with_by_bank_manager(1500)
User.if_you_are_auth()


# *********   Single  Inheritance Example.   *********

class My_Father:
    Properties = "20 Acres of Forming Land and One House"
    Vehicals = "One Bike and one Tractor"
    def My_Father_Properties(self):
        print("My_Father_Properties:",self.Properties)
        print("My_Father_Vehicals:",self.Vehicals)
        print()

class Me(My_Father):
    def My_Own_Properties(self,Properties,Vehicals):
        self.Properties = Properties
        self.Vehicals = Vehicals
        print("My_Own_Properties:",self.Properties)
        print("My_Vehicals:",self.Vehicals)

Obj = Me()
Obj.My_Father_Properties()
Obj.My_Own_Properties("One Plat and One Plywood Business ", "One Ninja zx10r bike and One Porsche car")

# *********   Multi Level Inheritance Example.   *********

class My_Grand_Father:
    Properties_GF = "40 Acres of Forming Land and One House"
    Vehicals_GF = "One By_Cycle and one Yedla Bandi"
    def My_Grand_Father_Properties(self):
        print("My_Grand_Father_Properties:",self.Properties_GF)
        print("My_Grand_Father_Vehicals:",self.Vehicals_GF)
        print()
class My_Father(My_Grand_Father):
    Properties_F = "20 Acres of Forming Land and One House"
    Vehicals_F = "One Bike and one Tractor"
    def My_Father_Properties(self):
        print("My_Father_Properties:",self.Properties_F)
        print("My_Father_Vehicals:",self.Vehicals_F)
        print()

class Me(My_Father):
    def My_Own_Properties(self,Properties,Vehicals):
        self.Properties = Properties
        self.Vehicals = Vehicals
        print("My_Own_Properties:",self.Properties)
        print("My_Vehicals:",self.Vehicals)


Obj = Me()
Obj.My_Grand_Father_Properties()
Obj.My_Father_Properties()
Obj.My_Own_Properties("One Plat and One Plywood Business ", "One Ninja zx10r bike and One Porsche car")

Obj2 = My_Father()
Obj2.My_Grand_Father_Properties()
Obj2.My_Father_Properties()

Obj3 = My_Grand_Father()
Obj3.My_Grand_Father_Properties()

# *********   Hierarchical Inheritance Example.   *********

class My_Father:
    Properties = "20 Acres of Forming Land and One House"
    Vehicals = "One Bike and one Tractor"
    def My_Father_Properties(self):
        print("My_Father_Properties:",self.Properties)
        print("My_Father_Vehicals:",self.Vehicals)
        print()

class Me(My_Father):
    def My_Own_Properties(self,Properties,Vehicals):
        self.Properties = Properties
        self.Vehicals = Vehicals
        print("My_Own_Properties:",self.Properties)
        print("My_Vehicals:",self.Vehicals)
        print()

class My_Brother(My_Father):
    def My_Brother_Own_Properties(self,Properties,Vehicals):
        self.Properties = Properties
        self.Vehicals = Vehicals
        print("My_Brother_Own_Properties:",self.Properties)
        print("My_Brother_Vehicals:",self.Vehicals)

Obj = Me()
Obj.My_Father_Properties()
Obj.My_Own_Properties("One Plat and One Plywood Business ", "One Ninja zx10r bike and One Porsche car")

Obj2 = My_Brother()
Obj2.My_Father_Properties()
Obj2.My_Brother_Own_Properties("One 3BHK Plat and 50 lakh gold  ", "One Bullet bike and One BMW car")


# *********   Multiple Inheritance Example.   *********

class My_Father:
    Properties_F = "20 Acres of Forming Land and One House"
    Vehicals_F = "One Bike and one Tractor"
    def My_Father_Properties(self):
        print("My_Father_Properties:",self.Properties_F)
        print("My_Father_Vehicals:",self.Vehicals_F)
        print()

class My_Mother():
    Properties_M = " 60 lakh Gold and One House"
    Vehicals_M = "One Activa Scooty"
    def My_Mother_Properties(self):
        print("My_Mother_Properties:",self.Properties_M)
        print("My_Mother_Vehicals:",self.Vehicals_M)
        print()

class Me(My_Father,My_Mother):
    def My_Own_Properties(self,Properties,Vehicals):
        self.Properties = Properties
        self.Vehicals = Vehicals
        print("My_Own_Properties:",self.Properties)
        print("My_Vehicals:",self.Vehicals)

Obj = Me()
Obj.My_Father_Properties()
Obj.My_Mother_Properties()
Obj.My_Own_Properties("One Plat and One Plywood Business ", "One Ninja zx10r bike and One Porsche car")



class My_Father:
    Properties_F = "20 Acres of Forming Land and One House"
    Vehicals_F = "One Bike and one Tractor"
    def Properties(self):
        print("My_Father_Properties:",self.Properties_F)
        print("My_Father_Vehicals:",self.Vehicals_F)
        print()

class My_Mother():
    Properties_M = " 60 lakh Gold and One House"
    Vehicals_M = "One Activa Scooty"
    def Properties(self):
        print("My_Mother_Properties:",self.Properties_M)
        print("My_Mother_Vehicals:",self.Vehicals_M)
        print()

class Me(My_Mother,My_Father):
# if Parent classes of both methods will same
# Here We Can Use anything of these two but output will give oder of the child class implimentation
# Me(My_Father,My_Mother) or Me(My_Mother,My_Father) :
    def My_Own_Properties(self,Properties,Vehicals):
        self.Properties = Properties
        self.Vehicals = Vehicals
        print("My_Own_Properties:",self.Properties)
        print("My_Vehicals:",self.Vehicals)

Obj = Me()
Obj.Properties()
Obj.My_Own_Properties("One Plat and One Plywood Business ", "One Ninja zx10r bike and One Porsche car")


# *********   Polymorphism   *********
# *********   Method overriding   *********

class P:
    def property(self):
        print("Gold+Land+Cash+Power")
    def marry(self):
        print("Virat")
class C(P):
    def property(self):
        super().property()
        print("One Porsche car")

    def marry(self):
        super().marry()
        # Here child class is not satisfied with parent class implementation
        #then the child class is allowed to redefined that method in chid class based on requirement
        #This concept is method overriding . We Can solve by using super().

        print("Kohili")

c = C()
c.property()
c.marry()

# *********   Method overloading   *********

class Test:
    def m1(self):
        # In python method overloading is not possible,
        # But We can overcome this problem passing the variable length of arguments into a func
        # In method overloading it will always consider last method.
        sum = 0
        for i in a:
            sum+= i
        print(sum)

    def m1(self,*a):
        for i in a:
            n = i*i
            print(n)
t = Test
t.m1(30,3,6,9)
t.m1(90,12,15,18)

# *********   Abstraction   *********

from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Bow Bow"
class Cat(Animal):
    def sound(self):
        return "Meow Meow"

dog = Dog("Chintu")
print(dog.sound())

cat = Cat("Julee")
print(cat.sound())


