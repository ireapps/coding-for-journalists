#! usr/bin/python















# Quick check to make sure we're getting all of our links before we move on




# Let's look at the URL string



# What we really care about are the numbers at the end of the link; that's
# how the whole setup for the website works. We feed it an ID, it generates
# a page.






    # We only need the number at the end; we can split the URL and grab it






# Just as a test, let's look at the first one to see what we're dealing with.




# Two tables on each page, both are functionally identical to BeautifulSoup,
# so we just grab both and take the second.




# The names are coming from a db that's dynamically combining them; we can use that.
# All the components are inside of label tags. If we try to extract the text, we're
# met with a mess of unicode junk (non-breaking spaces, in this case) meant to
# glue the title, first name, middle initial and last name together.



# Pull the name and clean it up with split(), which by default will work on
# whitespace. .join and .split together can be handy for cleaning.




# Depending on how we need the name to be parsed, it might be better for us
# to chop it up into components.





# Now that we see how this works, we can write a full run. We'll feed
# requests.get a page, parse it with BeautifulSoup, and write it to CSV.

# We can use the 'with' syntax here to open the file




        # We can basically use what we've done above to zero in on the table




        # Another for loop to move inside each row (except the header)






            # If it's a vacancy, let's not go through the trouble of splitting.



                # Slot the different components here






                # Last name is currently including suffixes like Jr, Sr, III, etc.
                # We can look for a comma that denotes the suffix.












