{
// Copyright: Wieger Wesselink 2011, <wieger at 10x10 dot org>
//
// Distributed under the Boost Software License, Version 1.0.
// http://www.boost.org/LICENSE_1_0.txt
//
// Time Control Grammar
//
// 31 August 2011
}

// Productions
TimeControl   : UNKNOWN | NOTIME | CompositeTime                        ;
TimeElement   : MOVES_SECONDS | INCREMENTAL | SUDDENDEATH | SANDCLOCK   ;
CompositeTime : TimeElement (COLON TimeElement)*                        ;

// Tokens
MOVES_SECONDS : "[0-9]+\/[0-9]+"                                        ;
INCREMENTAL   : "[0-9]+\+[0-9]+"                                        ;
SUDDENDEATH   : "[0-9]+"                                                ;
SANDCLOCK     : "\*[0-9]+"                                              ;
UNKNOWN       : "\?"                                                    ;
NOTIME        : "\-"                                                    ;
COLON         : "\:"                                                    ;

// Additional checks need to be done to make sure that SUDDENDEATH,
// SANDCLOCK and INCREMENTAL are the last values of the range.
