# Here are some strings with a similar structure:

some_string = "Alex is in Chicago, writing some code."
some_other_string = "John is in the park, feeding some birds."
and_another_string = "Sandra is in Austin, hiring some people."
promise_last_string = "Jenny is in an office, editing some stories."

# Redundant, right? The idea is that you can weave in information from other
# variables into a string with substitution; it's kind of like Madlibs.

name = 'Robby'
print 'Where is %s?' % name

age = 47
print '%s is %d years old.' % (name, age)

# But this format of substitution is being depreciated for a similar method.

print 'Where is {}?'.format(name)

# Numbers in the brackets let you specify position.

print '{0} is {1} years old.'.format(name, age)

# Nice thing about .format? You can repeat variables when necessary:

print "Where's {0}, that adorable {1}-year-old? Oh, there's {0}.".format(name, age)

# With substitution, we could handle printing all those strings above with
# a loop.

names = ['Alex', 'John', 'Sandra', 'Jenny']
locs = ['Chicago', 'the park', 'Austin', 'an office']
actions = ['writing', 'feeding', 'hiring', 'editing']
stuff = ['code', 'birds', 'people', 'stories']

for x in range(0, len(names)):
    print "{0} is in {1}, {2} some {3}.".format(names[x], locs[x], actions[x], stuff[x])


# If we needed to add to these four categories:

names.append('Roger')
locs.append('Pasadena')
actions.append('baking')
stuff.append('cookies')

print "{0} is in {1}, {2} some {3}.".format(names[-1], locs[-1], actions[-1], stuff[-1])
