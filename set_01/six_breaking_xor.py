# the cryptopals crypto challenges
# Challenges   Set 1   Challenge 6
# Break repeating-key XOR
# It is officially on, now.
# This challenge isn't conceptually hard, but it involves actual error-prone coding. The other challenges in this set are there to bring you up to speed. This one is there to qualify you. If you can do this one, you're probably just fine up to Set 6.
# There's a file here. It's been base64'd after being encrypted with repeating-key XOR.
# Decrypt it.
# Here's how:
# Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
# Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:
# this is a test
# and
# wokka wokka!!!
# is 37. Make sure your code agrees before you proceed.
# For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
# The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.
# Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
# Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
# Solve each block as if it was single-character XOR. You already have code to do this.
# For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.
# This code is going to turn out to be surprisingly useful later on. Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise, a "Crypto 101" thing. But more people "know how" to break it than can actually break it, and a similar technique breaks something much more important.
# No, that's not a mistake.
# We get more tech support questions for this challenge than any of the other ones. We promise, there aren't any blatant errors in this text. In particular: the "wokka wokka!!!" edit distance really is 37.

import base64
import three_single_byte_xor_cipher as xor
import pprint

#remove the base64 on the file to get the ciphertext
file = open("6.txt", 'r')
whole_file = []
for line in file:
  whole_file.append(base64.b64decode(line))
whole_file = ''.join(whole_file)

def to_binary(astring):
  # creates a list of each byte's decimal value
  binary_list = []
  for x in bytearray(astring):
    binary_list.append(format(x, 'd'))
  return binary_list

def hamming_distance(binary1, binary2):
  # tests for edit distance
  # performs a check if both bits in a binary blob are the same
  # then notes the number of bits that are different
  binary = []
  for x in range(0, len(binary1)):
    # you can do the comparison on an int and then convert
    # the result to binary and count the 1s to note the difference
    binary.append(format(int(binary1[x]) ^ int(binary2[x]), 'b'))
  count = ''.join(binary).count('1')
  return count

def guess_keysize(message, size):
  # we can look at the edit distance to estimate the keysize
  # given a keysize and a message, this'll return the edit distance
  part1 = message[0:size-1]
  part2 = message[size:(size*2)]
  binary1 = to_binary(part1)
  binary2 = to_binary(part2)
  edit_distance = hamming_distance(binary1,binary2) / size
  return edit_distance

def calculate_keysizes(message):
  # given a message, we'll perform one edit distance test per keysize
  keysizes = {}
  for x in range(2,41):
    edit_size = guess_keysize(message, x)
    try: 
      keysizes[edit_size].append(x)
    except KeyError:
      keysizes[edit_size] = [x]
  return keysizes

def smallest_keysize(keysizes, message, tries):
  # given a message, we'll perform as many tries on the edit distance test as supplied
  # we'll also round to two decimal places
  keysizes_more_samples = {}
  for keysize in keysizes:
    edit_size = 0
    iterations = range(0,tries)
    for x in iterations:
      edit_size += guess_keysize(message[keysize*x:],keysize)
    edit_size = round(edit_size / float(len(iterations)),2)
    try: 
      keysizes_more_samples[edit_size].append(keysize)
    except KeyError:
      keysizes_more_samples[edit_size] = [keysize]
  return keysizes_more_samples

def minimum(keysizes, message):
  # takes a dict of edit distances with the corresponding key sizes and returns the minimum
  while len(keysizes[min(keysizes)]) > 1:
    minimum = min(keysizes)
    keysizes = smallest_keysize(keysizes[minimum], message, 6)
  return keysizes[min(keysizes)][0]

def break_up_file_by_keysize(key_size, message):
  # chops up an input file by the size of the suspected key
  single_key_xor = {}
  for byte in range(0, len(whole_file)):
    modulo = byte % key_size
    try:
      single_key_xor[modulo].append(whole_file[byte])
    except KeyError:
      single_key_xor[modulo] = [whole_file[byte]]
  strings = []
  for key, value in single_key_xor.iteritems():
    strings.append(''.join(value))
  return strings

def assemble_plaintext(key_size,plaintexts):
  # puts back together plaintexts that were chopped up to perform single key xors
  # try/except is in there to handle if a specific plaintext is shorter than expected
  length = len(plaintexts[0])
  text = []
  for n in range(0,length):
    for x in range(0,key_size):
      try:
        text.append(plaintexts[x][n])
      except:
        pass
  return ''.join(text)


def run_edit_test():
  # Hamming distance test per directions
  string1 = "this is a test\n"
  string2 = "wokka wokka!!!\n"

  binary1 = to_binary(string1)
  binary2 = to_binary(string2)

  expected_result = 37
  result = hamming_distance(binary1, binary2)
  assert expected_result == result

def main():
  # run it!
  keysizes = smallest_keysize(range(2,41), whole_file, 20)
  pp = pprint.PrettyPrinter()
  pp.pprint(keysizes)
  key_size = raw_input("Use this keysize: ")
  key_size = int(key_size)
  strings = break_up_file_by_keysize(key_size, whole_file)
  guessed_key_array, plaintexts = [], []
  for astring in strings:
    results, printable = {},{}
    results = xor.single_byte_xor(astring)
    printable = xor.check_if_printable(results)
    result = xor.max_spaces(printable)
    guessed_key_array.append(chr(result[0]))
    plaintexts.append(result[1])
  guessed_key = ''.join(guessed_key_array)
  text = assemble_plaintext(key_size, plaintexts)
  print("Key is: {0}".format(guessed_key))
  print("Plaintext is \n {0}".format(text))

if __name__ == '__main__':
  run_edit_test()
  main()
