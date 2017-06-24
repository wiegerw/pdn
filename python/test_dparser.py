import os
from path import *

for file in path('../games/fail').walkfiles('*.pdn'):
    print file
    os.system('cat "%s" | ../dparser/pdn' % file)

for file in path('../games/succeed').walkfiles('*.pdn'):
    print file
    os.system('cat "%s" | ../dparser/pdn' % file)
