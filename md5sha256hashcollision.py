#import python modules
import random
import hashlib
import argparse
import time
import sys

#define command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--md5' , dest='string_to_hash_using_md5', help="Hash a string of text using MD5 and then shuffle the letters of the string until a collision occurs.")
parser.add_argument('--sha256' , dest='string_to_hash_using_sha256' , help="Hash a string of text using SHA-256 and then shuffle the letters of the string until a collision occurs.")
args = parser.parse_args()
#print help messages and exit if no command line arguments provided
if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
#if --md5 argument specified
if args.string_to_hash_using_md5:
	print("The original input is: ") 
	print(args.string_to_hash_using_md5)
#hash using MD5 and encode in unicode
	hash1 = hashlib.md5((args.string_to_hash_using_md5).encode('utf-8'))
#if --sha256 argument specified
else:
	print("The original input is: ") 
	print(args.string_to_hash_using_sha256)
#hash using SHA-256 and encode in unicode
	hash1 = hashlib.sha256((args.string_to_hash_using_sha256).encode('utf-8'))
#returns a hexadecimal representation of the binary digest
hashnew = hash1.hexdigest()
print("The original hash is: ")
print(hash1.hexdigest())
hash3 = 0
counter = 0
#start a timer
start_time = time.time()
#loops until there is a collision
while hashnew != hash3:
	if args.string_to_hash_using_md5:
#converts a string to a list
		chars = list(args.string_to_hash_using_md5)
	else:
		chars = list(args.string_to_hash_using_sha256)
#randomizes the string by shuffling letters
	random.shuffle(chars)
#converts a list to a string
	str1 = ''.join(chars)
#if --md5 argument specified
	if args.string_to_hash_using_md5:
#hash using MD5 and encode in unicode
		hash2 = hashlib.md5(str1.encode('utf-8'))
#if --sha256 argument specified
	else:
#hash using SHA-256 and encode in unicode
		hash2 = hashlib.sha256(str1.encode('utf-8'))
#returns a hexadecimal representation of the binary digest
	hash3 = hash2.hexdigest()
#counts number of iterations of randomizer
	counter = counter + 1
#output the number of iterations and elapsed time until a collision occurred
print("The collision hash is: ")
print(hash2.hexdigest())
print("The number of randomizations of the input that occurred until a collision resulted is: ")
print(counter)
elapsed_time = time.time() - start_time
print("Elapsed time to collision was: ")
print(elapsed_time)
print("seconds.")

