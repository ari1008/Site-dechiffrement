from Cesar import César
from Vingere import Vingere

class Factory:
    @staticmethod
    def factory(chiffrement,test):
        return  globals()[chiffrement]().auto(test)

