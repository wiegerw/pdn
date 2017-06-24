.. _issues-section:

==================
PDN parsing issues
==================

This section gives an overview of some issues with existing PDN definitions. In particular
those issues that are important when writing a PDN parser.

------------------
Game Separator (1)
------------------

The ``*`` symbol is both used as a game terminator/separator and as a move strength
indicator to denote a forced move. This introduces a nasty ambiguity.
For example the string ``1-6* 32-28`` can be interpreted as one game containing two moves,
or as two games separated by a ``*``. Since ``*`` is commonly used in draughts publications
to denote forced moves, the preferred solution would be to disallow ``*`` as a game separator,
and to use a different symbol like ``#``. However, this would completely destroy backward
compatibility. A less intrusive solution is to disallow ``*`` as a move strength indicator.
Note that there is an alternative available in the form of the ``$7`` numeric annotation
glyph. Yet another solution is to demand that there can be no space between a move and it's
corresponding move strength. Then a move and it's corresponding move strength can be
defined as one token.

------------------
Game Separator (2)
------------------

It is common practice to terminate games with their result. In PGN this is no problem,
since the chess results differ substantially from chess moves. But in draughts some
results like ``1-0`` and ``1-1`` are very similar to normal draughts moves. This complicates
parsing. For example, if the result ``1-1`` is defined as a token, then parsers may easily
get confused by a move like ``1-18``. Several parsers insist on parsing this as
``1-1`` followed by an ``8``. This problem is likely to occur when a move is split up into
separate tokens.

Since the result of a game can already be specified in PDN using the ``Result`` tag, there
is no need to use a game result as a game separator. It can even be considered as bad style
to have two different ways to specify the result of a game. It seems therefore logical to
forbid using the result of a game as a game terminator (or separator).

-----------------
Capture Separator
-----------------

The squares of a capture are separated using the symbol ``x``, for example in the
move ``32x23``. If one defines a capture as a production

  ..

     CaptureMove = Square "x" Square
  
then there can easily be conflicts with identifier tokens. Tokenizers are often greedy,
which means that they can insist on parsing ``x23`` as an identifier token, instead
of a capture separator ``x`` followed by a square ``23``. Some parsers offer solutions to
this type of problem, but not all of them. Note that this problem can be avoided by defining
a move as a single token.

----------
Move token
----------

It is an important question whether a move should be defined as a single token (by means of
a regular expression), or as a production consisting of multiple elements. A production has
the benefit that the structure of a move can be represented more clearly. But as explained
above, then a more powerful parser is needed. If a move is defined as a token, then a
simple LL(1) parser is enough to parse PDN.

-------------
Move strength
-------------

In draughts publications a move strength can be wrapped in parentheses, like in ``31-27(?)``.
Parentheses are also used to define variations in an analysis, for example
``1.32-28 18-23 2.38-32 ( 2.37-32? 23-29! ) 12-18``. This introduces an ambiguity, but in
most parsers this can be resolved by defining a move strength as a single token.
