
class Name(object):
   
    def __init__(self, name):
        self.name = name

    def title(self):
        if self.name == 'ss':
            return 'Dr.'
        elif self.name == 'fe':
            return 'Mr.'
        else:
            return 'Shitty'

