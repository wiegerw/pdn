#!/usr/bin/env python3

# Copyright 2009-2023 Wieger Wesselink, <wieger at 10x10 dot org>
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE_1_0.txt or http://www.boost.org/LICENSE_1_0.txt)
#
# Portable Draughts Notation (PDN) Reading Grammar
#
# 12 March 2012

import tpg

# For tpg see http://cdsoft.fr/tpg/

class PDNParser(tpg.Parser):
    r'''
        separator space: '\s+' ;
        separator comments: '%.*' ;

        token WIN1             '1-0'                                                                   ;
        token DRAW1            '1/2-1/2'                                                               ;
        token LOSS1            '0-1'                                                                   ;
        token WIN2             '2-0'                                                                   ;
        token DRAW2            '1-1(?![0-9])'                                                          ;
        token LOSS2            '0-2'                                                                   ;
        token DOUBLEFORFEIT    '0-0'                                                                   ;
        token LPAREN           '\('                                                                    ;
        token RPAREN           '\)'                                                                    ;
        token LBRACKET         '\['                                                                    ;
        token RBRACKET         '\]'                                                                    ;
        token ASTERISK         '\*'                                                                    ;
        token ELLIPSES         '\.\.\.'                                                                ;
        token MOVENUMBER       '\d+\.(\.\.)?'                                                          ;
        token NUMERICMOVE      '[\d]+(\s?[-x]\s?[\d]+)+[*?!]?'                                         ;
        token ALPHANUMERICMOVE '([a-h][1-8](\s*[x:]\s*[a-h][1-8])+)|([a-h][1-8]\s*[-]?\s*[a-h][1-8])'  ;
        token MOVESTRENGTH     '([!?]+)|(\([!?]+\))'                                                   ;
        token NAG              '\$\d+'                                                                 ;
        token SETUP            '/[^/]*/'                                                               ;
        token STRING           '"(\\"|[^"])*"'                                                         ;
        token COMMENT          '\{[^}]*\}'                                                             ;
        token IDENTIFIER       '[A-Z][a-zA-Z0-9_]*'                                                    ;
                                                                                                       
        # Game independent productions                                                                 
        START         -> PdnFile                                                                       ;
        PdnFile       -> Game (GameSeparator Game)* GameSeparator?                                     ;
        GameSeparator -> ASTERISK | Result1 | Result2                                                  ;
        Game          -> (GameHeader GameBody?) | GameBody                                             ;
        GameHeader    -> PdnTag+                                                                       ;
        GameBody      -> (GameMove | Variation | COMMENT | SETUP | NAG)+                               ;
        PdnTag        -> LBRACKET IDENTIFIER STRING RBRACKET                                           ;
        GameMove      -> MOVENUMBER? Move MOVESTRENGTH?                                                ;
        Variation     -> LPAREN GameBody RPAREN                                                        ;
                                                                                                       
        # Game dependent productions                                                                   
        Move          -> NUMERICMOVE | ALPHANUMERICMOVE | ELLIPSES                                     ;
        GameResult    -> Result1 | Result2                                                             ;
        Result1       -> WIN1 | DRAW1 | LOSS1                                                          ;
        Result2       -> WIN2 | DRAW2 | LOSS2 | DOUBLEFORFEIT                                          ;
    '''


def pdn_parse(text):
    try:
        parser = PDNParser()
        parser(text)
        return True
    except Exception as e:
        print(e)
        return False
