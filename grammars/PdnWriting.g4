// Copyright: Wieger Wesselink 2011-2024, <wieger at 10x10 dot org>
//
// Distributed under the Boost Software License, Version 1.0.
// http://www.boost.org/LICENSE_1_0.txt
//
// Portable Draughts Notation (PDN) Writing Grammar — ANTLR4
//
// More restrictive than the reading grammar:
//   - Game separator is '*' only (no result tokens).
//   - Capture separator is 'x' only (not ':').
//   - Square numbers have no zero prefix (1-50, not 01-09).
//   - No ELLIPSES, no DOUBLEFORFEIT, no international results.

grammar PdnWriting;

// Parser rules

pdnFile         : game (ASTERISK game)* ASTERISK? EOF ;
game            : (gameHeader gameBody?) | gameBody ;
gameHeader      : pdnTag+ ;
gameBody        : (gameMove | variation | COMMENT | SETUP | NAG)+ ;
pdnTag          : LBRACKET IDENTIFIER STRING RBRACKET ;
gameMove        : MOVENUMBER? move MOVESTRENGTH? ;
variation       : LPAREN gameBody RPAREN ;

move            : normalMove | captureMove | ALPHAMOVE ;
normalMove      : square MOVESEPARATOR square ;
captureMove     : square (CAPTURESEPARATOR square)+ ;
square          : ALPHASQUARE | NUMSQUARE ;

// Lexer rules

MOVENUMBER      : [0-9]+ '.' '..'? ;

MOVESTRENGTH    : [!?]+ | '(' [!?]+ ')' ;
NAG             : '$' [0-9]+ ;

ALPHAMOVE       : [a-h] [1-8] [a-h] [1-8] ;
ALPHASQUARE     : [a-h] [1-8] ;
NUMSQUARE       : [1-9] [0-9]? ;

MOVESEPARATOR   : '-' ;
CAPTURESEPARATOR: 'x' ;

LPAREN          : '(' ;
RPAREN          : ')' ;
LBRACKET        : '[' ;
RBRACKET        : ']' ;
ASTERISK        : '*' ;

SETUP           : '/' ~'/'* '/' ;
STRING          : '"' ( ~[\\"] | '\\' . )* '"' ;
COMMENT         : '{' ~'}'* '}' ;
IDENTIFIER      : [A-Z] [a-zA-Z0-9_]* ;

WS              : [ \t\n\r]+ -> skip ;
LINE_COMMENT    : '%' ~[\r\n]* -> skip ;
