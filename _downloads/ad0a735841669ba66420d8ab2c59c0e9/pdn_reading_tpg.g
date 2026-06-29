separator space: '\s+' ;
separator comments: '%.*' ;

token WIN1             '1-0'                                                                   ;
token DRAW1            '1/2-1/2'                                                               ;
token LOSS1            '0-1'                                                                   ;
token WIN2             '2-0'                                                                   ;
token DRAW2            '1-1(?![0-9])'                                                          ;
token LOSS2            '0-2'                                                                   ;
token DOUBLEFORFEIT    '0-0'                                                                   ;
token MOVESTRENGTH     '([!?]+)|(\([!?]+\))'                                                   ;
token LPAREN           '\('                                                                    ;
token RPAREN           '\)'                                                                    ;
token LBRACKET         '\['                                                                    ;
token RBRACKET         '\]'                                                                    ;
token ASTERISK         '\*'                                                                    ;
token ELLIPSES         '\.\.\.'                                                                ;
token MOVENUMBER       '\d+\.(\.\.)?'                                                          ;
token NUMERICMOVE      '[\d]+(\s?[-x]\s?[\d]+)+[*?!]?'                                         ;
token ALPHANUMERICMOVE '([a-h][1-8](\s*[x:]\s*[a-h][1-8])+)|([a-h][1-8]\s*[-]?\s*[a-h][1-8])'  ;
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
