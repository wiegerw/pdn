.. _implementation-section:

==================
PDN Implementation
==================

This section contains concrete examples of PDN grammars.

-------
DParser
-------

[DParser]_ is a C parser generator.

* :download:`pdn_reading.g <../grammars/pdn_reading.g>` A fairly liberal reading grammar.
* :download:`pdn_writing.g <../grammars/pdn_writing.g>` A PDN 3.0 writing grammar.
* :download:`fen.g <../grammars/fen.g>` A grammar for FEN strings.
* :download:`timecontrol.g <../grammars/timecontrol.g>` A grammar for time controls.

----------
Grammatica
----------

[Grammatica]_ is a java parser generator.

* :download:`pdn_reading.grammar <../grammars/pdn_reading.grammar>` A fairly liberal reading grammar.
* :download:`pdn_writing.grammar <../grammars/pdn_writing.grammar>` A PDN 3.0 writing grammar.
* :download:`fen.grammar <../grammars/fen.grammar>` A grammar for FEN strings.
* :download:`timeControl.grammar <../grammars/timeControl.grammar>` A grammar for time controls.

- The Grammatica grammars are LL(1) grammars. They define a move as a token to make this possible.
- The Grammatica grammars contain a workaround for move strengths, since the regular expressions in Grammatica do not behave correctly.

--------------------
Toy Parser Generator
--------------------

[TPG]_ is a python parser generator.

* :download:`pdn_reading_tpg.py <../python/pdn_reading_tpg.py>` A fairly liberal reading grammar.
* :download:`pdn_writing_tpg.py <../python/pdn_writing_tpg.py>` A PDN 3.0 writing grammar.

------
ANTLR4
------

[ANTLR4]_ is a parser generator supporting many target languages, including Python.

* :download:`PdnReading.g4 <../grammars/PdnReading.g4>` A fairly liberal reading grammar.
* :download:`PdnWriting.g4 <../grammars/PdnWriting.g4>` A PDN 3.0 writing grammar.

- The ANTLR4 grammars use a semantic predicate on the ``DRAW2`` token to prevent
  the result ``1-1`` from being mis-tokenised when it appears as part of a numeric
  move such as ``1-10``.

----------
Test files
----------
* :download:`games.zip <../games/games.zip>` A collection of PDN games used for testing the grammars.

.. [DParser] DParser, a GLR parser generator written in C http://dparser.sourceforge.net/
.. [Grammatica] Grammatica, an LL parser generator written in java http://grammatica.percederberg.net/
.. [TPG] Toy Parser Generator, a parser written in python http://cdsoft.fr/tpg/
.. [ANTLR4] ANTLR4, a parser generator supporting multiple target languages https://www.antlr.org/
