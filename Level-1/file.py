print("Hello World!!")

print()
print('-----------------------')
print()

poem = 'Whose woods these are I think I know. \
\n\
His house is in the village though; \
\n\
He will not see me stopping here \
\n\
To watch his woods fill up with snow. \
\n\
My little horse must think it queer \
\n\
To stop without a farmhouse near \
\n\
Between the woods and frozen lake \
\n\
The darkest evening of the year. \
\n\
He gives his harness bells a shake \
\n\
To ask if there is some mistake. \
\n\
The only other sound’s the sweep \
\n\
Of easy wind and downy flake. \
\n\
The woods are lovely, dark and deep, \
\n\
But I have promises to keep, \
\n\
And miles to go before I sleep, \
\n\
And miles to go before I sleep. \
\n\
'

poemFile = 'poem.txt'
binFile = 'binary'
print(note := 'python has open function to open files for reading and writing')

print(note := 'we can pass w, r, r+, a as the mode of opening the file')
print(note := 'w will open the file in write mode, and will overwrite if the same file exists')
print(note := 'r will open the file in read mode, if file doesnt exists we shall get an error')
print(note := 'r+ will open the file in both read and write mode, but file should exists before hand')
print(note := 'a will open the file in append mode')
print(note := 'if no mode is passed then python assumes r mode')
print(note := 'its is recommened to use "with" keyword as it would ensure that file is closed after the with block')

with open(poemFile, 'w') as f:
    count = f.write(poem)
    print(note := 'write returns the number of characters written')
    print('number of character written :', count)

print(note := 'we shall see that f handle is closed')
print(f.closed)
assert f.closed == True
print(note := 'If you’re not using the with keyword, then you should call f.close()')
print()
print('-----------------------')
print()

print(note := 'we can use the path functionality to confirm if file exists or not')
from os import path

print(note := 'we shall the file available now')
print(path.exists(poemFile))

print(note := 'we can use the read function to read entire content of file')
with open(poemFile) as f:
    print(f.read())

print()
print('-----------------------')
print()

print(note := 'or we can pass the size of that that we want to read from the file')
with open(poemFile) as f:
    print(f.read(37))

print()
print('-----------------------')
print()

print(note := 'or we can use readline to read each line once')

with open(poemFile) as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())

print()
print('-----------------------')
print()

print(note := 'we can also iterate over the file object to print each line, one at a time')
print(note := 'This is memory efficient, fast, and leads to simple code')
with open(poemFile) as f:
    for line in f:
        print(line)

print()
print('-----------------------')
print()

print(note := 'we can also get entire content of file as a list')
with open(poemFile) as f:
    print(list(f))

print()
print('-----------------------')
print()

print(note := 'python also supports opening file in binary mode')
print(note := 'we need to pass b with mode values for same')

with open(binFile, 'wb') as f:
    # b in start of string tells python that we are writing binary data
    f.write(b'721011081081113287111114108100')

with open(binFile, 'rb') as f:
    # we can move the file pointer via seek
    print(note := 'seek can take a whence value of 0,1,2')
    print(note := '0 means absolute value, i.e. from the start, this is the default value if nothing is passed')
    print(f.seek(8, 0))
    print(f.read(3))
    print(note := '1 means absolute value, i.e. from the current position')
    print(f.seek(4, 1))
    print(f.read(3))
    print(note := '2 means absolute value, i.e. from the end of file')
    print(f.seek(-4, 2))
    print(f.read(3))

print()
print('-----------------------')
print()

import os

print(note := 'we can use the remove function provided by os to remove/delete the file')
os.remove(poemFile)
os.remove(binFile)
print(path.exists(poemFile))
print(path.exists(poemFile))
assert path.exists(poemFile) == False
assert path.exists(binFile) == False

print()
print('-----------------------')
print()
