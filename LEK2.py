'''
1. Powtórzenie

1.1* OOP

2. Wstęp do automatów

'''
import math
import random

'''
USUWANIE OBIEKTÓW Z LISTY

metody

.pop() - usuwa ostatni element z listy

.clear() - wywala wszystko

.remove() - usuwa wybrany element
'''
#
# def _func1():
#     c = []
#     for i in range(0,random.randint(20,40)):
#         b = random.randint(0, 20)
#         c.append(b)
#     return c
#
# def func2():
#     d = []
#     c = _func1()
#     g = []
#     h = []
#     for i in c:
#         if i % 2 == 0:
#             d.append(i)
#         else:
#             pass
#     for i in d:
#         j=i*i
#         g.append(j)
#     for i in c:
#         j = i*i
#         h.append(j)
#     gs = sum(g)
#     hs = sum(h)
#     print(gs)
#     print(hs)
#
# func2()

import string


'''
DICT COMPREHENSION

'''
# def _func1():
#     keys = []
#     value = []
#     for i in string.ascii_letters:
#         value.append(i)
#     for i in range(0,int(len(value))):
#         keys.append(i)
#     dicter = dict(zip(keys,value))
#     print(dicter)
#
# _func1()

import string


class _obiekcik:
    # def _private(self = None):
    #     f = list(range(0,10))
    #     return f
    # def _private2(self = None):
    #     g = obiekcik._private()
    #     k = []
    #     for i in g:
    #         j = i*i
    #         k.append(j)
    #     return k
    # def __init__(self):
    #     b = obiekcik._private2()
    #     for i in b:
    #         if i%2==0:
    #             print("parzyste")
    #         else:
    #             print("npar")
    #
    # def _privfunc(self=None):
    #     g = list(range(0,21))
    #     return g
    # def func1(self=None):
    #     b = []
    #     c = _obiekcik._privfunc()
    #     b.append(c)
    #     yield b
    def _func_login(self=None):
        g = []
        for i in string.ascii_letters:
            g.append(i)
        login = []
        for i in range(0,10):
            f = int(len(g))-1
            login.append(g[random.randint(0,f)])
        return login
    def _func_passwd(self=None):
        g = []
        for i in string.ascii_letters:
            g.append(i)
        passwd = []
        for i in range(0,20):
            f = int(len(g))-1
            passwd.append(g[random.randint(0,f)])
        return passwd

    def gener(self=None):
        fulldata = []
        fulldata.append(_obiekcik._func_login())
        fulldata.append(_obiekcik._func_passwd())
        yield fulldata








def func1():
    g = []
    for i in range(0,5):
        b = next(_obiekcik.gener())
        g.append(b)
    print(g)

func1()


