from django.test import TestCase

from rest_framework.mixins import UpdateModelMixin

from copy import copy, deepcopy
from rest_framework.serializers import ModelSerializer


class A(object):
    def test(self):
        print('from A')


class B(A):
    def test(self):
        print('from B')


class C(A):
    def test(self):
        print('from C')


class D(B):
    def test(self):
        print('from D')


class E(C):
    def test(self):
        print('from E')


class F(D, E):
    # def test(self):
    #     print('from F')
    pass


# print(F.__mro__)


class UpperAttrMetaClass(type):
    def __new__(cls, name, bases, attrs, *args, **kwargs):
        new_attrs = dict()
        for k, val in attrs.items():
            if callable(val) or k.startswith('_'):
                new_attrs[k] = val
            else:
                new_attrs[k.upper()] = val

        print('attrs', new_attrs)
        new_cls = super().__new__(cls, name, bases, new_attrs, *args, **kwargs)
        return new_cls


class W(metaclass=UpperAttrMetaClass):
    c = 10
    b = 20


# print(W.c)
# print(callable(W.c))

print(W.__dict__)


# class Dog:
#     __slots__ = ('name')
#
#     def  __init__(self,
#
#      name):
#     self.name = name
#
#         
#     
#
# def  test(self):
#
#         print('预先定义的test方法')
# d = Dog('Snoopy')
# d.age = 5


class Dog:
    __slots__ = ('name',)

    # name = 'dog'

    def __init__(self, name):
        self.name = name
        # self.age = 10

    def test(self):
        print('预先定义的test方法!', self.name)


d = Dog('Snoopy')
e = Dog('hehe')
# print(d.age)
d.test()
e.test()
d.name = 'hahah'
d.test()
print(d.__slots__)
print(e.__slots__)
# Create your tests here.


li = ['a', 'b', 'c', 'd']

for idx, val in enumerate(li):
    print(idx, val)


def new_enumerate(l):
    if not isinstance(l, (list, tuple)):
        raise Exception('必须是列表或者元组')
    l_len = len(l)
    for i in range(l_len):
        yield i, l[i]


for i, j in new_enumerate(li):
    print(i, j)
