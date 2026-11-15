# Builds the S2 course cards ("fiches de cours et d'étude") from fiches_s2/fiches_*.md.
# Same card format as the S1 revision cards, plus a study part on its own page:
#   @document <nature et source>   the text to study (article, case, interview, official extract)
#   @questions                      numbered reflection questions (printed with writing lines)
#   @pistes                         answer leads for the questions (printed in the answer key only)
# Each card = recto (the lesson) + verso (the study and the QCM); answer key at the end.
# Usage: python build_fiches_s2.py <out_dir>
import glob, os, re, subprocess, sys, tempfile
import fitz
from build_fiches import parse, paras, table, inl, slug, LETTERS, BOX, CHROME, HERE
try:
    from fiches_figures_s2 import FIGS
except ImportError:
    FIGS = {}

TITLE = 'Fiches de cours · Systèmes d\'information, cartographie et risques'
CSS = open(os.path.join(HERE, 'fiches_veille', 'fiches.css'), encoding='utf8').read() + open(os.path.join(HERE, 'fiches_s2', 'fiches_s2.css'), encoding='utf8').read()


def numbered(lines):
    items = [re.sub(r'^\d+[.)]\s*', '', l.strip()) for l in lines if l.strip()]
    return '<ol class="questions">' + ''.join(f'<li><p>{inl(q)}</p><div class="lignes"></div><div class="lignes"></div></li>' for q in items) + '</ol>'


def render_card(c, renvoi=None):
    out = [f'<section class="fiche" id="fiche-{c["num"]}">',
           f'<header><span class="num">Fiche {c["num"]}</span><h2>{inl(c["title"])}</h2><span class="chap">Cours · chapitre {inl(c["chap"])}</span></header>']
    boxes, etude = [], []
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
        elif k == 'document':
            etude.append(f'<div class="document"><p class="source">{inl(b["arg"])}</p>{paras(b["lines"])}</div>')
        elif k == 'questions':
            etude.append(f'<div class="reflexion"><h3>Questions de réflexion</h3>{numbered(b["lines"])}</div>')
    if boxes:
        out.append('<div class="boxes">' + ''.join(boxes) + '</div>')
    qs = []
    for i, q in enumerate(c['qcm'], 1):
        opts = ''.join(f'<li><span class="case"></span><b>{LETTERS[j]}</b> {inl(o)}</li>' for j, o in enumerate(q['opts']))
        qs.append(f'<li><p class="q">{inl(q["q"])}</p><ul class="opts">{opts}</ul></li>')
    qcm = f'<div class="qcm"><h3>QCM · une seule bonne réponse par question</h3><ol>{"".join(qs)}</ol><p class="renvoi">{renvoi or f"Corrigé en fin de livret, fiche {c['num']}."}</p></div>'
    out.append(f'<div class="etude"><p class="etude-titre">Fiche {c["num"]} · Étude de document</p>{"".join(etude)}{qcm}</div>')
    out.append('</section>')
    return '\n'.join(out)


def render_key(cards, single=False):
    blocks = []
    for c in cards:
        rows = ''.join(f'<tr><td class="kq">Q{i}</td><td class="kr">{LETTERS[q["ok"]]}</td><td>{inl(q["why"])}</td></tr>' for i, q in enumerate(c['qcm'], 1))
        pistes = next((b['lines'] for b in c['blocks'] if b['kind'] == 'pistes'), [])
        blocks.append(f'<div class="cle"><h3><span>{c["num"]}</span>{inl(c["title"])}</h3>'
                      f'<table class="key"><thead><tr><th>Question</th><th>Réponse</th><th>Pourquoi</th></tr></thead><tbody>{rows}</tbody></table>'
                      f'<div class="pistes"><h4>Pistes pour les questions de réflexion</h4>{numbered_plain(pistes)}</div></div>')
    head = 'Corrigé' if single else 'Corrigés'
    return (f'<section class="corrige" id="corrige"><header><span class="num">{head}</span><h2>Les réponses des QCM et des pistes pour les questions de réflexion</h2></header>'
            '<p class="avert">Les pistes ne sont pas des corrigés types : d\'autres réponses sont recevables si elles sont argumentées et appuyées sur le document.</p>'
            + ''.join(blocks) + '</section>')


def numbered_plain(lines):
    items = [re.sub(r'^\d+[.)]\s*', '', l.strip()) for l in lines if l.strip()]
    return '<ol>' + ''.join(f'<li>{inl(p)}</li>' for p in items) + '</ol>'


def render_sommaire(cards):
    items = ''.join(f'<li><a href="#fiche-{c["num"]}"><span>{c["num"]}</span>{inl(c["title"])}</a></li>' for c in cards)
    return ('<section class="couverture"><p class="sur">Cycle Expert en informatique et SI · UE2 · Semaine S2</p>'
            '<h1>Fiches de cours<br>Systèmes d\'information, cartographie et risques</h1>'
            f'<p class="chapo">{len(cards)} fiches de deux pages, une par notion du cours. Le recto donne l\'essentiel, un tableau ou un schéma et des encadrés « Rappel » qui définissent les mots techniques. '
            'Le verso propose une étude de document (un article, un cas, un entretien ou un extrait de guide officiel), des questions de réflexion et un QCM de trois questions. '
            'Les corrigés des QCM et des pistes pour les questions sont à la fin du livret.</p>'
            '<p class="conseil">Comment s\'en servir : lisez le recto, puis faites l\'étude sans le regarder ; rédigez vos réponses en quelques lignes avant de lire les pistes. Le cours complet reste la référence, et les consignes du dossier D2 font foi. '
            'Les documents signalés comme fictifs ont été écrits pour le cours ; les cas réels sont résumés à partir des sources indiquées.</p>'
            f'<ol class="sommaire">{items}<li><a href="#corrige"><span>✓</span>Corrigés et pistes</a></li></ol></section>')


def page_html(title, body):
    return ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{title}</title>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,400;0,700;1,400&family=Bitter:wght@600;700&display=swap">\n'
            f'<style>{CSS}</style>\n</head>\n<body>\n{body}\n</body>\n</html>\n')


def print_pdf(html_path, pdf_path):
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_path}',
                    'file:///' + os.path.abspath(html_path).replace('\\', '/')], check=True, capture_output=True)


def finish(pdf, title, toc=None):
    doc = fitz.open(pdf)
    if toc:
        doc.set_toc(toc)
    doc.set_metadata({'title': title, 'author': '3W Academy · Cycle Expert en informatique et SI'})
    doc.save(pdf + '.tmp', garbage=3, deflate=True); n = doc.page_count; doc.close(); os.replace(pdf + '.tmp', pdf)
    return n


def build(out_dir, base='Fiches_cours_S2'):
    text = ''.join(open(f, encoding='utf8').read() + '\n' for f in sorted(glob.glob(os.path.join(HERE, 'fiches_s2', 'fiches_*.md'))))
    cards = parse(text)
    os.makedirs(out_dir, exist_ok=True)
    page = os.path.join(out_dir, base + '.html')
    open(page, 'w', encoding='utf8').write(page_html(TITLE, render_sommaire(cards) + '\n'.join(render_card(c) for c in cards) + render_key(cards)))
    pdf = os.path.abspath(os.path.join(out_dir, base + '.pdf'))
    print_pdf(page, pdf)
    doc = fitz.open(pdf)
    toc = []
    for c in cards:
        for pg in range(doc.page_count):
            t = doc[pg].get_text()
            if f'Fiche {c["num"]}' in t and c['title'][:20] in t:
                toc.append([1, f'Fiche {c["num"]} · {c["title"]}', pg + 1]); break
    for pg in range(doc.page_count):
        if 'Les réponses des QCM et des pistes' in doc[pg].get_text():
            toc.append([1, 'Corrigés et pistes', pg + 1]); break
    doc.close()
    n = finish(pdf, TITLE, toc)
    print(page); print(pdf, n, 'pages,', len(cards), 'fiches,', sum(len(c['qcm']) for c in cards), 'questions de QCM')
    split = os.path.join(out_dir, base + '_une_par_fichier')
    os.makedirs(split, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for c in cards:
            h = os.path.join(tmp, f'{c["num"]}.html')
            open(h, 'w', encoding='utf8').write(page_html(f'Fiche {c["num"]} · {c["title"]}', render_card(c, 'Corrigé en dernière page.') + render_key([c], single=True)))
            p = os.path.abspath(os.path.join(split, f'Fiche_{c["num"]}_{slug(c["title"])}.pdf'))
            print_pdf(h, p)
            print(os.path.basename(p), finish(p, f'Fiche {c["num"]} · {c["title"]}'), 'pages')
    return cards


if __name__ == '__main__':
    build(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'out_fiches_s2'))
