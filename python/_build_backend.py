"""Build backend extending setuptools to auto-build dparser from ../github-dparser.

When `pip install -e .` is run, this backend clones the dparser repository (if
absent), compiles the C libraries with make, and installs the Cython extension --
all before setuptools processes the pdn package itself.  If the build fails for
any reason (no C compiler, no make, no network), installation of pdn continues
and dparser tests are simply skipped via pytest.importorskip.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from setuptools.build_meta import *  # noqa: F401, F403
from setuptools.build_meta import build_editable as _orig_build_editable
from setuptools.build_meta import build_wheel as _orig_build_wheel

_DPARSER_SRC = Path(__file__).parent.parent / 'github-dparser'
_DPARSER_REPO = 'https://github.com/jplevyak/dparser.git'


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


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    _ensure_dparser()
    return _orig_build_wheel(wheel_directory, config_settings, metadata_directory)


def build_editable(wheel_directory, config_settings=None, metadata_directory=None):
    _ensure_dparser()
    return _orig_build_editable(wheel_directory, config_settings, metadata_directory)
