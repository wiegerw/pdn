============
Introduction
============

This document defines the official portable draughts notation standard, PDN 3.0.
The goal of this document is to give a formal definition of PDN.
Nowadays there are many conflicts between draughts programs regarding their
interpretation of valid PDN. This document aims to take away the sources of
conflicts, by defining grammars, and by giving additional restrictions. Note
that the PDN definition as given in this document slightly deviates from earlier
versions. This has been done to make parsing PDN easier. Furthermore, some
extensions are defined to support setting up positions and to add clock times.

In [Wikipedia]_, [Sage]_, [Nemesis]_ and [Grimminck]_ earlier versions
of PDN definitions can be found. PDN was derived from the PGN standard
in chess, see [PGN]_. The PDN proposal in this document takes the PDN 2.0 draft
[Nemesis]_ as a starting point, since it is more complete and precise than the
earlier ones. Several additions, restrictions and extensions to the PDN 2.0 draft
are made.

This document first discusses PDN tags, then a grammar for PDN 3.0 is given, followed
by some PDN extensions, and some example implementations of the grammar. The
design of the grammar was influenced by a number of issues of the existing
PDN standards. These issues are discussed in the :ref:`issues-section` section.

For convenience a Java Webstart `PDN 3.0 Checker <http://10x10.org/pdn/test/index.html>`_
is available, that can be used for checking the validity of a PDN file.

-----------
PDN Example
-----------

A PDN file consists of a section of tags (key-value pairs between brackets)
followed by a section with moves and variations. A typical example is:

::

  [Event "FMJD World Championship"]
  [Site "Hardenberg, NED"]
  [Date "2007.05.19"]
  [Round "7"]
  [White "Mikhalchenko,I."]
  [Black "Ndjofang,J."]
  [Result "0-2"]
  [GameType "20"]
  [WhiteTime "1:36"]
  [BlackTime "1:17"]
  
   1.32-28 17-22  2.28x17 11x22  3.37-32  6-11  4.41-37 12-17  5.46-41  8-12
   6.34-30  2-8   7.30-25 19-23  8.35-30  1-6   9.40-35 13-19 10.31-27 22x31
  11.36x27  9-13 12.33-28  4-9  13.41-36 17-22 14.28x17 11x31 15.37x26 23-28
  16.32x23 19x28 17.42-37 20-24 18.30x19 14x23 19.37-31 16-21 20.26x17 12x21
  21.31-27 21x32 22.38x27  6-11 23.47-42 15-20 24.25x14 10x19 25.39-33 28x39
  26.44x33  8-12 27.42-38 23-28 28.33x22 12-17 29.49-44 17x28 30.38-33 28x39
  31.44x33 18-22 32.27x18 13x22 33.43-38 19-23 34.38-32 11-17 35.32-27 22x31
  36.36x27  9-13 37.45-40 13-18 *

-------------------
Reading and writing
-------------------

Programmers are encouraged to follow the PDN 3.0 standard closely when writing
PDN. When reading, it is recommended to treat the input much more liberally.
To this end an example of a liberal reading grammar is given. Also the character
encoding requirement can be relaxed.

----------------
Acknowledgements
----------------

Thanks to everyone who took part in the discussions on the World Draughts Forum [Forum]_,
and to Rein Halbersma for leading the review.

----------
References
----------

.. [Wikipedia] Wikipedia: Portable Draughts Notation http://en.wikipedia.org/wiki/Portable_Draughts_Notation

.. [Nemesis] PDN 2.0 Specification by Murray Cash (draft) :download:`pdn2.txt <pdn2.txt>` An archived copy of http://www.nemesis.info/pdn2.txt, 17 July 2012.

.. [PGN] Portable Game Notation Specification and Implementation Guide http://www.saremba.de/chessgml/standards/pgn/pgn-complete.htm

.. [Sage] Adrian Millet's PDN description: http://homepages.tcp.co.uk/~pcsol/sagehlp1.htm#PDN

.. [Grimminck] Michel Grimminck's PDN page http://www.xs4all.nl/~mdgsoft/draughts/pdn.html

.. [DGT] DGT Clock times extension http://digitalgametechnology.com/site/index.php/Board-Driver/pgn-clock-times-extension.html

.. [Forum] PDN standard topic on World Draughts Forum http://laatste.info/bb/viewtopic.php?t=2544

