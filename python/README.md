# PDN Python parsers

This directory contains PDN (Portable Draughts Notation) parsers implemented
in Python, together with their tests.

## Parsers

| Grammar engine | Grammar files |
|---|---|
| [TPG](https://codeberg.org/cdsoft/tpg) | `grammars/pdn_reading_tpg.g`, `grammars/pdn_writing_tpg.g` |
| [ANTLR4](https://www.antlr.org/) | `grammars/pdn_reading_antlr.g4`, `grammars/pdn_writing_antlr.g4` |
| [dparser](https://github.com/jplevyak/dparser) | `grammars/pdn_reading_dparser.g`, `grammars/pdn_writing_dparser.g` |
| [Grammatica](https://grammatica.percederberg.net/) | `grammars/pdn_reading_grammatica.grammar`, `grammars/pdn_writing_grammatica.grammar` |

## Install

Run from within the `python/` directory, selecting the parser engines you want:

```bash
pip install -e ".[tpg]"                                # TPG only
pip install -e ".[tpg,antlr4]"                         # TPG + ANTLR4
pip install -e ".[tpg,dparser,antlr4,grammatica]"      # all parsers
pip install -e ".[tpg,dparser,antlr4,grammatica,dev]"  # all parsers + pytest
```

Each extra corresponds to one parser engine:

| Extra | What it needs |
|---|---|
| `tpg` | nothing extra (Python only) |
| `dparser` | a C compiler and `make` |
| `antlr4` | Java runtime and the `antlr4` command |
| `grammatica` | Java runtime |
| `dev` | nothing extra |

The build backend (`_build_backend.py`) handles installation of all four parsers:

- **TPG** — clones https://codeberg.org/cdsoft/tpg to `../git-tpg` on first use, then installs from the local clone.
- **dparser** — clones https://github.com/jplevyak/dparser to `../git-dparser` on first use, compiles the C libraries, then installs the Cython extension.
- **ANTLR4** — runs `antlr4 -Dlanguage=Python3` on the grammar files and writes the generated Python source into `pdn_antlr/`.
- **Grammatica** — downloads the v1.6 release ZIP into `../git-grammatica` on first use.

If a parser cannot be installed (missing compiler, missing `antlr4`/`java`, no network), a warning is printed and its tests are skipped automatically. Already-cloned repositories are reused on subsequent installs.

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
