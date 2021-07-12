# Import system library to get version info.
import sys

# This script does only work with python 3 and later. So we're going to request the version.
majorVersion = sys.version_info[0]

# If statement to check version and exit if it is below 3
if majorVersion <= 2:
	print('To run this script, python version 3 is required.')
	print('USAGE: \npython3 ./HelloWorld.py')
	exit(2) # it is usually not neat to exit in the middle of a script, but it is the quickest way.

# Simple print statement to say hello.
print('Hello world!')

# Ask for user input (your name) amd store it in variable 'userName'
userName = input('What is your name? \n')

# This is a dictionary mapping, mapping the keys (on the lef of the colon) with the values (on the right). 
# This all is stored in a variable named 'nameMessages'.
nameMessages = {
	'NIELS':'Nice to see you, O grande creator!',
	'ALEKS':'Well met, fair lady of the north.'
}

# the f at the beginning of the string states that this one is special, and variables in the text between { and } should be replaced with values. This is the default message (if the name is not in the nameMessages list above.)
defaultMessage = f'I do not think I have seen you here before, {userName}, but still nice to meet you.'

# put the username to capitalisation, so it doesn't matter how you wrote it, it always picks the right name.
userNameUpper = userName.upper()

# this generates the return message, find the message by the key (userNameUpper), and if not found, set it to defaultMessage
returnMessage = nameMessages.get(userNameUpper, defaultMessage)

# print the actual resulting message
print(returnMessage)

