
import re
class Findhash:
    
    def __init__(self,chaine):
        self.hash  = {
             "SHA-1":r"\b[0-9a-f]{5,40}\b",
             "MD5":r"^[a-f0-9]{32}$", 
             "SHA256":r"\b[A-Fa-f0-9]{64}\b", 
             "SHA512":r"^\w{128}$",
            }
        self.chaine=chaine
    
    def auto(self):
        for key, values in self.hash.items():
            re.findall(values, self.chaine)
            return key, self.chaine
        return 0
s="f610433d3d23b2ed59349e254a2906985589ac96518fb7b2cbf650eacabce1798febd6cd0506d3d2b381e0d60664f02ee05de7adfcfbd476bc117939be64c55b"
#print(Findhash(s).auto())


