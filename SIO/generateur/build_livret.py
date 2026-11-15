# Livret de fiches « Veille technologique » pour BTS SIO 2 (format manuel de STMG).
# Sources : fiches/jours.md (intercalaires) et fiches/f*.md (fiches). Voir FORMAT.md.
# Usage : python build_livret.py <dossier_sortie> [fiche.md ...]
#   sans fiche : livret complet (élève + enseignant) ; avec fiches : construction de test + PNG des pages.
import glob, hashlib, html as H, os, re, subprocess, sys
import fitz
from frtypo import fr

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'fiches')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
GAP = re.compile(r'\[\[(.+?)\]\]')
WARN = []


def esc(s):
    return fr(H.escape(s))


def inl(s, teacher):
    out, last = [], 0
    for m in GAP.finditer(s):
        out.append(esc(s[last:m.start()]))
        out.append(f'<span class="trou rempli">{esc(m.group(1))}</span>' if teacher else
                   f'<span class="trou" style="min-width:{max(4, len(m.group(1)) * 0.62):.1f}em"></span>')
        last = m.end()
    out.append(esc(s[last:]))
    s = ''.join(out)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    return s


# ---------------------------------------------------------------- parsing
def new_item(kind, **kw):
    d = {'kind': kind, 'lines': [], 'answer': None, 'table': []}
    d.update(kw)
    return d


def parse(text, path):
    sheets = []
    for chunk in re.split(r'^# FICHE ', text, flags=re.M)[1:]:
        lines = chunk.rstrip().split('\n')
        try:
            num, title, jour = [p.strip() for p in lines[0].split('|')]
        except ValueError:
            raise SystemExit(f'{path} : en-tête mal formé : « # FICHE {lines[0]} »')
        sh = {'num': num, 'title': title, 'jour': jour, 'accroche': [], 'objectifs': [], 'duree': '', 'notions': [],
              'jeux': [], 'annexes': [], 'questions': [], 'reflexion': None, 'monprojet': None, 'retiens': [],
              'corriges': {}}
        cur = None
        last = None   # dernier élément pouvant recevoir @lignes / @tableau
        for ln in lines[1:]:
            if ln.startswith('@'):
                kind, _, arg = ln[1:].partition(' ')
                arg = arg.strip()
                if kind in ('accroche', 'objectifs', 'notions', 'retiens'):
                    cur = sh[kind]
                elif kind == 'duree':
                    sh['duree'] = arg; cur = None
                elif kind == 'jeu':
                    typ, _, t = arg.partition('|')
                    j = new_item(typ.strip(), title=t.strip())
                    if j['kind'] not in ('vraifaux', 'associe', 'quiz', 'classe'):
                        raise SystemExit(f'{path} fiche {num} : jeu inconnu « {j["kind"]} »')
                    sh['jeux'].append(j); cur = j['lines']
                elif kind == 'annexe':
                    n, t, src = ([p.strip() for p in arg.split('|')] + ['', ''])[:3]
                    a = new_item('texte', n=n, title=t, source=src, opt='')
                    sh['annexes'].append(a); cur = a['lines']
                elif kind in ('graphique', 'schema'):
                    if not sh['annexes']:
                        raise SystemExit(f'{path} fiche {num} : @{kind} hors annexe')
                    sh['annexes'][-1]['kind'] = kind; sh['annexes'][-1]['opt'] = arg
                elif kind == 'question':
                    n, cap, ann = ([p.strip() for p in arg.split('|')] + ['', ''])[:3]
                    q = new_item('question', n=n, cap=cap, ann=ann)
                    sh['questions'].append(q); cur = q['lines']; last = q
                elif kind == 'reflexion':
                    sh['reflexion'] = new_item('reflexion'); cur = sh['reflexion']['lines']; last = sh['reflexion']
                elif kind == 'monprojet':
                    sh['monprojet'] = new_item('monprojet'); cur = sh['monprojet']['lines']; last = sh['monprojet']
                elif kind == 'lignes':
                    last['answer'] = ('lignes', int(arg or 4)); cur = None
                elif kind == 'tableau':
                    last['answer'] = ('tableau', 0); cur = last['table']
                elif kind == 'corrige':
                    sh['corriges'][arg] = []; cur = sh['corriges'][arg]
                else:
                    raise SystemExit(f'{path} fiche {num} : bloc inconnu @{kind}')
                continue
            if cur is not None:
                cur.append(ln)
        missing = [q['n'] for q in sh['questions'] if q['n'] not in sh['corriges']]
        if missing:
            raise SystemExit(f'{path} fiche {num} : corrigé manquant pour la question {", ".join(missing)}')
        if sh['reflexion'] and 'R' not in sh['corriges']:
            WARN.append(f'fiche {num} : pas de @corrige R (pistes pour « Je réfléchis »)')
        if not sh['monprojet']:
            WARN.append(f'fiche {num} : pas de bloc @monprojet')
        if not sh['jeux']:
            WARN.append(f'fiche {num} : aucun @jeu')
        if not (2 <= len(sh['annexes']) <= 4):
            WARN.append(f'fiche {num} : {len(sh["annexes"])} annexes (2 à 4 attendues)')
        if not (4 <= len(sh['questions']) <= 7):
            WARN.append(f'fiche {num} : {len(sh["questions"])} questions (4 à 7 attendues)')
        sheets.append(sh)
    return sheets


def parse_jours(path):
    jours = {}
    if not os.path.exists(path):
        return jours
    for chunk in re.split(r'^# ', open(path, encoding='utf8').read(), flags=re.M)[1:]:
        lines = chunk.rstrip().split('\n')
        key, title = [p.strip() for p in lines[0].split('|')]
        jours[key] = {'title': title, 'lines': lines[1:]}
    return jours


# ---------------------------------------------------------------- rendering helpers
def table(lines, teacher, blank=False):
    rows = [[c.strip() for c in l.strip().strip('|').split('|')] for l in lines if l.strip().startswith('|')]
    rows = [r for r in rows if not all(re.fullmatch(r':?-{2,}:?', c) for c in r)]
    if not rows:
        return ''
    head, body = rows[0], rows[1:]
    th = ''.join(f'<th>{inl(c, teacher)}</th>' for c in head)
    trs = ''.join('<tr>' + ''.join(f'<td class="{"vide" if blank and not c else ""}">{inl(c, teacher)}</td>' for c in r) + '</tr>' for r in body)
    return f'<table class="{"acompleter" if blank else ""}"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>'


def schema_rows(lines, teacher):
    rows = []
    for l in lines:
        boxes = [b.strip() for b in l.split('->') if b.strip()]
        if not boxes:
            continue
        cells = []
        for i, b in enumerate(boxes):
            m = GAP.fullmatch(b)
            if m:
                cells.append(f'<div class="boite {"remplie" if teacher else "vide"}">{esc(m.group(1)) if teacher else "&nbsp;"}</div>')
            else:
                cells.append(f'<div class="boite">{inl(b, teacher)}</div>')
            if i < len(boxes) - 1:
                cells.append('<div class="fleche">→</div>')
        rows.append(f'<div class="schema-ligne">{"".join(cells)}</div>')
    return f'<div class="schema">{"".join(rows)}</div>'


def rich(lines, teacher):
    """Paragraphes, tableaux, encadrés !def / !astuce / !attention / !exemple, schémas !schema."""
    out, buf, tab, sch = [], [], [], []

    def flush(keep=None):
        nonlocal buf, tab, sch
        if buf:
            out.append(f'<p>{inl(" ".join(x.strip() for x in buf), teacher)}</p>'); buf = []
        if tab and keep != 'tab':
            out.append(table(tab, teacher)); tab = []
        if sch and keep != 'sch':
            out.append(schema_rows(sch, teacher)); sch = []

    for l in lines + ['']:
        s = l.strip()
        if s.startswith('|'):
            flush(keep='tab'); tab.append(s); continue
        if s.startswith('!schema'):
            flush(keep='sch'); sch.append(s[7:].strip()); continue
        m = re.match(r'!(def|astuce|attention|exemple|savoir)\s+(.*?)\s*\|\s*(.*)', s)
        if m:
            flush()
            cls, t, body = m.groups()
            lab = {'def': 'Définition', 'astuce': 'Astuce', 'attention': 'Attention', 'exemple': 'Exemple', 'savoir': 'Le saviez-vous ?'}[cls]
            out.append(f'<div class="encadre {cls}"><p class="enc-titre"><span>{lab}</span>{inl(t, teacher)}</p><p>{inl(body, teacher)}</p></div>')
            continue
        if not s:
            flush(); continue
        if tab or sch:
            flush()
        buf.append(s)
    return ''.join(out)


def num(s):
    return float(s.replace('\u202f', '').replace(' ', '').replace(',', '.'))


def chart(a):
    kind, _, unit = a['opt'].partition(' ')
    pts = []
    for l in a['lines']:
        if ':' in l:
            k, v = l.rsplit(':', 1)
            pts.append((k.strip(), num(v.strip())))
    if not pts:
        return '<p class="err">Graphique sans données</p>'
    W, Hh, L, R, T, B = 640, 230, 56, 16, 18, 48
    vmax = max(v for _, v in pts) or 1
    step = 10 ** len(str(int(vmax))) / 10
    top = (int(vmax / step) + 1) * step
    pw, ph = W - L - R, Hh - T - B
    g = [f'<svg viewBox="0 0 {W} {Hh}" class="graph" xmlns="http://www.w3.org/2000/svg" font-family="Source Sans 3, Calibri, sans-serif">']
    for i in range(5):
        y = T + ph - ph * i / 4; val = top * i / 4
        g.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W - R}" y2="{y:.1f}" stroke="#d5dfdd" stroke-width="1"/>')
        lab = f'{val:,.0f}'.replace(',', ' ') if val == int(val) else f'{val:.1f}'.replace('.', ',')
        g.append(f'<text x="{L - 6}" y="{y + 4:.1f}" font-size="11" text-anchor="end" fill="#5e6b78">{lab}</text>')
    n = len(pts); slot = pw / n
    coords = []
    for i, (k, v) in enumerate(pts):
        cx = L + slot * (i + .5); y = T + ph - ph * v / top
        coords.append((cx, y))
        if kind == 'barres':
            bw = min(46, slot * .62)
            g.append(f'<rect x="{cx - bw / 2:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{T + ph - y:.1f}" fill="#1f6f78" rx="2"/>')
        vl = f'{v:,.2f}'.rstrip('0').rstrip('.').replace(',', '\u202f').replace('.', ',')
        g.append(f'<text x="{cx:.1f}" y="{y - 5:.1f}" font-size="11" text-anchor="middle" fill="#1b2a33">{vl}</text>')
        words, l1, l2 = k.split(), '', ''
        for w in words:
            if not l2 and len(l1 + ' ' + w) <= 18: l1 = (l1 + ' ' + w).strip()
            else: l2 = (l2 + ' ' + w).strip()
        g.append(f'<text x="{cx:.1f}" y="{T + ph + 16}" font-size="11" text-anchor="middle" fill="#1b2a33">{H.escape(l1)}</text>')
        if l2:
            g.append(f'<text x="{cx:.1f}" y="{T + ph + 29}" font-size="11" text-anchor="middle" fill="#1b2a33">{H.escape(l2)}</text>')
    if kind == 'lignes':
        g.append('<polyline fill="none" stroke="#1f6f78" stroke-width="2.5" points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in coords) + '"/>')
        g += [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#e09f3e"/>' for x, y in coords]
    g.append(f'<line x1="{L}" y1="{T + ph}" x2="{W - R}" y2="{T + ph}" stroke="#5e6b78"/>')
    if unit:
        g.append(f'<text x="{L}" y="{T - 6}" font-size="11" fill="#5e6b78">{H.escape(fr(unit))}</text>')
    g.append('</svg>')
    return ''.join(g)


def answer_zone(item, teacher):
    if teacher or not item['answer']:
        return ''
    if item['answer'][0] == 'lignes':
        return '<div class="lignes">' + '<div></div>' * item['answer'][1] + '</div>'
    return table(item['table'], False, blank=True)


# ---------------------------------------------------------------- jeux
def shuffle_key(s):
    return hashlib.md5(s.encode('utf8')).hexdigest()


def jeu(j, teacher):
    lines = [l for l in j['lines'] if l.strip()]
    o = [f'<div class="jeu"><p class="jeu-titre"><span>Je m\'entraîne</span>{inl(j["title"], teacher)}</p>']
    if j['kind'] == 'vraifaux':
        rows = []
        for l in lines:
            parts = [p.strip() for p in l.split('|')]
            aff, rep, expl = (parts + ['', ''])[:3]
            if teacher:
                rows.append(f'<tr><td class="aff">{inl(aff, teacher)}</td><td class="vf rep">{"Vrai" if rep.upper().startswith("V") else "Faux"}</td>'
                            f'<td class="expl">{inl(expl, teacher)}</td></tr>')
            else:
                rows.append(f'<tr><td class="aff">{inl(aff, teacher)}</td><td class="vf"><span class="case"></span> V</td><td class="vf"><span class="case"></span> F</td></tr>')
        head = '<tr><th>Affirmation</th><th>Réponse</th><th>Explication</th></tr>' if teacher else '<tr><th>Affirmation</th><th>Vrai</th><th>Faux</th></tr>'
        o.append(f'<table class="vft"><thead>{head}</thead><tbody>{"".join(rows)}</tbody></table>')
    elif j['kind'] == 'associe':
        pairs = [[p.strip() for p in l.split('|', 1)] for l in lines]
        right = sorted(range(len(pairs)), key=lambda i: shuffle_key(pairs[i][1]))
        letter = {idx: chr(65 + k) for k, idx in enumerate(right)}
        rows = []
        for k in range(len(pairs)):
            g = f'<td class="num-a">{k + 1}</td><td>{inl(pairs[k][0], teacher)}</td>'
            ridx = right[k]
            d = f'<td class="num-a">{chr(65 + k)}</td><td>{inl(pairs[ridx][1], teacher)}</td>'
            rows.append(f'<tr>{g}<td class="sep"></td>{d}</tr>')
        o.append(f'<table class="assoc"><tbody>{"".join(rows)}</tbody></table>')
        if teacher:
            o.append('<p class="solution">Solution : ' + ' · '.join(f'{i + 1} → {letter[i]}' for i in range(len(pairs))) + '</p>')
        else:
            o.append('<p class="reponses-assoc">' + ''.join(f'<span>{i + 1} → <span class="trou" style="min-width:2em"></span></span>' for i in range(len(pairs))) + '</p>')
    elif j['kind'] == 'quiz':
        qs, cur = [], None
        for l in lines:
            s = l.strip()
            if s.startswith('?'):
                cur = {'q': s[1:].strip(), 'opts': []}; qs.append(cur)
            elif s[:1] in '-+' and cur:
                cur['opts'].append((s[1:].strip(), s[0] == '+'))
        items = []
        for q in qs:
            opts = ''.join(f'<li class="{"bon" if ok and teacher else ""}"><span class="case{" coche" if ok and teacher else ""}"></span>{inl(t, teacher)}</li>' for t, ok in q['opts'])
            items.append(f'<li><p class="qq">{inl(q["q"], teacher)}</p><ul class="opts">{opts}</ul></li>')
        o.append(f'<ol class="quiz">{"".join(items)}</ol>')
    elif j['kind'] == 'classe':
        rows = [[c.strip() for c in l.strip().strip('|').split('|')] for l in lines if l.strip().startswith('|')]
        rows = [r for r in rows if not all(re.fullmatch(r':?-{2,}:?', c) for c in r)]
        head, body = rows[0], rows[1:]
        th = ''.join(f'<th>{inl(c, teacher)}</th>' for c in head)
        trs = ''
        for r in body:
            tds = f'<td>{inl(r[0], teacher)}</td>'
            for c in r[1:]:
                mark = c.strip().lower() in ('x', '✓')
                if teacher:
                    tds += f'<td class="cl">{"✓" if mark else (inl(c, teacher) if not mark and c and c.lower() != "x" else "")}</td>'
                else:
                    tds += '<td class="cl"><span class="case"></span></td>'
            trs += f'<tr>{tds}</tr>'
        o.append(f'<table class="classe"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>')
    o.append('</div>')
    return ''.join(o)


# ---------------------------------------------------------------- sheet
def render_sheet(sh, teacher):
    jl = sh['jour']
    o = [f'<section class="fiche" id="f-{sh["num"]}">',
         f'<header><span class="num">Fiche {sh["num"]}</span><h2>{esc(sh["title"])}</h2>'
         f'<span class="chap">{esc(jl)}{" · " + esc(sh["duree"]) if sh["duree"] else ""} · Veille technologique · BTS SIO 2</span></header>']
    objs = ''.join(f'<li>{inl(c.strip(), teacher)}</li>' for c in sh['objectifs'] if c.strip())
    o.append(f'<div class="intro"><div class="accroche">{rich(sh["accroche"], teacher)}</div>'
             f'<div class="objectifs"><h3>Je serai capable de</h3><ul>{objs}</ul></div></div>')
    o.append(f'<div class="bloc notions"><h3 class="titre-bloc"><span class="pic">1</span>Je découvre les notions</h3>{rich(sh["notions"], teacher)}</div>')
    if sh['jeux']:
        o.append(f'<div class="bloc"><h3 class="titre-bloc"><span class="pic">2</span>Je teste mes connaissances</h3>{"".join(jeu(j, teacher) for j in sh["jeux"])}</div>')
    o.append('<div class="bloc"><h3 class="titre-bloc"><span class="pic">3</span>J\'analyse des documents</h3><div class="annexes">')
    for a in sh['annexes']:
        if a['kind'] == 'graphique':
            body = chart(a)
        elif a['kind'] == 'schema':
            body = schema_rows(a['lines'], teacher)
        else:
            body = rich(a['lines'], teacher)
        o.append(f'<div class="annexe"><p class="an-titre"><span>Document {esc(a["n"])}</span>{inl(a["title"], teacher)}</p>{body}'
                 f'<p class="an-source">{esc(a["source"])}</p></div>')
    o.append('</div><ol class="questions">')
    for q in sh['questions']:
        o.append(f'<li><p class="q"><span class="cap">{esc(q["cap"])}</span>{inl(" ".join(l.strip() for l in q["lines"] if l.strip()), teacher)}'
                 f'{"<span class=ann>" + esc(q["ann"]) + "</span>" if q["ann"] else ""}</p>')
        if teacher:
            o.append(f'<div class="ftcor"><p class="c-titre">Corrigé</p>{rich(sh["corriges"][q["n"]], True)}</div>')
        else:
            o.append(answer_zone(q, teacher))
        o.append('</li>')
    o.append('</ol></div>')
    if sh['reflexion']:
        r = sh['reflexion']
        o.append(f'<div class="bloc reflexion"><h3 class="titre-bloc"><span class="pic">4</span>Je réfléchis</h3>{rich(r["lines"], teacher)}')
        if teacher and 'R' in sh['corriges']:
            o.append(f'<div class="ftcor"><p class="c-titre">Pistes de réflexion</p>{rich(sh["corriges"]["R"], True)}</div>')
        o.append(answer_zone(r, teacher) + '</div>')
    if sh['monprojet']:
        p = sh['monprojet']
        o.append(f'<div class="bloc monprojet"><h3 class="titre-bloc"><span class="pic">5</span>J\'avance sur mon dossier de veille</h3>{rich(p["lines"], teacher)}')
        if teacher and 'P' in sh['corriges']:
            o.append(f'<div class="ftcor"><p class="c-titre">Ce que l\'enseignant vérifie</p>{rich(sh["corriges"]["P"], True)}</div>')
        if teacher and p['answer'] and p['answer'][0] == 'tableau':
            o.append(table(p['table'], False, blank=True))
        o.append(answer_zone(p, teacher) + '</div>')
    if sh['retiens']:
        o.append(f'<div class="retiens"><h3>Je retiens</h3>{rich(sh["retiens"], teacher)}</div>')
    o.append('</section>')
    return '\n'.join(o)


def intercalaire(key, j, sheets, teacher):
    items = ''.join(f'<li><span>{s["num"]}</span>{esc(s["title"])}</li>' for s in sheets if s['jour'] == key)
    return (f'<section class="jour"><p class="sur">{esc(key)}</p><h2>{esc(j["title"])}</h2>'
            f'<div class="jour-texte">{rich(j["lines"], teacher)}</div><h3>Les fiches du jour</h3><ol class="jour-liste">{items}</ol></section>')


CSS = open(os.path.join(HERE, 'fiches.css'), encoding='utf8').read() + r'''
.fiche { break-before: page; max-width: 186mm; margin: 0 auto; }
@media screen { .fiche, .jour { padding: 18px 16px 28px; border-bottom: 1px dashed var(--pale); } }
code { font-family: Consolas, monospace; font-size: .92em; background: var(--mist); padding: 0 3px; border-radius: 3px; }
.intro { display: grid; grid-template-columns: 1.6fr 1fr; gap: 3mm; margin-bottom: 3mm; }
.accroche { background: var(--attention); border-radius: 7px; padding: 6px 10px; }
.accroche p { font-size: 10pt; }
.accroche p:first-child::before { content: "Pour commencer · "; font-weight: 700; color: var(--brick); }
.objectifs { background: var(--rappel); border-radius: 7px; padding: 6px 10px; }
.objectifs ul { margin: 0; padding-left: 15px; font-size: 9.4pt; }
.bloc { margin-bottom: 2mm; }
.titre-bloc { font-size: 12.5pt; margin: 3mm 0 2mm; border-bottom: 2px solid var(--amb); padding-bottom: 1mm; display: flex; align-items: center; gap: 7px; break-after: avoid; }
.pic { display: inline-flex; width: 22px; height: 22px; border-radius: 50%; background: var(--amb); color: var(--ink); font-size: 10pt; align-items: center; justify-content: center; font-family: var(--body); }
.notions p { font-size: 10.2pt; text-align: justify; }
.notions table, .annexe table, .questions table, .ftcor table, .monprojet table, .reflexion table { margin: 1mm 0 2mm; break-inside: avoid; }
.encadre { border-radius: 7px; padding: 5px 10px; margin: 1.5mm 0 2.5mm; break-inside: avoid; }
.encadre p { margin: 0; font-size: 9.8pt; }
.enc-titre { font-weight: 700; margin-bottom: .8mm !important; }
.enc-titre span { font-size: 8.2pt; text-transform: uppercase; letter-spacing: .04em; border-radius: 4px; padding: 0 5px; margin-right: 6px; color: #fff; }
.encadre.def { background: var(--rappel); border-left: 4px solid var(--teal); }
.encadre.def .enc-titre span { background: var(--teal); }
.encadre.astuce { background: var(--astuce); border-left: 4px solid var(--green); }
.encadre.astuce .enc-titre span { background: var(--green); }
.encadre.attention { background: var(--attention); border-left: 4px solid var(--brick); }
.encadre.attention .enc-titre span { background: var(--brick); }
.encadre.exemple { background: var(--mist); border-left: 4px solid var(--slate); }
.encadre.exemple .enc-titre span { background: var(--slate); }
.encadre.savoir { background: #f3eefa; border-left: 4px solid #6b4c9a; }
.encadre.savoir .enc-titre span { background: #6b4c9a; }
.jeu { background: var(--mist); border-radius: 8px; padding: 6px 10px; margin-bottom: 2.5mm; break-inside: avoid; }
.jeu-titre { font-weight: 700; color: var(--pet); margin-bottom: 1.5mm !important; }
.jeu-titre span { background: var(--green); color: #fff; border-radius: 4px; padding: 1px 6px; margin-right: 6px; font-size: 8.5pt; text-transform: uppercase; }
.jeu table td { background: #fff !important; }
.vft td.vf { width: 13mm; text-align: center; white-space: nowrap; font-weight: 400; }
.vft td.rep { font-weight: 700; color: var(--brick); width: 14mm; }
.vft td.expl { font-size: 8.8pt; color: var(--ink); width: 42%; }
.vft td.aff, .assoc td, .classe td { font-weight: 400; color: var(--ink); }
.assoc td.num-a { width: 7mm; font-weight: 700; color: var(--teal); text-align: center; }
.assoc td.sep { width: 6mm; background: var(--mist) !important; border: none; }
.reponses-assoc, .solution { font-size: 9.6pt; margin-top: 1.5mm !important; display: flex; flex-wrap: wrap; gap: 4mm; }
.solution { color: var(--brick); font-weight: 700; }
.classe td.cl { text-align: center; width: 18mm; color: var(--brick); font-weight: 700; }
.quiz { margin: 0; padding-left: 18px; display: grid; grid-template-columns: 1fr 1fr; gap: 2mm 6mm; }
.quiz .qq { font-weight: 700; font-size: 9.6pt; margin: 0 0 .5mm; }
.quiz li.bon { color: var(--brick); font-weight: 700; }
.case.coche { background: var(--brick); border-color: var(--brick); }
.annexe { border: 1px solid var(--pale); border-radius: 7px; padding: 6px 10px 4px; margin-bottom: 2.5mm; break-inside: avoid; }
.an-titre { font-weight: 700; color: var(--pet); margin-bottom: 1.5mm; }
.an-titre span { background: var(--pet); color: #fff; border-radius: 4px; padding: 1px 6px; margin-right: 6px; font-size: 9pt; }
.an-source { font-size: 8.4pt; color: var(--slate); font-style: italic; text-align: right; margin: 1mm 0 0; }
.annexe p { font-size: 9.8pt; text-align: justify; }
.graph { width: 100%; max-width: 150mm; height: auto; display: block; margin: 0 auto; }
.schema { display: grid; gap: 2mm; margin: 1.5mm 0 2.5mm; break-inside: avoid; }
.schema-ligne { display: flex; align-items: center; justify-content: center; gap: 1.5mm; flex-wrap: wrap; }
.boite { border: 1.5px solid var(--teal); border-radius: 6px; padding: 4px 7px; font-size: 9.2pt; background: #fff; min-width: 24mm; text-align: center; font-weight: 700; color: var(--pet); }
.boite.vide { border-style: dashed; border-color: var(--amb); min-height: 8mm; min-width: 32mm; }
.boite.remplie { border-color: var(--amb); background: var(--attention); }
.fleche { color: var(--teal); font-weight: 700; font-size: 13pt; }
.questions { padding-left: 20px; margin: 0; }
.questions > li { margin-bottom: 3mm; break-inside: avoid; }
.questions .q { margin: 0 0 1mm; font-size: 10.2pt; }
.cap { display: inline-block; background: var(--amb); color: var(--ink); font-weight: 700; font-size: 8.3pt; border-radius: 4px; padding: 0 5px; margin-right: 6px; text-transform: uppercase; letter-spacing: .03em; }
.ann { color: var(--slate); font-size: 8.8pt; margin-left: 6px; }
.ann::before { content: "("; } .ann::after { content: ")"; }
.lignes div { height: 7.5mm; border-bottom: 1px solid var(--pale); }
table.acompleter td.vide { height: 9.5mm; background: #fff !important; }
.reflexion { border: 1.5px dashed var(--teal); border-radius: 8px; padding: 2px 10px 6px; break-inside: avoid; }
.reflexion p { font-style: italic; font-size: 10.2pt; }
.monprojet { background: #f2f7f1; border: 2px solid var(--green); border-radius: 8px; padding: 2px 10px 6px; break-inside: avoid; }
.monprojet .titre-bloc { border-bottom-color: var(--green); }
.monprojet .pic { background: var(--green); color: #fff; }
.monprojet table.acompleter td.vide { height: 11mm; }
.retiens { border: 2px solid var(--teal); border-radius: 8px; padding: 6px 10px; margin-top: 3mm; break-inside: avoid; }
.retiens p { font-size: 10.2pt; line-height: 1.9; }
.trou { display: inline-block; border-bottom: 1.3px solid var(--ink); height: 1em; vertical-align: baseline; }
.trou.rempli { border-bottom-color: var(--amb); min-width: 0; height: auto; background: var(--attention); padding: 0 3px; font-weight: 700; color: var(--brick); }
.ftcor { background: var(--attention); border-left: 4px solid var(--brick); border-radius: 0 6px 6px 0; padding: 4px 9px; margin: 1mm 0 2mm; font-style: normal; }
.ftcor p { font-size: 9.6pt; font-style: normal; }
.c-titre { font-weight: 700; color: var(--brick); font-size: 8.8pt; text-transform: uppercase; margin-bottom: 1mm !important; }
.jour { break-before: page; max-width: 186mm; margin: 0 auto; padding-top: 30mm; }
.jour .sur { color: var(--amb); font-weight: 700; font-size: 14pt; letter-spacing: .06em; text-transform: uppercase; }
.jour h2 { font-size: 26pt; line-height: 1.15; margin: 2mm 0 6mm; border-bottom: 4px solid var(--amb); padding-bottom: 3mm; }
.jour-texte p { font-size: 11.5pt; text-align: justify; }
.jour-texte table { margin: 2mm 0 4mm; font-size: 10pt; }
.jour h3 { margin-top: 6mm; font-size: 13pt; }
.jour-liste { list-style: none; padding: 0; font-size: 12pt; }
.jour-liste li { display: flex; gap: 8px; align-items: center; margin-bottom: 2mm; }
.jour-liste span { background: var(--pet); color: #fff; border-radius: 12px; padding: 2px 9px; font-weight: 700; font-size: 10pt; }
.err { color: #c00; }
.vf .case, .cl .case { display: inline-block; width: 11px; height: 11px; border: 1.4px solid var(--teal); border-radius: 2px; vertical-align: -1px; margin-right: 2px; transform: none; }
.opts .case { display: inline-block; }
table.acompleter td:first-child { width: 34%; }
'''


def page(title, body):
    return ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{H.escape(title)}</title>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,400;0,700;1,400&family=Bitter:wght@600;700&display=swap">\n'
            f'<style>{CSS}</style>\n</head>\n<body>\n{body}\n</body>\n</html>\n')


def cover(sheets, jours, teacher):
    groups = ''
    for key, j in jours.items():
        items = ''.join(f'<li><a href="#f-{s["num"]}"><span>{s["num"]}</span>{esc(s["title"])}</a></li>' for s in sheets if s['jour'] == key)
        if items:
            groups += f'<li class="grp">{esc(key)} · {esc(j["title"])}</li>{items}'
    who = 'Livret de l\'enseignant · avec corrigés' if teacher else 'Livret de l\'étudiant'
    warn = ('<p class="conseil">Ce livret contient les corrigés, les solutions des jeux et les pistes de réflexion. Il est réservé à l\'enseignant et ne doit pas être déposé dans l\'espace des étudiants.</p>' if teacher else
            '<p class="conseil">Chaque fiche suit le même parcours en cinq temps. Vous découvrez les notions, vous les testez par un petit jeu, vous analysez des documents en répondant à des questions qui vont du repérage à l\'argumentation, vous prenez du recul avec une question de réflexion, puis vous appliquez la notion à votre propre dossier de veille. L\'encadré « Je retiens » se complète en fin de fiche. Les documents sont fictifs, sauf mention contraire : ils suivent Inès et Yanis, deux étudiants de BTS SIO 2 en alternance.</p>')
    nf = len(sheets)
    return ('<section class="couverture"><p class="sur">BTS SIO · deuxième année · Semaine de veille technologique</p>'
            f'<h1>Ma veille technologique<br>en {nf} fiches</h1><p class="chapo">{who}. '
            'Une semaine pour apprendre à surveiller une technologie comme un professionnel : cadrer un sujet lié à votre projet professionnel, trouver des sources fiables, automatiser la collecte, analyser, puis partager ce que vous avez appris. '
            'À la fin de la semaine, votre dossier de veille est lancé ; vous le ferez vivre pendant votre période en entreprise.</p>'
            f'{warn}<ol class="sommaire">{groups}</ol></section>')


COVER_CSS = '.sommaire li.grp { column-span: none; font-weight: 700; color: var(--teal); margin-top: 2mm; break-after: avoid; }'


def to_pdf(html_path, pdf_path, title):
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_path}',
                    'file:///' + os.path.abspath(html_path).replace('\\', '/')], check=True, capture_output=True)
    d = fitz.open(pdf_path)
    d.set_metadata({'title': title, 'author': 'BTS SIO · Veille technologique'})
    d.save(pdf_path + '.tmp', garbage=3, deflate=True); n = d.page_count; d.close(); os.replace(pdf_path + '.tmp', pdf_path)
    return n


def pages_per_sheet(pdf_path, sheets):
    d = fitz.open(pdf_path)
    starts = []
    for s in sheets:
        for p in range(d.page_count):
            if re.search(rf'Fiche {s["num"]}\s', d[p].get_text()) and 'Veille technologique · BTS SIO 2' in d[p].get_text():
                starts.append(p); break
        else:
            starts.append(None)
    out = {}
    for i, s in enumerate(sheets):
        if starts[i] is None:
            out[s['num']] = '?'; continue
        nxt = next((x for x in starts[i + 1:] if x is not None), d.page_count)
        out[s['num']] = nxt - starts[i]
    return out


def build(out_dir, sources=None, base='Livret_Veille_SIO'):
    test = bool(sources)
    sources = sources or sorted(glob.glob(os.path.join(SRC, 'f*.md')))
    jours = parse_jours(os.path.join(SRC, 'jours.md'))
    sheets = []
    for f in sources:
        sheets += parse(open(f, encoding='utf8').read(), f)
    sheets.sort(key=lambda s: s['num'])
    for w in WARN:
        print('  avertissement :', w)
    os.makedirs(out_dir, exist_ok=True)
    res = {}
    for teacher, suffix, label in ((False, 'etudiant', 'étudiant'), (True, 'enseignant', 'enseignant')):
        body = [cover(sheets, jours, teacher)]
        seen = set()
        for s in sheets:
            if s['jour'] not in seen and s['jour'] in jours and not test:
                seen.add(s['jour']); body.append(intercalaire(s['jour'], jours[s['jour']], sheets, teacher))
            body.append(render_sheet(s, teacher))
        hp = os.path.join(out_dir, f'{base}_{suffix}.html')
        open(hp, 'w', encoding='utf8').write(page(f'Veille technologique BTS SIO · livret {label}', '\n'.join(body)).replace('</style>', COVER_CSS + '</style>'))
        pp = os.path.abspath(os.path.join(out_dir, f'{base}_{suffix}.pdf'))
        n = to_pdf(hp, pp, f'Ma veille technologique · livret {label}')
        res[suffix] = (pp, n)
        print(pp, n, 'pages')
        print('  pages par fiche :', pages_per_sheet(pp, sheets))
        if test:
            d = fitz.open(pp)
            for i, p in enumerate(d):
                p.get_pixmap(dpi=60).save(os.path.join(out_dir, f'{suffix}_p{i + 1:02d}.png'))
    return sheets, res


def slug(t):
    import unicodedata
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    return re.sub(r'[^A-Za-z0-9]+', '_', t).strip('_')[:60]


def build_split(out_student, out_teacher):
    """Un PDF par fiche (sans couverture), pour l'étudiant et pour l'enseignant."""
    sheets = []
    for f in sorted(glob.glob(os.path.join(SRC, 'f*.md'))):
        sheets += parse(open(f, encoding='utf8').read(), f)
    sheets.sort(key=lambda s: s['num'])
    for teacher, out, label in ((False, out_student, 'étudiant'), (True, out_teacher, 'enseignant')):
        os.makedirs(out, exist_ok=True)
        for old in glob.glob(os.path.join(out, 'Fiche_*.pdf')):
            os.remove(old)
        for s in sheets:
            name = f'Fiche_{s["num"]}_{slug(s["title"])}' + ('_CORRIGE' if teacher else '')
            hp = os.path.join(out, name + '.html')
            html = page(f'Fiche {s["num"]} · {s["title"]}', render_sheet(s, teacher)).replace('.fiche { break-before: page;', '.fiche { break-before: auto;')
            open(hp, 'w', encoding='utf8').write(html)
            n = to_pdf(hp, os.path.abspath(os.path.join(out, name + '.pdf')), f'Fiche {s["num"]} · {s["title"]} · {label}')
            os.remove(hp)
            print(f'  {label} {name}.pdf {n} p.')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'split':
        build_split(sys.argv[2], sys.argv[3]); sys.exit()
    build(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'out'), sys.argv[2:] or None)
