# Construit un PDF de cours par jour de la semaine S2 : uniquement les chapitres du jour, sans les annexes.
# Le chapitre 6 est coupé : ateliers 1 et 2 au Jour 3, ateliers 3 à 5 et la fin du chapitre au Jour 4.
# Usage : python build_cours_jours_s2.py   (après build_cours.py ; écrit dans Semaine2/JourN_*/)
import glob, json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'cours_s2', 'chapitres')
S2 = os.path.join(HERE, '..', '..', 'Semaine2')
META = json.load(open(os.path.join(HERE, 'cours_s2', 'meta.json'), encoding='utf8'))
CUT6 = '### Atelier 3 : scénarios stratégiques'

DAYS = [  # jour, dossier, titre du jour, chapitres (6a / 6b = moitiés du chapitre 6)
    (1, 'Jour1_Notions_de_base_et_lancement', "Organisation, système d'information, stratégie : les notions de base", ['01']),
    (2, 'Jour2_Strategie_SI_et_cartographie', 'De la stratégie SI à la cartographie : décrire avant de décider', ['02', '03', '04']),
    (3, 'Jour3_Securite_risques_EBIOS', 'Sécurité, risque et EBIOS Risk Manager : cadrer l\'analyse', ['05', '6a']),
    (4, 'Jour4_Data_IA_et_continuite', "Risques data et IA, fin de l'analyse de risques, continuité", ['07', '6b', '08']),
    (5, 'Jour5_Diagnostic_et_autonomie', "Juger l'état du SI : environnement et diagnostic", ['09', '10']),
]


def chapter(code):
    if code in ('6a', '6b'):
        text = open(os.path.join(SRC, 'ch06.md'), encoding='utf8').read()
        i = text.index(CUT6)
        if code == '6a':
            return text[:i].rstrip() + '\n'
        head = '## 6. Analyser les risques avec EBIOS Risk Manager (suite : ateliers 3 à 5)\n\n'
        return head + text[i:]
    return open(os.path.join(SRC, f'ch{code}.md'), encoding='utf8').read()


for k, folder, title, chs in DAYS:
    tmp = tempfile.mkdtemp(prefix=f's2_j{k}_')
    os.makedirs(os.path.join(tmp, 'chapitres'))
    for n, code in enumerate(chs):
        # l'ordre des fichiers fixe l'ordre des chapitres (au Jour 4 : 7, puis 6 suite, puis 8, comme le diaporama)
        open(os.path.join(tmp, 'chapitres', f'ch{n:02d}.md'), 'w', encoding='utf8').write(chapter(code))
    meta = dict(META)
    meta['kicker'] = f"3W Academy · Semaine S2 · Systèmes d'information, cartographie et risques · Jour {k}"
    meta['title'] = title
    meta['subtitle'] = f'Cours du Jour {k}'
    meta['intro'] = ('Ce document ne contient que les chapitres traités ce jour. Les fiches de travail du jour sont dans le dossier '
                     '« Fiches_travail_du_jour » ; le cours complet et ses annexes (gabarits, glossaire, sources) sont dans « Semaine_complete ».')
    meta['page_title'] = f'Cours S2 – Jour {k}'
    json.dump(meta, open(os.path.join(tmp, 'meta.json'), 'w', encoding='utf8'), ensure_ascii=False)
    html = os.path.join(tmp, f'J{k}.html')
    subprocess.run([sys.executable, os.path.join(HERE, 'build_cours.py'), os.path.join(tmp, 'chapitres'), html], check=True)
    d = os.path.join(S2, folder)
    for old in glob.glob(os.path.join(d, f'J{k}_Cours*.pdf')):
        os.remove(old)
    out = os.path.join(d, f'J{k}_Cours_du_jour.pdf')
    subprocess.run([sys.executable, os.path.join(HERE, 'make_pdf_cours.py'), html, out,
                    f'Cours S2 – Jour {k} – {title}', 'Cours de la semaine S2, novembre 2026'], check=True)
    shutil.rmtree(tmp, ignore_errors=True)
