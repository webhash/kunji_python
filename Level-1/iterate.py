print("Hello World!!")

print()
print('-----------------------')
print()
print(note := 'Iterables are all the python object that support the feature of looping through them by simple for loop')

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in l:
    print(i)

print(note := 'list, string, sets, dict, tuple are all iterable')
print(note := 'this feature is made possible by __next__ and __iter__ methods - \
we shall see that an iterable must have support for __iter__, __next__ is optional')
print(note := 'as name suggests __next__ returns the next object , and __iter__ returns the object itself')
print(note := 'what if we want to create a user defined class that support the iterable feature')
print(note := 'we have to add the __next__ and __iter__ method to them')

print()
print('-----------------------')
print()


class HouseParty:
    def __init__(self, limit):
        self.limit = limit
        self.people = ['adam', 'eve', 'snake', 'tree', 'lord']
        self.index = 0;

    def __iter__(self):
        print('__iter__called')
        return self

    def __next__(self):
        print('__next__called')
        if self.index >= self.limit:
            raise StopIteration
        else:
            pos = self.index
            self.index += 1
            return 'invitee : ' + self.people[pos]


hp = HouseParty(5)
for i in hp:
    print(i)

print(note := 'as we reached the limit of iterator, the loop ended')
print(note := 'and we wont be able to again iterate over this object, \
we have to again create a new object and loop through it')
print(note := 'we shall see the call to iter and next but no data shall be printed as we have reached the limit')
for i in hp:
    print(i)

print(note := 'we shall see the call to iter and next and data shall be printed as we have created a new object')

hp = HouseParty(2)
for i in hp:
    print(i)

print()
print('-----------------------')
print()

print(note := 'this behavior is different from the iterable of list, etc, \
as we can loop through them again and again')

print(note := 'some must be missing ...')

print(note := 'we have to separate the data from the iterator, so that we need not to initiate the data each time')

print(note := 'but then our main data class wont be iteratable, we have to use the iterator')

print(note := 'solution is to add the __iter__ in Party class that returns the iterator')


class IterateParty:
    def __init__(self, partyObj):
        self._index = 0
        self._partyObj = partyObj

    def __iter__(self):
        print('iterate __iter__called')
        return self

    def __next__(self):
        print('iterate __next__called')
        if self._index >= len(self._partyObj):
            raise StopIteration
        else:
            pos = self._index
            self._index += 1
            return 'invitee : ' + self._partyObj._people[pos]


class Party:
    invitee = ['adam', 'eve', 'snake', 'tree', 'lord']

    def __init__(self, numbers):
        if (numbers <= len(self.invitee)):
            self._people = self.invitee[0:numbers]
        else:
            self._people = self.invitee

    def __len__(self):
        print('Party __len__called')
        return len(self._people)


print(note := 'first we shall create the party object')
p = Party(4)
print(note := 'then we initiate the party iterator by passing the party object created')
p_iter = IterateParty(p)
print(note := 'and then we can iterate over the party object via the iterator created')
for invitee in p_iter:
    print(invitee)

print(note := 'But here we need to call the party iterate to iterate over party object')
print(note := 'there is a way we can directly use the Party object rather than initiating th e iterator first')

print()
print('-----------------------')
print()


class NewParty:
    invitee = ['adam', 'eve', 'snake', 'tree', 'lord']

    # self containg the iterater
    class IterateParty:
        def __init__(self, partyObj):
            self._index = 0
            self._partyObj = partyObj

        def __iter__(self):
            print('iterate __iter__called')
            return self

        def __next__(self):
            print('iterate __next__called')
            if self._index >= len(self._partyObj):
                raise StopIteration
            else:
                pos = self._index
                self._index += 1
                return 'invitee : ' + self._partyObj._people[pos]

    def __init__(self, numbers):
        if (numbers < len(self.invitee)):
            self._people = self.invitee[0:numbers]
            self.numbers = numbers
        else:
            self._people = self.invitee
            self.numbers = len(self.invitee)

    def __len__(self):
        print('NewParty __len__called')
        return len(self._people)

    def __iter__(self):
        print('NewParty __iter__ called')
        return IterateParty(self)


np = NewParty(5)
for invitee in np:
    print(invitee)

print(note := 'we can use the next and iter function to iterate over the object')
print(next(iter(np)))

print()
print('-----------------------')
print()

print(note := 'lists are also sequences i.e we can refer to individual items via index')
print(note := 'our NewParty doesnt support that...')
print(note := 'welcome to __getitem__ method')


class FinalParty:
    invitee = ['adam', 'eve', 'snake', 'tree', 'lord']

    # self containg the iterater
    class IterateParty:
        def __init__(self, partyObj):
            self._index = 0
            self._partyObj = partyObj

        def __iter__(self):
            print('iterate __iter__called')
            return self

        def __next__(self):
            print('iterate __next__called')
            if self._index >= len(self._partyObj):
                raise StopIteration
            else:
                pos = self._index
                self._index += 1
                return 'invitee : ' + self._partyObj._people[pos]

    def __init__(self, numbers):
        if (numbers < len(self.invitee)):
            self._people = self.invitee[0:numbers]
            self.numbers = numbers
        else:
            self._people = self.invitee
            self.numbers = len(self.invitee)

    def __len__(self):
        print('FinalParty __len__called')
        return len(self._people)

    def __iter__(self):
        print('FinalParty __iter__ called')
        return IterateParty(self)

    def __getitem__(self, index):
        print('Getting the invitee at index ', index)
        if (index < self.numbers):
            return self.invitee[index]
        else:
            raise IndexError


fp = FinalParty(3)

print(fp[1])

try:
    print(fp[3])
except IndexError:
    print("we shall throw the index error")

print(note := 'we can use the next and iter function to iterate over the object')
piter = iter(fp)
print(next(piter))
print(next(piter))

print(note := 'or we can use the for loop')
for i in fp:
    print(i)

print()
print('-----------------------')
print()

print(note := 'lets quickly look at iter() function')
print(note := 'iter supports two constructor , iter(object-> where object supports its own iterable)')
print(note := 'and iter(callable, sentinel) where callable is called until the sentinel value is not hit')


def pow2():
    i = 1

    def inside():
        nonlocal i
        ret = 2 ** i
        i += 1
        return ret

    return inside


print(note := 'here basically the python is creating an iterator for us')
iterate_pow = iter(pow2(), 1024)

print(note := 'below shall print the result till 1024 not hit')
for v in iterate_pow:
    print(v)

print(note := 'if you put sentinel value as 1025, you shall have an infinite loop as 1025 is not power of two')

print()
print('-----------------------')
print()
