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
s="WXLWV HZRG WVXIBKGVI OV XSRUUIV ZGYZHS"

test=Atbash().auto(s)
print(test)
