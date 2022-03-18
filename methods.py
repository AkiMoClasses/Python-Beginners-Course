class Male:
    # Class Variable
    ADDRESS = 'INDIA'

    def __init__(self, name, level):
        self.name = name
        self.level = level

    # Instance methods
    def get_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name

    def get_level(self):
        print(self.level)

    # Class method
    @classmethod
    def set_citizenship_level(cls, name, amount):
        if amount < 100:
            level = 'basic'
        elif amount < 100 or amount < 500:
            level = 'Intermediate'
        else:
            level = 'Premium'
        return cls(name, level)

    # Class methods
    @classmethod
    def set_address(cls, address):
        cls.ADDRESS = address

    @classmethod
    def get_address(cls):
        print(cls.ADDRESS)

    # Static Method
    @staticmethod
    def waiting():
        print('Waiting...')


# Male().set_name()
# Instance Method
# male = Male('AkimoClasses')
# male.get_name()
# male.set_name('Akhilesh Singh')
# male.get_name()
#
# male2 = Male('Akhilesh Singh')
# male2.get_name()
# male2.set_name('AkimoClasses')
# male2.get_name()


# Class Method/Factory Method
# male = Male('Akhilesh Singh', 'Basic')
# Male.set_address('USA')
# male.get_level()
# male.get_address()
# male2 = Male.set_citizenship_level('Manoj', 1000)
# male2.get_name()
# male2.get_level()
# male.get_address()

# Static method
Male.waiting()
