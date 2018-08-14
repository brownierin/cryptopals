# Detect single-character XOR
# One of the 60-character strings in this file has been encrypted by single-character XOR.
# Find it.
# (Your code from #3 should help.)

import single_byte_xor_cipher as xor

file = open("4.txt", "r")
all_results = []
for line in file:
  line = line.replace('\n','')
  all_results = xor.single_byte_xor(line, all_results)
printable_results = xor.check_if_printable(all_results)
print xor.max_spaces(printable_results)
