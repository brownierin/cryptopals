"""
Now that you have ECB and CBC working:
Write a function to generate a random AES key; that's just 16 random bytes.

Write a function that encrypts data under an unknown key --- 
that is, a function that generates a random key and encrypts under it.

The function should look like:

encryption_oracle(your-input)
=> [MEANINGLESS JIBBER JABBER]
Under the hood, have the function append 5-10 bytes (count chosen randomly) 
before the plaintext and 5-10 bytes after the plaintext.

Now, have the function choose to encrypt under ECB 1/2 the time, and under 
CBC the other half (just use random IVs each time for CBC). 
Use rand(2) to decide which to use.

Detect the block cipher mode the function is using each time. 
You should end up with a piece of code that, pointed at a block box that 
might be encrypting ECB or CBC, tells you which one is happening.
"""

from .ten import aes_ecb_encrypt, aes_ecb_decrypt, aes_cbc_encrypt, aes_cbc_decrypt
from .nine import pad_block
import os
import random
import set_01.eight as eight

KEY_SIZE = 16 

def make_me_a_key():
    return os.urandom(KEY_SIZE)

def coin_flip():
    return random.randrange(0,2)

def encryption_oracle(data):
    key = make_me_a_key()
    padding_amount = random.randrange(5,11)
    padding = padding_amount * '\x00'
    data = padding + data + padding
    data = pad_block(data, KEY_SIZE)
    flip = coin_flip()
    if flip == 0:
        return aes_ecb_encrypt(key, data), flip
    else:
        return aes_cbc_encrypt(key, data), flip

def detect(ciphertext):
    results = {ciphertext: eight.check_the_line(ciphertext)} 
    answer = eight.detect_ecb_mode(results)
    if answer == {}:
        print "This ciphertext is encrypted in CBC mode"
        return 1
    for potential in answer:
        most_repeated_block = max(results[potential], key=lambda i: results[potential][i])
        print "This ciphertext is encrypted in ECB mode"
        print "The block {!r} was repeated {} times".format(most_repeated_block, results[potential][most_repeated_block])
        return 0

def main():
    print "===test case 1==="
    plaintext = "YELLOW SUBMARINE" *15
    ciphertext, flip = encryption_oracle(plaintext)
    print "Ciphertext is: {!r}".format(ciphertext)
    assert detect(ciphertext) == flip

if __name__ == '__main__':
    main()
