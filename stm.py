class meta_persistent(type):
    def __new__(meta, classname, bases, dct):
        print 'Class Name:', classname
        print 'Bases:', bases
        print 'Class Attributes', dct
        return type.__new__(meta, classname, bases, dct)


class persistent(object):
    __metaclass__ = meta_persistent


class world(object):
    pass
