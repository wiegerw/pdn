#!/usr/bin/env python3

import shutil
import subprocess
from pathlib import Path

import pytest

GAMES_DIR = Path(__file__).parent.parent.parent / 'games'
GRAMMAR = Path(__file__).parent.parent.parent / 'grammars' / 'pdn_reading_grammatica.grammar'
_GRAMMATICA_SRC = Path(__file__).parent.parent.parent / 'git-grammatica'


def _find_jar():
    if _GRAMMATICA_SRC.exists():
        jars = sorted(_GRAMMATICA_SRC.rglob('grammatica*.jar'))
        if jars:
            return jars[0]
    return None


JAR = _find_jar()

pytestmark = pytest.mark.skipif(
    shutil.which('java') is None or JAR is None,
    reason='Java or grammatica JAR not available; run pip install -e ".[grammatica]"',
)


def _grammatica(path):
    return subprocess.run(
        ['java', '-jar', str(JAR), str(GRAMMAR), '--parse', str(path)],
        capture_output=True,
    ).returncode


@pytest.mark.parametrize('path', sorted((GAMES_DIR / 'succeed').glob('*.pdn')), ids=lambda p: p.name)
def test_parse_succeed(path):
    assert _grammatica(path) == 0


@pytest.mark.parametrize('path', sorted((GAMES_DIR / 'fail').glob('*.pdn')), ids=lambda p: p.name)
def test_parse_fail(path):
    assert _grammatica(path) != 0
