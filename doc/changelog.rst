=========
Changelog
=========

8 December 2025

* Added optional player tags ``WhiteFmjdId`` and ``BlackFmjdId``.

9 January 2025

* Use a new layout for the documentation.

* Automatically generate the documentation using CI.

24 June 2017

* Put the standard in a github repository on https://github.com/wiegerw/pdn.

9 June 2017

* Added some time control tag examples provided by Igor Le Masson.

1 January 2016

* Made some corrections and improvements to the FEN grammar, noted by Rein Halbersma.

* Added an archived copy of the PDN 2.0 standard, since it is no longer available online.

* Added Zimbabwean pool checkers.

3 May 2014

* Changed the GameType tag for Jamaican draughts: A5 -> A1

* Removed the vertical direction from the Notation field, since in all
  known cases the notation direction is horizontal.

30 April 2014

* Added a test page for the GameType tag.

* Corrected the description of the notation field of the GameType tag.

* Made some corrections to the GameType table.

  * Pool checkers (unified): A1 -> A0

  * Turkish draughts: A1 -> A0

27 April 2014

* Changed the result type of Frisian draughts to Default.

18 April 2014

* Made some corrections to the gametype table, noted by Rein Halbersma.

  * Russian/Brazilian/Czech: A1 -> A0

  * Spantsiretti: N2 -> A0

  * Thai: black starts, and N1 -> N2

* Added an improved description of move disambiguation, supplied by Ed Gilbert.

* Added a section with proposals for the next version of the standard.

27 May 2013

* Made some improvements to the gametype section, with the help of Jake Cacher.

  * Added game types Jamaican draughts and Pool checkers

  * Added some examples of the board layout of game types

  * Adapted the interpretation of the invert flag in the game type

  * Extended the notation flag of the game type, such that the Jamaican draughts notation is supported

* Added an example for setup commands, supplied by Gérard Taille.

* Added a proposal for the notation null moves, by Gérard Taille.

12 March 2012

* Added a section about character encodings.

* Adapted the allowed values for the ``Result`` tag, and added a ``ResultFormat`` tag that can be used to specify uncommon result values.

* Added ``clk``, ``mct``, ``egt`` and ``emt`` embedded commands.

* Added ``TimeControlWhite`` and ``TimeControlBlack`` tags for specifying individual time settings.

* Added requirements for notation type and capture separators.

* Adapted the grammars to allow alpha numeric moves without separator (a3b4).

* Added documentation about when the full capture notation may/must be used.

* Added requirement about disambiguation of ambiguous moves.

* Added a comment that the empty string is always allowed for a PDN tag value.

* Added line comments starting with a ``%``.

* Added FEN values with unknown color (specified using ``?``).

* Updated the grammars.

* Updated the PDN checker.
