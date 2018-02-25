#import python modules
import argparse
import sys

#define command line arguments --encrypt for encryption of text and --decrypt for decryption of text. --help or -h displays the help messages.
parser = argparse.ArgumentParser()
parser.add_argument('--encrypt' , dest='string_to_encrypt' , help="Encrypt a string of text using a Caesar Cipher, will prompt for key. Input string is not case sensitive, output will be all uppercase.")
parser.add_argument('--decrypt' , dest='string_to_decrypt' , help="Decrypt a string of text using a Caesar Cipher, will prompt for key. Input string is not case sensitive, output will be all uppercase.")
args = parser.parse_args()
#display help messages and exit if no command line arguments provided
if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
#Choose an encryption key from 1 through 25, exit if invalid key
key = int(input("Please enter your key: (1-25)"))
if (key < 1) or (key > 25):
	print("Invalid key entered, exiting.")
	sys.exit(1)
#if --encrypt argument specified
if args.string_to_encrypt:
#loop through each letter in plain text string, converting to lower case and ASCII integer
	for letter in args.string_to_encrypt:
		letter = letter.lower()
#add encryption key integer to integer value of letter
		letter = ord(letter) + key
#if encrypted character is past z, wrap around to a
		if letter > 122:
			letter = letter - 26
#convert ASCII integer back to letter and upper case
		letter = chr(letter)
		letter = letter.upper()
#print cipher text
		sys.stdout.write(letter)
else:
#if --decrypt argument specified
#loop through each letter in plain text string, converting to lower case and ASCII integer
	for letter in args.string_to_decrypt:
		letter = letter.lower()
#subtract encryption key integer from integer value of letter
		letter = ord(letter) - key 
#if encrypted character is past a, wrap around to z
		if letter < 97:
			letter = letter + 26
#convert ASCII integer back to letter and upper case
		letter = chr(letter)
		letter = letter.upper()
#print clear text
		sys.stdout.write(letter)

