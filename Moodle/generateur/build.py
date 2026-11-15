# Builds a Moodle-ready, self-contained HTML page from the Medisecure doc export.
# Every style is inline (Moodle's HTML filter drops <style> blocks) and every
# figure is an <img> with an SVG data URI (Moodle drops inline <svg>).
import base64, json, sys
from html import escape
sys.path.insert(0, sys.argv[1])
from svgs import FIGS, fr

blocks = json.load(open(sys.argv[2], encoding='utf8'))
out_path = sys.argv[3]

INK = '#1f2933'; QUIET = '#5f6b76'; ACC = '#0b7285'; DARK = '#0b4f6c'; LINE = '#dde3e8'; SOFT = '#f4f7f9'; ACCBG = '#e3f2f4'; ZEBRA = '#e6f1f4'
FONT = "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"


def inl(parts):
    s = ''
    for kind, text in parts:
        t = escape(fr(text))
        s += f'<strong>{t}</strong>' if kind == 'b' else t
    return s


def plain(parts):
    return ''.join(t for _, t in parts)


def table(rows):
    head, body = rows[0], rows[1:]
    th = ''.join(f'<th style="text-align:left;vertical-align:bottom;padding:10px 12px;background:{DARK};color:#ffffff;'
                 f'font-weight:600;font-size:13px;">{inl(c["inl"])}</th>' for c in head)
    trs = ''
    for i, r in enumerate(body):
        bg = '#ffffff' if i % 2 == 0 else ZEBRA
        tds = ''.join(f'<td style="vertical-align:top;padding:9px 12px;border-bottom:1px solid {LINE};'
                      f'{"font-weight:600;" if j == 0 else ""}">{inl(c["inl"])}</td>' for j, c in enumerate(r))
        trs += f'<tr style="background:{bg};">{tds}</tr>'
    return (f'<div style="overflow-x:auto;margin:16px 0 22px 0;border:1px solid {LINE};border-radius:8px;">'
            f'<table style="width:100%;border-collapse:collapse;font-size:14px;line-height:1.45;color:{INK};">'
            f'<thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>')


def quotes(rows):
    cards = ''
    for r in rows[1:]:
        who, said = plain(r[0]['inl']), plain(r[1]['inl'])
        cards += (f'<div style="margin:0 0 12px 0;padding:14px 18px;background:{SOFT};border-left:4px solid {ACC};border-radius:0 8px 8px 0;">'
                  f'<p style="margin:0 0 6px 0;font-size:15px;line-height:1.5;color:{INK};font-style:italic;">{escape(fr(said))}</p>'
                  f'<p style="margin:0;font-size:13px;color:{QUIET};font-weight:600;">{escape(fr(who))}</p></div>')
    return f'<div style="margin:16px 0 22px 0;">{cards}</div>'


def figure(ref, caption):
    data = base64.b64encode(FIGS[ref]().encode('utf8')).decode('ascii')
    return (f'<div style="margin:20px 0 24px 0;padding:12px;border:1px solid {LINE};border-radius:10px;background:#ffffff;text-align:center;">'
            f'<img src="data:image/svg+xml;base64,{data}" alt="{escape(caption)}" style="width:100%;height:auto;display:block;" />'
            f'<p style="margin:8px 0 0 0;font-size:12px;color:{QUIET};text-align:left;">{escape(caption)}</p></div>')


# Student version: drop the byline and the trainer-only section.
body_blocks = []
for b in blocks[2:]:
    if b['type'] == 'h2' and plain(b['inl']).startswith('Usage pédagogique'):
        break
    body_blocks.append(b)

sections = [plain(b['inl']) for b in body_blocks if b['type'] == 'h2']
intro = inl(blocks[2]['inl']) if blocks[2]['type'] == 'p' else ''
body_blocks = body_blocks[1:] if blocks[2]['type'] == 'p' else body_blocks

html = []
html.append(f'<div style="font-family:{FONT};color:{INK};max-width:980px;margin:0 auto;font-size:15px;line-height:1.6;">')

# Header band
html.append(f'<div style="background:{DARK};color:#ffffff;border-radius:12px;padding:28px 24px;margin:0 0 24px 0;">'
            f'<p style="margin:0 0 6px 0;font-size:13px;letter-spacing:0.08em;text-transform:uppercase;color:#bfe3ea;">3W Academy · Cycle Expert en informatique et SI · Cas fil rouge</p>'
            f'<h1 style="margin:0 0 6px 0;font-size:34px;line-height:1.2;color:#ffffff;font-weight:700;">Medisecure</h1>'
            f'<p style="margin:0 0 14px 0;font-size:18px;color:#e6f4f6;">Dossier de présentation de l\'entreprise, octobre 2026</p>'
            f'<p style="margin:0;font-size:14px;color:#cfe8ed;max-width:760px;">{intro}</p></div>')

# Key figures
figs = [('14', 'centres de santé'), ('410 000', 'patients actifs'), ('1,1 million', 'consultations par an'),
        ('620', 'salariés'), ('68 M€', 'recettes de soins 2025'), ('2,84 M€', 'budget SI 2026')]
tiles = ''
for v, l in figs:
    tiles += (f'<div style="display:inline-block;vertical-align:top;width:31%;min-width:140px;box-sizing:border-box;margin:0 1.5% 10px 0;'
              f'background:#ffffff;border:1px solid {LINE};border-radius:10px;padding:12px 14px;">'
              f'<div style="font-size:24px;font-weight:700;color:{ACC};line-height:1.2;">{fr(v)}</div>'
              f'<div style="font-size:13px;color:{QUIET};">{l}</div></div>')
html.append(f'<div style="margin:0 0 18px 0;">{tiles}</div>')

# Table of contents
toc = ''.join(f'<li style="margin:2px 0;"><a href="#s{i + 1}" style="color:{ACC};text-decoration:none;">{escape(s)}</a></li>'
              for i, s in enumerate(sections))
html.append(f'<div style="background:{SOFT};border-radius:10px;padding:18px 24px;margin:0 0 28px 0;">'
            f'<p style="margin:0 0 8px 0;font-weight:700;font-size:15px;color:{DARK};">Sommaire</p>'
            f'<ol style="margin:0;padding-left:22px;font-size:14px;columns:2;column-gap:32px;">{toc}</ol></div>')

n = 0
for b in body_blocks:
    t = b['type']
    if t == 'h2':
        n += 1
        html.append(f'<h2 id="s{n}" style="margin:40px 0 12px 0;padding:0 0 8px 0;border-bottom:2px solid {LINE};font-size:24px;line-height:1.3;color:{DARK};font-weight:700;">'
                    f'<span style="display:inline-block;min-width:34px;height:34px;line-height:34px;text-align:center;border-radius:8px;background:{ACC};color:#ffffff;font-size:16px;margin-right:10px;vertical-align:middle;">{n}</span>'
                    f'{escape(fr(plain(b["inl"])))}</h2>')
    elif t == 'h3':
        html.append(f'<h3 style="margin:26px 0 8px 0;font-size:18px;line-height:1.35;color:{ACC};font-weight:600;">{escape(fr(plain(b["inl"])))}</h3>')
    elif t == 'p':
        html.append(f'<p style="margin:0 0 12px 0;">{inl(b["inl"])}</p>')
    elif t == 'table':
        head = [plain(c['inl']) for c in b['rows'][0]]
        html.append(quotes(b['rows']) if head == ['Partie prenante', 'Verbatim'] else table(b['rows']))
    elif t == 'embed':
        html.append(figure(b['ref'], b['caption']))

# Download banner pointing to the PDF version (removed again by make_pdf.py when printing).
# Pass the Moodle URL of the PDF as 4th argument; by default the PDF sits next to the HTML file.
PDF_URL = sys.argv[4] if len(sys.argv) > 4 else '01_Medisecure_dossier_entreprise.pdf'
PDF_ICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 56"><path d="M6 2h26l14 14v36a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2z" fill="#ffffff"/>'
            '<path d="M32 2v12a2 2 0 0 0 2 2h12" fill="#cfe8ed"/><rect x="0" y="28" width="38" height="16" rx="3" fill="#e8590c"/>'
            '<text x="19" y="40" font-family="Segoe UI, Arial, sans-serif" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">PDF</text></svg>')
icon_uri = 'data:image/svg+xml;base64,' + base64.b64encode(PDF_ICON.encode('utf8')).decode('ascii')
html.append('<!--pdf-cartouche-->'
            f'<div style="margin:44px 0 0 0;background:{DARK};border-radius:14px;padding:22px 24px;color:#ffffff;">'
            # Two inline blocks: side by side on a wide screen, the button drops below the text on a phone.
            '<div style="display:inline-block;vertical-align:middle;width:68%;min-width:260px;margin:0 0 4px 0;">'
            '<table style="border-collapse:collapse;"><tr>'
            f'<td style="width:56px;vertical-align:middle;padding:0 16px 0 0;"><img src="{icon_uri}" alt="" style="width:48px;height:auto;display:block;" /></td>'
            '<td style="vertical-align:middle;padding:0;">'
            '<p style="margin:0 0 4px 0;font-size:12px;letter-spacing:0.08em;text-transform:uppercase;color:#bfe3ea;">Version imprimable</p>'
            '<p style="margin:0 0 6px 0;font-size:20px;font-weight:700;color:#ffffff;line-height:1.3;">Le dossier Medisecure en PDF</p>'
            '<p style="margin:0;font-size:14px;color:#d6edf1;line-height:1.5;">37 pages A4, sommaire et signets cliquables, schémas en couleur. '
            'Pratique pour annoter, imprimer ou consulter hors ligne.</p></td></tr></table></div>'
            '<div style="display:inline-block;vertical-align:middle;min-width:200px;margin:10px 0 4px 0;">'
            f'<a href="{escape(PDF_URL)}" download style="display:inline-block;background:#ffffff;color:{DARK};font-weight:700;font-size:15px;'
            'text-decoration:none;padding:12px 22px;border-radius:10px;white-space:nowrap;">Télécharger le PDF&nbsp;&nbsp;↓</a>'
            '<p style="margin:8px 0 0 4px;font-size:12px;color:#bfe3ea;">Environ 780 Ko</p></div>'
            '</div><!--/pdf-cartouche-->')

html.append(f'<p style="margin:40px 0 0 0;padding:14px 0 0 0;border-top:1px solid {LINE};font-size:12px;color:{QUIET};">'
            f'Medisecure est une organisation fictive créée pour le cycle Expert en informatique et systèmes d\'information de la 3W Academy. '
            f'Les noms, chiffres et événements sont inventés à des fins pédagogiques.</p></div>')

page = ('<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="utf-8" />\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1" />\n'
        '<title>Medisecure – Dossier de présentation</title>\n</head>\n'
        f'<body style="margin:0;padding:24px 16px;background:#ffffff;">\n{"".join(html)}\n</body>\n</html>\n')
open(out_path, 'w', encoding='utf8').write(page)
print(out_path, len(page), 'octets,', n, 'sections')
