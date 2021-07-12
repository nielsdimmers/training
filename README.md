# Niels' Training Repository
This repository is meant for training and practise purposes, for instance with using GIT, GITHUB and programming in general.

# Writing code
There are many ways and theories to writing good programming code. Apart from the obvious choice in language, the code to achieve a certain goal can be written in many different ways. Although there are many theories and best practices, my message here would be to not be scared by those views. As you grow and develop in learning to write code, you will learn the advantages and disadvantages of those methods and make a informed decision for yourself.

Keep in mind that each piece of code has goal and purpose on its own, and that you have to choose the approach which best fits the situation. For instance, this line of code:

```python
print(nameMessages.get(userName.upper(), f"I do not think I have seen you here before, {userName}, but still nice to meet you."))
```

It can easily be split into four separate lines and still do exactly the same thing. This might be perceived as "slower" by the experienced developer, and I admit, it is, but still I decided to split it up into four lines in the example code "HelloWorld.py". This is because its purpose is not to be a quick script, but to be comprehensible to the beginner programmer.

Also note that this makes that each developer has their own signature method of programming. This makes it (almost) possible to find the developer of a piece of code without looking at the blame. FYI, the HelloWorld script does break quite a few of my own signature rules, so don't start comparing.

# Version history
Versions are named as follows:

``## <Version number> - <Date (YYYY-MM-DD format)> - Title``

You can name them pretty much ny title you want, so feel free to come up with something witty ;-). Add new versions to the top, so users can easily see which version it is.

## 1 - 2021-07-12 - First version
This version was created by Niels Dimmers and contains a file in .gitignore (CONFIG) and a simple python script.

The script is quite simple and inline commented, it does a check for the python version, prints a hello world, asks for the username, and based on the input prints a response string. That's it. The file has inline comments.

### Source
The "switch" statement at the end of the script, using the dictionary, was derived from [this website](https://jaxenter.com/implement-switch-case-statement-python-138315.html)