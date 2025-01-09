.. _fen-section:

==================================
FEN tag
==================================

The Forsyth-Edwards Notation or shortly FEN tag defines a position on the board.
In the PDN 2.0 draft standard the following syntax is proposed:

``[TURN]:[COLOUR1][[K][SQUARE_NUM][,]...]:[COLOUR2][[K][SQUARE_NUM][,]...]``

We extend this syntax with ranges of numeric fields, such that the start
position of international draughts can be defined as ``[FEN "W:W31-50:B1-20"]``.

Another extension is that we allow ``?`` to denote an unknown color.

The following grammar describes the formal syntax of the value of a FEN tag.

::

  // Productions
  Fen                        : COLOR (NumericSquares | AlphaNumericSquares) DOT?
  NumericSquares             : (COLON COLOR NumericSquareSequence)+
  NumericSquareSequence      : NumericSquareRange (COMMA NumericSquareRange)*
  NumericSquareRange         : KING? NUMSQUARE (HYPHEN NUMSQUARE)?
  AlphaNumericSquares        : (COLON COLOR AlphaNumericSquareSequence)+
  AlphaNumericSquareSequence : KING? ALPHASQUARE (COMMA KING? ALPHASQUARE)*
  
  // Tokens
  COLOR                      : "[WB?]"
  KING                       : "K"
  ALPHASQUARE                : "[a-h][1-8]"
  NUMSQUARE                  : "([1-9][0-9]*)|(0[1-9][0-9]*)|0"
  HYPHEN                     : "\-"
  COMMA                      : "\,"
  COLON                      : "\:"
  DOT                        : "\."

.. important::
   Some corrections have been made.

   * The ``COMMA`` in ``NumericSquareSequence`` and ``AlphaNumericSquareSequence`` is mandatory.

   * A missing ``KING?`` in ``AlphaNumericSquareSequence`` has been added.

   * ``NUMSQUARE`` may contain more than two digits (it is up to the implementer to do range checks).

------------
Restrictions
------------

The following restrictions apply when writing a FEN tag:

- No embedded spaces are allowed inside the value of a FEN tag
- No dot ('.') is allowed at the end of the value of a FEN tag

--------
Examples
--------

::

  [FEN "B:W18,24,27,28,K10,K15:B12,16,20,K22,K25,K29"]
  [FEN "B:W18,19,21,23,24,26,29,30,31,32:B1,2,3,4,6,7,9,10,11,12"]
  [FEN "W:W31-50:B1-20"]

----------
Extensions
----------

The above grammar does not allow positions with no pieces for one of the
players. It should therefore be extended to accept empty ranges of pieces.
