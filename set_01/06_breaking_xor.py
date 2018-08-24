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

#removing the base64 on the file to get the ciphertext
file = open("6.txt", 'r')
whole_file = []
for line in file:
  line = line.replace('\n', '')
  whole_file.append(base64.b64decode(line))
whole_file = ''.join(whole_file)

def to_binary(astring):
  # return ''.join(format(ord(char), 'b') for char in astring)
  # binary_list = (format(x, '#b') for x in bytearray(astring))
  binary_list = []
  for x in bytearray(astring):
    binary_list.append(format(x, 'd'))
  return binary_list

def hamming_distance(binary1, binary2):
  # i = 0
  # for x in range(0, len(binary1)-1):
  #   i += int(binary1[x]) ^ int(binary2[x])
  # return i
  binary = []
  for x in range(0, len(binary1)):
    binary.append(format(int(binary1[x]) ^ int(binary2[x]), 'b'))
  count = ''.join(binary).count('1')
  return count

def guess_keysize(message, size):
  part1 = whole_file[0:size-1]
  part2 = whole_file[size:(size*2)]
  binary1 = to_binary(part1)
  binary2 = to_binary(part2)
  edit_distance = hamming_distance(binary1,binary2) / size
  return edit_distance

def calculate_keysizes():
  keysizes = {}
  for x in range(2,41):
    edit_size = guess_keysize(whole_file, x)
    try: 
      keysizes[edit_size].append(x)
    except KeyError:
      keysizes[edit_size] = [x]
  return keysizes

#Hamming distance test:
string1 = "this is a test\n"
string2 = "wokka wokka!!!\n"

binary1 = to_binary(string1)
binary2 = to_binary(string2)

expected_result = 37
result = hamming_distance(binary1, binary2)
assert expected_result == result

