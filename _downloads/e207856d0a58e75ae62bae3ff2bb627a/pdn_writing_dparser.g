{
// Copyright: Wieger Wesselink 2011, <wieger at 10x10 dot org>
//
// Distributed under the Boost Software License, Version 1.0.
// http://www.boost.org/LICENSE_1_0.txt
//
// Portable Draughts Notation (PDN) 3.0 Draft Standard
//
// 12 March 2012
}

// Game independent productions
PdnFile          : Game (GameSeparator Game)* GameSeparator?                        ;
GameSeparator    : ASTERISK                                                         ;
Game             : (GameHeader GameBody?) | GameBody                                ;
GameHeader       : PdnTag+                                                          ;
GameBody         : (GameMove | Variation | COMMENT | SETUP | NAG)+                  ;
PdnTag           : LBRACKET IDENTIFIER STRING RBRACKET                              ;
GameMove         : MOVENUMBER? Move MOVESTRENGTH?                                   ;
Variation        : LPAREN GameBody RPAREN                                           ;

// Game dependent productions
Move             : NormalMove | CaptureMove | ALPHAMOVE                             ;
NormalMove       : Square MOVESEPARATOR Square                                      ;
CaptureMove      : Square (CAPTURESEPARATOR Square)+                                ;
Square           : ALPHASQUARE | NUMSQUARE                                          ;

// Tokens
MOVENUMBER       : "[0-9]+\.(\.\.)?"                                                ;
MOVESEPARATOR    : "-"                                                              ;
CAPTURESEPARATOR : "x"                                                              ;
ALPHASQUARE      : "[a-h][1-8]"                                                     ;
ALPHAMOVE        : "[a-h][1-8][a-h][1-8]"                                           ;
NUMSQUARE        : "[1-9][0-9]?"                                                    ;
MOVESTRENGTH     : "([\!\?]+)|(\([\!\?]+\))"                                        ;
NAG              : "\$[0-9]+"                                                       ;
LPAREN           : "\("                                                             ;
RPAREN           : "\)"                                                             ;
LBRACKET         : "\["                                                             ;
RBRACKET         : "\]"                                                             ;
ASTERISK         : "\*"                                                             ;
SETUP            : "\/[^\/]*\/"                                                     ;
STRING           : "\"([^\"]|\\\")*\""                                              ;
COMMENT          : "\{[^}]*\}"                                                      ;
IDENTIFIER       : "[A-Z][a-zA-Z0-9_]*"                                             ;

whitespace       : "([ \t\n\r]|(%[^\n\r]*))*"                                       ;
