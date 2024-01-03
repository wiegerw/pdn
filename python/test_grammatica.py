#!/usr/bin/env python3

import os
from pathlib import Path


if __name__ == "__main__":
    for file in Path('../games').rglob('*.pdn'):
        print(file)
        os.system('java -jar grammatica-1.5.jar ../grammars/pdn_reading.grammar --parse "{}"'.format(file))
