#!/usr/bin/env python3

# Copyright 2009-2023 Wieger Wesselink, <wieger at 10x10 dot org>
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE_1_0.txt or http://www.boost.org/LICENSE_1_0.txt)
#
# Portable Draughts Notation (PDN) Writing Grammar
#
# 12 March 2012

from pathlib import Path

import tpg

_grammar = (Path(__file__).parent.parent / 'grammars' / 'pdn_writing_tpg.g').read_text()

PDNParser = tpg.ParserMetaClass('PDNParser', (tpg.Parser,), {'__doc__': _grammar})


def pdn_parse(text):
    try:
        parser = PDNParser()
        parser(text)
        return True
    except Exception as e:
        print(e)
        return False
