# PDN Python parsers

This directory contains PDN (Portable Draughts Notation) parsers implemented
in Python, together with their tests.

## Parsers

| Module / package | Grammar engine | Grammar file |
|---|---|---|
| `pdn_reading_tpg.py` | [TPG](https://codeberg.org/cdsoft/tpg) | `grammars/pdn_reading_tpg.g` |
| `pdn_writing_tpg.py` | TPG | `grammars/pdn_writing_tpg.g` |
| `pdn_antlr/` | [ANTLR4](https://www.antlr.org/) | `grammars/pdn_reading_antlr.g4`, `grammars/pdn_writing_antlr.g4` |
| *(via `grammars/pdn_reading_dparser.g`)* | [dparser](https://github.com/jplevyak/dparser) | `grammars/pdn_reading_dparser.g` |
| *(via `grammars/pdn_reading_grammatica.grammar`)* | [Grammatica](https://grammatica.percederberg.net/) | `grammars/pdn_reading_grammatica.grammar` |

## Requirements

- Python 3.8 or later
- pip
- For dparser: a C compiler and `make`
- For ANTLR4 parser generation: Java runtime and the `antlr4` command

## Install

From within the `python/` directory:

```bash
pip install -e ".[dev]"
```

This single command:

1. **Downloads TPG** from Codeberg (git source) and installs it.
2. **Installs `antlr4-python3-runtime`** (required to run the generated ANTLR4
   parser at test time).
3. **Builds dparser** — clones `../github-dparser` if it does not exist, runs
   `make` to build the C libraries, then installs the Cython Python extension.
   If the build fails (no C compiler, no `make`, no network) a warning is
   printed and dparser tests are skipped automatically.
4. **Generates the ANTLR4 parser** — runs `antlr4 -Dlanguage=Python3` on both
   grammar files and writes the generated Python source into `pdn_antlr/`.
   If `antlr4` or Java is not available a warning is printed and ANTLR4 tests
   are skipped automatically.

Downloads are cached: repeating `pip install -e .` reuses the already-cloned
dparser repository and skips `make` targets whose outputs are up to date.
TPG and `antlr4-python3-runtime` are cached by pip in the usual pip cache.

## Run the tests

```bash
pytest
```

| Test file | Parser tested | Skip condition |
|---|---|---|
| `tests/test_tpg.py` | TPG | never skipped |
| `tests/test_antlr.py` | ANTLR4 | `pdn_antlr/` not yet generated |
| `tests/test_dparser.py` | dparser | `dparser` not importable |
| `tests/test_grammatica.py` | Grammatica | `java` not on PATH |

Each test suite is parametrised over the PDN game files in `../games/`:

- `succeed/` — each file must parse without errors.
- `fail/` — each file must be rejected by the parser.

## Regenerate the ANTLR4 parser

The generated files in `pdn_antlr/` are excluded from version control.
To regenerate them (e.g. after editing the `.g4` grammar files) run:

```bash
pip install -e .
```

Or invoke `antlr4` directly:

```bash
antlr4 -Dlanguage=Python3 -o pdn_antlr -visitor ../grammars/pdn_reading_antlr.g4
antlr4 -Dlanguage=Python3 -o pdn_antlr -visitor ../grammars/pdn_writing_antlr.g4
```
