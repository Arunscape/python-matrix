
from random import randint
import terminalsize #this is the other file terminalsize.py
string = ""
#start an infinite loop
boolean = False
while boolean == False:
  (width, height) = terminalsize.getTerminalSize() #this allows you to print exactly enough ones and zeros to fill one line
  for i in range(width-1):

    x = randint(0,1)
    string += str(x)
  print("\033[1;32;40m %s" %string) #print in the colour green
  string = "" #clearing the string allows a new line of ones and zeroes to be generated

