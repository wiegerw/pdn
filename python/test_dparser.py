#!/usr/bin/env python3

# Grammar actions for the Python dparser package (https://pypi.org/project/dparser/).
# Each d_* function's docstring is one grammar production; dparser collects them from
# this module's globals via dparser.Parser(modules=globals()).
#
# NOTE: dparser requires swig and a C compiler to build. If swig is not available,
# all tests in this file are automatically skipped.

from pathlib import Path

import pytest

dparser = pytest.importorskip('dparser')

GAMES_DIR = Path(__file__).parent.parent / 'games'


# ---------------------------------------------------------------------------
# Tokens
# ---------------------------------------------------------------------------

def d_win1(t):
    r'''WIN1: "1-0"'''


def d_draw1(t):
    r'''DRAW1: "1\/2-1\/2"'''


def d_loss1(t):
    r'''LOSS1: "0-1"'''


def d_win2(t):
    r'''WIN2: "2-0"'''


def d_draw2(t):
    r'''DRAW2: "1-1"'''


def d_loss2(t):
    r'''LOSS2: "0-2"'''


def d_doubleforfeit(t):
    r'''DOUBLEFORFEIT: "0-0"'''


def d_ellipses(t):
    r'''ELLIPSES: "\.\.\."'''


def d_movenumber(t):
    r'''MOVENUMBER: "[0-9]+\.(\.\.)?"'''


def d_moveseparator(t):
    r'''MOVESEPARATOR: "-"'''


def d_captureseparator(t):
    r'''CAPTURESEPARATOR: "[x:]"'''


def d_alphasquare(t):
    r'''ALPHASQUARE: "[a-h][1-8]"'''


def d_alphamove(t):
    r'''ALPHAMOVE: "[a-h][1-8][a-h][1-8]"'''


def d_numsquare(t):
    r'''NUMSQUARE: "([1-9][0-9]?)|(0[1-9])"'''


def d_movestrength(t):
    r'''MOVESTRENGTH: "([\!\?]+)|(\([\!\?]+\))"'''


def d_nag(t):
    r'''NAG: "\$[0-9]+"'''


def d_lparen(t):
    r'''LPAREN: "\("'''


def d_rparen(t):
    r'''RPAREN: "\)"'''


def d_lbracket(t):
    r'''LBRACKET: "\["'''


def d_rbracket(t):
    r'''RBRACKET: "\]"'''


def d_asterisk(t):
    r'''ASTERISK: "\*"'''


def d_setup(t):
    r'''SETUP: "\/[^\/]*\/"'''


def d_string(t):
    r'''STRING: "\"([^\"]|\\\")*\""'''


def d_comment(t):
    r'''COMMENT: "\{[^}]*\}"'''


def d_identifier(t):
    r'''IDENTIFIER: "[A-Z][a-zA-Z0-9_]*"'''


def d_whitespace(t):
    r'''whitespace: "([ \t\n\r]|(%[^\n\r]*))*"'''


# ---------------------------------------------------------------------------
# Productions
# ---------------------------------------------------------------------------

def d_pdn_file(t):
    r'''PdnFile: Game (GameSeparator Game)* GameSeparator?'''


def d_game_separator_asterisk(t):
    r'''GameSeparator: ASTERISK'''


def d_game_separator_result(t):
    r'''GameSeparator: Result'''


def d_game_with_header(t):
    r'''Game: GameHeader GameBody?'''


def d_game_body_only(t):
    r'''Game: GameBody'''


def d_game_header(t):
    r'''GameHeader: PdnTag+'''


def d_game_body(t):
    r'''GameBody: GameBodyItem+'''


def d_game_body_item_move(t):
    r'''GameBodyItem: GameMove'''


def d_game_body_item_variation(t):
    r'''GameBodyItem: Variation'''


def d_game_body_item_comment(t):
    r'''GameBodyItem: COMMENT'''


def d_game_body_item_setup(t):
    r'''GameBodyItem: SETUP'''


def d_game_body_item_nag(t):
    r'''GameBodyItem: NAG'''


def d_pdn_tag(t):
    r'''PdnTag: LBRACKET IDENTIFIER STRING RBRACKET'''


def d_game_move(t):
    r'''GameMove: MOVENUMBER? Move MOVESTRENGTH?'''


def d_variation(t):
    r'''Variation: LPAREN GameBody RPAREN'''


def d_move_normal(t):
    r'''Move: NormalMove'''


def d_move_capture(t):
    r'''Move: CaptureMove'''


def d_move_alpha(t):
    r'''Move: ALPHAMOVE'''


def d_move_ellipses(t):
    r'''Move: ELLIPSES'''


def d_normal_move(t):
    r'''NormalMove: Square MOVESEPARATOR Square'''


def d_capture_move(t):
    r'''CaptureMove: Square (CAPTURESEPARATOR Square)+'''


def d_square_alpha(t):
    r'''Square: ALPHASQUARE'''


def d_square_num(t):
    r'''Square: NUMSQUARE'''


def d_result_result1(t):
    r'''Result: Result1'''


def d_result_result2(t):
    r'''Result: Result2'''


def d_result_doubleforfeit(t):
    r'''Result: DOUBLEFORFEIT'''


def d_result1_win(t):
    r'''Result1: WIN1'''


def d_result1_draw(t):
    r'''Result1: DRAW1'''


def d_result1_loss(t):
    r'''Result1: LOSS1'''


def d_result2_win(t):
    r'''Result2: WIN2'''


def d_result2_draw(t):
    r'''Result2: DRAW2'''


def d_result2_loss(t):
    r'''Result2: LOSS2'''


# ---------------------------------------------------------------------------
# Parser (compiled once at import time)
# ---------------------------------------------------------------------------

PARSER = dparser.Parser(modules=globals())


# dparser's default my_syntax_error_func calls self.this.__getattr__() on the
# SWIG C object, which does not exist in Python 3. Provide a compatible replacement
# that only accesses loc.s (which is handled via dparser_swigc directly).
def _syntax_error_fn(loc):
    raise dparser.SyntaxErr(f'syntax error at byte offset {loc.s}')


def _parse(text):
    return PARSER.parse(text, syntax_error_fn=_syntax_error_fn)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize('path', sorted((GAMES_DIR / 'succeed').glob('*.pdn')), ids=lambda p: p.name)
def test_parse_succeed(path):
    _parse(path.read_text(encoding='utf-8', errors='replace'))


@pytest.mark.parametrize('path', sorted((GAMES_DIR / 'fail').glob('*.pdn')), ids=lambda p: p.name)
def test_parse_fail(path):
    with pytest.raises(Exception):
        _parse(path.read_text(encoding='utf-8', errors='replace'))
