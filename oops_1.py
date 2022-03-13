# class is created
# Always use camelcase for class name
class Human:
    pass


# How to create constructor
class Human:
    # Class variable
    # Always in CAPS
    ADDRESS = "India"

    # Default Constructor
    # def __init__(self):
    #     print('Default Constructor')

    # Parameterized constructor
    # When we want to restrict object creation with minimum data.
    def __init__(self, name):
        # Instance variable
        # Always in lower case. In case two words, use  underscore (_) between them
        self.name = name


# Why we need constructor
# To create object
name1 = "AkimoClasses"
name2 = "Akhilesh Singh"

# Instance/object
human1 = Human(name=name1)
human2 = Human(name=name2)

Human.ADDRESS = "New Delhi"
print(Human.ADDRESS)
print(human1.ADDRESS)
print(human2.ADDRESS)

human2.name = "Please like & subscribe to the channel"
print(human1.name)
print(human2.name)
