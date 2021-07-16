# HelloWorld.py
# Niels Dimmers 2021
# Shows custom message based on commandline name given or asks for name.
# Requires at least python version 3 (python3)

# Import system library to get version info.
import sys

# sys.argv contains commandline arguments, the first is the script name, the second the argument, if there are fewer than 2, ask for the name, otherwise, assume the given command is the name (useful for automated testing)
if len(sys.argv) < 2 or sys.argv[1] == '':
	# Ask for user input (your name) amd store it in variable 'userName'
	userName = input('What is your name? \n')
else:
	# Set the name to the argument given on commandline
	userName = sys.argv[1]

# This is a dictionary mapping, mapping the keys (on the lef of the colon) with the values (on the right). 
# This all is stored in a variable named 'nameMessages'.
nameMessages = {
	'NIELS':'Nice to see you, O grande creator!',
	'ALEKS':'Hello there, Aleksandra'
}

# the f at the beginning of the string states that this one is special, and variables in the text between { and } should be replaced with values. This is the default message (if the name is not in the nameMessages list above.)
defaultMessage = f'I do not think I have seen you here before, {userName}, but still nice to meet you.'

# put the username to capitalisation, so it doesn't matter how you wrote it, it always picks the right name.
userNameUpper = userName.upper()

# this generates the return message, find the message by the key (userNameUpper), and if not found, set it to defaultMessage
returnMessage = nameMessages.get(userNameUpper, defaultMessage)

# print the actual resulting message
print(returnMessage)