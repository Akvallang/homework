# Task 1
# Imports practice
#  Make a directory with 2 modules; make a function in one of them; then import this function in the
# other module and use that in your script of choice.

 
import my_functions.multiple as mult
import my_functions.summ as summ

mult.multiple(5,5,10)
summ.summ(10,10,10)

# Task 2
# The sys module.
#  The “sys.path” list is initialized from the PYTHONPATH environment variable. Is it possible to change 
# it from within Python? If so, does it affect where Python looks for module files? Run some interactive 
# tests to find it out.

# 
from pprint import pprint
import sys
pprint(sys.path)

new_path = "D:\\Хозяйства\\Авангард\\Вентиляція"
sys.path.append(new_path)
pprint(sys.path)
from my_functions.multiple import multiple
multiple(3,3)


# Task 3
# Basics, import, work with os module
# Write a program that counts lines and characters in a file (similar to `wc` Unix-utility, 
# for additional info about it follow the link: https://www.geeksforgeeks.org/wc-command-linux-examples/
# or in case you have macOS or Linux - just call manual for this utility via command: `man wc`).
#  Create a Python module called "mymod.py", which has three functions:

# count_lines(name) function that reads an input file and counts the number of lines in it 
# (hint: file.readlines() does most of the work for you, and "len" does the rest) 
# count_chars(name) function that reads an input file and counts the number of characters in it 
# (hint: file.read() returns a single string)
# test(name) function that calls both counting functions with a given input file­name. 
# Such a filename generally might be passed-in, hard-coded, input with input(),
# or pulled from a command-line via the sys.argv list; for now, assume it’s a passed-in function argument.
# All three `mymod.py` functions should expect a filename string to be passed in. 

# Test your module interactively, using import and name qualification to fetch your exports. 

# Does your PYTHONPATH need to include the directory where you created mymod.py?

# Try running your module on itself: e.g., test("mymod.py"). Note that the test opens the file twice; 
# if you’re feeling ambitious, you may be able to improve this by passing an open file object into the
# two count functions (hint: file.seek(0) is a file rewind).

from my_mod import test
test("lessons\\text.txt")