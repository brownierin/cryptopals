# cryptopals 01-05
# Implement repeating-key XOR
# Here is the opening stanza of an important work of the English language:
# Burning 'em, if you ain't quick and nimble
# I go crazy when I hear a cymbal

# Encrypt it, under the key "ICE", using repeating-key XOR.
# In repeating-key XOR, you'll sequentially apply each byte of the key; 
# the first byte of plaintext will be XOR'd against I, the next C, the 
# next E, then I again for the 4th byte, and so on.
# It should come out to:
# 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
# a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f

import binascii

string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
answer = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
key = "ICE"
solution = []

# binary = ''.join(format(ord(s), 'b') for s in initial_string)

def repeating_key_xor(string):
  # eventually this should scale per size of string
  for byte in range(0,len(string)):
    if byte % 3 == 0:
      piece = binascii.hexlify(chr(ord(string[byte]) ^ ord('I')))
      solution.append(piece)
      print "byte {0}, piece: {1}".format(byte, piece)
    elif byte % 3 == 1:
      piece = binascii.hexlify(chr(ord(string[byte]) ^ ord('C')))
      solution.append(piece)
    elif byte % 3 == 2:
      piece = binascii.hexlify(chr(ord(string[byte]) ^ ord('E')))
      solution.append(piece)
    else: 
      print "error"
  return ''.join(solution)

def key_xor(string,key):
  length = len(key)
  for byte in range(0,len(string)):
    modulo = byte % length
    piece = chr(ord(string[byte]) ^ ord(key[modulo]))
    piece = binascii.hexlify(piece)
    solution.append(piece)
  return ''.join(solution)

my_answer = repeating_key_xor(string)
# assert repeating_key_xor(string) == answer