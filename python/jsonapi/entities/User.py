from jsonapi.entities.Entity import Entity


class User(Entity):

    def __init__(
            self,
            username=None,
            email=None,
            password=None,
            *args,
            **kwargs
    ):
        Entity.__init__(self, *args, **kwargs)
        self.username = username
        self.email = email
        self.password = password
