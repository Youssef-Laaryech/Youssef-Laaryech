import sys
from xml.sax.saxutils import escape

# usage: python scripts/gen_neofetch.py src/art.txt src/figlet.txt assets/neofetch.svg
art_path, fig_path, out_path = sys.argv[1:4]
art = [l.rstrip("\n") for l in open(art_path, encoding="utf-8")]
aw = max(len(l) for l in art)
art = [l.ljust(aw) for l in art]
fig = [l.rstrip("\n") for l in open(fig_path, encoding="utf-8")]
name = [l[:31].rstrip() for l in fig[:4]] + [l[31:].rstrip() for l in fig]

info = [
    ("Alias", "sokalary"),
    ("Role", "Aspiring Cybersecurity Engineer"),
    ("Host", "INPT, Morocco"),
    ("Focus", "Red Teaming / Pentesting"),
    ("Passion", "Blockchain & Web3 security"),
    ("OS", "Kali Linux · Windows AD"),
    ("Uptime", "since 2025-07"),
    ("Pwned", "6 HTB boxes, all written up"),
    ("Packages", "8 projects · 13 tools built"),
    ("Langs", "Python, TypeScript, Bash"),
    ("Arsenal", "burp, bloodhound, impacket"),
    ("Web3", "hedera-sdk, x402, ctfd"),
]
WAVE = ["#39ff14", "#00e5ff", "#58a6ff"]
PALETTE = ["#39ff14", "#2ea043", "#00e5ff", "#58a6ff"]

# right column: list of (kind, payload) per row
right = [("name", l) for l in name] + [("blank", "")]
right += [("title", ""), ("rule", "------------")]
right += [("info", kv) for kv in info] + [("blank", ""), ("blocks", "")]
pad = len(art) - len(right)
right = [("blank", "")] * (pad // 2) + right + [("blank", "")] * (pad - pad // 2)

FS, LH, PADX, PADY = 14, 18, 24, 34
ROW_DELAY = 0.12
lines = []


def t(text, cls=None, style=None):
    attrs = (f' class="{cls}"' if cls else "") + (f' style="{style}"' if style else "")
    return f"<tspan{attrs}>{escape(text)}</tspan>"


lines.append(t("youssef@inpt", "pu") + t(":", "fg") + t("~", "bl") + t("$ ", "fg") + t("neofetch", "fg"))
for i, (a, (kind, payload)) in enumerate(zip(art, right)):
    delay = f"animation-delay:-{i * ROW_DELAY:.2f}s"
    row = t(a, "wave", delay) + "   "
    if kind == "name":
        row += t(payload, "wave", delay)
    elif kind == "title":
        row += t("youssef", "pu") + t("@", "fg") + t("inpt", "pu")
    elif kind == "rule":
        row += t(payload, "fg")
    elif kind == "info":
        k, v = payload
        row += t(k.ljust(11), "key") + t(v, "val")
    elif kind == "blocks":
        row += " ".join(f'<tspan fill="{c}">███</tspan>' for c in PALETTE)
    lines.append(row)
lines.append("")
lines.append(t("youssef@inpt", "pu") + t(":", "fg") + t("~", "bl") + t("$ ", "fg") + t("cat /etc/motd", "fg"))
lines.append(t("Building labs, not just collecting certs.", "val"))
lines.append(t("I build stuff, break stuff, write down what broke, and see where it goes.", "val"))

cols = 132  # shared window width, see build_readme.py
W = PADX * 2 + int(cols * FS * 0.6)
H = PADY + LH * len(lines) + 20
kf = " ".join(f"{int(i * 100 / len(WAVE))}%{{fill:{c}}}" for i, c in enumerate(WAVE)) + f" 100%{{fill:{WAVE[0]}}}"

svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="neofetch: ASCII portrait of Youssef Laaryech with profile info">',
    "<style>",
    "text{font-family:ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'DejaVu Sans Mono','Liberation Mono',monospace;"
    f"font-size:{FS}px;white-space:pre}}",
    ".fg{fill:#e6edf3}.pu{fill:#d2a8ff;font-weight:bold}.bl{fill:#79c0ff}.key{fill:#79c0ff;font-weight:bold}.val{fill:#a5d6ff}",
    f".wave{{fill:{WAVE[0]};animation:hue 6s linear infinite}}",
    f"@keyframes hue{{{kf}}}",
    "@media (prefers-reduced-motion:reduce){.wave{animation:none}}",
    "</style>",
    f'<rect width="{W}" height="{H}" rx="10" fill="#0d1117"/>',
    f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="10" fill="none" stroke="#30363d"/>',
    '<circle cx="20" cy="16" r="5" fill="#ff5f56"/><circle cx="38" cy="16" r="5" fill="#ffbd2e"/><circle cx="56" cy="16" r="5" fill="#27c93f"/>',
]
for i, l in enumerate(lines):
    svg.append(f'<text x="{PADX}" y="{PADY + 14 + i * LH}" xml:space="preserve">{l}</text>')
svg.append("</svg>")
open(out_path, "w", encoding="utf-8", newline="\n").write("\n".join(svg) + "\n")
print(W, H)
