from sys import argv
script, file_we_modified = argv
print("We are about to read the file you modified a while ago.")

file_to_be_read = open(file_we_modified)
print(file_to_be_read.read())

file_to_be_read.close()

