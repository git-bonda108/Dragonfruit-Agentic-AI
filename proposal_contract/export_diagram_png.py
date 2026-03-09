#!/usr/bin/env python3
"""
Export architecture_diagram.svg to architecture_diagram.png.
Requires: pip install cairosvg
"""
from pathlib import Path

try:
    import cairosvg
except ImportError:
    print("Install cairosvg: pip install cairosvg")
    raise SystemExit(1)

BASE = Path(__file__).resolve().parent
SVG = BASE / "architecture_diagram.svg"
PNG = BASE / "architecture_diagram.png"

if not SVG.exists():
    print(f"Not found: {SVG}")
    raise SystemExit(1)

# Export at 1x (900x620) and optional 2x for retina
cairosvg.svg2png(url=str(SVG), write_to=str(PNG), output_width=900, output_height=620)
print(f"Wrote {PNG} (900×620)")

PNG_2X = BASE / "architecture_diagram_2x.png"
cairosvg.svg2png(url=str(SVG), write_to=str(PNG_2X), output_width=1800, output_height=1240)
print(f"Wrote {PNG_2X} (1800×1240, retina)")
