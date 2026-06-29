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
