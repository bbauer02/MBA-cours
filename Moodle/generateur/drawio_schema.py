# Builds flow diagrams for the worksheets with draw.io: the @schema lines of a worksheet become a
# .drawio file (laid out here), exported to SVG by the draw.io desktop CLI, then inlined in the HTML.
#
# Syntax of the @schema lines (one line = one row of boxes separated by "->"):
#   A -> B -> C                 a row (at most 5 boxes)
#   ... -> D -> E               continues the previous row (elbow connector from C to D)
#   Libellé :: A -> B           a row with a label tag on its left (lanes) or on its first arrow (fan)
#   [[texte]]                   a box to complete: empty and dashed for the student, filled for the teacher
# When every row starts with the same box, or ends with the same box, the shared box is drawn once
# and the rows fan out from it / converge on it.
#
# The .drawio and .svg files are cached in fiches_travail_s2/schemas/ (re-exported only when changed);
# the .drawio files can be opened and edited in draw.io.
import hashlib, html as H, os, re, subprocess
from frtypo import fr

DRAWIO = r'C:\Program Files\draw.io\draw.io.exe'
GAP = re.compile(r'\[\[(.+?)\]\]')
W = 690            # usable width (px)
G = 34             # horizontal gap between boxes (arrow)
VG = 22            # vertical gap between independent rows
VGC = 40           # vertical gap before a continuation row
LBL = 78           # label column width (lanes)

BOX = ('rounded=1;whiteSpace=wrap;html=1;arcSize=12;fillColor=#EEF3F2;strokeColor=#1F6F78;strokeWidth=1.5;'
       'fontColor=#12343B;fontStyle=1;fontSize=11.5;fontFamily=Source Sans 3;spacing=5;shadow=1;')
SHARED = BOX.replace('#EEF3F2', '#DCEBEA').replace('strokeWidth=1.5', 'strokeWidth=2')
EMPTY = ('rounded=1;whiteSpace=wrap;html=1;arcSize=12;fillColor=#FFFFFF;strokeColor=#E09F3E;strokeWidth=1.8;'
         'dashed=1;dashPattern=6 4;fontColor=#C8D6D4;fontSize=10;fontStyle=2;fontFamily=Source Sans 3;')
FILLED = ('rounded=1;whiteSpace=wrap;html=1;arcSize=12;fillColor=#FBEFDC;strokeColor=#E09F3E;strokeWidth=1.8;'
          'fontColor=#9E2A2B;fontStyle=1;fontSize=11.5;fontFamily=Source Sans 3;spacing=5;')
TAG = ('rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#12343B;strokeColor=none;fontColor=#FFFFFF;'
       'fontStyle=1;fontSize=10.5;fontFamily=Source Sans 3;spacing=3;')
CAPTION = ('text;html=1;align=left;verticalAlign=bottom;spacing=0;fontSize=10.5;fontStyle=1;fontColor=#1F6F78;'
           'fontFamily=Source Sans 3;')
EDGE = ('edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=blockThin;endFill=1;endSize=7;'
        'strokeColor=#1F6F78;strokeWidth=1.6;fontSize=10;fontStyle=1;fontColor=#12343B;'
        'fontFamily=Source Sans 3;labelBackgroundColor=#FFFFFF;')


def parse_rows(lines):
    rows = []
    for l in lines:
        if '->' not in l and not l.strip():
            continue
        label, cont = '', False
        if '::' in l.split('->')[0]:
            label, _, l = l.partition('::')
            label = label.strip()
        boxes = [b.strip() for b in l.split('->') if b.strip()]
        if boxes and boxes[0] == '...':
            boxes, cont = boxes[1:], True
        rows.append({'label': label, 'boxes': boxes, 'cont': cont and bool(rows)})
    return rows


def text_lines(t, w):
    per = max(6, int((w - 12) / 6.3))
    n, cur = 1, 0
    for word in t.split():
        if cur and cur + 1 + len(word) > per:
            n, cur = n + 1, len(word)
        else:
            cur += (1 if cur else 0) + len(word)
    return n


def layout(rows):
    """Returns (cells, edges) with geometry; cells: dict(id, text, x, y, w, h, kind)."""
    fan_start = len(rows) > 1 and not any(r['cont'] for r in rows) and len({r['boxes'][0] for r in rows}) == 1
    fan_end = len(rows) > 1 and not any(r['cont'] for r in rows) and len({r['boxes'][-1] for r in rows}) == 1
    lanes = any(r['label'] for r in rows) and not (fan_start or fan_end)
    mids = [r['boxes'][1 if fan_start else 0: len(r['boxes']) - (1 if fan_end else 0)] for r in rows]
    ncols = max(len(m) for m in mids) + fan_start + fan_end
    avail = W - (LBL if lanes else 0)
    bw = min(170, (avail - (ncols - 1) * G) / ncols)
    cells, edges = [], []

    def h_of(texts):
        return max([46] + [18 + 15 * text_lines(GAP.sub(r'\1', t), bw) for t in texts])

    x0 = (LBL if lanes else 0) + (bw + G if fan_start else 0)
    y = 0
    prev_last = None
    first_ids, last_ids, row_boxes = [], [], []
    captions = (fan_start or fan_end) and any(r['label'] for r in rows)
    for i, (r, m) in enumerate(zip(rows, mids)):
        h = h_of(m)
        if i:
            y += VGC if r['cont'] else VG
        if captions:
            if r['label']:
                cells.append(dict(id=f'r{i}c', text=r['label'], x=x0, y=y, w=bw, h=15, caption=True))
            y += 17
        ids = []
        for j, t in enumerate(m):
            cid = f'r{i}b{j}'
            cells.append(dict(id=cid, text=t, x=x0 + j * (bw + G), y=y, w=bw, h=h))
            if j:
                edges.append(dict(src=ids[-1], dst=cid))
            ids.append(cid)
        if r['cont'] and prev_last:
            edges.append(dict(src=prev_last, dst=ids[0], elbow=True))
        if lanes and r['label']:
            cells.append(dict(id=f'r{i}t', text=r['label'], x=0, y=y + h / 2 - 15, w=LBL - 14, h=30, tag=True))
        row_boxes.append((y, h))
        first_ids.append(ids[0]); last_ids.append(ids[-1]); prev_last = ids[-1]
        y += h
    top, bot = row_boxes[0][0] - (17 if captions else 0), row_boxes[-1][0] + row_boxes[-1][1]
    if fan_start:
        t = rows[0]['boxes'][0]
        h = h_of([t])
        cells.append(dict(id='s', text=t, x=0, y=(top + bot) / 2 - h / 2, w=bw, h=h, shared=True))
        for i, f in enumerate(first_ids):
            edges.append(dict(src='s', dst=f))
    if fan_end:
        t = rows[0]['boxes'][-1]
        h = h_of([t])
        xe = x0 + max(len(m) for m in mids) * (bw + G)
        cells.append(dict(id='e', text=t, x=xe, y=(top + bot) / 2 - h / 2, w=bw, h=h, shared=True))
        for i, l in enumerate(last_ids):
            edges.append(dict(src=l, dst='e'))
    # centre a single-width diagram
    right = max(c['x'] + c['w'] for c in cells)
    if not lanes and right < W:
        dx = (W - right) / 2
        for c in cells:
            c['x'] += dx
    return cells, edges


def to_xml(cells, edges, teacher):
    out = ['<mxfile host="build_fiches_travail"><diagram name="schema"><mxGraphModel dx="800" dy="400" grid="0" '
           'page="0" math="0" shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>']
    for c in cells:
        t = c['text']
        m = GAP.fullmatch(t)
        if c.get('tag'):
            style, val = TAG, t
        elif c.get('caption'):
            style, val = CAPTION, t
        elif m:
            style, val = (FILLED, m.group(1)) if teacher else (EMPTY, '')
        else:
            style, val = (SHARED if c.get('shared') else BOX), t
        out.append(f'<mxCell id="{c["id"]}" value="{H.escape(fr(val), quote=True)}" style="{style}" vertex="1" parent="1">'
                   f'<mxGeometry x="{c["x"]:.1f}" y="{c["y"]:.1f}" width="{c["w"]:.1f}" height="{c["h"]:.1f}" as="geometry"/></mxCell>')
    for k, e in enumerate(edges):
        style = EDGE
        if e.get('elbow'):
            style += 'exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;'
        else:
            style += 'exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;'
        lab = H.escape(fr(e.get('label', '')), quote=True)
        out.append(f'<mxCell id="e{k}" value="{lab}" style="{style}" edge="1" parent="1" source="{e["src"]}" target="{e["dst"]}">'
                   '<mxGeometry relative="1" as="geometry"/></mxCell>')
    out.append('</root></mxGraphModel></diagram></mxfile>')
    return ''.join(out)


def render(lines, teacher, cache_dir, name):
    """Returns the inline SVG of the schema; writes <name>.drawio / .svg in cache_dir."""
    rows = parse_rows(lines)
    for r in rows:
        if len(r['boxes']) > 5:
            raise SystemExit(f'{name} : une ligne de schéma dépasse 5 boîtes')
    cells, edges = layout(rows)
    xml = to_xml(cells, edges, teacher)
    os.makedirs(cache_dir, exist_ok=True)
    base = os.path.join(cache_dir, name + ('_enseignant' if teacher else '_eleve'))
    digest = hashlib.md5(xml.encode('utf8')).hexdigest()
    svg_path = base + '.svg'
    if not (os.path.exists(svg_path) and open(svg_path, encoding='utf8').read().find(digest) > 0):
        open(base + '.drawio', 'w', encoding='utf8').write(xml)
        subprocess.run([DRAWIO, '-x', '-f', 'svg', '--svg-theme', 'light', '-b', '6', '-o', svg_path, base + '.drawio'],
                       check=True, capture_output=True)
        svg = open(svg_path, encoding='utf8').read()
        open(svg_path, 'w', encoding='utf8').write(svg + f'\n<!-- {digest} -->\n')
    svg = open(svg_path, encoding='utf8').read()
    svg = svg[svg.index('<svg'):svg.rindex('</svg>') + 6]
    m = re.search(r'viewBox="([\d.\s-]+)"', svg)
    vw = float(m.group(1).split()[2]) if m else W
    svg = re.sub(r'^<svg([^>]*?) width="[^"]*" height="[^"]*"', r'<svg\1', svg, count=1)
    return f'<div class="schema-drawio" style="max-width:{vw:.0f}px">{svg}</div>'
