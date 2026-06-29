=========
Changelog
=========

29 June 2026

* Renamed all grammar files in ``grammars/`` to follow a consistent
  ``topic_parser.ext`` convention (e.g. ``pdn_reading_dparser.g``,
  ``pdn_reading_antlr.g4``, ``pdn_reading_grammatica.grammar``).

* Extracted the TPG grammars from inline Python class docstrings into
  standalone files ``grammars/pdn_reading_tpg.g`` and
  ``grammars/pdn_writing_tpg.g``.

* Added an ANTLR4 reading and writing grammar
  (``grammars/pdn_reading_antlr.g4``, ``grammars/pdn_writing_antlr.g4``)
  with an auto-generated Python parser.

* Moved Python tests to ``python/tests/``.

* Restructured the Python package build: each parser engine now has its
  own pip extra (``[tpg]``, ``[dparser]``, ``[antlr4]``, ``[grammatica]``).
  All parser dependencies are managed via a custom build backend that clones
  or downloads each engine to a fixed local directory (``git-tpg``,
  ``git-dparser``, ``git-grammatica``) so repeated installs do not
  re-download anything.

25 June 2026

* Replaced the board-diagram images in the documentation, which had been
  produced by different tools over the years and had inconsistent styles,
  with images generated directly from the GameType test page
  (``doc/_static/gametype_tester.html``) via ``doc/generate_images.py``.

24 June 2026

* Made the test page for the GameType tag fully interactive: every tag
  field (game type, start color, columns, rows, notation, etc.) and every
  board/piece color can now be edited directly, in addition to selecting
  a predefined game type from the dropdown.

* Gave the pieces on the test page a more realistic, 3D look.

* Added a button to the test page for submitting a change request or an
  addition by email.

* Published the test page as a regular page
  (``doc/_static/gametype_tester.html``) instead of a download, so it no
  longer clashes with the page generated from ``gametype.rst``.

13 April 2026

* Corrected the starting player of Jamaican draughts, noted by Harris Mowbray.

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
