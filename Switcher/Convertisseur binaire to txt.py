#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string


def repr_bin(s):
    """
    renvoie la représentation binaire de la chaîne de caractère s en UTF8
    sb = version binaire de s
    """
    sb = ""
    for c in s :
        sb += bin(ord(c))[2:].zfill(8)
    print(sb)
    return sb

def BinaryToDecimal(binary):
    string = int(binary, 2)
    print(string)
    return string

def decode_binaire(sb) :
    """
    sb = version binaire de s
    Connaissant sb, la fonction renvoie s
    """ 
    s =' '
    for i in range(0, len(sb), 7):
        temp_data = sb[i:i + 7]
        decimal_data = BinaryToDecimal(temp_data)
        s = s + chr(decimal_data)
    print(s)
    return s
    
#########################################    
    
def choose1() :
    print('=== txt to bin ===')
    s = input("Txt to convert : ")
    repr_bin(s)
   
def choose2() :
    print('=== bin to txt ===')
    sb = str(input("Bin to convert : "))
    decode_binaire(sb)

########################################

print('=== CHOOSE ===')
choose = """1) txt to bin
2) bin to txt

Your choice : """
c = int(input(choose))
if c == 1 :
    choose1()
if c == 2 :
    choose2()
