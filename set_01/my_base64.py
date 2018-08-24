# cryptopals challenge 1

import binascii
import base64

def to_base64(hex_value):
	# binascii deals with hex nicely
	ascii = binascii.unhexlify(hex_value)
	# decode() returns unicode instead of ascii
	base64_output = base64.b64encode(ascii).decode()
	return base64_output