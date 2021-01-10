#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
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
    upload  = request.files.get('file')
    if upload :
        name, ext = os.path.splitext(upload.filename)
        if ext not in ('.txt'):
            return 'File extension not allowed.'
        save_path = "file/"+ name + ext
        upload.save(save_path)
        f = open(save_path, "r")
        chaine = f.read()
        f.close()
        os.remove(save_path)
    else:
        chaine = chaine = request.forms.texte_chiffrer
    result = soluce(chaine)
    print(result)
    return  template('index',type_chiffrement=result[0],cle=result[1],texte=result[2])


def soluce(texte_chiffrer):
    text = Find(texte_chiffrer)
    test = text.automatisation()
    if test == "hash":
        return "hash","Y a pas de clé",text.text
    else:
        dechiffrement= Factory().factory(test[0],test[1])
        texte_dechiffrement=traitement(chaine,dechiffrement[1])
        return test[0], dechiffrement[0],texte_dechiffrements

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