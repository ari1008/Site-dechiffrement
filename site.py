#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, request, template
from find_encryption import Find
from Cesar import César
from factory import Factory
import string
@route('/')
def index():
    return template('index',type_chiffrement="",cle="",texte="")


@route('/', method='POST')
def do_index():
    chaine = request.forms.get('texte_chiffrer')
    result = soluce(chaine)
    dechiffrement= Factory().factory(result[0],result[1])
    print(chaine)
    texte_dechiffrement=traitement(chaine,dechiffrement[1])
    return  template('index',type_chiffrement=result[0],cle=dechiffrement[0],texte=texte_dechiffrement)


def soluce(texte_chiffrer):
    text = Find(texte_chiffrer)
    text.automatisation()
    return text.chiffrement,text.text_upper

def traitement(chaine,texte):
    result=[]
    y=0
    for x in range(0,len(chaine)):
        if chaine[x] in string.ascii_letters:
            if chaine[x].islower():
                result.append(texte[y].lower())
            else:
                result.append(texte[y])
            y+=1
        else:
            result.append(chaine[x])
        dechiffrer = ''.join(result)
    return dechiffrer


run(host='localhost', port=8080, debug=True)