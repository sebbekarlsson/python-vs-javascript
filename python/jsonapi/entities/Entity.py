class Entity(object):

    def __init__(self, id=None):
        self.id = id

    def export(self):
        return self.__dict__
