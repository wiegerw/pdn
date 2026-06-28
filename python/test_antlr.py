#!/usr/bin/env python3

# Tests for the ANTLR4 PDN reading grammar.
# The generated parser files (python/pdn_antlr/) are created by the build hook
# when running: pip install -e .
# If the files are absent this module is skipped automatically.

from pathlib import Path

import pytest

try:
    from antlr4 import CommonTokenStream, InputStream
    from antlr4.error.ErrorListener import ErrorListener
    from pdn_antlr.PdnReadingLexer import PdnReadingLexer
    from pdn_antlr.PdnReadingParser import PdnReadingParser
except ImportError as _e:
    pytest.skip(
        f'ANTLR4 parser not available ({_e}); run pip install -e . to generate it',
        allow_module_level=True,
    )

GAMES_DIR = Path(__file__).parent.parent / 'games'


class _RaisingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f'line {line}:{column} {msg}')


def _parse(text: str) -> bool:
    stream = InputStream(text)
    lexer = PdnReadingLexer(stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(_RaisingErrorListener())
    tokens = CommonTokenStream(lexer)
    parser = PdnReadingParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(_RaisingErrorListener())
    parser.pdnFile()
    return True


@pytest.mark.parametrize('path', sorted((GAMES_DIR / 'succeed').glob('*.pdn')), ids=lambda p: p.name)
def test_parse_succeed(path):
    assert _parse(path.read_text(encoding='utf-8', errors='replace'))


@pytest.mark.parametrize('path', sorted((GAMES_DIR / 'fail').glob('*.pdn')), ids=lambda p: p.name)
def test_parse_fail(path):
    with pytest.raises((SyntaxError, Exception)):
        _parse(path.read_text(encoding='utf-8', errors='replace'))
