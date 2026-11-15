# Prints the Medisecure HTML page to an A4 PDF with Chrome, then adds bookmarks and metadata.
# Usage: python make_pdf.py <page.html> <out.pdf> <medisecure.json>
import json, os, re, subprocess, sys, tempfile
import fitz

CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
PRINT_CSS = '''<style>
@page { size: A4; margin: 14mm 12mm 16mm 12mm; }
html, body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { padding: 0 !important; }
tr, img, h2, h3 { break-inside: avoid; }
h2, h3 { break-after: avoid; }
div[style*="border-left:4px"], div[style*="text-align:center"] { break-inside: avoid; }
div[style*="overflow-x:auto"] { overflow: visible !important; }
</style>'''

src, out, data = sys.argv[1], os.path.abspath(sys.argv[2]), sys.argv[3]
html = open(src, encoding='utf8').read().replace('</head>', PRINT_CSS + '</head>', 1)
html = re.sub(r'<!--pdf-cartouche-->.*?<!--/pdf-cartouche-->', '', html, flags=re.S)  # no download link inside the PDF
tmp = os.path.join(tempfile.gettempdir(), 'medisecure_print.html')
open(tmp, 'w', encoding='utf8').write(html)
subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                f'--print-to-pdf={out}', 'file:///' + tmp.replace('\\', '/')], check=True, capture_output=True)

titles = []
for b in json.load(open(data, encoding='utf8')):
    if b['type'] == 'h2':
        t = ''.join(s for _, s in b['inl'])
        if t.startswith('Usage'):
            break
        titles.append(t)

doc = fitz.open(out)
big = []  # large text lines = section headings
for pg in range(doc.page_count):
    for bl in doc[pg].get_text('dict')['blocks']:
        for ln in bl.get('lines', []):
            txt = ''.join(s['text'] for s in ln['spans']).strip()
            if txt and max(s['size'] for s in ln['spans']) >= 15:
                big.append((pg, ln['bbox'][1], txt))
norm = lambda s: s.replace('\u2019', "'").replace('\xa0', ' ')
toc, k = [], 0
for i, t in enumerate(titles):
    while k < len(big) and norm(t)[:20] not in norm(big[k][2]):
        k += 1
    if k < len(big):
        pg, y, _ = big[k]
        toc.append([1, f'{i + 1}. {t}', pg + 1, {'kind': fitz.LINK_GOTO, 'page': pg, 'to': fitz.Point(0, max(0, y - 12))}])
        k += 1
doc.set_toc(toc)
doc.set_metadata({'title': "Medisecure – Dossier de présentation de l'entreprise",
                  'author': '3W Academy · Cycle Expert en informatique et SI', 'subject': 'Cas fil rouge, octobre 2026'})
doc.save(out + '.tmp', garbage=3, deflate=True)
doc.close()
os.replace(out + '.tmp', out)
print(out, len(toc), 'signets')
