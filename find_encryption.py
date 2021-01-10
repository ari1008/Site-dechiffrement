import string
from Hash import Findhash
class Find:
    def __init__(self, text):
        self.text=text
        self.chiffrement=""
        self.text_upper=""

    def automatisation(self):
        testhash = Findhash(self.text).auto()
        if testhash !=  0:
            self.chiffrement = testhash[1]
            return  "hash"
        chaine_upper = self.majuscules(self.text)
        if self.freqAtbash(chaine_upper):
            self.chiffrement = "Atbash"
        else:
            chaine = self.freq(chaine_upper)
            indice = self.incide_coincidence(chaine)
            self.chiffrement = self.typechiffrement(indice)
        return "chifrement"
    
    @staticmethod
    def incide_coincidence(chaine):
        somme = sum(chaine)*(sum(chaine)-1)
        ic=sum(n*(n-1) for n in chaine)
        return ic/somme
    
    def majuscules(self,text):
        chaine_upper=[]
        result=""
        for x in range(len(self.text)):
            if self.text[x] in string.ascii_letters:
                chaine_upper.append(''.join(str.upper(self.text[x])))
        self.text_upper=''.join(chaine_upper)
        return    self.text_upper

    @staticmethod
    def freq(chaine_upper):
        alphabet = [0] * 26
        for c in chaine_upper:
            alphabet[ord(c)-ord('A')]+=1
        return alphabet
    
    @staticmethod
    def typechiffrement(indice):
        if indice>=0.04 and indice<=0.05:
            return "Vingere"
        else:
            return "César"
    
    @staticmethod
    def freqAtbash(string):
        alphabet = [0] * 26
        for c in string:
            alphabet[ord(c)-ord('A')]+=1
        sumAstbash = alphabet[1] + alphabet[5] + alphabet[11] + alphabet[17]+ alphabet[20]+ alphabet[25]
        stat = sum(alphabet)-sumAstbash
        result = stat/sumAstbash
        print(result)
        if result<=3:
            return 1
        else:
            return 0