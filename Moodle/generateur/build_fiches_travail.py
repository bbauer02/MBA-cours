# Builds the S2 worksheets ("fiches de travail", STMG textbook style) from fiches_travail_s2/ft_*.md:
# a student booklet (answer lines, blank tables, gaps) and a teacher booklet (same sheets + answer keys).
# Usage: python build_fiches_travail.py <out_dir> [source.md ...]
#   with no source: every fiches_travail_s2/ft_*.md, booklets named Fiches_travail_S2_eleve / _enseignant
#   with sources: test build of those files only, plus one PNG per page for checking
import glob, html as H, os, re, subprocess, sys
import fitz
from frtypo import fr
import drawio_schema

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'fiches_travail_s2')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
GAP = re.compile(r'\[\[(.+?)\]\]')


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
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', ''.join(out))


# ---------------------------------------------------------------- parsing
def parse(text, path):
    sheets = []
    for chunk in re.split(r'^# FT ', text, flags=re.M)[1:]:
        lines = chunk.rstrip().split('\n')
        try:
            num, title, chap = [p.strip() for p in lines[0].split('|')]
        except ValueError:
            raise SystemExit(f'{path} : en-tête de fiche mal formé : « # FT {lines[0]} »')
        sh = {'num': num, 'title': title, 'chap': chap, 'situation': [], 'capacites': [], 'duree': '', 'annexes': [],
              'questions': [], 'retiens': [], 'corriges': {}}
        cur = None
        for ln in lines[1:]:
            if ln.startswith('@'):
                kind, _, arg = ln[1:].partition(' ')
                arg = arg.strip()
                if kind == 'situation': cur = sh['situation']
                elif kind == 'capacites': cur = sh['capacites']
                elif kind == 'retiens': cur = sh['retiens']
                elif kind == 'duree': sh['duree'] = arg; cur = None
                elif kind == 'annexe':
                    n, t, src = ([p.strip() for p in arg.split('|')] + ['', ''])[:3]
                    a = {'n': n, 'title': t, 'source': src, 'kind': 'texte', 'lines': [], 'opt': ''}
                    sh['annexes'].append(a); cur = a['lines']
                elif kind in ('graphique', 'schema'):
                    if not sh['annexes']:
                        raise SystemExit(f'{path} fiche {num} : @{kind} hors annexe')
                    sh['annexes'][-1]['kind'] = kind; sh['annexes'][-1]['opt'] = arg
                elif kind == 'question':
                    n, cap, ann = ([p.strip() for p in arg.split('|')] + ['', ''])[:3]
                    q = {'n': n, 'cap': cap, 'ann': ann, 'lines': [], 'answer': None, 'table': []}
                    sh['questions'].append(q); cur = q['lines']
                elif kind == 'lignes':
                    sh['questions'][-1]['answer'] = ('lignes', int(arg or 4)); cur = None
                elif kind == 'tableau':
                    q = sh['questions'][-1]; q['answer'] = ('tableau', 0); cur = q['table']
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
        if not (3 <= len(sh['annexes']) <= 5):
            print(f'  avertissement : fiche {num} : {len(sh["annexes"])} annexes (3 à 5 attendues)')
        if not (6 <= len(sh['questions']) <= 9):
            print(f'  avertissement : fiche {num} : {len(sh["questions"])} questions (6 à 9 attendues)')
        sheets.append(sh)
    return sheets


# ---------------------------------------------------------------- rendering helpers
def paras(lines, teacher):
    text = '\n'.join(lines).strip()
    out = []
    for block in re.split(r'\n\s*\n', text):
        if not block.strip():
            continue
        if block.lstrip().startswith('|'):
            out.append(table(block.split('\n'), teacher))
        else:
            out.append(f'<p>{inl(" ".join(l.strip() for l in block.split(chr(10))), teacher)}</p>')
    return ''.join(out)


def table(lines, teacher, blank=False):
    rows = [[c.strip() for c in l.strip().strip('|').split('|')] for l in lines if l.strip().startswith('|')]
    rows = [r for r in rows if not all(re.fullmatch(r':?-{2,}:?', c) for c in r)]
    if not rows:
        return ''
    head, body = rows[0], rows[1:]
    th = ''.join(f'<th>{inl(c, teacher)}</th>' for c in head)
    trs = ''.join('<tr>' + ''.join(f'<td class="{"vide" if blank and not c else ""}">{inl(c, teacher)}</td>' for c in r) + '</tr>' for r in body)
    return f'<table class="{"acompleter" if blank else ""}"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>'


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
    W, Hh, L, R, T, B = 640, 250, 56, 16, 18, 52
    vmax = max(v for _, v in pts) or 1
    step = 10 ** len(str(int(vmax))) / 10
    top = (int(vmax / step) + 1) * step
    pw, ph = W - L - R, Hh - T - B
    g = [f'<svg viewBox="0 0 {W} {Hh}" class="graph" xmlns="http://www.w3.org/2000/svg" font-family="Source Sans 3, Calibri, sans-serif">']
    for i in range(5):
        y = T + ph - ph * i / 4; val = top * i / 4
        g.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W - R}" y2="{y:.1f}" stroke="#d5dfdd" stroke-width="1"/>')
        lab = f'{val:,.0f}'.replace(',', '\u202f') if top >= 10 else f'{val:.1f}'.replace('.', ',')
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
        lab = H.escape(k)
        g.append(f'<text x="{cx:.1f}" y="{T + ph + 16}" font-size="11" text-anchor="middle" fill="#1b2a33">{lab[:16]}</text>')
        if len(lab) > 16:
            g.append(f'<text x="{cx:.1f}" y="{T + ph + 29}" font-size="11" text-anchor="middle" fill="#1b2a33">{lab[16:32]}</text>')
    if kind == 'lignes':
        g.append('<polyline fill="none" stroke="#1f6f78" stroke-width="2.5" points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in coords) + '"/>')
        g += [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#e09f3e"/>' for x, y in coords]
    g.append(f'<line x1="{L}" y1="{T + ph}" x2="{W - R}" y2="{T + ph}" stroke="#5e6b78"/>')
    if unit:
        g.append(f'<text x="{L}" y="{T - 6}" font-size="11" fill="#5e6b78">{H.escape(fr(unit))}</text>')
    g.append('</svg>')
    return ''.join(g)


def schema(a, teacher, num):
    return drawio_schema.render(a['lines'], teacher, os.path.join(SRC, 'schemas'), f'FT{num}_annexe{a["n"]}')


def render_sheet(sh, teacher):
    o = [f'<section class="ft" id="ft-{sh["num"]}">',
         f'<header><span class="num">Fiche de travail {sh["num"]}</span><h2>{esc(sh["title"])}</h2>'
         f'<span class="chap">Cours · chapitre {esc(sh["chap"])}{" · " + esc(sh["duree"]) if sh["duree"] else ""} · Kestrel Logistique</span></header>']
    caps = ''.join(f'<li>{esc(c.strip())}</li>' for c in sh['capacites'] if c.strip())
    o.append(f'<div class="intro"><div class="situation"><h3>Situation</h3>{paras(sh["situation"], teacher)}</div>'
             f'<div class="capacites"><h3>Capacités travaillées</h3><ul>{caps}</ul></div></div>')
    o.append('<h3 class="titre-bloc">Dossier documentaire</h3><div class="annexes">')
    for a in sh['annexes']:
        if a['kind'] == 'graphique':
            body = chart(a)
        elif a['kind'] == 'schema':
            body = schema(a, teacher, sh['num'])
        else:
            body = paras(a['lines'], teacher)
        o.append(f'<div class="annexe"><p class="an-titre"><span>Annexe {esc(a["n"])}</span>{esc(a["title"])}</p>{body}'
                 f'<p class="an-source">{esc(a["source"])}</p></div>')
    o.append('</div><h3 class="titre-bloc">Questions</h3><ol class="questions">')
    for q in sh['questions']:
        o.append(f'<li><p class="q"><span class="cap">{esc(q["cap"])}</span>{inl(" ".join(l.strip() for l in q["lines"] if l.strip()), teacher)}'
                 f'<span class="ann">{esc(q["ann"])}</span></p>')
        if teacher:
            o.append(f'<div class="ftcor"><p class="c-titre">Corrigé</p>{paras(sh["corriges"][q["n"]], True)}</div>')
        elif q['answer'] and q['answer'][0] == 'lignes':
            o.append('<div class="lignes">' + '<div></div>' * q['answer'][1] + '</div>')
        elif q['answer'] and q['answer'][0] == 'tableau':
            o.append(table(q['table'], False, blank=True))
        o.append('</li>')
    o.append('</ol>')
    if sh['retiens']:
        o.append(f'<div class="retiens"><h3>Je retiens</h3>{paras(sh["retiens"], teacher)}</div>')
    o.append('</section>')
    return '\n'.join(o)


CSS = open(os.path.join(HERE, 'fiches_veille', 'fiches.css'), encoding='utf8').read() + r'''
.ft { break-before: page; max-width: 186mm; margin: 0 auto; }
@media screen { .ft { padding: 18px 16px 28px; border-bottom: 1px dashed var(--pale); } }
.intro { display: grid; grid-template-columns: 1.7fr 1fr; gap: 3mm; margin-bottom: 3mm; }
.situation { background: var(--mist); border-radius: 7px; padding: 6px 10px; }
.capacites { background: var(--rappel); border-radius: 7px; padding: 6px 10px; }
.capacites ul { margin: 0; padding-left: 15px; font-size: 9.4pt; }
.situation p { font-size: 10pt; }
.titre-bloc { font-size: 12pt; margin: 3mm 0 2mm; border-bottom: 2px solid var(--amb); padding-bottom: 1mm; }
.annexe { border: 1px solid var(--pale); border-radius: 7px; padding: 6px 10px 4px; margin-bottom: 2.5mm; break-inside: avoid; }
.an-titre { font-weight: 700; color: var(--pet); margin-bottom: 1.5mm; }
.an-titre span { background: var(--pet); color: #fff; border-radius: 4px; padding: 1px 6px; margin-right: 6px; font-size: 9pt; }
.an-source { font-size: 8.4pt; color: var(--slate); font-style: italic; text-align: right; margin: 1mm 0 0; }
.annexe p { font-size: 9.8pt; text-align: justify; }
.annexe table, .questions table, .ftcor table { margin: 1mm 0 1.5mm; }
.graph { width: 100%; max-width: 150mm; height: auto; display: block; margin: 0 auto; }
.schema { display: grid; gap: 2mm; margin: 1.5mm 0; }
.schema-ligne { display: flex; align-items: center; justify-content: center; gap: 1.5mm; flex-wrap: wrap; }
.boite { border: 1.5px solid var(--teal); border-radius: 6px; padding: 4px 7px; font-size: 9.2pt; background: #fff; min-width: 26mm; text-align: center; font-weight: 700; color: var(--pet); }
.boite.vide { border-style: dashed; border-color: var(--amb); min-height: 8mm; min-width: 34mm; }
.boite.remplie { border-color: var(--amb); background: var(--attention); }
.schema-drawio { margin: 2mm auto 1mm; } .schema-drawio svg { width: 100%; height: auto; display: block; }
.questions { padding-left: 20px; margin: 0; }
.questions > li { margin-bottom: 3mm; break-inside: avoid; }
.questions .q { margin: 0 0 1mm; font-size: 10.2pt; }
.cap { display: inline-block; background: var(--amb); color: var(--ink); font-weight: 700; font-size: 8.3pt; border-radius: 4px; padding: 0 5px; margin-right: 6px; text-transform: uppercase; letter-spacing: .03em; }
.ann { color: var(--slate); font-size: 8.8pt; margin-left: 6px; }
.ann::before { content: "("; } .ann::after { content: ")"; }
.lignes div { height: 7.5mm; border-bottom: 1px solid var(--pale); }
table.acompleter td.vide { height: 9.5mm; background: #fff !important; }
.retiens { border: 2px solid var(--teal); border-radius: 8px; padding: 6px 10px; margin-top: 3mm; break-inside: avoid; }
.retiens p { font-size: 10.2pt; line-height: 1.9; }
.trou { display: inline-block; border-bottom: 1.3px solid var(--ink); height: 1em; vertical-align: baseline; }
.trou.rempli { border-bottom-color: var(--amb); min-width: 0; height: auto; background: var(--attention); padding: 0 3px; font-weight: 700; color: var(--brick); }
.ftcor { background: var(--attention); border-left: 4px solid var(--brick); border-radius: 0 6px 6px 0; padding: 4px 9px; margin: 1mm 0 2mm; }
.ftcor p { font-size: 9.6pt; }
.c-titre { font-weight: 700; color: var(--brick); font-size: 8.8pt; text-transform: uppercase; margin-bottom: 1mm !important; }
.couv-ft { max-width: 186mm; margin: 0 auto; }
.err { color: #c00; }
'''


def page(title, body):
    return ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{H.escape(title)}</title>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,400;0,700;1,400&family=Bitter:wght@600;700&display=swap">\n'
            f'<style>{CSS}</style>\n</head>\n<body>\n{body}\n</body>\n</html>\n')


def cover(sheets, teacher):
    items = ''.join(f'<li><a href="#ft-{s["num"]}"><span>{s["num"]}</span>{esc(s["title"])}</a></li>' for s in sheets)
    who = 'Livret de l\'enseignant · avec corrigés' if teacher else 'Livret de l\'apprenant'
    warn = ('<p class="conseil">Ce livret contient les corrigés : il est réservé à l\'équipe pédagogique et ne doit pas être déposé dans l\'espace des apprenants.</p>' if teacher else
            '<p class="conseil">Chaque fiche se fait en atelier, seul ou à deux, en 45 à 75 minutes. Lisez la situation, parcourez le dossier documentaire, puis répondez dans l\'ordre : les questions vont du repérage à l\'argumentation. Les documents sont fictifs ; ils prolongent l\'exemple de Kestrel Logistique du cours. Le cours et les consignes du dossier D2 restent la référence.</p>')
    return ('<section class="couverture"><p class="sur">Cycle Expert en informatique et SI · UE2 · Semaine S2</p>'
            f'<h1>Fiches de travail<br>Systèmes d\'information, cartographie et risques</h1><p class="chapo">{who}. '
            f'{len(sheets)} fiches, une par notion clé du cours, construites comme des fiches de manuel : une situation chez Kestrel Logistique, un dossier documentaire, des questions progressives et une synthèse à compléter.</p>'
            f'{warn}<ol class="sommaire">{items}</ol></section>')


def to_pdf(html_path, pdf_path, title):
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_path}',
                    'file:///' + os.path.abspath(html_path).replace('\\', '/')], check=True, capture_output=True)
    d = fitz.open(pdf_path)
    d.set_metadata({'title': title, 'author': '3W Academy · Cycle Expert en informatique et SI'})
    d.save(pdf_path + '.tmp', garbage=3, deflate=True); n = d.page_count; d.close(); os.replace(pdf_path + '.tmp', pdf_path)
    return n


def pages_per_sheet(pdf_path, sheets):
    d = fitz.open(pdf_path)
    starts = []
    for s in sheets:
        for p in range(d.page_count):
            if f'Fiche de travail {s["num"]}' in d[p].get_text():
                starts.append(p); break
    starts.append(d.page_count)
    return {s['num']: starts[i + 1] - starts[i] for i, s in enumerate(sheets)}


def build(out_dir, sources=None, base='Fiches_travail_S2'):
    test = bool(sources)
    sources = sources or sorted(glob.glob(os.path.join(SRC, 'ft_*.md')))
    sheets = []
    for f in sources:
        sheets += parse(open(f, encoding='utf8').read(), f)
    sheets.sort(key=lambda s: s['num'])
    os.makedirs(out_dir, exist_ok=True)
    res = {}
    for teacher, suffix, label in ((False, 'eleve', 'apprenant'), (True, 'enseignant', 'enseignant')):
        body = cover(sheets, teacher) + '\n'.join(render_sheet(s, teacher) for s in sheets)
        hp = os.path.join(out_dir, f'{base}_{suffix}.html')
        open(hp, 'w', encoding='utf8').write(page(f'Fiches de travail S2 · {label}', body))
        pp = os.path.abspath(os.path.join(out_dir, f'{base}_{suffix}.pdf'))
        n = to_pdf(hp, pp, f'Fiches de travail S2 · livret {label}')
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
    """One PDF per worksheet: student version (no answer keys) and teacher version (_CORRIGE)."""
    sheets = []
    for f in sorted(glob.glob(os.path.join(SRC, 'ft_*.md'))):
        sheets += parse(open(f, encoding='utf8').read(), f)
    sheets.sort(key=lambda s: s['num'])
    for d in (out_student, out_teacher):
        os.makedirs(d, exist_ok=True)
        for old in glob.glob(os.path.join(d, 'FT_*.pdf')):
            os.remove(old)
    for teacher, d, suf in ((False, out_student, ''), (True, out_teacher, '_CORRIGE')):
        for s in sheets:
            name = f'FT_{s["num"]}_{slug(s["title"])}{suf}'
            hp = os.path.join(d, name + '.html')
            label = f'Fiche de travail {s["num"]} · {s["title"]}' + (' · corrigé' if teacher else '')
            open(hp, 'w', encoding='utf8').write(page(label, render_sheet(s, teacher)))
            n = to_pdf(hp, os.path.abspath(os.path.join(d, name + '.pdf')), label)
            os.remove(hp)
            print(name, n, 'pages')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'split':
        build_split(sys.argv[2], sys.argv[3]); sys.exit()
    build(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'out_ft'), sys.argv[2:] or None)
