class Sample(object):
    pass


x = Sample()


class Dog(object):

    # Class Object attribute
    _species = "mammal"

    def __init__(self, name, breed, fur=True):
        self._breed = breed
        self._name = name
        self._fur = fur

    def set_species(self, species):
        self._species = species

    def get_species(self):
        return self._species


sam = Dog(name="Sammy", breed="Huskie")


class Circle(object):

    PI = 3.14

    def __init__(self, radius=1):
        self._radius = radius

    def area(self):
        return (self._radius**2) * self.PI

    def set_radius(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius


c = Circle(radius=100)
print c.area()


# NOTE: inheritance

class Animal(object):
    def __init__(self):
        print "Animal created"

    def whoAmI(self):
        print "Animal"

    def eat(self):
        print "Eating"


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print "Cat created"

    def whoAmI(self):
        print "Cat"

    def bark(self):
        print "Woof!"

# NOTE: spcial method


class Book(object):
    def __init__(self, title, author, pages):
        print "A book is created"
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title:%s , author:%s, pages:%s " % (self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print "A book is destroyed"


book = Book("Python Rocks!", "Jose Portilla", 159)

# Special Methods
print book
print len(book)
del book
