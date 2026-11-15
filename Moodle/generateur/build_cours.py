# Builds the Moodle-ready HTML course from cours_veille/chapitres/*.md (same look as the Medisecure page).
# Usage: python build_cours.py <chapters_dir> <output.html> [pdf_url]
import base64, glob, os, re, sys
from html import escape
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from frtypo import fr
import cours_figures
try:
    import cours_figures_s2
    cours_figures.FIGS.update(cours_figures_s2.FIGS)
except ImportError:
    pass

INK = '#1f2933'; QUIET = '#5f6b76'; ACC = '#0b7285'; DARK = '#0b4f6c'; LINE = '#dde3e8'; SOFT = '#f4f7f9'; ZEBRA = '#e6f1f4'
FONT = "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
CALLOUTS = {  # label, accent, background
    'OBJECTIFS': ('Objectifs du chapitre', '#0b7285', '#e3f2f4'),
    'EXEMPLE': ('Exemple travaillé · Kestrel Logistique', '#364fc7', '#edf2ff'),
    'EXERCICE': ('Exercice · Medisecure', '#d9480f', '#fff4e6'),
    'METHODE': ('Méthode', '#2b8a3e', '#ebfbee'),
    'ATTENTION': ('Attention', '#c92a2a', '#fff5f5'),
    'DOSSIER': ('Pour votre dossier D1', '#5f3dc4', '#f3f0ff'),
    'DEFINITION': ('Définition', '#0b4f6c', '#eef4f8'),
    'ETUDE': ('Étude de document', '#8a5a00', '#fff9db'),
    'FICHE': ('Fiche de travail · à réaliser maintenant', '#087f5b', '#e6fcf5'),
}

src_dir, out = sys.argv[1], sys.argv[2]
PDF_URL = sys.argv[3] if len(sys.argv) > 3 else None

# Optional course metadata (meta.json next to the chapters folder); defaults = S1 veille course.
import json
META = {'kicker': '3W Academy · Cycle Expert en informatique et SI · Semaine S1',
        'title': 'La veille technologique et réglementaire',
        'subtitle': 'Cours et guide de travail en autonomie pour le dossier D1',
        'intro': "Ce cours accompagne la semaine S1, puis les trois semaines d'intersession en entreprise. "
                 "Il donne les méthodes, les outils et les repères réglementaires pour concevoir, faire vivre et exploiter un dispositif de veille au service de Medisecure.",
        'page_title': 'La veille technologique et réglementaire – Cours S1',
        'dossier_label': 'Pour votre dossier D1',
        'hide_callouts': ['DEFINITION', 'ETUDE']}
_meta_path = os.path.join(os.path.dirname(os.path.abspath(os.path.normpath(src_dir))), 'meta.json')
if os.path.exists(_meta_path):
    META.update(json.load(open(_meta_path, encoding='utf8')))
CALLOUTS['DOSSIER'] = (META['dossier_label'],) + CALLOUTS['DOSSIER'][1:]
LEGEND = {k: v for k, v in CALLOUTS.items() if k not in META['hide_callouts']}


def links(h):
    # bare URLs become links; trailing punctuation stays outside
    return re.sub(r'(https?://[^\s<>«»]+?)([.,;)]?(?=\s|$|<|&nbsp;| ))',
                  lambda m: f'<a href="{m.group(1)}" style="color:{ACC};word-break:break-all;">{m.group(1)}</a>{m.group(2)}', h)


def inl(s):
    parts = re.split(r'(\*\*[^*]+\*\*)', s)
    return links(''.join(f'<strong>{escape(fr(p[2:-2]))}</strong>' if p.startswith('**') else escape(fr(p)) for p in parts))


def table(rows):
    head, body = rows[0], rows[1:]
    wide = len(head) >= 7  # many columns: fixed layout and smaller type so the table fits the page
    fs, pad = ('12px', '6px 6px') if wide else ('14px', '8px 11px')
    layout = ''
    th = ''.join(f'<th style="text-align:left;vertical-align:bottom;padding:{pad};background:{DARK};color:#ffffff;font-weight:600;font-size:{"11.5px" if wide else "13px"};">{inl(c)}</th>' for c in head)
    trs = ''
    for i, r in enumerate(body):
        bg = '#ffffff' if i % 2 == 0 else ZEBRA
        tds = ''.join(f'<td style="vertical-align:top;padding:{pad};border-bottom:1px solid {LINE};{"font-weight:600;" if j == 0 else ""}">{inl(c)}</td>' for j, c in enumerate(r))
        trs += f'<tr style="background:{bg};">{tds}</tr>'
    return (f'<div style="overflow-x:auto;margin:14px 0 20px 0;border:1px solid {LINE};border-radius:8px;">'
            f'<table style="width:100%;border-collapse:collapse;{layout}font-size:{fs};line-height:1.45;color:{INK};"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>')


def figure(fid, title, desc):
    svg = cours_figures.FIGS.get(fid)
    if svg is None:
        return (f'<div style="margin:18px 0;padding:16px;border:2px dashed #c92a2a;border-radius:10px;color:#c92a2a;font-size:13px;">'
                f'Figure à dessiner : {escape(fid)} · {escape(title)} · {escape(desc)}</div>')
    data = base64.b64encode(svg().encode('utf8')).decode('ascii')
    return (f'<div style="margin:18px 0 22px 0;padding:12px;border:1px solid {LINE};border-radius:10px;background:#ffffff;">'
            f'<img src="data:image/svg+xml;base64,{data}" alt="{escape(title)}" style="width:100%;height:auto;display:block;" />'
            f'<p style="margin:8px 0 0 0;font-size:12px;color:{QUIET};">{escape(fr(title))}</p></div>')


def render_lines(lines):
    """Render paragraphs, tables, numbered lists and check-lists from a list of lines."""
    html, para, rows, items, kind = [], [], [], [], None

    def flush():
        nonlocal para, rows, items, kind
        if para:
            txt = " ".join(para)
            if re.fullmatch(r'\*\*[^*]+\*\*', txt):
                html.append(f'<p style="margin:18px 0 8px 0;break-after:avoid;page-break-after:avoid;">{inl(txt)}</p>')
            else:
                html.append(f'<p style="margin:0 0 11px 0;">{inl(txt)}</p>')
            para = []
        if rows:
            html.append(table(rows)); rows = []
        if items:
            if kind == 'check':
                lis = ''.join(f'<li style="margin:5px 0;list-style:none;">'
                              f'<span style="display:inline-block;width:14px;height:14px;border:2px solid {ACC};border-radius:3px;vertical-align:-2px;margin-right:9px;"></span>{inl(t)}</li>' for t in items)
                html.append(f'<ul style="margin:6px 0 14px 0;padding-left:4px;">{lis}</ul>')
            else:
                tag = 'ol' if kind == 'ol' else 'ul'
                lis = ''.join(f'<li style="margin:4px 0;">{inl(t)}</li>' for t in items)
                html.append(f'<{tag} style="margin:6px 0 14px 0;padding-left:24px;">{lis}</{tag}>')
            items = []; kind = None

    for raw in lines:
        line = raw.rstrip()
        s = line.strip()
        if s.startswith('|'):
            if para or items: flush()
            cells = [c.strip() for c in s.strip('|').split('|')]
            if not all(re.fullmatch(r':?-{3,}:?', c) for c in cells):
                rows.append(cells)
            continue
        if rows: flush()
        m_fig = re.fullmatch(r'\[\[FIGURE:([^|\]]+)\|([^|\]]+)\|([^\]]+)\]\]', s)
        m_chk = re.match(r'^- \[[ xX]\] (.*)', s)
        m_ol = re.match(r'^\d+[.)] (.*)', s)
        m_ul = re.match(r'^[-*] (.*)', s)
        if m_fig:
            flush(); html.append(figure(*[g.strip() for g in m_fig.groups()]))
        elif m_chk:
            if kind != 'check': flush(); kind = 'check'
            items.append(m_chk.group(1))
        elif m_ol:
            if kind != 'ol': flush(); kind = 'ol'
            items.append(m_ol.group(1))
        elif m_ul:
            if kind != 'ul': flush(); kind = 'ul'
            items.append(m_ul.group(1))
        elif not s:
            flush()
        else:
            if items: flush()
            para.append(s)
    flush()
    return ''.join(html)


def callout(kind, title, lines):
    label, acc, bg = CALLOUTS.get(kind, ('Note', ACC, SOFT))
    inner = render_lines(lines)
    t = f'<p style="margin:0 0 8px 0;font-size:16px;font-weight:700;color:{INK};break-after:avoid;page-break-after:avoid;">{inl(title)}</p>' if title else ''
    return (f'<div style="margin:18px 0 20px 0;background:{bg};border-left:5px solid {acc};border-radius:0 10px 10px 0;padding:14px 18px 6px 18px;">'
            f'<p style="margin:0 0 4px 0;break-after:avoid;font-size:11.5px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:{acc};">{label}</p>{t}{inner}</div>')


chapters = []
for path in sorted(glob.glob(os.path.join(src_dir, 'ch*.md'))):
    chapters.append(open(path, encoding='utf8').read())

toc, body, n_fig_missing = [], [], 0
for ci, text in enumerate(chapters):
    lines = text.splitlines()
    buf, quote, i = [], None, 0
    for line in lines + ['']:
        if line.startswith('## '):
            body.append(render_lines(buf)); buf = []
            title = line[3:].strip()
            m = re.match(r'(\d+)\.\s*(.*)', title)
            num, name = (m.group(1), m.group(2)) if m else ('', title)
            anchor = f'ch{num or ci}'
            toc.append((num, name, anchor))
            body.append(f'<h2 id="{anchor}" style="margin:44px 0 14px 0;padding:0 0 8px 0;border-bottom:2px solid {LINE};font-size:24px;line-height:1.3;color:{DARK};font-weight:700;">'
                        f'<span style="display:inline-block;min-width:34px;height:34px;line-height:34px;text-align:center;border-radius:8px;background:{ACC};color:#ffffff;font-size:16px;margin-right:10px;vertical-align:middle;">{escape(num)}</span>{escape(fr(name))}</h2>')
        elif line.startswith('### '):
            body.append(render_lines(buf)); buf = []
            body.append(f'<h3 style="margin:26px 0 8px 0;font-size:18.5px;line-height:1.35;color:{ACC};font-weight:600;">{escape(fr(line[4:].strip()))}</h3>')
        elif line.startswith('>'):
            content = line[1:].lstrip() if len(line) > 1 else ''
            m = re.match(r'\[!(\w+)\]\s*(.*)', content)
            if m:
                if quote: body.append(callout(*quote))
                body.append(render_lines(buf)); buf = []
                quote = (m.group(1).upper(), m.group(2), [])
            elif quote:
                quote[2].append(content)
            else:
                buf.append(content)
        else:
            if quote:
                body.append(callout(*quote)); quote = None
            buf.append(line)
    if quote: body.append(callout(*quote))
    body.append(render_lines(buf))

toc_html = ''.join(f'<li style="margin:3px 0;list-style:none;"><a href="#{a}" style="color:{ACC};text-decoration:none;">'
                   f'<span style="display:inline-block;min-width:26px;font-weight:700;">{escape(n)}</span>{escape(fr(t))}</a></li>' for n, t, a in toc)
legend = ''.join(f'<span style="display:inline-block;margin:0 8px 6px 0;padding:3px 9px;border-radius:6px;background:{bg};border-left:4px solid {acc};font-size:12.5px;color:{INK};">{lab}</span>'
                 for lab, acc, bg in LEGEND.values())
head = (f'<div style="background:{DARK};color:#ffffff;border-radius:12px;padding:28px 24px;margin:0 0 24px 0;">'
        f'<p style="margin:0 0 6px 0;font-size:13px;letter-spacing:0.08em;text-transform:uppercase;color:#bfe3ea;">{escape(META["kicker"])}</p>'
        f'<h1 style="margin:0 0 6px 0;font-size:32px;line-height:1.2;color:#ffffff;font-weight:700;">{escape(fr(META["title"]))}</h1>'
        f'<p style="margin:0 0 14px 0;font-size:17px;color:#e6f4f6;">{escape(fr(META["subtitle"]))}</p>'
        f'<p style="margin:0;font-size:14.5px;color:#d6edf1;max-width:820px;">{escape(fr(META["intro"]))}</p></div>'
        f'<div style="background:{SOFT};border-radius:10px;padding:18px 24px;margin:0 0 28px 0;">'
        f'<p style="margin:0 0 8px 0;font-weight:700;font-size:15px;color:{DARK};">Sommaire</p>'
        f'<ul style="margin:0 0 12px 0;padding:0;columns:2;column-gap:32px;font-size:14px;">{toc_html}</ul>'
        f'<p style="margin:0 0 6px 0;font-size:13px;color:{QUIET};">Les encadrés du cours :</p>{legend}</div>')

pdf = ''
if PDF_URL:
    pdf = ('<!--pdf-cartouche-->'
           f'<div style="margin:44px 0 0 0;background:{DARK};border-radius:14px;padding:20px 24px;color:#ffffff;">'
           '<p style="margin:0 0 4px 0;font-size:12px;letter-spacing:0.08em;text-transform:uppercase;color:#bfe3ea;">Version imprimable</p>'
           '<p style="margin:0 0 10px 0;font-size:19px;font-weight:700;color:#ffffff;">Le cours en PDF, avec ses gabarits</p>'
           f'<a href="{escape(PDF_URL)}" download style="display:inline-block;background:#ffffff;color:{DARK};font-weight:700;font-size:15px;text-decoration:none;padding:11px 20px;border-radius:10px;">Télécharger le PDF&nbsp;&nbsp;↓</a>'
           '</div><!--/pdf-cartouche-->')

page = ('<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="utf-8" />\n<meta name="viewport" content="width=device-width, initial-scale=1" />\n'
        f'<title>{escape(META["page_title"])}</title>\n</head>\n'
        f'<body style="margin:0;padding:24px 16px;background:#ffffff;">\n<div style="font-family:{FONT};color:{INK};max-width:980px;margin:0 auto;font-size:15.5px;line-height:1.65;">'
        f'{head}{"".join(body)}{pdf}'
        f'<p style="margin:40px 0 0 0;padding:14px 0 0 0;border-top:1px solid {LINE};font-size:12px;color:{QUIET};">3W Academy · Cycle Expert en informatique et systèmes d\'information · Titre RNCP 40573. '
        'Kestrel Logistique et Medisecure sont des organisations fictives créées pour ce cours.</p></div>\n</body>\n</html>\n')
open(out, 'w', encoding='utf8').write(page)
missing = page.count('Figure à dessiner')
print(out, len(page), 'octets,', len(toc), 'chapitres,', missing, 'figure(s) à dessiner')
