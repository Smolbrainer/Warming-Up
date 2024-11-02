import random
import string

length = int(input("How long do you want the password to be? "))
password = ''.join(random.choices(string.hexdigits + string.punctuation, k=length)) # a string that joins the random choices of hexdigits and punctiation. k number of timesr
#hexdigits = 0123456789abcdefABCDEF
#punctiation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
print(password)