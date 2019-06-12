# Detect AES in ECB mode
# In this file are a bunch of hex-encoded ciphertexts. One of them has been encrypted with ECB. Detect it.
# Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext.

import collections
import binascii

BLOCK_SIZE = 16

def file_read_unhex(filename):
  with open(filename, "r") as f:
    return [binascii.unhexlify(line.strip('\n')) for line in f]

def compute_repetitions(data):
  results = {}
  for line in data:
    results[line] = check_the_line(line)
  return results

def detect_ecb_mode(results):
  ecb = collections.defaultdict(list)
  for line, dictionary in results.items():
    for chunk, count in dictionary.items():
      if count >= 2:
        ecb[line].append(chunk)
  return ecb

def check_the_line(line):
  work = line
  data = collections.Counter()
  for _ in range(len(line)// BLOCK_SIZE):
    chunk = work[:BLOCK_SIZE]
    data[chunk] += 1
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
