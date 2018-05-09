#import python modules
from stegano import lsb 
import argparse
import sys

#define command line arguments --hide <text> <filename> for hiding of text or just <filename> argument for decryption of text. --help or -h displays the help messages.
parser = argparse.ArgumentParser()
parser.add_argument('--hide' , dest='text_to_hide' , help="Hide a string of text using steganography.")
parser.add_argument('filename')
args = parser.parse_args()
#display help messages and exit if no command line arguments provided
if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
#if --hide argument specified
if args.text_to_hide:
	imageFile = open(args.filename, 'rb') 
	hiddentext = lsb.hide(imageFile, args.text_to_hide)
	hiddentext.save(args.filename)
#if no arguments specified besides filename
else:
	revealed_text = lsb.reveal(args.filename)
	print(revealed_text)
