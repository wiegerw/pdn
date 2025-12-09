========
PDN Tags
========

This section gives an overview of predefined PDN tags. Tags are key-value pairs
between brackets, in which the value is surrounded by double quotes. More extensive
documentation about most of the tags given here can be found in [PGN]_. The number
of predefined tags has been kept limited. It is allowed to add user defined tags.
Note that a key must start with a capital.

We adopt the rule that a tag is omitted if it has no value. This deviates from [PGN]_,
that defines an explicit *no value* for some tags in the form of a minus sign ``"-"``.
To denote that a tag has an unknown value, in most cases a ``"?"`` value can be used. For
example ``[Event "?"]`` denotes that the event of the game was unknown. Some tags have
a more specific unknown value. Instead of a ``"?"`` value, it is also allowed to
use the empty string ``""``.

This section gives an overview of the predefined tags, followed by some examples
and additional details about the tags.

'Mandatory' tags
----------------

========  =====================================================  ===============
  Tag       Description                                          Unknown value
========  =====================================================  ===============
Event     Name of the tournament or match event, see [Nemesis]_   "?"
Site      Location of the event, see [Nemesis]_                   "?"
Date      Starting date of the game, see [Nemesis]_               "????.??.??"
Round     Playing round ordinal of the game, see [Nemesis]_       "?"
White     Player of the White pieces, see [Nemesis]_              "?"
Black     Player of the Black pieces, see [Nemesis]_              "?"
Result    Result of the game, see [Nemesis]_                      "*"
========  =====================================================  ===============

N.B. The name *mandatory tags* is misleading, since these tags are not mandatory
for an arbitrary PDN file. It is however recommended to include all of the mandatory
tags in tournament games.

Result tag
----------
  The ``Result`` tag is used to specify whether a game ended in a win, draw or a loss.
  Each game type has a specific set of allowed values for the ``Result`` tag.

  ================  ====================================
    ResultType        Allowed result values
  ================  ====================================
    Default           1-0, 0-1, 1/2-1/2, 0-0, *
    International     2-0, 0-2, 1-1, 0-0, *
  ================  ====================================

  In the section :ref:`gametype-section` it is specified which result values belong
  to which game type.

  The value ``*`` denotes that the game was unfinished, or there is no result available.
  The value ``0-0`` denotes that the game was declared lost for both players.

  When reading a PDN document, it is recommended to accept arbitrary strings as results.
  Note that when the ``ResultFormat`` tag is set, the set of allowed values for the ``Result``
  tag is overruled.

  Examples:

  ::

    [Result "1/2-1/2"]

  Sometimes tournaments are being played with different result values. To this end the
  ``ResultFormat`` tag is defined. Below a table is given for some common result formats:

  ================  ================================================================================
    ResultFormat      Allowed result values
  ================  ================================================================================
    Plus draw         2-0, 0-2, 1-1, 0-0, 1+ - 1-, 1- - 1+, *
    Delfts            2-0, 0-2, 1 1/2 - 1/2, 1/2 - 1 1/2, 1-1, 0-0, *
    Goes              2-0, 0-2, ..., -0.98-1.02, -0.99-1.01, 1-1, 1.01-0.99, 1.02-0.98, ..., 0-0, *
  ================  ================================================================================

  When the ``ResultFormat`` tag is set, the ``Result`` tag must have a corresponding allowed value.

  Examples:

  ::

    [ResultFormat "Plus draw"]
    [Result "1+ - 1-"]

Player related tags
-------------------

==========================   ============================================
  Tag                          Description
==========================   ============================================
WhiteTitle, BlackTitle       FMJD titles of the players
WhiteRating, BlackRating     FMJD rating
WhiteFmjdId, BlackFmjdId     FMJD IDs of the players
WhiteNA, BlackNA             E-mail or network addresses of the players
WhiteType, BlackType         Player types ("human" or "program")
==========================   ============================================

The tags ``WhiteRating`` and ``BlackRating`` are named ``WhiteElo`` and ``BlackElo`` in chess.

The FMJD IDs used in ``WhiteFmjdId`` and ``BlackFmjdId`` can be obtained through the
`FMJD public API <https://fmjd.org/webservices/api/public/api_doc/>`_.

Event related tags
------------------

=============  =================================================================
  Tag            Description
=============  =================================================================
EventDate      Starting date of the event
EventSponsor   Sponsor of the event
Section        Playing section of a tournament (e.g., "Open" or "Reserve")
Stage          Stage of a multistage event (e.g., "Preliminary" or "Semifinal")
Board          Board number in a team event or in a simultaneous exhibition
=============  =================================================================

Game related tags
-----------------

===========  ==============================
  Tag         Description
===========  ==============================
GameType      Type of the game, see :ref:`gametype-section`
FEN           The position at the start of the game, see :ref:`fen-section`
PlyCount      The number of ply (moves) in the game
Termination   Describes the reason for conclusion of the game, see [PGN]_
===========  ==============================

The ``GameType`` tag is specific for draughts, and is used to distinguish between
the different draughts variants.

Clock related tags
------------------

=================  ========================================================
  Tag                 Description
=================  ========================================================
TimeControl         Time control settings for both players, see [PGN]_
TimeControlWhite    Time control settings for the white player
TimeControlBlack    Time control settings for the black player
WhiteTime           Time used by the White player at the end of the game
BlackTime           Time used by the Black player at the end of the game
=================  ========================================================

The ``WhiteTime`` and ``BlackTime`` tags are new. It is common practice
to record the time used by both players, so it seems useful to define a
tag for it. The ``TimeControlWhite`` and ``TimeControlBlack`` tags can
be used when the players start with different times on the clock.
This is for example the case in Georgiev-Lehmann tie-breaks.

Time and date tags
------------------

=============  ================================================
  Tag            Description
=============  ================================================
Time           Time-of-day value in "HH:MM:SS" format
UTCTime        Time-of-day in Universal Coordinated Time format
UTCDate        Date in Universal Coordinated Time format
=============  ================================================

Miscellaneous tags
------------------

=============  ==============================
  Tag            Description
=============  ==============================
Annotator      Identifies the annotator or annotators of the game
=============  ==============================

Problemism related tags
-----------------------

===============   =============================
  Tag               Description
===============   =============================
Author            Author(s) of the analysis or composition
Publication       Original publication of the analysis or composition
PublicationDate   Date of the original publication
===============   =============================

These tags are new. PDN can be used to store databases with problems,
so it seems useful to define tags to support this.

--------------------
Details and Examples
--------------------

**Event Tag**
  The Event tag specifies the event. Abbreviations are to be avoided.

  Example:

  ::

  [Event "FMJD World Championship"]

**Site Tag:**
  The Site tag specifies the location. Use IOC country codes to denote
  countries.

  Examples:

  ::

    [Site "New York City, NY USA"]
    [Site "St. Petersburg RUS"]
    [Site "Riga LAT"]

**Date Tag**
  The Date tag must be specified in ``YYYY.MM.DD`` format. Question
  marks may be used for unknown fields.

  A regular expression for Date values is:

  ::

    ([0-9]{4}|[?]{4})\.([0-9]{2}|[?]{2})\.([0-9]{2}|[?]{2})

  Examples:

  ::

    [Date "1996.12.28"]
    [Date "2007.??.??"]

**Round Tag**

  Examples:

  ::

    [Round "1"]
    [Round "3.1"]
    [Round "4.1.2"]

**White/Black Tag**

  The White and Black tag are used to specify the names of the players.
  The family or last name appears first.

  Examples:

  ::

    [White "Wiersma, Harm"]
    [White "van der Wal, Jannes"]
    [White "Dragon v.4.0"]
    [White "Schwarzman, A."]

**WhiteTime/BlackTime Tag**
  The WhiteTime and BlackTime tags specify the amount of time that the players
  have used during the game. Note that these tags do not exist in earlier versions
  of the PDN standard. It is common practice to record these times, hence it seems
  logical to define a tag for it.

  Clock times are specified in ``[H]H:MM[:SS]`` format. Note that in practice also
  ``[H]H.MM[.SS]`` is used.

  *When Fischer time controls are used it makes more sense to record the remaining
  time on the clock. A notation is needed to specify this.*

  Examples:

  ::

    [WhiteTime "1:59:20"]
    [BlackTime "1:17:28"]

**TimeControl Tag**

  The time controls are specified using the TimeControl tag.

  Time control values should match with the following grammar:

  ::

    // Productions
    TimeControl   : UNKNOWN | NOTIME | CompositeTime
    TimeElement   : MOVES_SECONDS | INCREMENTAL | SUDDENDEATH | SANDCLOCK
    CompositeTime : TimeElement (COLON TimeElement)*

    // Tokens
    MOVES_SECONDS : "[0-9]+\/[0-9]+"
    INCREMENTAL   : "[0-9]+\+[0-9]+"
    SUDDENDEATH   : "[0-9]+"
    SANDCLOCK     : "\*[0-9]+"
    UNKNOWN       : "\?"
    NOTIME        : "\-"
    COLON         : "\:"

  Examples:

  ::

  [TimeControl "40/7200:3600"]          { 40 moves in 7200 seconds, 3600 seconds for the rest of the game }
  [TimeControl "4800+60"]               { 80 minutes with increment of 60 seconds/move }
  [TimeControl "40/7200:3600+60"]       { 40 moves in 2 hours, 1 hour for the rest of the game with increment of 60 seconds/move }
  [TimeControl "40/7200:20/2400:600+5"] { 40 moves in 2 hours, 20 moves in 40 minutes, 10 minutes for the rest of the game with increment of 5 seconds/move }
  [TimeControl "*120"]                  { 2 minutes for a "sandclock" or "hourglass" control period, more suitable usage with physical sandclock }

