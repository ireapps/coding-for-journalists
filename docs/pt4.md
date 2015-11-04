#### Making a function

This is a pretty quick task -- the next time we have to deal with a list from the same agency, we shouldn't have to spend time rewriting our code from scratch or even go back to revise it to handle a new file. We have something that works, so let's turn it into a function we can call whenever we need to parse addresses for a list of financial licensees.

This exercise contains the following files:

**payday_parser.py**: Our parser from [from the previous exercise](pt3.md). We'll turn the existing work into a function and generalize it a bit to handle a file that's not specifically the list of licensed payday lenders.

**consumer_installment.html**: Another listing from the state of Illinois, but this time it encompasses more than 1,000 licensed consumer installment lenders.

**call_function.py**: A script we'll write to call the parser function from **payday_parser.py** and direct it toward our HTML file.

Finished versions are in the **completed** folder.