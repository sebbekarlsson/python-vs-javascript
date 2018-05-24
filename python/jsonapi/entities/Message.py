from jsonapi.entities.Entity import Entity
import datetime
import time


class Message(Entity):

    def __init__(
            self,
            message=None,
            created=datetime.datetime.now(),
            sender=None,
            receiver=None,
            *args,
            **kwargs
    ):
        Entity.__init__(self, *args, **kwargs)
        self.message = message
        self.created = time.mktime(created.timetuple())\
            if isinstance(created, datetime.datetime) else created
        self.sender = sender
        self.receiver = receiver
