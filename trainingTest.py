# trainingTest.py
# Niels Dimmers 2021
# test example, tests the training tools

# Import system library to get version info.
import subprocess

# execute the given python command, with the script name and some options
def executeCommand(linuxCommand, scriptname, name):
	return subprocess.run([linuxCommand, scriptname,name], stdout=subprocess.PIPE).stdout.decode('utf-8')

# execute the helloworld python script with given name
def helloWorld(name):
	return executeCommand('python3', 'HelloWorld.py',name)

# execute hello world original script
def helloWorldOriginal():
	return executeCommand('python3', 'HelloWorldOriginal.py','')

# Returns the error count in compare
def compare(expected,result):
	if expected != result:
		print(f"Error! Expected: \n{expected}\nResult: \n{result}")
		return 1
	else:
		return 0
	
# Set empty variables for counting
testcounter = 0
errcounter = 0

# do some tests
expected = "Nice to see you, O grande creator!\n"
result = helloWorld('Niels')
testcounter += 1
errcounter += compare(expected,result)

expected = "Well met, fair lady of the north.\n"
result = helloWorld('Aleks')
testcounter += 1
errcounter += compare(expected,result)

expected = "I do not think I have seen you here before, Mike, but still nice to meet you.\n"
result = helloWorld('Mike')
testcounter += 1
errcounter += compare(expected,result)

expected = "Hello World!\n"
result = helloWorldOriginal()
testcounter += 1
errcounter += compare(expected,result)

# calculate successful tests
testsuccessful = testcounter - errcounter

# print test result
print(f"Testing complete, {testcounter} tests executed, {errcounter} errors found and {testsuccessful} tests without errors")