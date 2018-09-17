# Single-byte XOR cipher
# The hex encoded string: 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.
# You can do this by hand. But don't: write code to do it for you.
# How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

import binascii 
import string

def single_byte_xor(binary):
  results = {}
  for xor_key in range(256):
    string = ''.join(chr(ord(b) ^ xor_key) for b in binary)
    results[xor_key] = string
  return results

def check_if_printable(results):
  printable_results = {}
  for key,result in results.iteritems():
    if set(result).issubset(set(string.printable)):
      printable_results[key] = result
  return printable_results

def max_spaces(results):
  return max(results.items(), key=lambda (key,string): string.count(' '))

def main():
  results = {}
  hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
  binary = binascii.unhexlify(hex_string)
  results = single_byte_xor(binary)
  printable = check_if_printable(results)
  print max_spaces(printable)

if __name__ == '__main__':
  main()
