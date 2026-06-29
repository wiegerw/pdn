.. _implementation-section:

==================
PDN Implementation
==================

This section contains concrete examples of PDN grammars.

-------
DParser
-------

[DParser]_ is a C parser generator.

* :download:`pdn_reading_dparser.g <../grammars/pdn_reading_dparser.g>` A fairly liberal reading grammar.
* :download:`pdn_writing_dparser.g <../grammars/pdn_writing_dparser.g>` A PDN 3.0 writing grammar.
* :download:`fen_dparser.g <../grammars/fen_dparser.g>` A grammar for FEN strings.
* :download:`timecontrol_dparser.g <../grammars/timecontrol_dparser.g>` A grammar for time controls.

----------
Grammatica
----------

[Grammatica]_ is a java parser generator.

* :download:`pdn_reading_grammatica.grammar <../grammars/pdn_reading_grammatica.grammar>` A fairly liberal reading grammar.
* :download:`pdn_writing_grammatica.grammar <../grammars/pdn_writing_grammatica.grammar>` A PDN 3.0 writing grammar.
* :download:`fen_grammatica.grammar <../grammars/fen_grammatica.grammar>` A grammar for FEN strings.
* :download:`timecontrol_grammatica.grammar <../grammars/timecontrol_grammatica.grammar>` A grammar for time controls.

- The Grammatica grammars are LL(1) grammars. They define a move as a token to make this possible.
- The Grammatica grammars contain a workaround for move strengths, since the regular expressions in Grammatica do not behave correctly.

--------------------
Toy Parser Generator
--------------------

[TPG]_ is a python parser generator.

* :download:`pdn_reading_tpg.g <../grammars/pdn_reading_tpg.g>` A fairly liberal reading grammar.
* :download:`pdn_writing_tpg.g <../grammars/pdn_writing_tpg.g>` A PDN 3.0 writing grammar.

------
ANTLR4
------

[ANTLR4]_ is a parser generator supporting many target languages, including Python.

* :download:`pdn_reading_antlr.g4 <../grammars/pdn_reading_antlr.g4>` A fairly liberal reading grammar.
* :download:`pdn_writing_antlr.g4 <../grammars/pdn_writing_antlr.g4>` A PDN 3.0 writing grammar.

- The ANTLR4 grammars use a semantic predicate on the ``DRAW2`` token to prevent
  the result ``1-1`` from being mis-tokenised when it appears as part of a numeric
  move such as ``1-10``.

----------
Test files
----------

The ``games/`` directory contains a collection of PDN games used for testing
the grammars, organised into two subdirectories:

* ``games/succeed/`` — files that every parser must accept without errors.
* ``games/fail/`` — files that every parser must reject.

.. [DParser] DParser, a GLR parser generator written in C https://github.com/jplevyak/dparser
.. [Grammatica] Grammatica, an LL parser generator written in Java https://github.com/cederberg/grammatica
.. [TPG] Toy Parser Generator, a parser written in Python https://codeberg.org/cdsoft/tpg
.. [ANTLR4] ANTLR4, a parser generator supporting multiple target languages https://www.antlr.org/
