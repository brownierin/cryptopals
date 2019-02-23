# Detect single-character XOR
# One of the 60-character strings in this file has been encrypted by single-character XOR.
# Find it.
# (Your code from #3 should help.)

import three as xor
import binascii

def file_open_unhexlify(filename):
  with open(filename, 'r') as file:
    return [binascii.unhexlify(line.strip('\n')) for line in file]

def get_all_xors(file):
  all_xors = []
  [all_xors.append(xor.single_byte_xor(line)) for line in file]
  return all_xors

def find_printable(all_xors):
  all_printables = []
  for line in all_xors:
    printable_results = xor.check_if_printable(line)
    if printable_results != {}:
      all_printables.append(xor.max_spaces(printable_results))
    return max(all_printables, key=lambda printable: printable[1].count(' '))

def main():
  file = file_open_unhexlify('4.txt')
  all_xors = get_all_xors(file)
  print find_printable(all_xors)


    