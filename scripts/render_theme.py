#!/usr/bin/env python3

from pathlib import Path

from jinja2 import Environment, FileSystemLoader


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / "themes" / "Blowtorch-color-theme.json.j2"
OUTPUT_PATH = ROOT / "themes" / "Blowtorch-color-theme.json"


def main() -> int:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_PATH.parent)),
        autoescape=False,
        keep_trailing_newline=True,
    )
    template = env.get_template(TEMPLATE_PATH.name)
    rendered = template.render().lstrip("\n")
    OUTPUT_PATH.write_text(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
