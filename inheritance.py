# Parent Class
class Human:
    def walk(self):
        print('walk')


# Child Class
class Male(Human):
    pass


class Female(Human):
    pass


# Male().walk()
# Female().walk()

'==============================================='


# Parameterized __init__ & super
# Parent Class
class Human:
    def __init__(self, nose, eyes, ears):
        self.nose = nose
        self.ears = ears
        self.eyes = eyes

    def walk(self):
        print('walk')


# Child Class
class Male(Human):
    def walking(self):
        super().walk()


class Female(Human):
    pass


# Male(nose=1, eyes=2, ears=2).walking()
# Female(nose=1, eyes=2, ears=2).walk()

'========================================================'


# Method Override
class Human:
    def walk(self):
        print('walk')


class Male1(Human):
    def walk(self):
        print('Not able to walk')


class Male2(Human):
    pass


Male1().walk()
Male2().walk()
