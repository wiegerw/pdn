==================
Character encoding
==================

For PDN 3.0 documents the UTF-8 character encoding is required. Note that this includes ASCII encoded documents.
When reading PDN, it is recommended to accept other encodings too, like ISO 8859/1 (Latin 1).

Note that PDN differs from PGN in this respect, see also http://www.saremba.de/chessgml/standards/pgn/pgn-complete.htm#c4.1.
The reason for this choice is that UTF-8 supports many different character sets like Cyrillic, Chinese, Japanese etc.
UTF-8 is also used in the XHTML standard.

There is no maximum line length defined for a PDN document. So it is allowed to put an entire game on one line.
