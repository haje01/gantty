class Job(object):
    def __init__(self, name, start, depend):
        self.name = name
        self.start = start
        self.depend = depend
    def __str__(self):
        return self.__unicode__().encode('utf-8')
    def __unicode__(self):
        attrs = ['%s="%s"' % (attr, getattr(self, attr)) for attr in dir(self) if not attr.startswith('__') and getattr(self, attr)]
        return u'<%s %s/>' % (self.__class__.__name__, ','.join(attrs))


class Task(Job):
    def __init__(self, parent, name, start, end, done, owners, depend):
        Job.__init__(self, name, start, depend)
        self.parent = parent
        self.end = end
        self.done = done
        self.owners = owners

class Milestone(Job):
    def __init__(self, name, start, depend):
        Job.__init__(self, name, start, depend)

