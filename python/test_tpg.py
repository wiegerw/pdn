#!/usr/bin/env python3

from pathlib import Path
from pdn_reading_tpg import *


if __name__ == '__main__':
    for file in Path('../games').rglob('*.pdn'):
        print(file)
        text = file.read_text()
        pdn_parse(text)
