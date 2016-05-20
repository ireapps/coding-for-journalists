#### Introduction

Before we do anything, we need to understand some of the components we'll be interacting with and switching between.

- **The Python interpreter**: we input commands, define variables and functions, write loops, etc. The interpreter parses it all for us, line by line as we write them, and takes action. We'll use one called **[iPython](http://ipython.org/)** — it has a few bells and whistles that make it a little more user-friendly.
<br><br>
- **Text editor**: this is where we essentially chain a bunch of commands together within a single document and save it as a Python script (ending in ```.py```) that can be executed whenever we choose to run it.
<br><br>
- **The command line**: Accessed via "Terminal" on OS X or "cmd.exe" (or possibly PowerShell) on Windows. It's where we actually run the Python interpreter, among other programs, and issue commands that allow us to navigate the folders on our hard drive. 

That's pretty much it. These three pieces give you a container for code you're writing (and a way to save it) and the program to run it. We'll be doing quite a bit of switching back and forth between entering code directly into the Python interpreter and the text editor; as you write code, testing completed chunks in the interpreter can work as your proving ground for whether it works.

We'll also deal a bit with external libraries by importing some variables from another Python script. As we progress, we're going to start leaning on this outside functionality more and more — Python comes with a standard library that has a ton of useful stuff we can import. Developers have written libraries that take this functionality even further. By importing parts of these libraries into our Python script, we can do complex things, like fetch a web page or read CSV files, with very little code.

This section serves as a crash course covering some of Python's major data types and and how they're used. We'll be doing things like mashing strings together, running through items in a list and defining very simple functions.

We're also going to deal with some of the fundamental ways we can guide a Python script: loops and conditionals.

We'll be using **iPython**'s interactive interpreter, which means we have access to a few extra features.

If we wanted to get everything from **var.py** queued up for use in the intepreter, we can run the script from within iPython:

```python
run var.py
```

We can also use the more traditional method of importing everything defined in a script, treating it as a module:

```python
from var import *
```

This will make a little more sense as we start bringing in other Python libraries to tackle our other tasks. Either way, it's going to get us those variables defined in **var.py**. We can quickly test that these variables were loaded by typing ```lucky_number```.

There are other benefits that come with using **iPython**.

Let's say I have a longer chunk of code that I want to try out in iPython to see if it works as expected.

```python
presents = ['A brand new car', 'Socks']

for gift in presents:
    if gift == 'A brand new car':
        print gift, '<- Oh yeah!'
    else:
        print gift, '<- Meh.'
```
Having to type this line by line into the interpreter and pay attention to indentation can be a pain.

But I can write that block of code in a text editor instead, then select it all and copy it. Switching over to iPython, I can use the built-in paste function:

```
%paste
```

This will paste the contents of my computer clipboard, preserving all the indentation and other white space, and execute whatever code was there. Pretty handy.

If you're wondering what commands have been entered into the interpreter, **iPython** has another function that will give you a recap of commands you've typed:

```
%history
```

The files in this folder:

- **var.py**: A Python script with some variables of different types like integers, lists and dictionaries.
<br><br>
- **exercises.py**: A file that gives a list of exercises in the form of comments; guidance on how to manipulate the variables in **var.py**. It's also the place we can write code to save for future reference. Nearly everything we do in this task will use iPython.
<br><br>
- **fun_with_subs.py**: A file for practicing string substitutions, which is something we'll be doing frequently. It covers the depreciated method you'll encounter frequently and covers ```str.format()```.
<br><br>
- **whitespace.py**: A guide to how Python decides which blocks of code to run when; it's all controlled by indentation.

Any finished versions will appear in the **completed** folder.

!!!note
	For more information on the basics in Python check out some of these sections from the official Python documentation.
	
	- Data types: [strings](https://docs.python.org/2/tutorial/introduction.html#strings), [numbers](https://docs.python.org/2/tutorial/introduction.html#numbers), [lists](https://docs.python.org/2/tutorial/introduction.html#lists) and [dictionaries](https://docs.python.org/2/tutorial/datastructures.html#dictionaries)
	- [Comparing values](https://docs.python.org/2/library/stdtypes.html#comparisons)
	- [String methods](https://docs.python.org/2/library/stdtypes.html#string-methods)
	- [List methods](https://docs.python.org/2/tutorial/datastructures.html#more-on-lists)
	- [Loops](https://docs.python.org/2/tutorial/controlflow.html#for-statements) (`for`)
	- [Conditionals](https://docs.python.org/2/tutorial/controlflow.html#if-statements) (`if`)
	- [Defining simple functions](https://docs.python.org/2/tutorial/controlflow.html#defining-functions)
	- [String formatting](https://docs.python.org/2/library/string.html#formatexamples)