#!/usr/bin/env python3

import shutil
import subprocess
from pathlib import Path

import pytest

GAMES_DIR = Path(__file__).parent.parent / 'games'
JAR = Path(__file__).parent / 'grammatica-1.5.jar'
GRAMMAR = Path(__file__).parent.parent / 'grammars' / 'pdn_reading.grammar'

pytestmark = pytest.mark.skipif(
    shutil.which('java') is None,
    reason='Java runtime not available',
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
