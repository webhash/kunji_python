print("Hello World!!")

print()
print('-----------------------')
print()

print(note := 'everything is basically a object in python')
print(note := 'this note is of type class string')
print('Type of note is ', type(note))
print(note := 'Lets have a look on how to create a class')

print()
print('-----------------------')
print()

print(note := 'class keyword is used to tell interpreter/compiler that we want to define a class')


class Empty:
    pass


print(note := 'Although the class is empty but by default python creates a lot of scaffolding for us')
print(note := 'Look python made Empty class callable')
e = Empty()
print(note := 'Like the __name__ ', Empty.__name__)
print(note := '__name__ is an example of class attributes ')

print(note := 'we can get the internal information of class by using dir')
print(dir(Empty))

print()
print('-----------------------')
print()

print(note := 'we can add user defined class attributes as below')


class NonEmpty:
    version = '1.0'


print(note := 'now version is a valid class attribute ', NonEmpty.version)

print(
    note := 'we can set the version attribute directly, as python doesnt have direct keyword support for the private/protected/public')
NonEmpty.version = '1.1'
print(note := 'now version is  ', NonEmpty.version)

print()
print('-----------------------')
print()

print(
    note := 'did you notice the getattr and setattr in the dir result for previous Empty class, we can use the getattr and setattr on the attributes')
print(getattr(NonEmpty, 'version'))
setattr(NonEmpty, 'version', '2.0')
print(getattr(NonEmpty, 'version'))
print(NonEmpty.version)

print()
print('-----------------------')
print()

print(note := 'As functions are also object we can add user defined attributed to any function')


def some_func():
    print('i don`t do anything')


setattr(some_func, 'version', '2.0')
print(getattr(some_func, 'version'))
print()
print(note := 'did that bow your mind ??? python is awesome')

print()
print('-----------------------')
print()

print(note := 'did you notice the __dict__ attribute in the dir of previous Empty class?')
print(NonEmpty.__dict__)
print(note := 'As you can see the version value is stored in this dict')
print(note := 'we can also the version atttribute via __delattr__')
delattr(NonEmpty, 'version')
print(note := 'And now we won`t see the version in the __dict__')
print(NonEmpty.__dict__)

print()
print('-----------------------')
print()

print(note := 'Let us create Some_Class')


class Some_Class:
    # __init__ is the constructor
    # first parameter self holds the object created when class initialized
    # we need not to use the name self, but its sort of nomenclature used by community
    # so better use it to make your code more readable
    def __init__(self, student, teacher, subject):
        self.student = student
        self.teacher = teacher
        self.subject = subject

    def print_class_info(self):
        print(self.student)
        print(self.teacher)
        print(self.subject)


print(
    note := 'if we print the __dict__  of Some_Class we shall the init, print_class_info as callable attributes pointing to a function')
print(Some_Class.__dict__)

print()
print('-----------------------')
print()

print(note := 'Lets create object of type Some_Class')
cls1 = Some_Class(10, 'Mr.X', 'programming')
cls2 = Some_Class(20, 'Mr.Y', 'history')

print(note := 'Type of cls1 is ', type(cls1))
print(note := 'Type of cls2 is ', type(cls2))

assert type(cls1) == type(cls2)

print(note := 'python has a function isinstance to check if an object is instance of particular type')

print(isinstance(cls1, Some_Class))
print(isinstance(cls2, Some_Class))

assert isinstance(cls1, Some_Class) == isinstance(cls2, Some_Class)

print()
print('-----------------------')
print()

print(note := 'the object defined is passed as "self" parameter so that we use the right instance of class')
print(cls1.student)
print(cls1.teacher)
print(cls1.subject)

cls2.print_class_info()

print()
print('-----------------------')
print()

print()
print(note := 'As mentioned before In python we don`t have the direct keywords of private/public ')
print(note := 'This means we can change the properties directly')
cls1.student = 100
cls2.student = 200
cls1.print_class_info()
print()
cls2.print_class_info()

print()
print('-----------------------')
print()

print(note := 'python has another approach for providing the protection or private behaviour')


class Better_Some_Class:
    def __init__(self, version, author, publisher):
        self.version = version
        self._author = author
        self.__publish = publisher

    def print_class_info(self):
        print(self.version)
        print(self._author)
        print(self.__publish)


b = Better_Some_Class('1.0', 'web', 'git')

b.print_class_info()

print(b.version)
print(b._author)
try:
    print(b.__publish)
except AttributeError:
    print(note := 'we shall get attribute error if we try to access the private variable')

print(note := "we can direclty set the version")
b.version = '1.1'

print(note := 'we can directly set the protected variable')
b._author = 'webhash'

print(note := 'if we do dir of the object we shall see __publish as _Better_Some_Class__publish variable')
print(dir(b))
print(note := 'so technically we can change the variable if we want to, but his should not be done')
b._Better_Some_Class__publish = 'github'
print(note := 'now the we have the updated values of "private" variable too')
b.print_class_info()

print()
print('-----------------------')
print()

print(note := 'Some_class contains 4 user defined attributes')
print(note := 'we can use the function dir to see them , among other fields')
print(dir(cls1))
print(note := 'callable attributes are called method and non-callable attributes are called properties')
print(
    note := 'did you see the __str__ key in above keys? ... this is the function called when we use function like str')
print(note := 'but if we use the str on some_class object, we will not get the expected result')
print(str(cls1))

print()
print('-----------------------')
print()

print(note := 'let us create another class that supports str')


class Some_Class_With_Str:
    # __init__ is the constructor
    # first parameter self holds the object created when class initialized
    # we need not to use the name self, but its sort of nomenclature used by community
    # so better use it to make your code more readable
    def __init__(self, student, teacher, subject):
        self.student = student
        self.teacher = teacher
        self.subject = subject

    def print_class_info(self):
        print(self.student)
        print(self.teacher)
        print(self.subject)

    def __str__(self):
        return 'student ' + str(self.student) + ' teacher ' + str(self.teacher) + 'subject ' + str(self.subject)


print(note := 'lets create two object with same data')
clsstr1 = Some_Class_With_Str(10, 'Mr.Z', 'programming')
clsstr2 = Some_Class_With_Str(10, 'Mr.Z', 'programming')
print(note := 'now the str function shall return us the expected result')
print(str(clsstr1))
print()
print(str(clsstr2))

print(note := 'Although both of the object clsstr1 and clsstr2 have same values, there comparison will return false')
print(note := clsstr1 == clsstr2)

print()
print('-----------------------')
print()

print(note := 'let us create another class that supports Eq')


class Some_Class_With_Eq:
    # __init__ is the constructor
    # first parameter self holds the object created when class initialized
    # we need not to use the name self, but its sort of nomenclature used by community
    # so better use it to make your code more readable
    def __init__(self, student, teacher, subject):
        self.student = student
        self.teacher = teacher
        self.subject = subject

    def print_class_info(self):
        print(self.student)
        print(self.teacher)
        print(self.subject)

    def __eq__(self, other):
        if isinstance(other, Some_Class_With_Eq):
            if ((self.student == other.student) and (self.teacher == other.teacher) and (
                    self.subject == other.subject)):
                return True
            else:
                return False
        else:
            return False


print(note := 'now lets create two object with same data')
clsstr1 = Some_Class_With_Eq(10, 'Mr.Z', 'programming')
clsstr1.print_class_info()
clsstr2 = Some_Class_With_Eq(10, 'Mr.Z', 'programming')
clsstr2.print_class_info()

print(note := 'and now the eq operator will work')
print(clsstr1 == clsstr2)
print(
    note := 'similarly we can add support for __lt__  and  __gt__ to have support of less than and greater than operator')

print()
print('-----------------------')
print()

print(note := 'lets have a look at the classmethod, staticmethod and instancemethod')


class NewClass:
    def method(self):
        # this is docstring which shall be consumed by the help function
        '''
		this method is bound to the object
		as you can see we pass self here, which refers to the object that calls this function
		Not only can they modify object state, instance methods can also access the class itself
		through the self.__class__ attribute.
		This means instance methods can also modify class state
		'''
        return 'instance method called', self

    # this @classmethod is a decorator, as name suggests it decorates or add behaviour to particular function
    @classmethod
    def classmethod(cls):
        '''
		class methods take a cls parameter that points to the class and not the object instance
		when the method is called. Because the class method only has access to this cls argument,
		it cant modify object instance state.
		'''
        return 'class method called', cls

    # this @staticmethod tells the complier that this function is static type
    @staticmethod
    def staticmethod():
        '''
		This type of method takes neither a self nor a cls parameter.
		Therefore a static method can neither modify object state nor class state.
		Static methods are restricted in what data they can access
		'''
        return 'static method called'


print(note := 'lets call the help function on the NewClass created')
help(NewClass)
print()

print()
print('-----------------------')
print()

print(note := 'lets create an object of NewClass type')
ncObj = NewClass()
print(note := 'lets print the address of the above object')
print(hex(id(ncObj)))
print(note := 'now lets call the method, which is bound to the object , we will see the address of the ncObj')
print(ncObj.method())
print(note := 'we shall see the same address of self as that of the ncObj address')
print(note := 'we can see the same result if we call the method directly from NewClass and pass the ncObj')
print(NewClass.method(ncObj))
print()
print(note := 'now lets call the classmethod, which is bound to the class, we will see the address of the class')
print(note := 'again we shall repeat ... evrything is object in python, even the class')
print(NewClass.classmethod())
print(note := 'we can also use the object to call the class method, and as you would see we see the address of class')
print(ncObj.classmethod())
print(
    note := 'now lets call the staticmethod, they are like regular function bound to a class, they dont have access to object or class instace')
print(NewClass.staticmethod())
print(note := 'we can also use the object to call the staticmethod')
print(ncObj.staticmethod())

print()
print('-----------------------')
print()

print(note := 'let us create a more real world scenario to understand the static, class and normal method')
print(note := 'but before that one should remeber that python allows only one __init__ constructor')


class Vehicle:
    def __init__(self, wheels, passenger):
        self.wheels = wheels
        self.passenger = passenger

    def __str__(self):
        return 'No of wheels : ' + str(self.wheels) + ' No of Passengers ' + str(self.passenger)

    def speedlimit(self):
        return 'my speed limit is ' + str(self.speeds(self.wheels))

    @classmethod
    def bike(cls):
        return cls(2, 2)

    @classmethod
    def car(cls):
        return cls(4, 5)

    @classmethod
    def suv(cls):
        return cls(4, 6)

    @classmethod
    def truck(cls):
        return cls(6, 2)

    @staticmethod
    def speeds(wheels):
        if type(wheels) == int:
            if wheels == 2:
                return 30
            elif wheels == 4:
                return 60
            elif wheels == 6:
                return 50
            else:
                return 20
        else:
            return 20


print(note := 'In the above class we have created clasmethod that represent the common vehicle type')
print(note := 'and we have created a static method that returns the speedlimit based on number of wheels')
print(
    note := 'So rather than creating object and passing the config of number of wheels and passenger to generic vehicle')
car = Vehicle(4, 5)
print(str(car))
print(car.speedlimit())
print()
print(note := 'User can directly create standard type of vehicles')
print()
b = Vehicle.bike()
print(str(b))
print(b.speedlimit())
print()
c = Vehicle.car()
print(str(c))
print(c.speedlimit())
print()
t = Vehicle.truck()
print(str(t))
print(t.speedlimit())
print()

print()
print('-----------------------')
print()
