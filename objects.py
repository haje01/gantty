
class Task(object):
    def __init__(self, name, start, end, done, owners, depend):
        self.name = name
        self.start = start
        self.end = end
        self.done = done
        self.owners = owners
        self.depend = depend

class Milestone(object):
    def __init__(self, name, start, depend):
        self.name = name
        self.start = start
        self.depend = depend

