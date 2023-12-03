# count_lines(name) function that reads an input file and counts the number of lines in it 
def count_lines(name):
    with open(name, "r") as file_1:
        num_of_lines = file_1.readlines()
        lenth = len(num_of_lines)
        print("Number of string is: ", lenth)    
# count_lines("lessons/text.txt")    
# 
# count_chars(name) function that reads an input file and counts the number of characters in it 
# (hint: file.read() returns a single string)

def count_chars(name):
    with open (name, "r") as file_1:
        text = file_1.read()
        lenth = len(text)
        num_of_newlines = text.count("\n")
        lenth -= num_of_newlines
        print("Nums of chars: ", lenth)
# count_chars("lessons/text.txt")
    
# test(name) function that calls both counting functions with a given input file­name. 
# Such a filename generally might be passed-in, hard-coded, input with input(),
# or pulled from a command-line via the sys.argv list; for now, assume it’s a passed-in function argument.

def test (name):
    count_lines(name), count_chars(name)
    return
    
    
# All three `mymod.py` functions should expect a filename string to be passed in. 