import string
from Cesar import César

class Atbash:
   def auto(self, text):
      N = 155
      ans=''
      for s in text:
          if " " != s:
            character =chr(N - ord(s))
            ans+=character
          else:
              ans+=" "
      return ans
s="WXLWVHZRGWVXIBKGVIOVXSRUUIVZGYZHS"
#s="DCODESAITDECRYPTERLECHIFFREATBASH"
# V=21,H=3,Z=25,R=17,G=6,M=12,I=8 
