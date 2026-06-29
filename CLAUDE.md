# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Official specification and reference implementations for the **Portable Draughts Notation (PDN) 3.0** standard. The primary artifact is the Sphinx documentation in `doc/`; the `python/` and `grammars/` directories contain reference parser implementations and formal grammars used to validate the spec.

## Directory layout

| Path | Purpose |
|---|---|
| `doc/` | Sphinx source for the PDN standard (reStructuredText) |
| `grammars/` | Formal grammar files — `.g` (dparser), `.grammar` (Grammatica), `.g4` (ANTLR4) |
| `python/` | Python parsers and their test suites |
| `games/succeed/` | PDN files that every parser must accept |
| `games/fail/` | PDN files that every parser must reject |
| `dparser/` | C++ reference parser using dparser |

## Building the documentation

From `doc/`:
```bash
make html       # builds to doc/build/html/
make latexpdf   # PDF output
```
Requires Sphinx.

## Python parsers

### Install (from `python/`)
```bash
pip install -e ".[dev]"
```
This single command installs TPG and antlr4 runtime, builds the dparser C extension (requires a C compiler and `make`), and regenerates the ANTLR4 parser from the `.g4` grammars (requires `antlr4` and Java). Missing tools produce warnings and the corresponding tests are skipped — not failures.

### Run tests (from `python/`)
```bash
pytest
```

Run a single test file:
```bash
pytest tests/test_tpg.py
pytest tests/test_antlr.py
pytest tests/test_dparser.py
pytest tests/test_grammatica.py   # requires java on PATH
```

Run tests for one PDN file only (e.g. `succeed/game1.pdn`):
```bash
pytest tests/test_tpg.py -k "game1"
```

## Grammar architecture

There are four parallel implementations of the same PDN grammar, each in a different parser technology:

- **TPG** (`python/pdn_reading_tpg.py`, `pdn_writing_tpg.py`): grammars live in `grammars/pdn_reading_tpg.g` and `grammars/pdn_writing_tpg.g`, loaded at import time via `tpg.ParserMetaClass`; always available, the most portable choice.
- **ANTLR4** (`grammars/pdn_reading_antlr.g4`, `grammars/pdn_writing_antlr.g4`): generated into `python/pdn_antlr/` at install time; generated files are git-ignored. Regenerate after editing `.g4` files by re-running `pip install -e .` or calling `antlr4` directly.
- **dparser** (`grammars/pdn_reading_dparser.g`, tested via `python/test_dparser.py`): uses the Cython-based `dparser` package built from `../github-dparser`.
- **Grammatica** (`grammars/pdn_reading_grammatica.grammar`): LL(1), tested by shelling out to `grammatica-1.5.jar`.

All four implementations are tested against the same `games/succeed/` and `games/fail/` PDN files. A change to any grammar must preserve the pass/fail behaviour on those files.

## Key grammar subtleties

- **DRAW2 (`1-1`) vs numeric moves**: `1-1` must not consume the trailing digit of moves like `1-10`. ANTLR4 uses a semantic predicate; TPG uses a negative lookahead regex.
- **MOVESTRENGTH vs LPAREN**: `(!)` is a valid move strength annotation — the `MOVESTRENGTH` token must match `([!?]+)` before `LPAREN` matches `(`.
- **Grammatica grammars are LL(1)**: they define `Move` as a single token (rather than composing squares and separators) to avoid lookahead conflicts.
