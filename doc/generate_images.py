#!/usr/bin/env python3
"""Regenerate the board-diagram PNGs used in the documentation.

Drives doc/_static/gametype_tester.html in a headless browser so every
diagram shares the same piece/board/notation style, instead of being a
one-off bitmap from a different tool. Run after editing
gametype_tester.html or after changing one of the FEN/tag/color values
below.

Requires: pip install playwright && playwright install chromium
"""
import pathlib
from playwright.sync_api import sync_playwright

DOC_DIR = pathlib.Path(__file__).parent
TOOL_URL = (DOC_DIR / "_static" / "gametype_tester.html").resolve().as_uri()

# The pool-checkers color scheme: used for setup/diagram1/italian.
DEFAULT_COLORS = dict(player="White", opponent="Black", light="Wheat", dark="Peru")

# Green squares, red/white pieces: used for pool checkers and jamaican.
GREEN_COLORS = dict(player="White", opponent="Crimson", light="Ivory", dark="ForestGreen")

IMAGES = [
    # -- gametype.rst: initial position of a named variant --
    dict(
        filename="gametype_italian.png",
        tag="22,W,8,8,N2,1",
        colors=DEFAULT_COLORS,
    ),
    dict(
        filename="gametype_american_pool_checkers.png",
        tag="23,B,8,8,N1,0",
        colors=GREEN_COLORS,
    ),
    dict(
        filename="gametype_unified_pool_checkers.png",
        tag="23,W,8,8,A0,0",
        colors=GREEN_COLORS,
    ),
    dict(
        filename="gametype_jamaican_draughts.png",
        tag="23,B,8,8,A1,1",
        colors=GREEN_COLORS,
    ),
    # -- extensions.rst: a game starting with an illegal move, corrected via Setup --
    dict(
        filename="setup1.png",
        tag="20,W,10,10,N2,0",
        fen='W:W31-50:B1-20',
        colors=DEFAULT_COLORS,
    ),
    dict(
        filename="setup2.png",
        tag="20,W,10,10,N2,0",
        fen='B:W28,31,33-50:B1-18,20',
        colors=DEFAULT_COLORS,
    ),
    dict(
        filename="setup3.png",
        tag="20,W,10,10,N2,0",
        fen='W:W28,31,33-50:B1-13,15-20',
        colors=DEFAULT_COLORS,
    ),
    # -- grammar.rst / pdnnext.rst: the 47x36 move-disambiguation example.
    # White (king) at 47 can fly-capture to 36 via two valid routes:
    #   47x38x24x13x36 capturing {42,29,19,31}, or
    #   47x38x20x9x36 capturing {42,29,14,31}
    # (verified the diagonal geometry of both routes programmatically -
    # see the session notes). Both 14 and 19 must be present so the
    # position is genuinely ambiguous between the two routes.
    dict(
        filename="diagram1.png",
        tag="20,W,10,10,N2,0",
        fen='W:W47:B14,19,29,31,42',
        colors=DEFAULT_COLORS,
    ),
]


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(TOOL_URL)

        for image in IMAGES:
            colors = image["colors"]
            if "fen" in image:
                page.evaluate(
                    "([tag, fen, player, opponent, light, dark]) => "
                    "renderFenPosition('canvas', tag, fen, player, opponent, light, dark)",
                    [image["tag"], image["fen"], colors["player"], colors["opponent"], colors["light"], colors["dark"]],
                )
            else:
                page.evaluate(
                    "([tag, player, opponent, light, dark]) => { "
                    "player_piece_color = player; opponent_piece_color = opponent; "
                    "light_field_color = light; dark_field_color = dark; draw(tag); }",
                    [image["tag"], colors["player"], colors["opponent"], colors["light"], colors["dark"]],
                )
            canvas = page.locator("#canvas")
            out_path = DOC_DIR / image["filename"]
            canvas.screenshot(path=str(out_path))
            print(f"wrote {out_path}")

        browser.close()


if __name__ == "__main__":
    main()
