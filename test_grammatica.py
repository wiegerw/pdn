import os
from path import *

for file in path('games').walkfiles('*.pdn'):
    print file
    os.system('java -jar ../../java/projects/core/lib/grammatica-1.5.jar grammars/pdn_reading.grammar --parse "%s"' % file)
