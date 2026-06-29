"""Build backend extending setuptools to auto-build optional dependencies.

When `pip install -e .` is run this backend:

1. Clones TPG from ../git-tpg (if absent) and installs it.
   If the clone fails, TPG tests are skipped.

2. Clones and compiles dparser from ../git-dparser (if absent), and installs
   the Cython extension.  If the build fails, dparser tests are skipped.

3. Clones Grammatica from ../git-grammatica (if absent) and builds the JAR
   with ant.  If ant is unavailable or the build fails, Grammatica tests are skipped.

4. Runs antlr4 to generate Python parser code from grammars/pdn_reading_antlr.g4 and
   grammars/pdn_writing_antlr.g4 into python/pdn_antlr/.  If antlr4 (or Java) is not
   available, the ANTLR4 tests are skipped.

All failures are non-fatal: the pdn package itself always installs successfully.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from setuptools.build_meta import *  # noqa: F401, F403
from setuptools.build_meta import build_editable as _orig_build_editable
from setuptools.build_meta import build_wheel as _orig_build_wheel
from setuptools.build_meta import (
    get_requires_for_build_editable as _orig_get_requires_editable,
)
from setuptools.build_meta import (
    get_requires_for_build_wheel as _orig_get_requires_wheel,
)

_TPG_SRC = Path(__file__).parent.parent / 'git-tpg'
_TPG_REPO = 'https://codeberg.org/cdsoft/tpg.git'

_DPARSER_SRC = Path(__file__).parent.parent / 'git-dparser'
_DPARSER_REPO = 'https://github.com/jplevyak/dparser.git'

_GRAMMATICA_SRC = Path(__file__).parent.parent / 'git-grammatica'
_GRAMMATICA_REPO = 'https://github.com/cederberg/grammatica.git'

_ANTLR_GRAMMARS = [
    Path(__file__).parent.parent / 'grammars' / 'pdn_reading_antlr.g4',
    Path(__file__).parent.parent / 'grammars' / 'pdn_writing_antlr.g4',
]
_ANTLR_OUT = Path(__file__).parent / 'pdn_antlr'


def _target_python() -> str:
    """Return the Python of the environment being installed into.

    pip runs build_editable in an isolated build env whose sys.executable
    differs from the user's venv.  VIRTUAL_ENV is not modified by build
    isolation, so we can use it to locate the actual target interpreter.
    """
    venv = os.environ.get('VIRTUAL_ENV')
    if venv:
        for name in ('python', 'python3'):
            candidate = Path(venv) / 'bin' / name
            if candidate.exists():
                return str(candidate)
    return sys.executable


def _ensure_tpg() -> None:
    try:
        if not _TPG_SRC.exists():
            print(f'Cloning tpg from {_TPG_REPO} ...', flush=True)
            subprocess.run(
                ['git', 'clone', '--depth=1', _TPG_REPO, str(_TPG_SRC)],
                check=True,
            )
        env = {k: v for k, v in os.environ.items()
               if k not in ('PYTHONPATH', 'PYTHONNOUSERSITE')
               and not k.startswith('_PYPROJECT_HOOKS_')}
        subprocess.run(
            [_target_python(), '-m', 'pip', 'install', str(_TPG_SRC)],
            check=True,
            env=env,
        )
    except Exception as exc:
        print(
            f'Warning: could not install tpg ({exc}); TPG tests will be skipped.',
            file=sys.stderr, flush=True,
        )


def _ensure_dparser() -> None:
    try:
        if not _DPARSER_SRC.exists():
            print(f'Cloning dparser from {_DPARSER_REPO} ...', flush=True)
            subprocess.run(
                ['git', 'clone', '--depth=1', _DPARSER_REPO, str(_DPARSER_SRC)],
                check=True,
            )
        subprocess.run(
            ['make', '-C', str(_DPARSER_SRC), 'libdparse.a', 'libmkdparse.a'],
            check=True,
        )
        # Strip build-isolation env vars so the inner pip install runs cleanly:
        # - _PYPROJECT_HOOKS_* would confuse pip about which backend to use
        # - PYTHONPATH is set to the isolated build env's site-packages (no pip there)
        # - PYTHONNOUSERSITE is set by build isolation but not needed here
        env = {k: v for k, v in os.environ.items()
               if k not in ('PYTHONPATH', 'PYTHONNOUSERSITE')
               and not k.startswith('_PYPROJECT_HOOKS_')}
        subprocess.run(
            [_target_python(), '-m', 'pip', 'install', '--no-build-isolation',
             '-e', str(_DPARSER_SRC / 'python')],
            check=True,
            env=env,
        )
    except Exception as exc:
        print(
            f'Warning: could not build dparser ({exc}); dparser tests will be skipped.',
            file=sys.stderr, flush=True,
        )


def _ensure_grammatica() -> None:
    import shutil
    try:
        if not _GRAMMATICA_SRC.exists():
            print(f'Cloning grammatica from {_GRAMMATICA_REPO} ...', flush=True)
            subprocess.run(
                ['git', 'clone', '--depth=1', _GRAMMATICA_REPO, str(_GRAMMATICA_SRC)],
                check=True,
            )
        if list(_GRAMMATICA_SRC.rglob('grammatica*.jar')):
            return  # JAR already built
        if not shutil.which('ant'):
            print('Warning: ant not found; grammatica tests will be skipped.',
                  file=sys.stderr, flush=True)
            return
        subprocess.run(
            ['ant', '-buildfile', str(_GRAMMATICA_SRC / 'build.xml')],
            check=True,
        )
    except Exception as exc:
        print(
            f'Warning: could not set up grammatica ({exc}); grammatica tests will be skipped.',
            file=sys.stderr, flush=True,
        )


def _ensure_antlr4() -> None:
    import shutil
    try:
        antlr4_cmd = shutil.which('antlr4')
        if not antlr4_cmd:
            print('Warning: antlr4 command not found; ANTLR4 tests will be skipped.',
                  file=sys.stderr, flush=True)
            return
        _create_antlr_package_stub()
        for grammar in _ANTLR_GRAMMARS:
            subprocess.run(
                [antlr4_cmd, '-Dlanguage=Python3', '-o', str(_ANTLR_OUT),
                 '-visitor', str(grammar)],
                check=True,
            )
    except Exception as exc:
        print(
            f'Warning: could not generate ANTLR4 parsers ({exc}); ANTLR4 tests will be skipped.',
            file=sys.stderr, flush=True,
        )


def _create_antlr_package_stub() -> None:
    """Create pdn_antlr/ with a bare __init__.py so setuptools can discover it.

    setuptools validates that every listed package directory exists during
    get_requires_for_build_*.  The actual parser files are generated later in
    build_wheel / build_editable after antlr4 runs.
    """
    _ANTLR_OUT.mkdir(exist_ok=True)
    init = _ANTLR_OUT / '__init__.py'
    if not init.exists():
        init.touch()


def get_requires_for_build_wheel(config_settings=None):
    _create_antlr_package_stub()
    return _orig_get_requires_wheel(config_settings)


def get_requires_for_build_editable(config_settings=None):
    _create_antlr_package_stub()
    return _orig_get_requires_editable(config_settings)


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    _ensure_tpg()
    _ensure_dparser()
    _ensure_grammatica()
    _ensure_antlr4()
    return _orig_build_wheel(wheel_directory, config_settings, metadata_directory)


def build_editable(wheel_directory, config_settings=None, metadata_directory=None):
    _ensure_tpg()
    _ensure_dparser()
    _ensure_grammatica()
    _ensure_antlr4()
    return _orig_build_editable(wheel_directory, config_settings, metadata_directory)
