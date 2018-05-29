# Single-byte XOR cipher
# The hex encoded string: 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.
# You can do this by hand. But don't: write code to do it for you.
# How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

import binascii 

def single_byte_xor(hex_string):
	binary = binascii.unhexlify(hex_string)
	strings = []
	for xor_key in range(256):
		strings.append(''.join(chr(ord(b) ^ xor_key) for b in binary))
	return max(strings, key=lambda string: string.count(' '))

print single_byte_xor('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'