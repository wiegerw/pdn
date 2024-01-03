#!/usr/bin/env python3

import os
from pathlib import Path


if __name__ == '__main__':
    for file in Path('../games/fail').glob('*.pdn'):
        print(file)
        os.system('cat "%s" | ../dparser/pdn' % file)

    for file in Path('../games/succeed').glob('*.pdn'):
        print(file)
        os.system('cat "%s" | ../dparser/pdn' % file)
