#!/usr/bin/env python3

from pathlib import Path

import pytest

from pdn_reading_tpg import pdn_parse

GAMES_DIR = Path(__file__).parent.parent / 'games'


@pytest.mark.parametrize('path', sorted((GAMES_DIR / 'succeed').glob('*.pdn')), ids=lambda p: p.name)
def test_parse_succeed(path):
    if path.name == 'movestrength.pdn':
        pytest.xfail('bracketed move strength e.g. (!?!!!) conflicts with variation syntax in this grammar')
    assert pdn_parse(path.read_text(encoding='utf-8', errors='replace'))


@pytest.mark.parametrize('path', sorted((GAMES_DIR / 'fail').glob('*.pdn')), ids=lambda p: p.name)
def test_parse_fail(path):
    assert not pdn_parse(path.read_text(encoding='utf-8', errors='replace'))
