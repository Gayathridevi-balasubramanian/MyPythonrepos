import secrets
import string

def create_passwords(length=12):
    characters = string.ascii_letters + string.punctuation + string.digits
    #passwords = " ".join(secrets.choice(characters))
    passwords = " ".join(secrets.choice(characters) for _ in range(length)) 
    return passwords

print(create_passwords(13))

################
# Another method 
################

def generate_passwords(num , file_path='gayathri.txt'):
    # also try using 'diceware.wordlist.asc'
    with open(file_path,'r',encoding='utf-8') as f:
        lines = f.readlines()[0:6]
        words_list = [ words for line in lines for words in line.split()]
        #print(words_list)
        passwords = "".join([secrets.choice(words_list)  for i in range(num)])
        return passwords
try:
    print(generate_passwords(3))
except Exception as e:
    print(e)