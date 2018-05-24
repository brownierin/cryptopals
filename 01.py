# cryptopals challenge 1

# Convert hex to base64
# The string: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# Should produce: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
# So go ahead and make that happen. You'll need to use this code for the rest of the exercises.
# Cryptopals Rule
# Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

original_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
correct_base64 = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

# one-liner
solution = original_hex.decode('hex').encode('base64')[:-1]

assert solution == correct_base64
print "Case 1: The one-liner passed!"

# let's do this from scratch though
# base64 values correspond with 0-63 in below string array
base64_values = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def hex_to_base64(hexstring):
  # base64 works on 6 bits (2^6)
  # hex is 4 bits

  bit_string = hex_to_bits(hexstring)
  length = len(bit_string) / 6
  remainder = len(bit_string) % 6
  padding = length % 4
  counter = 0
  base64_string = ''

  # process six bytes at a time
  while length > counter:
    position = (counter * 6)
    current_six_bits = bit_string[position:position+6]
    base64_string += bits_to_base64(current_six_bits)
    counter += 1

  # dealing with remainders, including padding
  if remainder != 0:
    position = counter * 6
    current_bits = bit_string[position:]
    length = len(current_bits)
    counter = length
    while counter < 6:
      current_bits += '0'
      counter += 1
    base64_string += bits_to_base64(current_bits)
    if length == 4:
      base64_string += '='
    if length == 2:
      base64_string += '=='

  return base64_string

def bits_to_base64(six_bits):
  # convert from bits to int values for base64

  positions = [32,16,8,4,2,1] 
  counter = 0
  total = 0
  
  for bit in six_bits:
    total += positions[counter]*int(bit)
    counter += 1
  
  return base64_values[total]

def hex_to_bits(hexstring):
  # go from hex to 4 bits
  # not using bin because you can't specify padding
  
  bit_lookup = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
  bits = ''

  for char in hexstring:
    dec = int(char, 16)
    bits += bit_lookup[dec]

  return bits

assert hex_to_base64(original_hex) == correct_base64
print "Case 2: Implementing my own base64 converter passed!"