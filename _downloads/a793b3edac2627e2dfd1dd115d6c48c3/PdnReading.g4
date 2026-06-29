// Copyright: Wieger Wesselink 2011-2024, <wieger at 10x10 dot org>
//
// Distributed under the Boost Software License, Version 1.0.
// http://www.boost.org/LICENSE_1_0.txt
//
// Portable Draughts Notation (PDN) Reading Grammar — ANTLR4

grammar PdnReading;

// Parser rules

pdnFile         : game (gameSeparator game)* gameSeparator? EOF ;
gameSeparator   : ASTERISK | result ;
game            : (gameHeader gameBody?) | gameBody ;
gameHeader      : pdnTag+ ;
gameBody        : (gameMove | variation | COMMENT | SETUP | NAG)+ ;
pdnTag          : LBRACKET IDENTIFIER STRING RBRACKET ;
gameMove        : MOVENUMBER? move MOVESTRENGTH? ;
variation       : LPAREN gameBody RPAREN ;

move            : normalMove | captureMove | ALPHAMOVE | ELLIPSES ;
normalMove      : square MOVESEPARATOR square ;
captureMove     : square (CAPTURESEPARATOR square)+ ;
square          : ALPHASQUARE | NUMSQUARE ;
result          : result1 | result2 | DOUBLEFORFEIT ;
result1         : WIN1 | DRAW1 | LOSS1 ;
result2         : WIN2 | DRAW2 | LOSS2 ;

// Lexer rules
// Result tokens are placed first so max-munch picks them over NUMSQUARE/MOVESEPARATOR.

WIN1            : '1-0' ;
DRAW1           : '1/2-1/2' ;
LOSS1           : '0-1' ;
WIN2            : '2-0' ;
// Semantic predicate: '1-1' must not be followed by a digit, otherwise
// numeric moves like 1-10 would be mis-tokenised as DRAW2 + stray '0'.
DRAW2           : '1-1' { self._input.LA(1) < 48 or self._input.LA(1) > 57 }? ;
LOSS2           : '0-2' ;
DOUBLEFORFEIT   : '0-0' ;

ELLIPSES        : '...' ;
// MOVENUMBER: digits followed by one dot, optionally followed by two more
// dots, giving "1." or "1..." (move continuation indicator).
MOVENUMBER      : [0-9]+ '.' '..'? ;

// MOVESTRENGTH must appear before LPAREN so the rule ordering is clear,
// though ANTLR4 max-munch already guarantees '(!?!!!)' beats '(' on length.
MOVESTRENGTH    : [!?]+ | '(' [!?]+ ')' ;
NAG             : '$' [0-9]+ ;

// ALPHAMOVE before ALPHASQUARE: "e4e5" (4 chars) beats "e4" (2 chars) via
// max-munch; explicit ordering documents the intent.
ALPHAMOVE       : [a-h] [1-8] [a-h] [1-8] ;
ALPHASQUARE     : [a-h] [1-8] ;
// Squares: 1-9, 10-50, and 01-09 (zero-prefixed, used in some game types).
NUMSQUARE       : [1-9] [0-9]? | '0' [1-9] ;

MOVESEPARATOR   : '-' ;
CAPTURESEPARATOR: [x:] ;

LPAREN          : '(' ;
RPAREN          : ')' ;
LBRACKET        : '[' ;
RBRACKET        : ']' ;
ASTERISK        : '*' ;

// SETUP: a setup string delimited by forward slashes, e.g. /W:Wk50.B:B1,2/.
SETUP           : '/' ~'/'* '/' ;
// STRING: double-quoted; backslash escapes any following character.
STRING          : '"' ( ~[\\"] | '\\' . )* '"' ;
COMMENT         : '{' ~'}'* '}' ;
// Tag identifiers start with an uppercase letter.
IDENTIFIER      : [A-Z] [a-zA-Z0-9_]* ;

WS              : [ \t\n\r]+ -> skip ;
LINE_COMMENT    : '%' ~[\r\n]* -> skip ;
