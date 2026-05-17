.. _gametype-section:

==================================
GameType tag
==================================

The GameType tag defines the type of the draughts game, including the size of the board
and the preferred notation. It has been previously defined on [Grimminck]_.

The GameType tag has the following syntax:

``GameType "Type-number [,Start colour (W/B),Board width, Board height, Notation [,Invert-flag]]"``

A regular expression for the GameType tag is

::

  "[0-9]+(,[WB],[0-9]+,[0-9]+,[ANS][0123](,[01])?)?"

The game type is a number followed by some optional attributes. Several numbers are
predefined, as given by the following table. A test page for the GameType tag can be
found at :download:`gametype.html <gametype.html>`.

+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| Type  | Game                                                                                   | Full details                 | Result type   | Capture Separator |
+=======+========================================================================================+==============================+===============+===================+
| 0     | `Chess <https://en.wikipedia.org/wiki/Chess>`_                                         |                              |               |                   |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 1     | `Chinese chess <https://en.wikipedia.org/wiki/Xiangqi>`_                               |                              |               |                   |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 2-19  | Future chess expansion                                                                 |                              |               |                   |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 20    | `10x10 International draughts <https://en.wikipedia.org/wiki/International_draughts>`_ | [GameType "20,W,10,10,N2,0"] | International | x                 |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 21    | `English draughts <https://en.wikipedia.org/wiki/English_draughts>`_                   | [GameType "21,B,8,8,N1,0"]   | Default       | x                 |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 22    | `Italian draughts <https://en.wikipedia.org/wiki/Italian_draughts>`_                   | [GameType "22,W,8,8,N2,1"]   | Default       | x                 |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 23    | `American pool checkers <https://en.wikipedia.org/wiki/Checkers>`_                     | [GameType "23,B,8,8,N1,0"]   | Default       | x                 |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
|       | Pool checkers (unified) ***)**                                                         | [GameType "23,W,8,8,A0,0"]   | Default       | x                 |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
|       | Zimbabwean pool checkers ***)**                                                        | [GameType "23,W,8,8,A0,0"]   | Default       | x                 |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
|       | Jamaican draughts ***)**                                                               | [GameType "23,B,8,8,A1,1"]   | Default       | x                 |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 24    | Spanish draughts                                                                       | [GameType "24,W,8,8,N1,1"]   | Default       | x                 |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 25    | `Russian draughts <https://en.wikipedia.org/wiki/Russian_draughts>`_                   | [GameType "25,W,8,8,A0,0"]   | Default       | :                 |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 26    | `Brazilian draughts <https://en.wikipedia.org/wiki/Brazilian_draughts>`_               | [GameType "26,W,8,8,A0,0"]   | Default       | x                 |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 27    | `Canadian draughts <https://en.wikipedia.org/wiki/Canadian_draughts>`_                 | [GameType "27,W,12,12,N2,0"] | International | x                 |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 28    | Portuguese draughts                                                                    | [GameType "28,W,8,8,N1,1"]   | Default       | x                 |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 29    | `Czech draughts <https://en.wikipedia.org/wiki/Czech_draughts>`_                       | [GameType "29,W,8,8,A0,0"]   | Default       | x                 |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 30    | `Turkish draughts <https://en.wikipedia.org/wiki/Turkish_draughts>`_                   | [GameType "30,W,8,8,A0,0"]   | Default       | x                 |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 31    | `Thai draughts <https://en.wikipedia.org/wiki/Thai_draughts>`_                         | [GameType "31,B,8,8,N2,0"]   | Default       | -                 |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 40    | `Frisian draughts <https://en.wikipedia.org/wiki/Frisian_draughts>`_                   | [GameType "40,W,10,10,N2,0"] | Default       | x                 |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 41    | Spantsiretti draughts                                                                  | [GameType "41,W,10,8,A0,0"]  | Default       | :                 |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 42-49 | Future draughts expansion                                                              |                              |               |                   |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 50    | `Othello <https://en.wikipedia.org/wiki/Othello_(board_game)>`_                        |                              |               |                   |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+
| 51..  | Future expansion                                                                       |                              |               |                   |
+-------+----------------------------------------------------------------------------------------+------------------------------+---------------+-------------------+

***)** Note that Pool checkers and Jamaican draughts have
been added later. They have the same rules as American pool checkers, but they use algebraic
notation. Moreover, in Jamaican draughts the direction of the
numbering is vertical instead of horizontal. Zimbabwean is played on the light squares.
All checkers variants share the number 23, but the abbreviated version ``[GameType "23"]``
still expands to ``[GameType "23,B,8,8,N1,0"]`` (American pool checkers).

The game types 29, 30, 31, 40 and 41 were added
based on conventions of the game site `Play OK <http://playok.com>`_ and the
program `Aurora Borealis <http://aurora.shashki.com/>`_.

===============  ===================================================
  Attribute          Description
===============  ===================================================
Start-colour     Either W or B - white/black side starts
Board-width      Width of board.
Board-height     Height of board.
Notation         A character indicating the notation type

                 - A = alpha/numeric like chess,
                 - N = numeric like draughts.
                 - S = SAN - short-form notation.

                 followed by a number indicating the location of the
                 first square (A1 or 1) from the perspective of the
                 starting player

                 - 0 = Bottom left
                 - 1 = Bottom right
                 - 2 = Top left
                 - 3 = Top right

Invert-flag      - 0 = The bottom left corner is a playing square
                 - 1 = The bottom left corner is not a playing square
===============  ===================================================

.. important::
   The interpretation of the Invert-flag has been changed! The previous
   interpretation (0 = Play on dark squares, 1 = Play on light squares)
   was not accurate for certain game types.

.. note::
   The Start-colour field is just an indication for the colour of the
   pieces, but it has no influence on the notation.

.. note::
   The principal direction of the notation is assumed to be horizontal.
   This means that square 2 is always to the left or to the right of square 1.

.. note::
   Usually the game is played on the dark squares.

--------
Examples
--------

::

  [GameType "0"]                   {Straight chess}
  [GameType "0,W,8,8,S0"]          {Straight chess with full spec}
  [GameType "20"]                  {10x10 draughts}
  [GameType "21,B,8,8,N1,0"]       {English draughts with full spec}

Italian draughts uses the following notation:

   .. image:: gametype_italian.png

For Italian draughts the first square (1) is located in the top left corner of
the board. The next square (2) can be found by moving in horizontal direction
to the right. Therefore Italian draughts gets the notation number 2, that
corresponds with (Top left, horizontal).

American pool checkers uses the following notation:

   .. image:: gametype_american_pool_checkers.png

Pool checkers uses the following notation:

   .. image:: gametype_unified_pool_checkers.jpg

Jamaican draughts uses the following notation:

   .. image:: gametype_jamaican_draughts.png

