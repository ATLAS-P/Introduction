



def encryptOne(char, rot):
    return chr(ord(char) + rot)

def decryptOne(char, rot):
    return chr(ord(char) - rot)

def encrypt(str, rot):
    encoded = ""

    for char in str:
        encoded += encryptOne(char, rot)

    return encoded

def decrypt(str, rot):
    decoded = ""

    for char in str:
        decoded += decryptOne(char, rot)

    return decoded


my_secret = '''
Ut at tristique neque, sit amet vestibulum quam.
Phasellus porttitor iaculis aliquet.
Nulla elementum, mi nec posuere lobortis, velit enim rhoncus risus, ut mollis dui eros eget massa.
Vestibulum commodo enim ut facilisis vulputate.
'''

hidden = encrypt(my_secret, 60)
visible = decrypt(hidden, 60)

print(my_secret)
print(hidden)
print(visible)