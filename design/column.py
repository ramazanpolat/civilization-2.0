# Emits SVG markup: a classical Ionic column whose upper-right half dissolves into a network.
import random, math, sys
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 8)
G = "#f9bf3b"
out = []
def a(s): out.append(s)

cx, sw = 930, 170                       # column centre, shaft width
x0, x1 = cx - sw/2, cx + sw/2
top, bot = 312, 760
n = 8                                   # flutes
flutes = [x0 + sw*(i+0.5)/n for i in range(n)]
cut = lambda x: 330 + (x - x0) / sw * 330   # solid below this y; digital above (spreads rightwards)

a(f'<g fill="none" stroke="{G}" stroke-linecap="round">')
# stylobate + base
for (l, r, y, h) in [(cx-180, cx+180, 812, 14), (cx-148, cx+148, 798, 14), (cx-114, cx+114, 780, 18)]:
    a(f'<rect x="{l}" y="{y}" width="{r-l}" height="{h}" stroke-width="1.6" stroke-opacity=".8"/>')
a(f'<path d="M{x0-10} 780 Q {x0-10} 762 {x0} 760 L {x1} 760 Q {x1+10} 762 {x1+10} 780" stroke-width="1.6" stroke-opacity=".8"/>')
# shaft edges: left solid, right solid then dotted
a(f'<line x1="{x0}" y1="{bot}" x2="{x0}" y2="{top}" stroke-width="2"/>')
cr = cut(x1)
a(f'<line x1="{x1}" y1="{bot}" x2="{x1}" y2="{cr}" stroke-width="2"/>')
a(f'<line x1="{x1}" y1="{cr}" x2="{x1}" y2="{top}" stroke-width="2" stroke-dasharray="2 9" stroke-opacity=".7"/>')
# flutes
nodes = []
for x in flutes:
    c = cut(x)
    a(f'<line x1="{x:.1f}" y1="{bot-8}" x2="{x:.1f}" y2="{max(c, top+10):.1f}" stroke-width="1.1" stroke-opacity=".55"/>')
    if c > top + 10:
        a(f'<line x1="{x:.1f}" y1="{c:.1f}" x2="{x:.1f}" y2="{top+10}" stroke-width="1.1" stroke-opacity=".35" stroke-dasharray="1 7"/>')
        y = c - 24
        while y > top + 16:
            if random.random() < .45: nodes.append((x, y))
            y -= 26
# capital: abacus, echinus, volutes (right volute digitised)
a(f'<rect x="{cx-118}" y="{top-40}" width="236" height="14" stroke-width="1.8"/>')
a(f'<path d="M{cx-100} {top-26} Q {cx} {top+4} {cx+100} {top-26}" stroke-width="1.6"/>')
a(f'<line x1="{cx-100}" y1="{top-26}" x2="{cx+100}" y2="{top-26}" stroke-width="1.2" stroke-opacity=".6"/>')
def spiral(vx, vy, dash):
    pts = []
    for k in range(0, 260):
        t = k / 260 * 2.6 * 2 * math.pi
        r = 28 * (1 - t / (2.6 * 2 * math.pi)) + 2
        pts.append((vx + r * math.cos(t), vy + r * math.sin(t)))
    d = "M" + " L".join(f"{p[0]:.1f} {p[1]:.1f}" for p in pts)
    extra = ' stroke-dasharray="1 6" stroke-opacity=".75"' if dash else ''
    a(f'<path d="{d}" stroke-width="1.6"{extra}/>')
spiral(cx - 104, top - 4, False)
spiral(cx + 104, top - 4, True)
a('</g>')

# network: nodes rising off the digitised side of the column
cloud = []
tries = 0
while len(cloud) < 30 and tries < 6000:
    tries += 1
    px = random.uniform(cx - 30, 1190)
    py = random.uniform(-40, 430)
    if px < x1 + 24 and py > top - 70: continue          # keep clear of the column body
    # density falls off away from the column's digitised top-right
    w = math.exp(-((px - x1 - 30) / 190) ** 2 - ((py - 230) / 230) ** 2)
    if random.random() > w: continue
    if any((px-qx)**2 + (py-qy)**2 < 34**2 for qx, qy in cloud): continue
    cloud.append((px, py))
pts = nodes + cloud
edges = set()
for i, p in enumerate(pts):
    d = sorted(range(len(pts)), key=lambda j: (pts[j][0]-p[0])**2 + (pts[j][1]-p[1])**2)
    for j in d[1:3 if i < len(nodes) else 4]:
        edges.add(tuple(sorted((i, j))))
a(f'<g stroke="{G}" stroke-width="1" stroke-opacity=".32">')
for i, j in edges:
    (ax, ay), (bx, by) = pts[i], pts[j]
    a(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}"/>')
a('</g>')
a(f'<g fill="{G}">')
big = []
for k, (px, py) in enumerate(pts):
    r = 2.4 if k < len(nodes) else random.choice([2.6, 3.2, 3.8, 5.5])
    if r > 5: big.append((px, py))
    op = .9 if r > 4 else .65
    a(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r}" fill-opacity="{op}"/>')
a('</g>')
# a few halo rings on the larger cloud nodes
a(f'<g fill="none" stroke="{G}" stroke-opacity=".35">')
for (px, py) in [c for c in cloud if c in big][:3]:
    a(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="11"/>')
a('</g>')
sys.stdout.write("\n".join(out))
