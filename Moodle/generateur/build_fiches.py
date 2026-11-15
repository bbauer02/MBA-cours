# Builds the revision cards ("fiches de révision") from fiches_veille/fiches_*.md
# into a printable HTML page (one A4 card per page, answer key at the end) and a PDF.
# Usage: python build_fiches.py <out_dir>
import glob, os, re, subprocess, sys, tempfile, unicodedata
from html import escape
import fitz
from frtypo import fr
from fiches_figures import FIGS

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
LETTERS = 'ABCD'


def inl(s):
    return fr(escape(s))


def parse(text):
    cards = []
    for chunk in re.split(r'^# FICHE ', text, flags=re.M)[1:]:
        lines = chunk.rstrip().split('\n')
        num, title, chap = [p.strip() for p in lines[0].split('|')]
        card = {'num': num, 'title': title, 'chap': chap, 'blocks': [], 'qcm': []}
        cur = None
        for ln in lines[1:]:
            if ln.startswith('@'):
                kind, _, arg = ln[1:].partition(' ')
                cur = {'kind': kind, 'arg': arg.strip(), 'lines': []}
                if kind == 'qcm':
                    cur = 'qcm'
                else:
                    card['blocks'].append(cur)
                continue
            if cur == 'qcm':
                if ln.startswith('Q: '):
                    card['qcm'].append({'q': ln[3:], 'opts': [], 'ok': None, 'why': ''})
                elif ln.startswith(('+ ', '- ')):
                    q = card['qcm'][-1]
                    if ln[0] == '+':
                        q['ok'] = len(q['opts'])
                    q['opts'].append(ln[2:])
                elif ln.startswith('E: '):
                    card['qcm'][-1]['why'] = ln[3:]
            elif cur is not None:
                cur['lines'].append(ln)
        for q in card['qcm']:
            assert q['ok'] is not None, (num, q['q'])
        cards.append(card)
    return cards


def paras(lines):
    text = '\n'.join(lines).strip()
    return ''.join(f'<p>{inl(p.strip())}</p>' for p in re.split(r'\n\s*\n', text) if p.strip())


def table(lines):
    rows = [[c.strip() for c in ln.strip().strip('|').split('|')] for ln in lines if ln.strip().startswith('|')]
    rows = [r for r in rows if not all(re.fullmatch(r'-+', c) for c in r)]
    head, body = rows[0], rows[1:]
    h = ''.join(f'<th>{inl(c)}</th>' for c in head)
    b = ''.join('<tr>' + ''.join(f'<td>{inl(c)}</td>' for c in r) + '</tr>' for r in body)
    return f'<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'


BOX = {'rappel': ('Rappel', 'rappel'), 'astuce': ('Astuce', 'astuce'), 'attention': ('Attention', 'attention')}


def render_card(c, renvoi=None):
    out = [f'<section class="fiche" id="fiche-{c["num"]}">',
           f'<header><span class="num">Fiche {c["num"]}</span><h2>{inl(c["title"])}</h2><span class="chap">Cours · chapitre {inl(c["chap"])}</span></header>']
    boxes = []
    for b in c['blocks']:
        k = b['kind']
        if k == 'essentiel':
            out.append(f'<div class="essentiel"><h3>L\'essentiel</h3>{paras(b["lines"])}</div>')
        elif k == 'schema':
            fid, _, title = b['arg'].partition(' ')
            out.append(f'<div class="tab fig"><h3>{inl(title)}</h3>{FIGS[fid]()}</div>')
        elif k == 'tableau':
            out.append(f'<div class="tab"><h3>{inl(b["arg"])}</h3>{table(b["lines"])}</div>')
        elif k in BOX:
            label, cls = BOX[k]
            head = f'{label} · {inl(b["arg"])}' if b['arg'] else label
            boxes.append(f'<aside class="box {cls}"><h4>{head}</h4>{paras(b["lines"])}</aside>')
        elif k == 'reflechir':
            if boxes:
                out.append('<div class="boxes">' + ''.join(boxes) + '</div>'); boxes = []
            out.append(f'<div class="reflechir"><h3>Pour réfléchir</h3>{paras(b["lines"])}<div class="lignes"></div></div>')
    if boxes:
        out.append('<div class="boxes">' + ''.join(boxes) + '</div>')
    qs = []
    for i, q in enumerate(c['qcm'], 1):
        opts = ''.join(f'<li><span class="case"></span><b>{LETTERS[j]}</b> {inl(o)}</li>' for j, o in enumerate(q['opts']))
        qs.append(f'<li><p class="q">{inl(q["q"])}</p><ul class="opts">{opts}</ul></li>')
    out.append(f'<div class="qcm"><h3>QCM · une seule bonne réponse par question</h3><ol>{"".join(qs)}</ol><p class="renvoi">{renvoi or f"Corrigé en fin de livret, fiche {c['num']}."}</p></div>')
    out.append('</section>')
    return '\n'.join(out)


def render_key(cards):
    rows = []
    for c in cards:
        for i, q in enumerate(c['qcm'], 1):
            first = f'<td rowspan="{len(c["qcm"])}" class="kf"><b>{c["num"]}</b> {inl(c["title"])}</td>' if i == 1 else ''
            rows.append(f'<tr>{first}<td class="kq">Q{i}</td><td class="kr">{LETTERS[q["ok"]]}</td><td>{inl(q["why"])}</td></tr>')
    return ('<section class="corrige" id="corrige"><header><span class="num">Corrigés</span><h2>Les réponses des QCM, avec une explication</h2></header>'
            '<table class="key"><thead><tr><th>Fiche</th><th>Question</th><th>Réponse</th><th>Pourquoi</th></tr></thead><tbody>'
            + ''.join(rows) + '</tbody></table></section>')


def render_sommaire(cards):
    items = ''.join(f'<li><a href="#fiche-{c["num"]}"><span>{c["num"]}</span>{inl(c["title"])}</a></li>' for c in cards)
    return ('<section class="couverture"><p class="sur">Cycle Expert en informatique et SI · UE1 · Semaine S1</p>'
            '<h1>Fiches de révision<br>Veille technologique et réglementaire</h1>'
            f'<p class="chapo">{len(cards)} fiches d\'une page, une par notion du cours. Chaque fiche donne l\'essentiel, un tableau, des encadrés « Rappel » qui définissent les mots techniques, une question pour réfléchir et un QCM de trois questions. Les corrigés sont à la fin du livret.</p>'
            '<p class="conseil">Comment s\'en servir : lisez la fiche, cachez-la, faites le QCM, puis vérifiez avec le corrigé. Le cours complet reste la référence, et les consignes du dossier D1 font foi.</p>'
            f'<ol class="sommaire">{items}<li><a href="#corrige"><span>✓</span>Corrigés des QCM</a></li></ol></section>')


CSS = open(os.path.join(HERE, 'fiches_veille', 'fiches.css'), encoding='utf8').read()


def page_html(title, body):
    return ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{escape(title)}</title>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,400;0,700;1,400&family=Bitter:wght@600;700&display=swap">\n'
            f'<style>{CSS}</style>\n</head>\n<body>\n{body}\n</body>\n</html>\n')


def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^A-Za-z0-9]+', '_', s).strip('_')[:50]


def print_pdf(html_path, pdf_path):
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_path}',
                    'file:///' + os.path.abspath(html_path).replace('\\', '/')], check=True, capture_output=True)


def build_split(cards, out_dir):
    # one PDF per card: the card on page 1, its own answer key on page 2 (print recto-verso)
    os.makedirs(out_dir, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for c in cards:
            h = os.path.join(tmp, f'{c["num"]}.html')
            open(h, 'w', encoding='utf8').write(page_html(f'Fiche {c["num"]} · {c["title"]}', render_card(c, 'Corrigé au verso.') + render_key([c])))
            pdf = os.path.abspath(os.path.join(out_dir, f'Fiche_{c["num"]}_{slug(c["title"])}.pdf'))
            print_pdf(h, pdf)
            doc = fitz.open(pdf)
            doc.set_metadata({'title': f'Fiche {c["num"]} · {c["title"]}', 'author': '3W Academy · Cycle Expert en informatique et SI'})
            doc.save(pdf + '.tmp', garbage=3, deflate=True); n = doc.page_count; doc.close(); os.replace(pdf + '.tmp', pdf)
            print(os.path.basename(pdf), n, 'pages')


def build(out_dir):
    text = ''.join(open(f, encoding='utf8').read() + '\n' for f in sorted(glob.glob(os.path.join(HERE, 'fiches_veille', 'fiches_*.md'))))
    cards = parse(text)
    body = render_sommaire(cards) + '\n'.join(render_card(c) for c in cards) + render_key(cards)
    html = page_html('Fiches de révision · Veille S1', body)
    os.makedirs(out_dir, exist_ok=True)
    page = os.path.join(out_dir, 'Fiches_revision_Veille_S1.html')
    open(page, 'w', encoding='utf8').write(html)
    pdf = os.path.abspath(os.path.join(out_dir, 'Fiches_revision_Veille_S1.pdf'))
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf}',
                    'file:///' + os.path.abspath(page).replace('\\', '/')], check=True, capture_output=True)
    doc = fitz.open(pdf)
    # one bookmark per card: find the page whose text contains "Fiche NN"
    toc = []
    for c in cards:
        for pg in range(doc.page_count):
            if f'Fiche {c["num"]}' in doc[pg].get_text() and doc[pg].get_text().find(c['title'][:20]) >= 0:
                toc.append([1, f'Fiche {c["num"]} · {c["title"]}', pg + 1]); break
    for pg in range(doc.page_count):
        if 'Les réponses des QCM' in doc[pg].get_text():
            toc.append([1, 'Corrigés des QCM', pg + 1]); break
    doc.set_toc(toc)
    doc.set_metadata({'title': 'Fiches de révision · Veille technologique et réglementaire', 'author': '3W Academy · Cycle Expert en informatique et SI'})
    doc.save(pdf + '.tmp', garbage=3, deflate=True); n = doc.page_count; doc.close(); os.replace(pdf + '.tmp', pdf)
    print(page); print(pdf, n, 'pages,', len(cards), 'fiches,', sum(len(c['qcm']) for c in cards), 'questions')
    build_split(cards, os.path.join(out_dir, 'Fiches_une_par_fichier'))
    return cards


if __name__ == '__main__':
    build(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'out_fiches'))
