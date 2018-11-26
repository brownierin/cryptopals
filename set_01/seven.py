# The Base64-encoded content in this file has been encrypted via AES-128 in ECB mode under the key
# "YELLOW SUBMARINE".
# (case-sensitive, without the quotes; exactly 16 characters; 
# I like "YELLOW SUBMARINE" because it's exactly 16 bytes long, and now you do too).
# Decrypt it. You know the key, after all.
# Easiest way: use OpenSSL::Cipher and give it AES-128-ECB as the cipher.
# Do this with code.
# You can obviously decrypt this using the OpenSSL command-line tool, 
# but we're having you get ECB working in code for a reason. 
# You'll need it a lot later on, and not just for attacking ECB.

import base64
from Crypto.Cipher import AES

def file_read_decode(filename):
  file = open(filename,'r')
  whole_file = []
  for line in file:
    whole_file.append(base64.b64decode(line))
  return ''.join(whole_file)

def aes_ecb_decrypt(key, data):
  cipher = AES.new(key, AES.MODE_ECB)
  plaintext = cipher.decrypt(data)
  return plaintext

if __name__ == '__main__':
  key = "YELLOW SUBMARINE"
  data = file_read_decode('7.txt')
  plaintext = aes_ecb_decrypt(key, data)
  print "===PLAINTEXT==="
  print plaintext
