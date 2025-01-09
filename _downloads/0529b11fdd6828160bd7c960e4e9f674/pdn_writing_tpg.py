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

        token LPAREN           '\('                                                                    ;                                          
        token RPAREN           '\)'                                                                    ;
        token LBRACKET         '\['                                                                    ;
        token RBRACKET         '\]'                                                                    ;                             
        token ASTERISK         '\*'                                                                    ;
        token MOVENUMBER       '\d+\.(\.\.)?'                                                          ;       
        token NUMERICMOVE      '[\d]+(\s?[-x]\s?[\d]+)+[*?!]?'                                         ;
        token ALPHANUMERICMOVE '([a-h][1-8](\s*[x:]\s*[a-h][1-8])+)|([a-h][1-8]\s*[-]?\s*[a-h][1-8]);' ;
        token MOVESTRENGTH     '([!?]+)|(\([!?]+\))'                                                   ;
        token NAG              '\$[0-9]+'                                                              ;
        token SETUP            '/[^/]*/'                                                               ;
        token STRING           '"(\\"|[^"])*"'                                                         ;
        token COMMENT          '\{[^}]*\}'                                                             ;
        token IDENTIFIER       '[A-Z][a-zA-Z0-9_]*'                                                    ;
                                                                                                       
        # Game independent productions                                                                 
        START         -> PdnFile                                                                       ;        
        PdnFile       -> Game (GameSeparator Game)* GameSeparator?                                     ;
        GameSeparator -> ASTERISK                                                                      ;
        Game          -> (GameHeader GameBody?) | GameBody                                             ;
        GameHeader    -> PdnTag+                                                                       ;
        GameBody      -> (GameMove | Variation | COMMENT | SETUP | NAG)+                               ;
        PdnTag        -> LBRACKET IDENTIFIER STRING RBRACKET                                           ;
        GameMove      -> MOVENUMBER? Move MOVESTRENGTH?                                                ;
        Variation     -> LPAREN GameBody RPAREN                                                        ;
                                                                                                       
        # Game dependent productions                                                                   
        Move          -> NUMERICMOVE | ALPHANUMERICMOVE                                                ;
    '''


def pdn_parse(text):
    try:
        parser = PDNParser()
        parser(text)
        return True
    except Exception as e:
        print(e)
        return False
