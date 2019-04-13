'''
Created on Oct 15, 2018
@author: Brandon Cao
bcao4
I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    return numToBinary(n//2) + str(n%2)

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=='':
        return 0
    elif s[0]=='0':
        return binaryToNum(s[1:])
    elif s[0]=='1':
        return ((2**(len(s)-1)) + binaryToNum(s[1:]))

def numToBinaryPadded(n):
    '''returns the binary string made to the compressed block size length'''
    s=numToBinary(n)
    return '0' * (COMPRESSED_BLOCK_SIZE-len(s)) + s

def prefixlength(s):
    '''returns the length of the repeating number at the beginning of the string without breaks'''
    if len(s)==1:
        return 1
    if s[1]==s[0]:
        return 1 + prefixlength(s[1:])
    return 1

def compress(s):
    ''' takes a binary string S of length 64 as input and returns another binary string as output'''
    def compressHelp(s,b):
        if s=='':
            return ''
        if s[0] != chr(b + ord('0')):
            return numToBinaryPadded(0) + compressHelp(s, 1-b)
        prefix_len= min(prefixlength(s), MAX_RUN_LENGTH)
        return numToBinaryPadded(prefix_len) + compressHelp(s[prefix_len:], 1-b)
    return compressHelp(s, 0)

def uncompress(s):
    ''' inverts or undoes the compressing in your compress function'''
    def uncompressHelp(s,b):
        if s=='':
            return ''
        n= binaryToNum(s[:COMPRESSED_BLOCK_SIZE])
        return chr(b + ord('0')) * n + uncompressHelp(s[COMPRESSED_BLOCK_SIZE:], 1-b) 
    return uncompressHelp(s, 0)

#===============================================================================
# the largest number of bits that the compress function can use to encode a 64-bit string
# is 325 bits because there can be a maximum of 5 bits for each bit in the 64-bit string,
# giving 320 bits. An extra 5 bits when a string starts with 1.
#===============================================================================

def compression(s):
    '''return the ratio of the compressed size to the original size for image S'''
    return len(compress(s))/len(s)

Penguin= "00011000"+"00111100"*3 +"01111110"+"11111111"+"00111100"+"00100100"
Smile= "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8
Five="1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"
Test= '0' * 32
Test2= '0' * 6 + '1' * 10 + '0' * 9 + '1' * 4

#===============================================================================
# Some test images used on the function compression outputs a ratio that is greater than one,
# showing that the length of the string that is compressed is actually longer than the length
# of the original string. However, other test images used on the function compression outputs
#a ratio that is less than one, showing that the length of the compressed string is shorter 
#than the length of the original string
#===============================================================================

#===============================================================================
# The compression algorithm cannot exist because if a string is constantly
# switching between 1 and 0, or is really short, multiple bits are being used to compress a 
# single number,creating a longer string
#===============================================================================

print(compression(Penguin))
print(compression(Smile))
print(compression(Five))
print(compression(Test))
print(compression(Test2))
