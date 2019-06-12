# CBC mode is a block cipher mode that allows us to encrypt irregularly-sized messages, 
# despite the fact that a block cipher natively only transforms individual blocks.
# In CBC mode, each ciphertext block is added to the next plaintext block before the next call to the cipher core.
# The first plaintext block, which has no associated previous ciphertext block, is added 
# to a "fake 0th ciphertext block" called the initialization vector, or IV.
# Implement CBC mode by hand by taking the ECB function you wrote earlier, making it encrypt 
# instead of decrypt (verify this by decrypting whatever you encrypt to test), and using your XOR function from the previous exercise to combine them.
# The file here is intelligible (somewhat) when CBC decrypted against "YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c)

import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

INITIAL_IV = '\x00' * 16

def file_open_decode_b64(filename):
  with open(filename, 'r') as file:
    whole_file = [base64.b64decode(line.strip('/n')) for line in file]
    return ''.join(whole_file)

def aes_ecb_encrypt(key, data):
  backend = default_backend()
  cipher = Cipher(algorithms.AES(key), modes.ECB, backend=backend)
  encryptor = cipher.encryptor()
  ciphertext = encryptor.update(data) + encryptor.finalize()
  return ciphertext

def aes_ecb_decrypt(key, data):
  backend = default_backend()
  cipher = Cipher(algorithms.AES(key), modes.ECB, backend=backend)
  decryptor = cipher.decryptor()
  plaintext = decryptor.update(ct) + decryptor.finalize()
  return plaintext

def iv_xor(string1, string2):
  solution = []
  for byte in range(len(string1)):
    item = chr(ord(string1[byte]) ^ ord(string2[byte]))
    solution.append(item)
  return "".join(solution)

def aes_cbc_encrypt(key, data):
  key_size = len(key)
  number_of_blocks = len(data) / key_size
  ciphertext = []
  next_iv = INITIAL_IV
  for block in range(number_of_blocks):
    position = key_size * block
    text = iv_xor(data[position:(position+key_size)], next_iv)
    ciphertext.append(aes_ecb_encrypt(key, text))
    next_iv = ciphertext[block]
  return "".join(ciphertext)

def aes_cbc_decrypt(key, data):
  key_size = len(key)
  number_of_blocks = len(data) / key_size
  plaintext = []
  next_iv = INITIAL_IV
  for block in range(number_of_blocks):
    position = key_size * block
    text = aes_ecb_decrypt(key, data[(position):(position+key_size)])
    plain = iv_xor(text, next_iv)
    plaintext.append(plain)
    next_iv = data[(position):(position+key_size)]
  return "".join(plaintext)

def main():
  key = 'YELLOW SUBMARINE'
  data = file_open_decode_b64('10.txt')
  decryption = aes_cbc_decrypt(key, data)
  print "{!r}".format(decryption)
  return decryption

def test():
  key = 'YELLOW SUBMARINE'
  data = "hello there hello there hello there hello there\n"
  encryption = aes_cbc_encrypt(key, data)
  print "==ENCRYPTED== \n{!r}".format(encryption)
  decryption = aes_cbc_decrypt(key, encryption)
  print "==DECRYPTED== \n {!r}".format(decryption)
