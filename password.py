import random
import string
charLetter=string.ascii_letters
digit=string.digits
symbols=string.punctuation
total=charLetter+digit+symbols
length=int(input("Enter the length of password:-"))
x=random.sample(total,length)
password="".join(x)
print("\n",password,"\n")