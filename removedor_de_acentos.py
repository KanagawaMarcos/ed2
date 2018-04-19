#!/usr/bin/env python3

from unicodedata import normalize

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

if __name__ == '__main__':
    from doctest import testmod
    testmod()