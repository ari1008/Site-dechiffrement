import string
from Cesar import César
class Vingere(César):


    def indice_coincidence(self,chaine):
        app = self.apparitions(chaine)
        s = sum (n * (n - 1) for n in app)
        somme = sum(app)
        return s / (somme * (somme - 1))
    
    def apparitions(self,chaine):
        app = [0] * 26
        for c in chaine :
            if c in string.ascii_uppercase:
                app[ord(c) - ord('A')] += 1
        return app

    def liste_indices(self,chaine, n):
        res=[0]
        for i in range(1, n + 1):
            res.append(sum(self.indice_coincidence(chaine[k::i]) for k in range(i)))
            res[-1] /= i
        return res

    def cherche_cle_vigenere(self,chaine, n) :
        return "".join( chr(ord('A') + self.cherche_cle_cesar(chaine[i::n])) for i in range(n))
    
    def cherche_longueur_cle(self,chaine, seuil=0.068, nmax=12):
        p = [(lcle, i) for lcle, i in enumerate(self.liste_indices(chaine, nmax)) if i > seuil]
        return min(p)
    

    
    
    def dechiffre_vigenere(self,s,cle):
        l = []
        for i, c in enumerate(s):
            if c in string.ascii_uppercase:
                c = ord(c) - ord(cle[i % len(cle)])
                c = chr(c % 26 + ord('A'))
            l.append(c)
            texte_déchiffrer = "".join(l)
        return texte_déchiffrer
    
    def auto(self,chaine):
        lgcle, indice = self.cherche_longueur_cle(chaine)
        cle = self.cherche_cle_vigenere(chaine, lgcle)
        return cle, self.dechiffre_vigenere(chaine, cle)
s= "SORHZIROWPQXJSPTHICGSBAISORHHSJGPTGGPGHTQVXHYGSWTQVTHIAOTGSQXSVTEYTGXXCRPJMSSVRSWIZEAORVIISIGWWJUFIROVASWEFMCQMESWSSWDZYIWSCDEGHMRIPXSVTAICHUJORSWPHOKXHHTGGWWJUFIHZIHDPJGWXATASWSSTTBHTBXSIKTBMTRIRVEFIIXRMDAITHTTIZTBXTHVTASSWJXSWTBKTBIGOPXZRNOTPGHPIXGSQDMICEYTRIHGENSVHIGRSWHWZTAICHICGISWVXUIPBXHIMKORIZIHDVDPEQWPXHIHHSJHIHZIHZECUYTGUJWZDIWHCRIQSCBYTGNJGUJOGTEYTJSJGENSDIFSJJIAOFDBRTAEXGHPBWASGWWJUFIFIMCCYHCGRITTHSJHISWJUWGJZXTOGTHIVOVSSXPWXGSWDZYTDEGZEHWKCOXJFIASVTPYHGYGZIBCXZWHSBIHHTDGWXPPTEYTRECGPPZECUYTORVZEXGIHORHQIIHIRWVRCRHHECQIYOYGOMHQSBAICQIBSWTGWPWWEOVASWEOKCCPTHPTTVPBEXGGDAQTSXPBXASWAORVIIHRECGPTGUJSPASWJBTXFEISHTGQTFWTGTPURDZIHOYGOMIRYASTAIWCOXJFIAZIBSRISRUSVBSVJBWTQVTHHTQIIHICOXJFIBOMHRECGPTQEHOGIIIAXIEFIHIQPWUJSPTQVNDXDUVPAQTSXPWXPBKAOMH"
