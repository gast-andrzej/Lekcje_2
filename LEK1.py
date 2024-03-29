import numpy as np
import seaborn as seab
import matplotlib.pyplot as pypl

'''
losowanie odpowiedzi

ciąg random numpy

n - ilość prób

size - kształt zwracanej tablicy

p - prawdopodobieństwo wystąpienia każdej liczby w przedziale n

'''
'''
seaplot z dodatkiem randomizera i division np 3
'''
# seab.distplot(np.random.binomial(n = 1, p = 0.5, size=1000), hist=True, kde= False)
# seab.distplot([[[0,0,0], [0,1,1], [5,6,8]]])
#
# pypl.show()


'''
Rozkład Poissona jest rozkładem dyskretnym.

Szacuje, ile razy zdarzenie może się zdarzyć w określonym czasie. 
np. Jeśli ktoś je dwa razy dziennie, jakie jest prawdopodobieństwo, że zje trzy razy?

Ma dwa parametry:

lam - częstość lub znana liczba wystąpień np. 2 dla powyższego problemu.

size — Kształt zwracanej tablicy.

'''
#
# x = np.random.poisson(lam=2, size=10)
#
# print(x)





# WIZUALIZACJA
# na size 1000 elementów
#
#
# kde - linia rzutu możliwego -> czyli inaczej względna w oparciu o parametry o największym zagęszczeniu występowania
#
#
#
# seab.distplot(np.random.poisson(lam=2, size=1000), kde=False)
#
# pypl.show()


'''

Różnica między rozkładem normalnym a rozkładem Poissona:

Rozkład normalny jest ciągły, podczas gdy poissona jest dyskretny.

Ale widzimy, że podobny do dwumianu dla wystarczająco dużego rozkładu Poissona, 
stanie się podobny do rozkładu normalnego z pewnymi odchyleniami i średnią.

'''

# seab.distplot(np.random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
# seab.distplot(np.random.poisson(lam=50, size=1000), hist=False, label='poisson')
#
# pypl.show()

'''
Różnica między rozkładem Poissona a rozkładem dwumianowym
Różnica jest bardzo subtelna, polega na tym, że:
    -rozkład dwumianowy dotyczy prób dyskretnych, 
    -podczas gdy rozkład poissona dotyczy prób ciągłych.

Ale dla bardzo dużego n i bliskiego zeru p rozkład dwumianowy jest 
prawie identyczny z rozkładem poissona, tak że n * p jest prawie równe lam.

'''

# seab.distplot(np.random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
# seab.distplot(np.random.poisson(lam=10, size=1000), hist=False, label='poisson')
#
# pypl.show()


'''
Jednolita dystrybucja
Używane do opisania prawdopodobieństwa, w którym każde zdarzenie ma równe szanse wystąpienia.

Np. Generowanie liczb losowych.

Ma trzy parametry:

a - dolna granica - domyślnie 0 .0.

b - górna granica - domyślnie 1.0.

size — Kształt zwracanej tablicy.

'''

# x = np.random.uniform(size=(2, 3))
#
# print(x)



# WIZUALIZACJA

#
# seab.distplot(np.random.uniform(size=1000), hist=True)
# seab.distplot(np.random.uniform(low=0,high=150,size=5))
# pypl.show()

'''
Dystrybucja logistyczna
Dystrybucja logistyczna jest używana do opisania wzrostu.

Szeroko stosowany w uczeniu maszynowym w regresji logistycznej, sieciach neuronowych itp.

Ma trzy parametry:

loc - średnia, gdzie jest szczyt. Domyślnie 0.

scale - odchylenie standardowe, płaskość rozkładu. Domyślnie 1.

size — Kształt zwracanej tablicy.

'''

# x = np.random.logistic(loc=0, scale=3, size=(2, 2))
#
# print(x)


# WIZUALIZACJA

# seab.distplot(np.random.logistic(loc=0,scale=10,size=1000), hist=False)
# seab.distplot(np.random.logistic(size=1000), hist=True)
#
# pypl.show()

'''
Różnica między dystrybucją logistyczną a normalną
Oba rozkłady są prawie identyczne, ale rozkład logistyczny ma większy obszar pod ogonami, co oznacza, że 
reprezentuje większe prawdopodobieństwo wystąpienia zdarzenia dalej od średniej.

Dla wyższej wartości skali (odchylenie standardowe) rozkłady normalny 
i logistyczny są prawie identyczne poza szczytem.

'''

# WIZUALIZACJA

# seab.distplot(np.random.normal(scale=2, size=1000), hist=True, label='normal')
# seab.distplot(np.random.logistic(size=1000), hist=True, label='logistic')
#
# seab.distplot(np.random.normal(scale=2, size=1000), hist=False, label='normal')
# seab.distplot(np.random.logistic(size=1000), hist=False, label='logistic')

# pypl.show()


'''
wewnątrz funkcja musi zwracać str w postaci parzyste or not po wprowadzeniu value


def func
    zmienne x = input
    try:
        warunek logiczny --> True by try się wykonał
        int(x)
        
        
        na potrzeby tak prostego rozwiązania posłużymy się instrukcją warunkową
        
        
        if x % 2 == 0:
            print("PARZYSTE")
        else:
            print("Nieparzyste")
            
            
        elementy wsadowe -> 0-100
        
        if 
        elif
        elif
        ... x100
        else
        
        python 3.11
            elem z C# czyli scenariusze case
            
            match index -- index == x
            
            case 1
            case 2
            case 3
            case4
            ...
        
        
    :except valueerror:
        print("Proszę nie bądź wrednym testerem i daj tutaj liczbę !")

'''

def func1():
    # x = input("Wprowadź liczbę ")
    while True:
        x = input("Wprowadź liczbę ")
        try:
            int(x)
            if int(x) % 2 == 0:
                print("PARZYSTE")
            else:
                print("Nieparzyste")
        except ValueError:
            print("Proszę nie bądź wrednym testerem i daj tutaj liczbę !")

# func1()

import random


def generator():
    c = []
    for i in range(0,100):
        c.append(random.randint(0,100))
    # return c
    print(c)


# generator()


'''
napisz mi generator losowych list zawierających elementy stringowe (generator uproszczony funkcyjny)
'''


'''
PROJEKT
liby? -> biblioteki

import string (domyślny encode UTF-8)



funkcja
    zmienne
    empty list 
    
    for i in string.asciiletter:
        append do listy
        
    


'''


import string


def gener_str_list():
    c = []
    b = []
    # randomlist = []
    # randUpper = []
    # randLower = []
    for i in string.ascii_letters:
        c.append(i)
    for i in range(0,int(len(c))-1):
        b.append(i)
    dictionar = dict(zip(b,c))
    print(dictionar)



    # print(c)
    # for i in range(0,100):
    #     randomlist.append(c[random.randint(0,int(len(c))-1)])
    # print(randomlist)
    #
    # for i in randomlist:
    #     if i == i.upper():
    #         randUpper.append(i)
    #     else:
    #         randLower.append(i)
    #
    # print(randUpper)
    # print(randLower)

# gener_str_list()


# #
# def func_list():
#     b = []
#     for i in range(0,3):
#         x = input()
#         try:
#             int(x)
#             b.append(int(x))
#         except:
#             b.append(x)
#     return b
#
# def func_app_list():
#     c = []
#     for i in range(0,2):
#         c.append(func_list())
#     return c
#
# def func_app_list_secondDim():
#     c = []
#     for i in range(0,2):
#         c.append(func_app_list())
#     print(c)
#
# func_app_list_secondDim()