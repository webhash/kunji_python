
print("Hello World!!")

print()
print('-----------------------')
print()
print(note:='lets dig bit deeper into numeric types')
print(note:='python supports the import keyword to import modules/functions')
print(note:='lets import sys module')
import sys

print(note:='as everything in python is an object, there is an overhead')
print(note:='an int is though 4 byte but we get a much bigger space usage, because of the overhead')
x = 1000
print(type(x))
print(sys.getsizeof(x))
print(note:='bigger number means more storage space')
y = 1000**100
print(type(y))
print(sys.getsizeof(y))

print(note:='python also supports the _  in numbers to make them more readable')
print(note:='1000000000 can be hard to read, but  1000_000_000 is easy as it comes')
z = 1000_000_000 
print(z)

print()
print('-----------------------')
print()

print(note:='int * int shall give us another int')
print(type(x*y))
print(note:='int / int shall give us float')
print(type(y/x))
print(note:='int // int i.e the floor operation shall give us int')
print(type(y//x))
print(note:='int % int i.e the modulo operation shall give us int')
print(type(y%x))
print(note:='Remember this from school days ? a = b * (a // b) + a % b')
print(x)
print(y * (x//y) + x%y)
assert x == (y * (x//y) + x%y) 

print()
print('-----------------------')
print()

print(note:='int type supports many functionality like')
print(dir(int))
print(note:='int constructor is smart ... converts floats/fractions to int')
assert int(1.9) == int(1)
print()
print('-----------------------')
print()

print(note:='int type need not be a number of base 10, python has constructor to initiate the int with different type of base')
print(note:='but when we create a number of diff base we have to pass the string representation of the number')
b1 = int('10101', 2)
print(b1)
b2 = int('10101', base=2)
print(b2)
assert b1 == b2 
print(note:='python uses English letters for higher bases, and they are case insensitive') 
h1 = int('EAF', 18)
h2 = int('eaf', base=18)
print(h1)
print(h2)
assert h1 == h2 


print()
print('-----------------------')
print()

print(note:='we also have built in base representation to make life of programmer easier')
print(note:='hex  starts with 0x / 0X')
print(hex(100))
print(note:='bin starts with 0b / 0B')
print(bin(100))
print(note:='oct starts with 0o / 0O')
print(oct(100))
print(note:='we can use the 0x, 0b, 0o to specify the number of particular base')
print(note:='underscores are supported, just dont use them at the start of the number')
h = '0xFF'
b = '0b_11_11'
o = '0o76'
print(h, end=' == ')
print(int(h,16))
print(b, end=' == ')
print(int(b,2))
print(o, end=' == ')
print(int(o,8))

print()
print('-----------------------')
print()

print(note:='python also supports the boolean type')
t = True 
f =  False
print('t is if type ' , type(t) , ' and has address as ' , hex(id(t)))
print('f is of type ' , type(f) , ' and has address as ' , hex(id(f)))
print(note:='True and false will point to a fixed memory address, when we do comparision the result would be True/false pointing to same memory address')
print(hex(id(10>1)))
print(hex(id(10<1)))
assert hex(id(t)) == hex(id(10>1))
assert hex(id(f)) == hex(id(10<1))

print()
print('-----------------------')
print()


print(note:='python has the function issubclass to check if one class is a subclass of another')

if issubclass(bool, int):
	print(note:='bool is subclass of int, and if we convert them to int we shall get 1 and 0')
	print(int(t))
	print(int(f))
	if isinstance(t, int) and isinstance(f, bool):
		print(note:='True and False are instance of bool, and by inheritance are also instance of int')

print(note:='bool of non zero value returns True, and zero value returns False')
print(bool(1), bool(-1), bool(0.5), bool(None), bool(0))
print(note:='but the above behavior happens because int, float have __bool__ implemented')
print((1).__bool__(), (-1).__bool__(), (0.5).__bool__())

print()
print('-----------------------')
print()


try:
	print(('0').__bool__())
except AttributeError:
	print(note:='str doesnt implement the __bool__ function , and return the default value of True for non-empty string')
	print(bool(''), bool('0'), bool('1')) 
	print(note:='This is called truthy and falsy behavior')


print(note:='An empty sequence type object or mapping type is Falsy, a non-empty one is truthy')
print(bool([1]), bool([]))
print(bool({'yes'}), bool({}))


print()
print('-----------------------')
print()


print(note:='now quickly have a look at the float types')
print(note:='unlike int float has a single constructor that takes a number or string representation of number and returns a float value')

print(float(1))
print(float('1'))
print(float(1.7))
print(float('1.7'))
print(float(1_000.7))

print()
print('-----------------------')
print()


print(note:='float type supports many functionality like')
print(dir(float))

f1 = float(1/3)
f2 = float('.33')
print(f1, end=' == ')
print(f1.as_integer_ratio())
print(f2, end=' == ')
print(f2.as_integer_ratio())

print()
print('-----------------------')
print()

print(float(22/7))

try:
	float('22/7')
except ValueError:
	print('we can`t pass a string with fraction like `22/7` to float')

print()
print('-----------------------')
print()

print(note:='float doesnt necessarily have the exact representation for all numbers, the magic of ration of 2s come into picture')
print(note:='Floating-point numbers are represented in computer hardware as base 2 (binary) fractions.')

fa = 0.1 + 0.1 + 0.1 
fb = 0.3
print(note:='though two numbers should have same value but if we check out enough precision point, we will see the difference')
print(fa)
print(fb)
assert fa != fb


print(note:='the difference is quite apparent if we get the fraction representation of float value')
print(fa, end=' == ')
print(fa.as_integer_ratio())
print(fb, end=' == ')
print(fb.as_integer_ratio())

print(note:='we can use the `round` function for approximate comparison')
assert round(fa, 8) == round(fb, 8)
print(round(fa, 8) , end=' == ' )
print(round(fb, 8))

print()
print('-----------------------')
print()

print(note:='python also supports the complex numbers .. oh how i love python')
print(note:='complex number have real part and imaginary part')

c1 = complex(3,4)
c2 = complex(1,2)

print(c1)
print(c2)
print(note:='real part type ' , type(c1.real) ,  ' imaginary part type ' , type(c1.imag))
print(note:='real part ' , c1.real , ' imaginary part ' , c1.imag)
print(note:='real part ' , c2.real , ' imaginary part ' , c2.imag)

print()
print('-----------------------')
print()

print(note:='python supports following operation with complex numbers')
print(note:='addition')
print(c1+c2)
print(note:='subtraction')
print(c1-c2)
print(note:='multiplication')
print(c1*c2)
print(note:='division')
print(c1/c2)
print(note:= 'operation like <, <=, >, >=, //, % are not supported for complex numbers')
print(note:=' although we can also get the conjugate of a complex number')
print(c1, end=' conjugate is ')
print(c1.conjugate())
print(c2, end=' conjugate is ')
print(c2.conjugate())

print()
print('-----------------------')
print()

