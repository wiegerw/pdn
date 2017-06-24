import os
from path import *

for file in path('../games').walkfiles('*.pdn'):
    print file
    os.system('java -jar grammatica-1.5.jar ../grammars/pdn_reading.grammar --parse "{}"'.format(file))
