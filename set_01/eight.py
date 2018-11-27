# Detect AES in ECB mode
# In this file are a bunch of hex-encoded ciphertexts. One of them has been encrypted with ECB. Detect it.
# Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext.

import binascii

BLOCK_SIZE = 16

def file_read_unhex(filename):
  file = open(filename,'r')
  data = []
  for line in file:
    data.append(binascii.unhexlify(line.strip('\n')))
  return data

def compute_repetitions(data):
  results = {}
  for line in data:
    results[line] = check_the_line(line)
  return results

def detect_ecb_mode(results):
  ecb = {}
  for line, dictionary in results.items():
    for chunk, count in dictionary.items():
      if count >= 2:
        try: 
          ecb[line].append(chunk)
        except KeyError:
          ecb[line] = [chunk]
  return ecb

def check_the_line(line):
  size = len(line)
  work = line
  data = {}
  for i in range(size/BLOCK_SIZE):
    chunk = work[:BLOCK_SIZE]
    if chunk in data:
      data[chunk] += 1
    else:
      data[chunk] = 1
    work = work[BLOCK_SIZE:]
  return data

if __name__ == '__main__':
  data = file_read_unhex('8.txt')
  results = compute_repetitions(data)
  answer = detect_ecb_mode(results)
  for potential in answer:
    most_repeated_block = max(results[potential], key=lambda i: results[potential][i])
    print "This ciphertext is encrypted in ECB mode: {!r}".format(potential)
    print "The block {!r} was repeated {} times".format(most_repeated_block, results[potential][most_repeated_block])
