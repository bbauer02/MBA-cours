# Builds the S2 day decks (PowerPoint), the teleprompter page (HTML) and the speaker script (Word)
# from one JSON spec per day (diapos_s2/spec/J1.json ... J5.json).
# The look is the S1 look: the S1 deck is reused as template (theme, masters, layouts).
# Usage: python build_diapos.py <out_dir> [J1 J2 ... semaine]
import copy, io, json, os, re, subprocess, sys
from PIL import ImageFont
from pptx import Presentation
from pptx.util import Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(GEN))
S1 = os.path.join(ROOT, 'Semaine1', 'Jour1_Lancement_et_cadrage')
TEMPLATE = os.path.join(S1, 'J1_Diaporama.pptx')
PROMPT_TEMPLATE = os.path.join(S1, 'J1_Prompteur.html')
DOCX_TEMPLATE = os.path.join(S1, 'J1_Script_prompteur.docx')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
FOOTER = "Systèmes d'information, cartographie et risques · UE2 · Semaine S2"
sys.path.insert(0, GEN)

C = {'pet': '12343B', 'teal': '1F6F78', 'amb': 'E09F3E', 'brick': '9E2A2B', 'green': '4F7F4E', 'ink': '1B2A33',
     'slate': '5E6B78', 'mist': 'EEF3F2', 'pale': 'C8D6D4', 'white': 'FFFFFF', 'warnbg': 'F8E1E1', 'ambbg': 'FBEFDC',
     'tealbg': 'DCEBEA', 'greenbg': 'E3EDE2', 'cream': 'FBF6E9', 'risk1': 'DCEBEA', 'risk2': 'FBEFDC', 'risk3': 'F4C9A8', 'risk4': 'E8A0A0'}
BODY = 'Calibri'; HEAD = 'Cambria'
X0, XW, Y0, YH = 43, 873, 126, 356          # content area (points), as in S1
FONT = {False: os.path.join(os.environ.get('WINDIR', r'C:\Windows'), 'Fonts', 'calibri.ttf'),
        True: os.path.join(os.environ.get('WINDIR', r'C:\Windows'), 'Fonts', 'calibrib.ttf')}
_fc = {}
WARN = []
CUR = {'n': 0}


HFONT = {False: os.path.join(os.environ.get('WINDIR', r'C:\Windows'), 'Fonts', 'cambria.ttc'),
         True: os.path.join(os.environ.get('WINDIR', r'C:\Windows'), 'Fonts', 'cambriab.ttf')}


def font(sz, bold=False, head=False):
    k = (round(sz * 4), bold, head)
    if k not in _fc:
        _fc[k] = ImageFont.truetype((HFONT if head else FONT)[bold], max(1, round(sz * 4)))  # measure at 4x for precision
    return _fc[k]


def tw(text, sz, bold=False, head=False):
    return font(sz, bold, head).getlength(text) / 4


def wrap_lines(text, sz, width, bold=False, head=False):
    n = 0
    for para in text.split('\n'):
        words, cur = para.split(), ''
        if not words:
            n += 1; continue
        for w in words:
            t = (cur + ' ' + w).strip()
            if tw(t, sz, bold, head) <= width or not cur:
                cur = t
            else:
                n += 1; cur = w
        n += 1
    return n


def text_height(paras, sz, width, lh=1.18, gap=0.45):
    """paras: list of (text, bold, rel_size[, head])"""
    h = 0
    for i, p in enumerate(paras):
        t, b, r = p[:3]; hd = len(p) > 3 and p[3]
        s = sz * r
        h += wrap_lines(t, s, width, b, hd) * s * (lh * 1.06 if hd else lh) + (s * gap if i < len(paras) - 1 else 0)
    return h


def fit(paras, width, height, maxs, mins=9):
    s = maxs
    while s > mins and text_height(paras, s, width) > height:
        s -= 0.5
    return s


def rgb(k):
    return RGBColor.from_string(C.get(k, k))


def strip_style(shape):
    st = shape._element.find(qn('p:style'))
    if st is not None:
        shape._element.remove(st)


def box(slide, x, y, w, h, fill='mist', radius=0.04, line=None, name='Carte', shape=MSO_SHAPE.ROUNDED_RECTANGLE):
    sp = slide.shapes.add_shape(shape, Pt(x), Pt(y), Pt(w), Pt(h))
    strip_style(sp)
    sp.name = name
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        sp.adjustments[0] = radius
    if fill:
        sp.fill.solid(); sp.fill.fore_color.rgb = rgb(fill)
    else:
        sp.fill.background()
    if line:
        sp.line.color.rgb = rgb(line); sp.line.width = Pt(1.25)
    else:
        sp.line.fill.background()
    sp.text_frame.text = ''
    return sp


def text(slide, x, y, w, h, paras, size=16, color='ink', anchor='top', align='left', font_name=BODY, maxs=None, mins=9,
         lh=1.0, name='Texte', italic=False, autofit=True):
    """paras: str | list of str | list of dict(t, b, c, r, i, f)"""
    if isinstance(paras, str):
        paras = [paras]
    P = [p if isinstance(p, dict) else {'t': p} for p in paras]
    if autofit:
        M = [(p['t'], p.get('b', False), p.get('r', 1), p.get('f', font_name) == HEAD) for p in P]
        size = fit(M, w - 1, h, maxs or size, mins)
        if size < 11 and (maxs or 16) >= 11:
            WARN.append(f"diapo {CUR['n']} : texte réduit à {size} pt ({P[0]['t'][:50]}…)")
        if text_height(M, size, w - 1) > h + 1:
            WARN.append(f"diapo {CUR['n']} : TEXTE QUI DÉBORDE ({P[0]['t'][:50]}…)")
    tb = slide.shapes.add_textbox(Pt(x), Pt(y), Pt(w), Pt(h))
    tb.name = name
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = {'top': MSO_ANCHOR.TOP, 'middle': MSO_ANCHOR.MIDDLE, 'bottom': MSO_ANCHOR.BOTTOM}[anchor]
    for i, p in enumerate(P):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.alignment = {'left': PP_ALIGN.LEFT, 'center': PP_ALIGN.CENTER, 'right': PP_ALIGN.RIGHT}[align]
        para.space_after = Pt(size * p.get('r', 1) * 0.45)
        para.line_spacing = lh
        r = para.add_run()
        r.text = p['t']
        f = r.font
        f.size = Pt(size * p.get('r', 1)); f.bold = p.get('b', False); f.italic = p.get('i', italic)
        f.name = p.get('f', font_name); f.color.rgb = rgb(p.get('c', color))
    return size


def card(slide, x, y, w, h, head=None, body=None, fill='mist', head_color='pet', body_color='ink', tag=None, maxs=15, pad=12, name='Carte'):
    box(slide, x, y, w, h, fill, name=name)
    paras = []
    if tag:
        paras.append({'t': tag.upper(), 'b': True, 'c': 'amb' if fill == 'pet' else 'teal', 'r': 0.72})
    if head:
        paras.append({'t': head, 'b': True, 'c': head_color, 'r': 1.05})
    for b in ([body] if isinstance(body, str) else (body or [])):
        paras.append({'t': b, 'c': body_color})
    if paras:
        text(slide, x + pad, y + pad - 2, w - 2 * pad, h - 2 * pad + 2, paras, maxs=maxs)


BANDS = {'info': ('tealbg', 'pet'), 'warn': ('warnbg', 'brick'), 'dossier': ('ambbg', 'ink'), 'dark': ('pet', 'white'), 'key': ('pet', 'white')}


def band(slide, y, h, t, style='info', x=X0, w=XW):
    style = style or 'info'
    bg, fg = BANDS[style]
    box(slide, x, y, w, h, bg, radius=0.12, name='Bandeau')
    lead = {'warn': 'Attention · ', 'dossier': 'Pour votre dossier D2 · '}.get(style, '')
    paras = [{'t': lead + t, 'c': fg, 'b': style in ('warn',)}]
    text(slide, x + 14, y + 6, w - 28, h - 12, paras, maxs=15, anchor='middle')


def pill(slide, x, y, d, label, fill='amb', color='ink', size=None):
    sp = slide.shapes.add_shape(MSO_SHAPE.OVAL, Pt(x), Pt(y), Pt(d), Pt(d))
    strip_style(sp); sp.name = 'Pastille'
    sp.fill.solid(); sp.fill.fore_color.rgb = rgb(fill); sp.line.fill.background()
    tf = sp.text_frame; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = label
    r.font.size = Pt(size or max(10, min(20, d * 0.42 if len(label) < 3 else d * 0.3))); r.font.bold = True
    r.font.color.rgb = rgb(color); r.font.name = BODY


def arrow(slide, x1, y1, x2, y2, color='teal', w=1.75):
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Pt(x1), Pt(y1), Pt(x2), Pt(y2))
    c.name = 'Flèche'
    c.line.color.rgb = rgb(color); c.line.width = Pt(w)
    ln = c.line._get_or_add_ln()
    tail = ln.makeelement(qn('a:tailEnd'), {'type': 'triangle', 'w': 'med', 'len': 'med'})
    ln.append(tail)


def chevron(slide, x, y, w, h, head, body, fill='teal', color='white'):
    sp = slide.shapes.add_shape(MSO_SHAPE.CHEVRON, Pt(x), Pt(y), Pt(w), Pt(h))
    strip_style(sp); sp.name = 'Étape'
    sp.adjustments[0] = 0.28
    sp.fill.solid(); sp.fill.fore_color.rgb = rgb(fill); sp.line.fill.background()
    paras = [{'t': head, 'b': True, 'c': color}] + ([{'t': body, 'c': color, 'r': 0.9}] if body else [])
    text(slide, x + h * 0.32 + 4, y + 4, w - h * 0.64 - 8, h - 8, paras, maxs=13, anchor='middle', align='center')


def table(slide, x, y, w, h, header, rows, widths=None, maxs=13, mins=8, fills=None, first_bold=True):
    ncol = len(header)
    widths = widths or [1] * ncol
    tot = sum(widths); cw = [w * a / tot for a in widths]
    allrows = [header] + rows

    def need(sz):
        H = 0
        for ri, r in enumerate(allrows):
            hh = max(wrap_lines(str(c), sz, cw[j] - 10, ri == 0 or (first_bold and j == 0)) for j, c in enumerate(r)) * sz * 1.18 + 8
            H += hh
        return H
    sz = maxs
    while sz > mins and need(sz) > h:
        sz -= 0.5
    if need(sz) > h + 1:
        WARN.append(f"diapo {CUR['n']} : TABLEAU QUI DÉBORDE (trop de lignes ou de texte)")
    elif sz < 10:
        WARN.append(f"diapo {CUR['n']} : tableau réduit à {sz} pt")
    gt = slide.shapes.add_table(len(allrows), ncol, Pt(x), Pt(y), Pt(w), Pt(h))
    gt.name = 'Tableau'
    tblPr = gt._element.graphic.graphicData.tbl.tblPr
    for k in ('bandRow', 'firstRow'):
        tblPr.set(k, '0')
    sid = tblPr.find(qn('a:tableStyleId'))
    if sid is not None:
        sid.text = '{5940675A-B579-460E-94D1-54222C63F5DA}'  # "No Style, Table Grid" -> we paint cells ourselves
    tbl = gt.table
    for j, c in enumerate(cw):
        tbl.columns[j].width = Pt(c)
    for ri, r in enumerate(allrows):
        hh = max(wrap_lines(str(c), sz, cw[j] - 10, ri == 0 or (first_bold and j == 0)) for j, c in enumerate(r)) * sz * 1.18 + 8
        tbl.rows[ri].height = Pt(hh)
        for j, val in enumerate(r):
            cell = tbl.cell(ri, j)
            cell.margin_left = cell.margin_right = Pt(5); cell.margin_top = cell.margin_bottom = Pt(3)
            fill = 'pet' if ri == 0 else ('white' if ri % 2 else 'mist')
            if fills and ri > 0 and fills[ri - 1] and fills[ri - 1][j]:
                fill = fills[ri - 1][j]
            cell.fill.solid(); cell.fill.fore_color.rgb = rgb(fill)
            tf = cell.text_frame; tf.word_wrap = True
            p = tf.paragraphs[0]
            run = p.add_run(); run.text = str(val)
            run.font.size = Pt(sz); run.font.name = BODY
            run.font.bold = ri == 0 or (first_bold and j == 0)
            run.font.color.rgb = rgb('white' if ri == 0 else ('pet' if j == 0 and first_bold else 'ink'))
            # thin borders
            tcPr = cell._tc.get_or_add_tcPr()
            for side in ('a:lnL', 'a:lnR', 'a:lnT', 'a:lnB'):
                ln = tcPr.makeelement(qn(side), {'w': '6350'})
                sf = ln.makeelement(qn('a:solidFill'), {}); clr = sf.makeelement(qn('a:srgbClr'), {'val': C['pale']})
                sf.append(clr); ln.append(sf); tcPr.append(ln)
    return need(sz)


# ---------------------------------------------------------------- figures from the course (SVG -> PNG)
FIGDIR = os.path.join(HERE, 'figs')


def figure_png(fid):
    import cours_figures, cours_figures_s2
    figs = dict(cours_figures.FIGS); figs.update(cours_figures_s2.FIGS)
    svg = figs[fid]()
    os.makedirs(FIGDIR, exist_ok=True)
    png = os.path.join(FIGDIR, fid + '.png')
    svgp = os.path.join(FIGDIR, fid + '.svg')
    old = open(svgp, encoding='utf8').read() if os.path.exists(svgp) else None
    if old != svg or not os.path.exists(png):
        open(svgp, 'w', encoding='utf8').write(svg)
        m = re.search(r'<svg[^>]*?viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
        W, H = round(float(m.group(1))), round(float(m.group(2)))
        html = os.path.join(FIGDIR, fid + '.html')
        open(html, 'w', encoding='utf8').write(f'<html><body style="margin:0;background:#fff">{svg}</body></html>')
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=2',
                        f'--window-size={W},{H}', f'--screenshot={png}', 'file:///' + html.replace('\\', '/')], check=True, capture_output=True)
        os.remove(html)
    from PIL import Image
    im = Image.open(png)
    return png, im.size


def picture(slide, x, y, w, h, fid):
    png, (pw, ph) = figure_png(fid)
    r = min(w / pw, h / ph)
    W, H = pw * r, ph * r
    slide.shapes.add_picture(png, Pt(x + (w - W) / 2), Pt(y + (h - H) / 2), Pt(W), Pt(H)).name = 'Figure'


# ---------------------------------------------------------------- slide patterns
def head(slide, s):
    slide.placeholders[100].text = s.get('kicker', '')
    slide.placeholders[101].text = s['title']
    if tw(s['title'], 30, True, True) > 861:
        WARN.append(f"diapo {CUR['n']} : TITRE SUR DEUX LIGNES, à raccourcir ({s['title']})")


def number(slide, n):
    text(slide, 866, 506, 50, 20, [{'t': str(n), 'c': 'slate'}], size=10, align='right', autofit=False, name='Numéro de diapositive')


def p_cover(slide, s):
    slide.placeholders[100].text = s.get('kicker', '')
    slide.placeholders[101].text = s['title']
    slide.placeholders[102].text = s.get('subtitle', '')
    # decorative map: concentric squares (cartography) on the right
    for i, d in enumerate([92, 184, 276, 368]):
        sp = box(slide, 760 - d / 2, 270 - d / 2, d, d, None, radius=0.08, line='teal', name='Décor')
    for (x, y, d) in [(745, 255, 14), (690, 300, 9), (842, 318, 12), (715, 160, 8), (815, 180, 10)]:
        sp = slide.shapes.add_shape(MSO_SHAPE.OVAL, Pt(x), Pt(y), Pt(d), Pt(d)); strip_style(sp)
        sp.fill.solid(); sp.fill.fore_color.rgb = rgb('amb'); sp.line.fill.background(); sp.name = 'Décor'


def p_section(slide, s):
    slide.placeholders[100].text = s.get('kicker', '')
    slide.placeholders[101].text = s['title']
    slide.placeholders[102].text = s.get('subtitle', '')


def p_definition(slide, s):
    side = s.get('side')
    w = 520 if side else XW
    hh = 250 if s.get('note') else YH
    box(slide, X0, Y0, w, hh, 'pet', name='Définition')
    paras = [{'t': 'DÉFINITION', 'b': True, 'c': 'amb', 'r': 0.7}, {'t': s['term'], 'b': True, 'c': 'white', 'r': 1.35, 'f': HEAD}]
    paras += [{'t': d, 'c': 'white'} for d in (s['definition'] if isinstance(s['definition'], list) else [s['definition']])]
    if s.get('source'):
        paras.append({'t': s['source'], 'c': 'pale', 'r': 0.8, 'i': True})
    text(slide, X0 + 20, Y0 + 16, w - 40, hh - 32, paras, maxs=19)
    if side:
        card(slide, X0 + w + 18, Y0, XW - w - 18, hh, side.get('head'), side.get('body'), fill=side.get('fill', 'mist'), tag=side.get('tag'), maxs=15)
    if s.get('note'):
        band(slide, Y0 + hh + 16, YH - hh - 16, s['note'], s.get('note_style', 'info'))


def p_cards(slide, s, y0=None, yh=None):
    Y0_, YH_ = (y0 or Y0), (yh or YH)
    cards = s['cards']
    n = len(cards); cols = s.get('cols') or (n if n <= 4 else (3 if n in (5, 6, 9) else 4))
    rows = -(-n // cols)
    y = Y0_
    if s.get('intro'):
        ih = s.get('intro_h', 46)
        text(slide, X0, y, XW, ih, s['intro'], maxs=16)
        y += ih + 10
    bottom = Y0_ + YH_ - ((s.get('note_h', 52) + 14) if s.get('note') else 0)
    gap = 14
    ch = (bottom - y - gap * (rows - 1)) / rows
    cw = (XW - gap * (cols - 1)) / cols
    for i, c in enumerate(cards):
        r, k = divmod(i, cols)
        fill = c.get('fill', 'mist')
        card(slide, X0 + k * (cw + gap), y + r * (ch + gap), cw, ch, c.get('head'), c.get('body'), fill=fill,
             head_color='white' if fill == 'pet' else ('brick' if fill == 'warnbg' else 'pet'),
             body_color='white' if fill == 'pet' else 'ink', tag=c.get('tag'), maxs=s.get('maxs', 15))
    if s.get('note'):
        band(slide, bottom + 14, s.get('note_h', 52), s['note'], s.get('note_style', 'info'))


def p_text_panel(slide, s):
    lw = s.get('left_w', 455)
    bottom = Y0 + YH - ((s.get('note_h', 50) + 14) if s.get('note') else 0)
    paras = []
    for t in s['text']:
        paras.append(t if isinstance(t, dict) else {'t': t})
    text(slide, X0, Y0, lw, bottom - Y0, paras, maxs=17)
    px = X0 + lw + 24; pw = XW - lw - 24
    pnl = s['panel']
    box(slide, px, Y0, pw, bottom - Y0, pnl.get('fill', 'pet'), name='Panneau')
    dark = pnl.get('fill', 'pet') == 'pet'
    P = []
    if pnl.get('kicker'):
        P.append({'t': pnl['kicker'], 'b': True, 'c': 'amb' if dark else 'teal', 'r': 0.85})
    for it in pnl.get('items', []):
        if it.get('big'):
            P.append({'t': it['big'], 'b': True, 'c': 'white' if dark else 'pet', 'r': 1.9, 'f': HEAD})
        if it.get('small'):
            P.append({'t': it['small'], 'c': 'white' if dark else 'ink'})
    for b in pnl.get('body', []):
        P.append({'t': b, 'c': 'white' if dark else 'ink'})
    text(slide, px + 18, Y0 + 16, pw - 36, bottom - Y0 - 32, P, maxs=16)
    if s.get('note'):
        band(slide, bottom + 14, s.get('note_h', 50), s['note'], s.get('note_style', 'info'))


def p_table(slide, s):
    y = Y0
    if s.get('intro'):
        ih = s.get('intro_h', 40)
        text(slide, X0, y, XW, ih, s['intro'], maxs=16); y += ih + 8
    bottom = Y0 + YH - ((s.get('note_h', 48) + 12) if s.get('note') else 0)
    side = s.get('side')
    w = XW - (290 if side else 0)
    table(slide, X0, y, w, bottom - y, s['header'], s['rows'], s.get('widths'), maxs=s.get('maxs', 16), fills=s.get('fills'))
    if side:
        card(slide, X0 + w + 18, y, 272, bottom - y, side.get('head'), side.get('body'), fill=side.get('fill', 'pet'),
             head_color='white' if side.get('fill', 'pet') == 'pet' else 'pet', body_color='white' if side.get('fill', 'pet') == 'pet' else 'ink',
             tag=side.get('tag'), maxs=14)
    if s.get('note'):
        band(slide, bottom + 12, s.get('note_h', 48), s['note'], s.get('note_style', 'info'))


def p_figure(slide, s):
    bottom = Y0 + YH - ((s.get('note_h', 46) + 12) if s.get('note') else 0)
    side = s.get('side')
    fw = XW - (300 if side else 0)
    picture(slide, X0, Y0 - 6, fw, bottom - Y0 + 6, s['fig'])
    if side:
        x = X0 + fw + 18
        if isinstance(side, dict):
            card(slide, x, Y0, XW - fw - 18, bottom - Y0, side.get('head'), side.get('body'), fill=side.get('fill', 'mist'), tag=side.get('tag'), maxs=15)
        else:
            text(slide, x, Y0, XW - fw - 18, bottom - Y0, side, maxs=16)
    if s.get('note'):
        band(slide, bottom + 12, s.get('note_h', 46), s['note'], s.get('note_style', 'info'))


def p_steps(slide, s):
    steps = s['steps']; n = len(steps)
    hl = set(s.get('highlight', []))
    sh = s.get('steps_h', 64)
    w = (XW + 12 * (n - 1)) / n
    for i, st in enumerate(steps):
        fill = 'amb' if i in hl else ('pet' if i % 2 else 'teal')
        chevron(slide, X0 + i * (w - 12), Y0, w, sh, st['head'], st.get('body'), fill=fill, color='ink' if i in hl else 'white')
    y = Y0 + sh + 18
    bottom = Y0 + YH - ((s.get('note_h', 46) + 12) if s.get('note') else 0)
    if s.get('cards'):
        sub = dict(s); sub.pop('intro', None); sub.pop('note', None)
        cards = s['cards']; cols = len(cards) if len(cards) <= 4 else 3
        rows = -(-len(cards) // cols); gap = 14
        cw = (XW - gap * (cols - 1)) / cols; ch = (bottom - y - gap * (rows - 1)) / rows
        for i, c in enumerate(cards):
            r, k = divmod(i, cols)
            f = c.get('fill', 'mist')
            card(slide, X0 + k * (cw + gap), y + r * (ch + gap), cw, ch, c.get('head'), c.get('body'), fill=f, tag=c.get('tag'), maxs=14,
                 head_color='white' if f == 'pet' else 'pet', body_color='white' if f == 'pet' else 'ink')
    elif s.get('text'):
        text(slide, X0, y, XW, bottom - y, s['text'], maxs=16)
    if s.get('note'):
        band(slide, bottom + 12, s.get('note_h', 46), s['note'], s.get('note_style', 'info'))


def p_pills(slide, s):
    items = s['items']; n = len(items)
    bottom = Y0 + YH - ((s.get('note_h', 46) + 12) if s.get('note') else 0)
    if s.get('layout', 'row') == 'row':
        gap = 18; w = (XW - gap * (n - 1)) / n; d = 48
        for i, it in enumerate(items):
            x = X0 + i * (w + gap)
            pill(slide, x, Y0, d, it['pill'], fill=it.get('fill', 'amb'))
            text(slide, x + d + 10, Y0, w - d - 10, d, [{'t': it['head'], 'b': True, 'c': 'pet'}], maxs=15, anchor='middle')
            if i < n - 1:
                arrow(slide, x + w - 4, Y0 + d / 2, x + w + gap - 2, Y0 + d / 2)
            card(slide, x, Y0 + d + 14, w, bottom - Y0 - d - 14, it.get('sub'), it.get('body'), fill=it.get('card_fill', 'mist'), maxs=14)
    else:  # list: pills down the left, two columns if many
        cols = 2 if n > 4 else 1
        per = -(-n // cols); gap = 10
        cw = (XW - 24 * (cols - 1)) / cols; rh = (bottom - Y0 - gap * (per - 1)) / per
        d = min(40, rh - 6)
        for i, it in enumerate(items):
            k, r = divmod(i, per)
            x = X0 + k * (cw + 24); y = Y0 + r * (rh + gap)
            pill(slide, x, y + (rh - d) / 2, d, it['pill'], fill=it.get('fill', 'amb'))
            P = [{'t': it['head'], 'b': True, 'c': 'pet'}] + ([{'t': it['body']}] if it.get('body') else [])
            text(slide, x + d + 12, y, cw - d - 12, rh, P, maxs=15, anchor='middle')
    if s.get('note'):
        band(slide, bottom + 12, s.get('note_h', 46), s['note'], s.get('note_style', 'info'))


def p_study(slide, s):
    lw = s.get('left_w', 500)
    box(slide, X0, Y0, lw, YH, 'cream', name='Document')
    edge = box(slide, X0, Y0, 5, YH, 'amb', radius=0, name='Filet', shape=MSO_SHAPE.RECTANGLE)
    P = [{'t': s['source'], 'b': True, 'c': 'slate', 'r': 0.78}] + [{'t': d} for d in s['document']]
    text(slide, X0 + 20, Y0 + 14, lw - 34, YH - 28, P, maxs=14)
    x = X0 + lw + 20; w = XW - lw - 20
    Q = [{'t': 'Questions de réflexion', 'b': True, 'c': 'pet', 'r': 1.1, 'f': HEAD}]
    Q += [{'t': f'{i}. {q}'} for i, q in enumerate(s['questions'], 1)]
    text(slide, x, Y0 + 4, w, YH - 8, Q, maxs=15)


def p_exercise(slide, s):
    box(slide, X0, Y0, XW, YH, 'ambbg', name='Exercice')
    box(slide, X0, Y0, 6, YH, 'amb', radius=0, name='Filet', shape=MSO_SHAPE.RECTANGLE)
    top = [{'t': 'EXERCICE · MEDISECURE' + (f' · {s["duration"]}' if s.get('duration') else ''), 'b': True, 'c': 'brick', 'r': 0.75},
           {'t': s['name'], 'b': True, 'c': 'pet', 'r': 1.25, 'f': HEAD}]
    lw = XW - 300
    th = 64 if tw(s['name'], 20 * 1.25, True, True) <= lw - 30 else 92
    text(slide, X0 + 22, Y0 + 14, lw - 30, th, top, maxs=20)
    text(slide, X0 + 22, Y0 + 20 + th, lw - 30, YH - 34 - th, s['consigne'], maxs=15)
    card(slide, X0 + lw + 6, Y0 + 16, 280, YH - 32, 'Livrable', [s['livrable']] + ([s['dossier']] if s.get('dossier') else []),
         fill='white', maxs=14)


def p_fiche(slide, s):
    # Invitation à prendre une fiche de travail (Kestrel) et à la réaliser maintenant.
    box(slide, X0, Y0, XW, YH, 'tealbg', name='Fiche de travail')
    box(slide, X0, Y0, 6, YH, 'teal', radius=0, name='Filet', shape=MSO_SHAPE.RECTANGLE)
    top = [{'t': 'FICHE DE TRAVAIL · ' + s['ft'] + (f' · {s["duration"]}' if s.get('duration') else '') + ' · KESTREL LOGISTIQUE',
            'b': True, 'c': 'pet', 'r': 0.75},
           {'t': s['name'], 'b': True, 'c': 'pet', 'r': 1.25, 'f': HEAD}]
    lw = XW - 300
    th = 64 if tw(s['name'], 20 * 1.25, True, True) <= lw - 30 else 92
    text(slide, X0 + 22, Y0 + 14, lw - 30, th, top, maxs=20)
    text(slide, X0 + 22, Y0 + 20 + th, lw - 30, YH - 34 - th, s['consigne'], maxs=15)
    card(slide, X0 + lw + 6, Y0 + 16, 280, YH - 32, 'À la fin de la fiche', s['livrable'] if isinstance(s['livrable'], list) else [s['livrable']],
         fill='white', maxs=14)


def p_quote(slide, s):
    qh = s.get('quote_h', 70)
    box(slide, X0, Y0, XW, qh, 'pet', name='Citation')
    text(slide, X0 + 24, Y0 + 8, XW - 48, qh - 16, [{'t': s['quote'], 'c': 'amb', 'b': True, 'f': HEAD}], maxs=22, anchor='middle', align='center')
    if s.get('cards'):
        sub = {'cards': s['cards'], 'cols': s.get('cols'), 'note': s.get('note'), 'note_style': s.get('note_style'), 'note_h': s.get('note_h', 52)}
        p_cards(slide, sub, Y0 + qh + 16, YH - qh - 16)
    elif s.get('header'):
        gy = Y0 + qh + 16
        table(slide, X0, gy, XW, Y0 + YH - gy, s['header'], s['rows'], s.get('widths'), maxs=s.get('maxs', 16))


PATTERNS = {'cover': ('DARK', p_cover), 'section': ('DARK', p_section), 'definition': ('CONTENT', p_definition),
            'cards': ('CONTENT', p_cards), 'text_panel': ('CONTENT', p_text_panel), 'table': ('CONTENT', p_table),
            'figure': ('CONTENT', p_figure), 'steps': ('CONTENT', p_steps), 'pills': ('CONTENT', p_pills),
            'study': ('CONTENT', p_study), 'exercise': ('CONTENT', p_exercise), 'quote': ('CONTENT', p_quote),
            'fiche': ('CONTENT', p_fiche)}


# ---------------------------------------------------------------- deck, notes, prompter, script
def fresh_template():
    prs = Presentation(TEMPLATE)
    lst = prs.slides._sldIdLst
    for sid in list(lst):
        prs.part.drop_rel(sid.rId); lst.remove(sid)
    for lay in prs.slide_layouts:
        for sh in lay.shapes:
            if sh.has_text_frame and 'Semaine S1' in sh.text_frame.text:
                r = sh.text_frame.paragraphs[0].runs
                r[0].text = FOOTER
                for x in r[1:]:
                    x.text = ''
    return prs


def notes_text(n, s):
    out = [f'▶ DIAPO {n} : cliquer en commençant ce bloc', '']
    for p in s['notes']:
        out.append(f'[Écran : {p["cue"]}]')
        out.append(p['text']); out.append('')
    return '\n'.join(out).rstrip()


def words(s):
    return sum(len(p['text'].split()) for p in s['notes'])


def build_deck(spec, out):
    prs = fresh_template()
    lay = {l.name: l for l in prs.slide_layouts}
    n0 = spec['first_number']
    for i, s in enumerate(spec['slides']):
        n = n0 + i
        CUR['n'] = n
        layout, fn = PATTERNS[s['pattern']]
        slide = prs.slides.add_slide(lay[layout])
        if layout == 'CONTENT':
            head(slide, s)
        fn(slide, s)
        if layout == 'CONTENT':
            number(slide, n)
        slide.notes_slide.notes_text_frame.text = notes_text(n, s)
    prs.core_properties.title = spec['title']
    prs.core_properties.author = '3W Academy · Cycle Expert en informatique et SI'
    prs.save(out)


def build_prompter(spec, out):
    html = open(PROMPT_TEMPLATE, encoding='utf8').read()
    data = [{'n': spec['first_number'] + i, 'title': s['title'], 'paras': s['notes'], 'words': words(s)} for i, s in enumerate(spec['slides'])]
    js = json.dumps(data, ensure_ascii=False)
    html = re.sub(r'const DATA = \[.*?\];\n', lambda m: f'const DATA = {js};\n', html, count=1, flags=re.S)
    html = re.sub(r'<title>.*?</title>', f'<title>Prompteur S2 · {spec.get("label", "Jour " + str(spec["day"]))}</title>', html, count=1)
    html = html.replace('Veille S1', 'S2').replace('Semaine S1', 'Semaine S2')
    open(out, 'w', encoding='utf8').write(html)


def build_script(spec, out):
    import docx
    d = docx.Document(DOCX_TEMPLATE)
    body = d.element.body
    for el in list(body):
        if el.tag != qn('w:sectPr'):
            body.remove(el)
    total = sum(words(s) for s in spec['slides'])
    lab = spec.get('label', f'Jour {spec["day"]}')
    d.add_paragraph(f'S2 · {lab} — script prompteur', style='Title')
    d.add_paragraph('Déroulé', style='Heading 2')
    d.add_paragraph(spec['deroule'])
    n0 = spec['first_number']; n1 = n0 + len(spec['slides']) - 1
    tot = f'{total:,}'.replace(',', ' ')
    d.add_paragraph(f'Diaporama : {spec.get("deck", "J" + str(spec["day"]) + "_Diaporama.pptx")} (diapositives {n0} à {n1}). Environ {tot} mots, soit près de {round(total / 130)} minutes de parole '
                    f'à 130 mots par minute, hors questions et hors ateliers. « ▶ DIAPO N » signale le clic qui affiche la diapositive ; '
                    "les repères entre crochets décrivent ce qui est à l'écran et ne se lisent pas.")
    for i, s in enumerate(spec['slides']):
        d.add_paragraph(f'▶ DIAPO {n0 + i} · {s["title"]}', style='Heading 1')
        d.add_paragraph(f'Cliquer en commençant ce bloc · durée indicative : {str(s.get("minutes", 1)).replace(".", ",")} min')
        for p in s['notes']:
            para = d.add_paragraph()
            r = para.add_run(f'[Écran : {p["cue"]}]  '); r.bold = True
            para.add_run(p['text'])
    d.core_properties.title = f'S2 · {lab} — script prompteur'
    d.save(out)


def build_day(day, out_dir):
    spec = json.load(open(os.path.join(HERE, 'spec', f'{day}.json'), encoding='utf8'))
    os.makedirs(out_dir, exist_ok=True)
    k = spec['day']
    build_deck(spec, os.path.join(out_dir, f'J{k}_Diaporama.pptx'))
    build_prompter(spec, os.path.join(out_dir, f'J{k}_Prompteur.html'))
    build_script(spec, os.path.join(out_dir, f'J{k}_Script_prompteur.docx'))
    print(day, len(spec['slides']), 'diapositives,', sum(words(s) for s in spec['slides']), 'mots de script')
    for w in WARN:
        print('  AVERTISSEMENT', w)
    WARN.clear()
    return spec


def build_week(out_dir):
    days = [json.load(open(os.path.join(HERE, 'spec', f'J{k}.json'), encoding='utf8')) for k in range(1, 6)]
    for a, b in zip(days, days[1:]):
        assert a['first_number'] + len(a['slides']) == b['first_number'], (a['day'], b['day'])
    week = {'day': 0, 'label': 'semaine complète', 'deck': 'S2_Diaporama.pptx', 'title': "Semaine S2 · Systèmes d'information, cartographie et risques",
            'first_number': 1, 'slides': [s for d in days for s in d['slides']],
            'deroule': ' '.join(f"Jour {d['day']} : diapositives {d['first_number']} à {d['first_number'] + len(d['slides']) - 1}." for d in days)}
    os.makedirs(out_dir, exist_ok=True)
    build_deck(week, os.path.join(out_dir, 'S2_Diaporama.pptx'))
    build_prompter(week, os.path.join(out_dir, 'S2_Prompteur.html'))
    build_script(week, os.path.join(out_dir, 'S2_Script_prompteur.docx'))
    print('semaine', len(week['slides']), 'diapositives,', sum(words(s) for s in week['slides']), 'mots de script')
    for w in WARN:
        print('  AVERTISSEMENT', w)
    WARN.clear()


if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'out')
    days = sys.argv[2:] or [f[:-5] for f in sorted(os.listdir(os.path.join(HERE, 'spec'))) if f.endswith('.json')]
    for d in days:
        if d == 'semaine':
            build_week(os.path.join(out, 'Semaine_complete'))
        else:
            build_day(d, os.path.join(out, d))
