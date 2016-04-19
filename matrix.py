boolean = False
from random import randint
import terminalsize
string = ""
while boolean == False:
  (width, height) = terminalsize.getTerminalSize()
  for i in range(width-1):

    x = randint(0,1)
    string += str(x)
  print("\033[1;32;40m %s" %string)
  string = ""

