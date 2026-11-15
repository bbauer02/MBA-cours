# Page HTML (Moodle) des consignes du dossier de veille SIO, depuis le Markdown. Copie adaptée du générateur MBA.
# Usage: python build_consignes.py <source.md> <output.html>
import re, sys, os
from html import escape
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from frtypo import fr

INK = '#1f2933'; QUIET = '#5f6b76'; ACC = '#0b7285'; DARK = '#0b4f6c'; LINE = '#dde3e8'; SOFT = '#f4f7f9'; ZEBRA = '#e6f1f4'
FONT = "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"

src, out = sys.argv[1], sys.argv[2]
text = open(src, encoding='utf8').read()
_, front, body = text.split('---', 2)
meta = dict(l.split(':', 1) for l in front.strip().splitlines())
meta = {k.strip(): v.strip() for k, v in meta.items()}


def inl(s):
    parts = re.split(r'(\*\*[^*]+\*\*)', s)
    return ''.join(f'<strong>{escape(fr(p[2:-2]))}</strong>' if p.startswith('**') else escape(fr(p)) for p in parts)


def table(rows):
    head, body_rows = rows[0], rows[1:]
    th = ''.join(f'<th style="text-align:left;vertical-align:bottom;padding:10px 12px;background:{DARK};color:#ffffff;'
                 f'font-weight:600;font-size:13px;">{inl(c)}</th>' for c in head)
    trs = ''
    for i, r in enumerate(body_rows):
        bg = '#ffffff' if i % 2 == 0 else ZEBRA
        tds = ''.join(f'<td style="vertical-align:top;padding:9px 12px;border-bottom:1px solid {LINE};'
                      f'{"font-weight:600;" if j == 0 else ""}">{inl(c)}</td>' for j, c in enumerate(r))
        trs += f'<tr style="background:{bg};">{tds}</tr>'
    return (f'<div style="overflow-x:auto;margin:16px 0 22px 0;border:1px solid {LINE};border-radius:8px;">'
            f'<table style="width:100%;border-collapse:collapse;font-size:14px;line-height:1.45;color:{INK};">'
            f'<thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>')


blocks, buf = [], []
for line in body.strip().splitlines():
    if line.startswith('|'):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if all(re.fullmatch(r'-{3,}', c) for c in cells):
            continue
        buf.append(cells)
        continue
    if buf:
        blocks.append(('table', buf)); buf = []
    if line.startswith('## '):
        blocks.append(('h2', line[3:]))
    elif line.startswith('### '):
        blocks.append(('h3', line[4:]))
    elif re.match(r'- \[[ xX]\] ', line):
        blocks.append(('check', line[6:].strip()))
    elif line.strip():
        blocks.append(('p', line.strip()))
if buf:
    blocks.append(('table', buf))

intro = blocks[0][1] if blocks and blocks[0][0] == 'p' else ''
blocks = blocks[1:] if intro else blocks
sections = [b[1] for b in blocks if b[0] == 'h2']

h = [f'<div style="font-family:{FONT};color:{INK};max-width:980px;margin:0 auto;font-size:15px;line-height:1.6;">',
     f'<div style="background:{DARK};color:#ffffff;border-radius:12px;padding:28px 24px;margin:0 0 24px 0;">'
     f'<p style="margin:0 0 6px 0;font-size:13px;letter-spacing:0.08em;text-transform:uppercase;color:#bfe3ea;">{escape(meta["kicker"])}</p>'
     f'<h1 style="margin:0 0 6px 0;font-size:30px;line-height:1.25;color:#ffffff;font-weight:700;">{escape(fr(meta["titre"]))}</h1>'
     f'<p style="margin:0 0 14px 0;font-size:17px;color:#e6f4f6;">{escape(fr(meta["soustitre"]))}</p>'
     f'<p style="margin:0;font-size:15px;color:#e6f4f6;max-width:820px;">{inl(intro)}</p></div>']
toc = ''.join(f'<li style="margin:2px 0;"><a href="#s{i + 1}" style="color:{ACC};text-decoration:none;">{escape(s)}</a></li>'
              for i, s in enumerate(sections))
h.append(f'<div style="background:{SOFT};border-radius:10px;padding:18px 24px;margin:0 0 28px 0;">'
         f'<p style="margin:0 0 8px 0;font-weight:700;font-size:15px;color:{DARK};">Sommaire</p>'
         f'<ol style="margin:0;padding-left:22px;font-size:14px;">{toc}</ol>'
         f'<p style="margin:12px 0 0 0;font-size:13px;color:{QUIET};">Document à lire avec le livret de fiches « Ma veille technologique ».</p></div>')
n = 0
for kind, val in blocks:
    if kind == 'h2':
        n += 1
        h.append(f'<h2 id="s{n}" style="margin:36px 0 12px 0;padding:0 0 8px 0;border-bottom:2px solid {LINE};font-size:23px;line-height:1.3;color:{DARK};font-weight:700;">'
                 f'<span style="display:inline-block;min-width:34px;height:34px;line-height:34px;text-align:center;border-radius:8px;background:{ACC};color:#ffffff;font-size:16px;margin-right:10px;vertical-align:middle;">{n}</span>'
                 f'{escape(fr(val))}</h2>')
    elif kind == 'h3':
        h.append(f'<h3 style="margin:24px 0 8px 0;font-size:18px;color:{ACC};font-weight:600;">{escape(fr(val))}</h3>')
    elif kind == 'p':
        txt = val
        if re.fullmatch(r'\*\*[^*]+\*\*.*', txt) and txt.startswith('**') and '?**' in txt:
            q, a = txt[2:].split('**', 1)  # FAQ: question in bold, answer after
            h.append(f'<div style="margin:0 0 12px 0;padding:12px 16px;background:{SOFT};border-radius:8px;">'
                     f'<p style="margin:0 0 4px 0;font-weight:700;color:{DARK};">{inl(q)}</p><p style="margin:0;">{inl(a.strip())}</p></div>')
        else:
            h.append(f'<p style="margin:0 0 12px 0;">{inl(txt)}</p>')
    elif kind == 'check':
        h.append(f'<p style="margin:0 0 7px 0;padding-left:26px;text-indent:-26px;">'
                 f'<span style="display:inline-block;width:14px;height:14px;border:2px solid {ACC};border-radius:3px;vertical-align:-2px;margin-right:10px;"></span>{inl(val)}</p>')
    else:
        h.append(table(val))
h.append(f'<p style="margin:40px 0 0 0;padding:14px 0 0 0;border-top:1px solid {LINE};font-size:12px;color:{QUIET};">'
         'BTS SIO · deuxième année · Veille technologique. Les personnages et organisations des exemples sont fictifs.</p></div>')

page = ('<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="utf-8" />\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1" />\n'
        f'<title>{escape(meta["titre"])}</title>\n</head>\n'
        f'<body style="margin:0;padding:24px 16px;background:#ffffff;">\n{"".join(h)}\n</body>\n</html>\n')
open(out, 'w', encoding='utf8').write(page)
print(out, len(page), 'octets,', n, 'sections')
