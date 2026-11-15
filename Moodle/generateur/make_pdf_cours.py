# Prints the course HTML page to an A4 PDF with Chrome, then adds chapter bookmarks and metadata.
# Usage: python make_pdf_cours.py <page.html> <out.pdf> [title] [subject]
import os, re, subprocess, sys, tempfile
from html import unescape
import fitz

CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
PRINT_CSS = '''<style>
@page { size: A4; margin: 14mm 12mm 16mm 12mm; }
html, body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { padding: 0 !important; zoom: 0.8; }
tr, img, li { break-inside: avoid; }
h2, h3 { break-after: avoid; break-inside: avoid; }
h2 { break-before: page; }
div[style*="border-left:5px"] > p:first-child { break-after: avoid; }
div[style*="overflow-x:auto"] { overflow: visible !important; }
ul[style*="columns:2"] { columns: 2 !important; }
</style>'''

src, out = sys.argv[1], os.path.abspath(sys.argv[2])
TITLE = sys.argv[3] if len(sys.argv) > 3 else 'La veille technologique et réglementaire – Cours S1'
SUBJECT = sys.argv[4] if len(sys.argv) > 4 else 'Cours et guide du dossier D1, octobre 2026'
html = open(src, encoding='utf8').read().replace('</head>', PRINT_CSS + '</head>', 1)
html = re.sub(r'<!--pdf-cartouche-->.*?<!--/pdf-cartouche-->', '', html, flags=re.S)
tmp = os.path.join(tempfile.gettempdir(), 'cours_veille_print.html')
open(tmp, 'w', encoding='utf8').write(html)
subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                f'--print-to-pdf={out}', 'file:///' + tmp.replace('\\', '/')], check=True, capture_output=True)

# Chapter titles as printed: "<number><title>" inside each h2
titles = [(m.group(1), unescape(re.sub('<[^>]+>', '', m.group(2))))
          for m in re.finditer(r'<h2 id="[^"]+"[^>]*><span[^>]*>([^<]*)</span>(.*?)</h2>', html)]
norm = lambda s: s.replace('\u2019', "'").replace('\xa0', ' ').replace('\u202f', ' ')
doc = fitz.open(out)
big = []
for pg in range(doc.page_count):
    for bl in doc[pg].get_text('dict')['blocks']:
        for ln in bl.get('lines', []):
            txt = ''.join(s['text'] for s in ln['spans']).strip()
            if txt and max(s['size'] for s in ln['spans']) >= 11:
                big.append((pg, ln['bbox'][1], txt))
toc, k = [], 0
for num, t in titles:
    key = norm(t)[:18]
    while k < len(big) and key not in norm(big[k][2]):
        k += 1
    if k < len(big):
        pg, y, _ = big[k]
        toc.append([1, f'{num}. {t}', pg + 1, {'kind': fitz.LINK_GOTO, 'page': pg, 'to': fitz.Point(0, max(0, y - 14))}])
        k += 1
doc.set_toc(toc)
doc.set_metadata({'title': TITLE, 'author': '3W Academy · Cycle Expert en informatique et SI', 'subject': SUBJECT})
doc.save(out + '.tmp', garbage=3, deflate=True)
n = doc.page_count
doc.close()
os.replace(out + '.tmp', out)
print(out, n, 'pages,', len(toc), 'signets sur', len(titles), 'chapitres')
