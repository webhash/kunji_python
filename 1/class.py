print("Hello World!!")


print()
print('-----------------------')
print()

print(note:= 'everything is basically a object in python')
print(note:= 'this note is of type class string')
print('Type of note is ' + str(type(note)))
print(note:= 'Lets have a look on how to create a class')


print()
print('-----------------------')
print()


print(note:= 'class keyword is used to tell interpreter/compiler that we want to define a class')

class Empty:
	pass


print(note:='Although the class is empty but by default python creates a lot of scaffolding for us')
print(note:='Look python made Empty class callable')
e = Empty()
print(note:= 'Like the __name__ ' + str(Empty.__name__))
print(note:= '__name__ is an example of class attributes ')

print(note:= 'we can get the internal information of class by using dir')
print(dir(Empty))


print()
print('-----------------------')
print()

print(note:= 'we can add user defined class attributes as below') 
class NonEmpty:
	version = '1.0'

print(note:= 'now version is a valid class attribute ' + str(NonEmpty.version)) 

print(note:= 'we can set the version attribute directly, as python doesnt have the concept of public/private')
NonEmpty.version = '1.1'
print(note:= 'now version is  ' + str(NonEmpty.version)) 

print()
print('-----------------------')
print()

print(note:= 'did you notice the getattr and setattr in the dir result for previous Empty class, we can use the getattr and setattr on the attributes')
print(getattr(NonEmpty, 'version'))
setattr(NonEmpty, 'version', '2.0')
print(getattr(NonEmpty, 'version'))
print(NonEmpty.version)

print()
print('-----------------------')
print()

print(note:= 'did you notice the __dict__ attribute in the dir of previous Empty class?')
print(NonEmpty.__dict__)
print(note:= 'As you can see the version value is stored in this dict')
print(note:= 'we can also the version atttribute via __delattr__')
delattr(NonEmpty, 'version')
print(note:= 'And now we won`t see the version in the __dict__')
print(NonEmpty.__dict__)

print()
print('-----------------------')
print()


print(note:= 'Let us create Some_Class')

class Some_Class:
	# __init__ is the constructor  
	# first parameter self holds the object created when class initialized
	# we need not to use the name self, but its sort of nomenclature used by community
	# so better use it to make your code more readable
	def __init__ (self, student, teacher, subject):
		self.student = student
		self.teacher = teacher
		self.subject = subject 
	
	def print_class_info(self):
		print(self.student)
		print(self.teacher)
		print(self.subject)



print(note:='if we print the __dict__  of Some_Class we shall the init, print_class_info as callable attributes pointing to a function')
print(Some_Class.__dict__)

print()
print('-----------------------')
print()


print(note:= 'Lets create object of type Some_Class')
cls1 = Some_Class(10, 'Mr.X', 'programming')
cls2 = Some_Class(20, 'Mr.Y', 'history')

print(note:='Type of cls1 is ' + str(type(cls1)))
print(note:='Type of cls2 is ' + str(type(cls2)))

assert type(cls1) == type(cls2)

print(note:='python has a function isinstance to check if an object is instance of particular type')

print(isinstance(cls1, Some_Class))
print(isinstance(cls2, Some_Class))

assert isinstance(cls1, Some_Class) == isinstance(cls2, Some_Class)

print()
print('-----------------------')
print()

print(note:='the object defined is passed as "self" parameter so that we use the right instance of class')
print(cls1.student)
print(cls1.teacher)
print(cls1.subject)

cls2.print_class_info()

print()
print('-----------------------')
print()


print()
print(note:='As mentioned before In python we don`t have the concept of private/public directly')
print(note:='This means we can change the properties directly')
cls1.student = 100
cls2.student = 200
cls1.print_class_info()
print()
cls2.print_class_info()
print()

print()
print('-----------------------')
print()


print(note:='Some_class contains 4 user defined attributes')
print(note:='we can use the function dir to see them , among other fields')
print(dir(cls1))
print(note:='callable attributes are called method and non-callable attributes are called properties')
print(note:='did you see the __str__ key in above keys? ... this is the function called when we use function like str')
print(note:='but if we use the str on some_class object, we will not get the expected result')
print(str(cls1))

print()
print('-----------------------')
print()

print(note:='let us create another class that supports str')
class Some_Class_With_Str:
	# __init__ is the constructor  
	# first parameter self holds the object created when class initialized
	# we need not to use the name self, but its sort of nomenclature used by community
	# so better use it to make your code more readable
	def __init__ (self, student, teacher, subject):
		self.student = student
		self.teacher = teacher
		self.subject = subject 
	
	def print_class_info(self):
		print(self.student)
		print(self.teacher)
		print(self.subject)
	
	def __str__(self):
		return 'student ' + str(self.student) + ' teacher ' + str(self.teacher) + 'subject ' + str(self.subject)

print(note:='lets create two object with same data')
clsstr1 = Some_Class_With_Str(10, 'Mr.Z' , 'programming')	
clsstr2 = Some_Class_With_Str(10, 'Mr.Z' , 'programming')
print(note:='now the str function shall return us the expected result')
print(str(clsstr1))
print()
print(str(clsstr2))

print(note:='Although both of the object clsstr1 and clsstr2 have same values, there comparison will return false')
print(note:= clsstr1 == clsstr2)

print()
print('-----------------------')
print()

print(note:='let us create another class that supports Eq')
class Some_Class_With_Eq:
	# __init__ is the constructor  
	# first parameter self holds the object created when class initialized
	# we need not to use the name self, but its sort of nomenclature used by community
	# so better use it to make your code more readable
	def __init__ (self, student, teacher, subject):
		self.student = student
		self.teacher = teacher
		self.subject = subject 
	
	def print_class_info(self):
		print(self.student)
		print(self.teacher)
		print(self.subject)
	
	def __eq__(self, other):
		if isinstance(other, Some_Class_With_Eq):
			if ( (self.student == other.student)  and (self.teacher == other.teacher) and (self.subject == other.subject) ) :
				return True
			else:
				return False
		else:
			return False

print(note:='now lets create two object with same data')
clsstr1 = Some_Class_With_Eq(10, 'Mr.Z' , 'programming')
clsstr1.print_class_info()
clsstr2 = Some_Class_With_Eq(10, 'Mr.Z' , 'programming')
clsstr2.print_class_info()

print(note:='and now the eq operator will work')
print(clsstr1 == clsstr2)
print(note:='similarly we can add support for __lt__  and  __gt__ to have support of less than and greater than operator')
print()
print('-----------------------')
print()