# cryptopals set 1 challenge 2

# Fixed XOR
# Write a function that takes two equal-length buffers and produces their XOR combination.
# If your function works properly, then when you feed it the string: 1c0111001f010100061a024b53535009181c
# after hex decoding, and when XOR'd against: 686974207468652062756c6c277320657965
# should produce: 746865206b696420646f6e277420706c6179

def xor(string1, string2):
	# convert from hex to binary
	binary1 = int(string1,16)
	binary2 = int(string2,16)
	# check if length is the same
	# if so, perform xor
	if buffers_same_length(string1,string2):
		solution = binary1 ^ binary2
		# chomp off the L and the 0x
		return hex(solution)[2:-1]
	else:
		raise Error('Input values not the same length')

def buffers_same_length(string1, string2):
	return True if len(string1) == len(string2) else False

solution = xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
assert solution == '746865206b696420646f6e277420706c6179'
print solution

# string1 = '1c0111001f010100061a024b53535009181c'
# string2 = '686974207468652062756c6c277320657965'

