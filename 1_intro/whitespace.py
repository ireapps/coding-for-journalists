# FUN WITH WHITESPACE IN PYTHON


# Whitespace is critical in Python. Unlike some other scripting languages,
# which use characters to tell the interpreter where functions and loops
# end, Python uses structured indentation for new lines, making "blocks" of
# code.

my_string = 'New York'

print "Start spreading the news,"

if my_string == 'New York':
    print "I'm leaving today,"
    print "I want to be a part of it,"
    
    for num in range(0,2):
        print my_string

else:
    print "you clearly don't know how this song goes. {}?".format(my_string)
    
# What do you think the above does? Let's step through it.
# (Notice how blank lines between code is A-OK.) 


# Some other places indentation and whitespace don't matter much:

# When assigning items to a list or a string; the below is ugly, but sometimes
# it's more readable in a script to define things on different lines.

list_of_cities = [

            'Buffalo',
            
                  'Key West',
                'Fort Collins',     'Bakersfield'     ]

wordy_string = "Four score and seven years ago, our fathers brought" \
    " forth on this continent ... hmm. I" \
            " am desperately trying to remember what Abraham Lincoln" \
        " said, because it was one of the most important and" \
        " and influentual speeches in modern history; I've even" \
                   " been to Gettysburg. Wow, this is pretty embarrasing."


# Tabs and spaces. Don't mix them. The interpreter will choke on it. Style
# dictates that you use four spaces instead of tabs. I generally set up my
# text editor to replace tabs on the fly or do it after I'm done with my
# script, because I much prefer hitting tab once instead of space four times.

print "Start spreading the news,"
if my_string == 'New York':
    print "I'm leaving today,"
	print "I want to be a part of it,"
    for num in range(0,2):
        print my_string
else:
    print "you clearly don't know how this song goes. {}?".format(my_string)

# The above looks fine, right? You will get an IndentationError. Most text
# editors have a function
