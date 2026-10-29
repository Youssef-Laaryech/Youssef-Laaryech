import random
import sys
from xml.sax.saxutils import escape

# usage: python scripts/gen_hero.py assets/hero.svg
# "sokalary" decodes from scrambled glyphs, holds with RGB glitch bursts, roles rotate below.
out_path = sys.argv[1]
random.seed(1337)

ALIAS = "sokalary"
ROLES = [
    "Aspiring Cybersecurity Engineer @ INPT",
    "Red Teaming / Pentesting enthusiast",
    "Blockchain & Web3 security enthusiast",
    "Hack The Box player · break, root, write it up",
]
GLYPHS = "01#$%&@*<>/\\?!{}[]=+"
W, H = 1000, 250
T = 8.0            # decode/glitch cycle
TICK = 0.07        # scramble glyph swap interval
FIRST, STEP = 0.4, 0.14
SIZE, PITCH = 84, 60
CY = 150
NSCR = 3
ROLE_T = 3.0       # seconds per role line


def pct(t):
    return f"{t / T * 100:.3f}%"


css = []
body = []
x0 = W / 2 - PITCH * (len(ALIAS) - 1) / 2

for i, ch in enumerate(ALIAS):
    x = x0 + i * PITCH
    resolve = FIRST + i * STEP
    # final letter: hidden until it resolves, visible for the rest of the cycle
    name = f"f{i}"
    css.append(f"@keyframes {name}{{0%{{opacity:0}}{pct(resolve)}{{opacity:1}}100%{{opacity:1}}}}")
    css.append(f".{name}{{animation:{name} {T}s step-end infinite}}")
    for cls in ("cy", "mg"):
        body.append(f'<text class="big {cls}" x="{x}" y="{CY}">{ch}</text>')
    body.append(f'<text class="big main {name}" x="{x}" y="{CY}">{ch}</text>')
    # scramble glyphs: cycle through NSCR random glyphs every TICK until resolve
    picks = random.sample(GLYPHS, NSCR)
    for k, g in enumerate(picks):
        name = f"s{i}_{k}"
        frames = []
        t, n = 0.0, 0
        while t < resolve:
            frames.append(f"{pct(t)}{{opacity:{1 if n % NSCR == k else 0}}}")
            t += TICK
            n += 1
        frames.append(f"{pct(resolve)}{{opacity:0}}")
        frames.append("100%{opacity:0}")
        css.append(f"@keyframes {name}{{{''.join(frames)}}}")
        css.append(f".{name}{{opacity:0;animation:{name} {T}s step-end infinite}}")
        body.append(f'<text class="big scr {name}" x="{x}" y="{CY}">{escape(g)}</text>')

# glitch bursts: offset cyan/magenta copies jump around at a few moments in the cycle
bursts = [(0.45, 0.16), (0.62, 0.08), (0.86, 0.12)]


def glitch_kf(name, dx):
    fr = ["0%{transform:translate(0,0);opacity:0}"]
    for start, dur in bursts:
        s = start * 100
        e = (start + dur / T) * 100
        fr.append(f"{s:.2f}%{{transform:translate({dx}px,-2px);opacity:.85}}")
        fr.append(f"{(s + e) / 2:.2f}%{{transform:translate({-dx}px,3px);opacity:.85}}")
        fr.append(f"{e:.2f}%{{transform:translate(0,0);opacity:0}}")
    fr.append("100%{transform:translate(0,0);opacity:0}")
    return f"@keyframes {name}{{{''.join(fr)}}}"


css.append(glitch_kf("gc", 5))
css.append(glitch_kf("gm", -5))

# rotating role lines
n = len(ROLES)
RT = ROLE_T * n
for j, role in enumerate(ROLES):
    a = j / n * 100
    fade = 0.25 / RT * 100
    b = (j + 1) / n * 100
    frames = (f"0%{{opacity:0}}{a:.3f}%{{opacity:0}}{a + fade:.3f}%{{opacity:1}}"
              f"{b - fade:.3f}%{{opacity:1}}{b:.3f}%{{opacity:0}}100%{{opacity:0}}")
    css.append(f"@keyframes r{j}{{{frames}}}")
    css.append(f".r{j}{{opacity:0;animation:r{j} {RT}s linear infinite}}")
    body.append(f'<text class="role r{j}" x="{W / 2}" y="{CY + 52}">{escape(role)}</text>')

style = [
    "text{font-family:ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'DejaVu Sans Mono','Liberation Mono',monospace;text-anchor:middle}",
    f".big{{font-size:{SIZE}px;font-weight:800}}",
    ".main{fill:#39ff14;filter:url(#glow)}",
    ".scr{fill:#2ea043}",
    f".cy{{fill:#00e5ff;opacity:0;animation:gc {T}s linear infinite}}",
    f".mg{{fill:#ff2bd6;opacity:0;animation:gm {T}s linear infinite}}",
    ".prompt{font-size:15px;text-anchor:start}",
    ".pu{fill:#d2a8ff;font-weight:bold}.fg{fill:#e6edf3}.bl{fill:#79c0ff}",
    ".role{font-size:20px;fill:#a5d6ff}",
    ".cur{fill:#39ff14;animation:blink 1s step-end infinite}",
    "@keyframes blink{50%{opacity:0}}",
    "@media (prefers-reduced-motion:reduce){*{animation:none!important}.main{opacity:1}.scr,.cy,.mg{opacity:0}.r0{opacity:1}}",
] + css

svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="sokalary, a.k.a. Youssef Laaryech">',
    "<defs><filter id=\"glow\" x=\"-20%\" y=\"-40%\" width=\"140%\" height=\"180%\">"
    "<feGaussianBlur stdDeviation=\"4\" result=\"b\"/><feMerge><feMergeNode in=\"b\"/><feMergeNode in=\"SourceGraphic\"/></feMerge></filter></defs>",
    "<style>" + "\n".join(style) + "</style>",
    f'<rect width="{W}" height="{H}" rx="10" fill="#0d1117"/>',
    f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="10" fill="none" stroke="#30363d"/>',
    '<circle cx="20" cy="16" r="5" fill="#ff5f56"/><circle cx="38" cy="16" r="5" fill="#ffbd2e"/><circle cx="56" cy="16" r="5" fill="#27c93f"/>',
    '<text class="prompt" x="24" y="52" xml:space="preserve"><tspan class="pu">youssef@inpt</tspan><tspan class="fg">:</tspan><tspan class="bl">~</tspan><tspan class="fg">$ whoami --alias</tspan></text>',
] + body + [
    f'<text class="prompt" x="24" y="{H - 18}" xml:space="preserve"><tspan class="fg">a.k.a. </tspan><tspan class="pu">Youssef Laaryech</tspan><tspan class="cur"> █</tspan></text>',
    "</svg>",
]
open(out_path, "w", encoding="utf-8", newline="\n").write("\n".join(svg) + "\n")
print(len(css), "css rules")
