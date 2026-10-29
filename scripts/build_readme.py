"""Build README.md from src/README.template.md.

- Every ```console block (outside <details>) becomes an SVG terminal window.
- Every local SVG the README shows gets a content-hashed filename, so GitHub's
  image cache picks up changes immediately.

usage: python scripts/build_readme.py   (run from the repo root)
"""
import glob
import hashlib
import os
import re
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "src", "README.template.md")
README = os.path.join(ROOT, "README.md")
ASSETS = os.path.join(ROOT, "assets")
BUILD = os.path.join(ROOT, "assets", "build")

COLS = 132            # shared window width, matches the neofetch card
FS, LH, PADX, PADY = 14, 18, 24, 34
W = PADX * 2 + int(COLS * FS * 0.6)
PROMPT = "youssef@inpt:~$ "
FONT = ("ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,"
        "'DejaVu Sans Mono','Liberation Mono',monospace")


def tspan(text, cls):
    return f'<tspan class="{cls}">{escape(text)}</tspan>'


def render_line(line):
    if line.startswith(PROMPT):
        return (tspan("youssef@inpt", "pu") + tspan(":", "fg") + tspan("~", "bl")
                + tspan("$ ", "fg") + tspan(line[len(PROMPT):], "fg"))
    m = re.search(r"(^|\s)(# .*)$", line)
    if m:
        return tspan(line[:m.start(2)], "out") + tspan(m.group(2), "cm")
    return tspan(line, "out")


def terminal_svg(lines):
    if lines and lines[-1] == "":
        lines = lines[:-1]
    widest = max(len(l) for l in lines)
    assert widest <= COLS, f"line too wide ({widest} > {COLS}): {lines}"
    H = PADY + LH * len(lines) + 16
    label = "terminal: " + "; ".join(l[len(PROMPT):] for l in lines if l.startswith(PROMPT))
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(label)}">',
        f"<style>text{{font-family:{FONT};font-size:{FS}px;white-space:pre}}"
        ".fg{fill:#e6edf3}.pu{fill:#d2a8ff;font-weight:bold}.bl{fill:#79c0ff}"
        ".out{fill:#a5d6ff}.cm{fill:#8b949e;font-style:italic}</style>",
        f'<rect width="{W}" height="{H}" rx="10" fill="#0d1117"/>',
        f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="10" fill="none" stroke="#30363d"/>',
        '<circle cx="20" cy="16" r="5" fill="#ff5f56"/><circle cx="38" cy="16" r="5" fill="#ffbd2e"/><circle cx="56" cy="16" r="5" fill="#27c93f"/>',
    ]
    for i, l in enumerate(lines):
        out.append(f'<text x="{PADX}" y="{PADY + 14 + i * LH}" xml:space="preserve">{render_line(l)}</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n", label


def publish(name, svg_text):
    digest = hashlib.sha1(svg_text.encode("utf-8")).hexdigest()[:8]
    fname = f"{name}-{digest}.svg"
    with open(os.path.join(BUILD, fname), "w", encoding="utf-8", newline="\n") as f:
        f.write(svg_text)
    return f"assets/build/{fname}"


def img(src, alt):
    return f'<p align="center">\n  <img src="{src}" width="100%" alt="{escape(alt, {chr(34): "&quot;"})}" />\n</p>'


def main():
    os.makedirs(BUILD, exist_ok=True)
    for old in glob.glob(os.path.join(BUILD, "*.svg")):
        os.remove(old)
    src = open(TEMPLATE, encoding="utf-8").read()

    # hand-made SVGs referenced as assets/<name>.svg get hashed copies
    def hashed(m):
        path = os.path.join(ASSETS, m.group(1) + ".svg")
        return f'src="{publish(m.group(1), open(path, encoding="utf-8").read())}"'
    src = re.sub(r'src="assets/([\w-]+)\.svg"', hashed, src)

    # console blocks -> terminal windows, except inside <details>
    parts = re.split(r"(<details>.*?</details>)", src, flags=re.S)
    n = 0
    for i, part in enumerate(parts):
        if part.startswith("<details>"):
            continue

        def block(m):
            nonlocal n
            n += 1
            svg_text, label = terminal_svg(m.group(1).split("\n"))
            return img(publish(f"term-{n:02d}", svg_text), label)
        parts[i] = re.sub(r"```console\n(.*?)```", block, part, flags=re.S)

    with open(README, "w", encoding="utf-8", newline="\n") as f:
        f.write("".join(parts))
    print(f"{n} terminal windows, width {W}px")


if __name__ == "__main__":
    main()
