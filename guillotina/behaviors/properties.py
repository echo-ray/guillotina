

class ContextProperty:

    def __init__(self, attribute, default):
        self.__name__ = attribute
        self.default = default

    def __get__(self, inst, klass):
        if inst is None:
            return self

        return getattr(inst.context, self.__name__, self.default)

    def __set__(self, inst, value):
        setattr(inst.context, self.__name__, value)
        inst.context._p_register()


class FunctionProperty:

    def __init__(self, attribute, getter, setter):
        self.__name__ = attribute
        self.setter = setter
        self.getter = getter

    def __get__(self, inst, klass):
        if inst is None:
            return self

        return self.getter(inst)

    def __set__(self, inst, value):
        return self.setter(inst, value)
