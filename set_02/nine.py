#Implement PKCS#7 padding
#A block cipher transforms a fixed-sized block (usually 8 or 16 bytes) of plaintext into ciphertext. But we almost never want to transform a single block; we encrypt irregularly-sized messages. One way we account for irregularly-sized messages is by padding, creating a plaintext that is an even multiple of the blocksize. The most popular padding scheme is called PKCS#7.
#So: pad any block to a specific block length, by appending the number of bytes of padding to the end of the block. For instance,
#"YELLOW SUBMARINE" ... padded to 20 bytes would be:
#"YELLOW SUBMARINE\x04\x04\x04\x04"

def message_padding_size(plaintext, block_size):
  remainder = len(plaintext) % block_size
  padding_size = block_size - remainder
  return padding_size

def pad_block(plaintext, block_size):
  padding_size = message_padding_size(plaintext, block_size)
  padding = chr(padding_size) * padding_size
  if len(plaintext) > block_size:
    number_of_blocks = len(plaintext) / block_size
    padded = plaintext[block_size*number_of_blocks:] + padding
  else: 
    padded = plaintext + padding
  return padded

def main():
  # case for plaintext smaller than the block size
  padded = pad_block("YELLOW SUBMARINE",20)
  print "The padded block is: {!r}".format(padded)
  # case for plaintext larger than the block size
  padded = pad_block("YELLOW SUBMARINEYELLOW SUBMARINE", 20)
  print "The padded block is: {!r}".format(padded)

if __name__ == '__main__':
  main()
