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