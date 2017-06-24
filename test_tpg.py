import os
from path import *
from pdn_reading_tpg import *

for file in path('games').walkfiles('*.pdn'):
    print file
    text = path(file).text()
    pdn_parse(text)
