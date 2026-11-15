# Builds one day, converts the deck to PDF with LibreOffice and writes contact sheets (6 slides per PNG) to check by eye.
# Usage: python render_check.py J2 <work_dir>
import os, subprocess, sys
import fitz
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_diapos as B
day, work = sys.argv[1], sys.argv[2]
out = os.path.join(work, day)
spec = B.build_day(day, out)
pptx = os.path.join(out, f"J{spec['day']}_Diaporama.pptx")
prof = 'file:///' + os.path.abspath(os.path.join(work, 'lo_profile_' + day)).replace(os.sep, '/')
subprocess.run([r'C:\Program Files\LibreOffice\program\soffice.exe', '-env:UserInstallation=' + prof, '--headless', '--convert-to', 'pdf', '--outdir', out, pptx], check=True, capture_output=True)
d = fitz.open(pptx[:-5] + '.pdf')
ims = []
for p in d:
    pm = p.get_pixmap(dpi=62); ims.append(Image.frombytes('RGB', [pm.width, pm.height], pm.samples))
w, h = ims[0].size
for k in range(0, len(ims), 6):
    chunk = ims[k:k + 6]; sh = Image.new('RGB', (w * 2, h * 3), 'white')
    for i, im in enumerate(chunk):
        sh.paste(im, ((i % 2) * w, (i // 2) * h))
    path = os.path.join(out, f'planche_{k // 6 + 1:02d}.png'); sh.save(path); print(path)
