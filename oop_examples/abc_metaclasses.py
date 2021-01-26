from abc import ABC, ABCMeta, abstractmethod, abstractclassmethod

# class Foo:
#     """My Foo class"""
#     bar = True

#     def echo_bar(self):
#         print(self.bar)

#     @classmethod
#     def echo_name(cls):
#         print(cls.__name__)


# альтернативное создание класса, который выше
# Foo = type('Foo', (), {'bar': True})
# наследуемый класс от Foo
# NewFoo = type('NewFoo', (Foo,), {'spam': 'eggs'})


def print_class_demo(klass):
    f = klass()
    print(klass, 'Принадлежит типу type:', klass.__class__, type(f))
    print(f, f.__class__, 'Экземпляр класса Foo:', type(f))
    # print(f.echo_name())
    # print(klass.echo_name())
    f.bar = False
    print(klass.bar, f.bar)


# print(Foo, type(Foo))
# print_class_demo(Foo)
# print(NewFoo)
# nf = NewFoo
# print(nf.spam)
# print(nf.mro())


# Метакласс - это класс для классов (тип для классов)

class MyMetaclass(type):
    def __new__(cls, name, bases, dct, *args, **kwargs):
        """
        name - имя класса
        based - от чего наследуется класс
        dct - docstring
        :type kwargs: object
        """
        print('New class', name)
        print('Bases:', bases)
        print('New attr:', dct)
        dct['SPAM'] = 'EGGS'  # добавили атрибут всем создаваемым классам
        new_cls = super().__new__(cls, name, bases, dct, *args, **kwargs)
        print('created new cls:', new_cls)
        return new_cls


# Foo = MyMetaclass('Foo', (), {})
# NewFoo = MyMetaclass('NewFoo', (Foo,), {'spam': 'eggs'})
# print(Foo, "Добавленный атрибут в метаклассе:", Foo.SPAM)
# print(NewFoo, NewFoo.SPAM)

class FileManagerABC(metaclass=ABCMeta):

    @abstractmethod
    def read_file(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def write_to_file(self, text: str) -> int:
        raise NotImplementedError


class FileManager(FileManagerABC):

    def __init__(self, filename: str):
        self._filename = filename

    def read_file(self) -> str:
        with open(self._filename, 'r') as f:
            text = f.read()
            # f.seek(0)
            return text

    def write_to_file(self, text: str) -> int:
        with open(self._filename, 'a') as f:
            count = f.write(text)
            print('written text', text)
            return count


file_manager = FileManager('file.txt')
print(file_manager.read_file())
print(file_manager.write_to_file(' hello'))

