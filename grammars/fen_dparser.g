{
// Copyright: Wieger Wesselink 2011-2016, <wieger at 10x10 dot org>
//
// Distributed under the Boost Software License, Version 1.0.
// http://www.boost.org/LICENSE_1_0.txt
//
// FEN Grammar
//
// 1 January 2016
}

// Productions
Fen                        : COLOR (NumericSquares | AlphaNumericSquares) DOT?       ;
NumericSquares             : (COLON COLOR NumericSquareSequence)+                    ;
NumericSquareSequence      : NumericSquareRange (COMMA NumericSquareRange)*          ;
NumericSquareRange         : KING? NUMSQUARE (HYPHEN NUMSQUARE)?                     ;
AlphaNumericSquares        : (COLON COLOR AlphaNumericSquareSequence)+               ;
AlphaNumericSquareSequence : KING? ALPHASQUARE (COMMA KING? ALPHASQUARE)*            ;

// Tokens
COLOR                      : "[WB?]"                                                 ;
KING                       : "K"                                                     ;
ALPHASQUARE                : "[a-h][1-8]"                                            ;
NUMSQUARE                  : "([1-9][0-9]*)|(0[1-9][0-9]*)|0"                        ;
HYPHEN                     : "\-"                                                    ;
COMMA                      : "\,"                                                    ;
COLON                      : "\:"                                                    ;
DOT                        : "\."                                                    ;
