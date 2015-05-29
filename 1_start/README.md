# 1_start

This is a crash course in some of Python's major data types and and how to tame them. We'll be doing things like mashing strings together, running through items in a list and defining very simple functions.

We'll be using iPython's interactive interpreter, which means we have access to a few extra features (which iPython modestly calls *magic functions*).

But first we have to fetch all these files. Using git and GitHub is a little bit outside the scope of this class (at the moment), so we'll download a [zipped copy of the repo](https://github.com/richardsalex/coding_for_journos/archive/master.zip), unzip it, and navigate to it using PowerShell.

This exercise has three files:

- **var.py**: A Python script with some variables of different types, like integers, lists and dictionaries.

- **exercises.py**: A file that gives a list of exercises in the form of comments -- guidance on how to manipulate the variables in **var.py**. It's also the place we can write code to save for future reference; nearly everything we do in this task will use iPython.

- **exercises_done.py**: Same as above, but will all the code filled in.

Opening iPython is as easy as typing ```ipython``` into PowerShell.

To get everything from **var.py** queued up, we can either run it from within iPython using one of the _magic functions_:

```
%run var.py
```

Or we can use the more traditional method of importing everything defined in a script, treating it as a module:

```
from var import *
```

This will make a little more sense as we start bringing in other Python libraries to tackle our other tasks. Either way, it's going to get us those variables defined in **var.py**. We can quickly test that these variables were loaded by typing ```lucky_number```.

Let's say I have a longer chunk of code that I want to try out in iPython to see if it works as expected.

```
presents = ['A brand new car', 'Socks']

for gift in presents:
    if gift == 'A brand new car':
        print gift, '<- Oh yeah!'
    else:
        print gift, '<- Meh.'
```
Having to type this line by line into the interpreter and pay attention to indentation can be a pain.

But I can write that block of code in a text editor instead, then select it all and then copy it. Switching over to iPython, I can use the built-in paste function:

```
%paste
```

This will paste the contents of my clipboard, preserving all the indentation and other whitespace, and execute whatever code was there. Pretty handy.

Finally, iPython has another function that will give you a recap of commands you've typed:

```
%history
```

