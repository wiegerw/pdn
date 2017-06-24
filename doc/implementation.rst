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

* :download:`pdn_reading_tpg.py <../pdn_reading_tpg.py>` A fairly liberal reading grammar.
* :download:`pdn_writing_tpg.py <../pdn_writing_tpg.py>` A PDN 3.0 writing grammar.

----------
Test files
----------
* :download:`games.zip <../games.zip>` A collection of PDN games used for testing the grammars.

.. [DParser] DParser, a GLR parser generator written in C http://dparser.sourceforge.net/
.. [Grammatica] Grammatica, an LL parser generator written in java http://grammatica.percederberg.net/
.. [TPG] Toy Parser Generator, a parser written in python http://cdsoft.fr/tpg/
