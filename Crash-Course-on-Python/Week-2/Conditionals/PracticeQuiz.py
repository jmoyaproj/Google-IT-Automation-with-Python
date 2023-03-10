# Question 2
# Complete the script by filling in the missing parts. The function receives a name, then returns a greeting based
# on whether or not that name is "Taylor"
def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))

# Question 5
# Question 5
# If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte
# will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096 * 2 = 8192 bytes of storage.
# Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates
# the total number of bytes needed to store a file of a given size?

def calculate_storage(filesize):
    block_size = 4096
    full_blocks = filesize // block_size
    partial_block_remainder = block_size % filesize
    
    if partial_block_remainder > 0:
        return 2 * block_size
    return block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192