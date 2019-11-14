# Private-Key-Generator
A private key generator using python

This is a simple private key generator, which does the following:

1) Prompts the user for a random input
2) Hash's the input using sha256
3) Verifies that the resulting hex is less than 2^256
4) Adds the version number
5) Adds a 32-bit checksum by double-hashing the hex
6) Convers the resulting hex to base58

This program makes use of the base58 file from https://gist.github.com/ianoxley/865912 
