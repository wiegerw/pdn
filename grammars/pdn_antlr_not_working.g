grammar pdn_antlr;

options {
  backtrack=true;
}

tokens {

Identifier       = '[a-zA-Z_][a-zA-Z0-9_]*'                                        ;
MoveNumber       = '[0-9]+\.(\.\.)?'                                               ;
Nag              = '\$[0-9]+'                                                      ;
LParen           = '('                                                             ;
RParen           = ')'                                                             ;
LBrace           = '{'                                                             ;
RBrace           = '}'                                                             ;
LBracket         = '['                                                             ;
RBracket         = ']'                                                             ;
Slash            = '/'                                                             ;
DoubleQuote      = '"'                                                             ;
Asterisk         = '*'                                                             ;
MoveSeparator    = '-'                                                             ;
CaptureSeparator = '[:x]'                                                          ;
AlphaSquare      = '[a-h][1-8]'                                                    ;
NumSquare        = '([1-9][0-9]?)|([0][1-9])'                                      ;
Win              = '1-0'                                                           ;
Draw             = '1/2-1/2'                                                       ;
Loss             = '0-1'                                                           ;
IWin             = '2-0'                                                           ;
IDraw            = '1-1'                                                           ;
ILoss            = '0-2'                                                           ;
IZero            = '0-0'                                                           ;

}

PdnFile          : Game (GameSeparator Game)* GameSeparator?                        ;
GameSeparator    : Asterisk | GameResult                                            ;
Game             : (GameHeader GameBody?) | GameBody                                ;
GameHeader       : (PdnTag)+                                                        ;
GameBody         : (GameMove | Variation | Comment | Setup | Nag)+                  ;
PdnTag           : LBracket Identifier String RBracket                              ;
GameMove         : MoveNumber? Move MoveStrength?                                   ;
Variation        : LParen GameBody RParen                                           ;
MoveStrength     : '?' | '!' | '(!)' | '!!' | '!?' '?!'                             ;
Setup            : Slash '[^\/]*' Slash                                             ;
String           : DoubleQuote '([^\"]|\\\")*' DoubleQuote                          ;
Comment          : LBrace '([^}]|\\})*' RBrace                                      ;
Move             : NormalMove | CaptureMove                                         ;
NormalMove       : Square MoveSeparator Square                                      ;
CaptureMove      : Square (CaptureSeparator Square)+                                ;
Square           : AlphaSquare | NumSquare                                          ;
GameResult       : Result | IResult                                                 ;
Result           : Win | Draw | Loss                                                ;
IResult          : IWin | IDraw | ILoss | IZero                                     ;
