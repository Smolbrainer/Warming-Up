import random
import string

length = int(input("How long do you want the password to be? "))
password = ''.join(random.choices(string.hexdigits + string.punctuation, k=length))
print(password)