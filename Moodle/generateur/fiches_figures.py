# Inline SVG diagrams for the revision cards. Called from build_fiches.py through a block
# "@schema <id> <title>" in fiches_veille/fiches_*.md. viewBox width is 700 (= 186 mm, so 1 unit ~ 0.27 mm).
# Text inherits the card font (Source Sans 3); colours follow fiches.css.
import math, re
from html import escape

PET = '#12343b'; TEAL = '#1f6f78'; AMB = '#e09f3e'; BRICK = '#9e2a2b'; GREEN = '#4f7f4e'
INK = '#1b2a33'; SLATE = '#5e6b78'; MIST = '#eef3f2'; PALE = '#c8d6d4'
TEAL_L = '#dcebea'; AMB_L = '#fbefdc'; BRICK_L = '#f3dcdc'; GREEN_L = '#e3ede2'
W = 700


def svg(h, body, label):
    return (f'<svg class="schema" viewBox="0 0 {W} {h}" role="img" aria-label="{escape(label)}">'
            '<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{TEAL}"/></marker></defs>{body}</svg>')


def wrap(s, n):
    s = re.sub(r' (?=[?:;!»%])', ' ', s)
    s = re.sub(r'(?<=«) ', ' ', s)
    s = re.sub(r'(?<=\b\d) (?=\w)', ' ', s)
    out, cur = [], ''
    for w in s.split(' '):
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur); cur = w
        else:
            cur = f'{cur} {w}'.strip()
    return out + ([cur] if cur else [])


def t(x, y, s, size=11, wt=400, fill=INK, anchor='start', italic=False):
    st = ' font-style="italic"' if italic else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{wt}" fill="{fill}" text-anchor="{anchor}"{st}>{escape(s)}</text>'


def tl(x, y, s, n, size=11, wt=400, fill=INK, anchor='start', lh=None, italic=False):
    """Wrapped text, first baseline at y. Returns (svg, number of lines)."""
    lh = lh or size * 1.25
    ls = wrap(s, n)
    return ''.join(t(x, y + i * lh, l, size, wt, fill, anchor, italic) for i, l in enumerate(ls)), len(ls)


def rect(x, y, w, h, fill, stroke='none', rx=6, sw=1.2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def arrow(x1, y1, x2, y2, col=TEAL, sw=1.6, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{sw}" marker-end="url(#ar)"{d}/>'


def line(x1, y1, x2, y2, col=PALE, sw=1.2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{sw}"{d}/>'


def card(x, y, w, h, title, text, fill=TEAL_L, stroke='none', n=None, tsize=11.5, size=10.5, tcol=PET):
    n = n or int((w - 16) / (size * 0.5))
    b = rect(x, y, w, h, fill, stroke)
    b += t(x + 8, y + 17, title, tsize, 700, tcol)
    if text:
        b += tl(x + 8, y + 32, text, n, size)[0]
    return b


def flow(items, y=4, h=70, gap=26, fills=None, n=None, size=10.3):
    """Horizontal chain of cards with arrows. items = [(title, text)]."""
    k = len(items); w = (W - gap * (k - 1)) / k
    b = ''
    for i, (ti, tx) in enumerate(items):
        x = i * (w + gap)
        b += card(x, y, w, h, ti, tx, (fills or [TEAL_L] * k)[i], n=n, size=size)
        if i < k - 1:
            b += arrow(x + w + 3, y + h / 2, x + w + gap - 3, y + h / 2)
    return b


def matrix(title_x, title_y, cols, rows, cells, fills, h=140, cell_h=None, n=34):
    """2 x 2 matrix. cells[r][c] = (title, text); row 0 is the top (strong) row."""
    x0, y0 = 118, 36; cw = (W - x0) / 2; ch = cell_h or (h - y0 - 4) / 2
    b = f'<text x="12" y="{y0 + ch:.1f}" font-size="11" font-weight="700" fill="{SLATE}" text-anchor="middle" transform="rotate(-90 12 {y0 + ch:.1f})">{escape(title_y)} →</text>'
    b += t(x0 + cw, 12, f'{title_x} →', 11, 700, SLATE, 'middle')
    for c in range(2):
        b += t(x0 + c * cw + cw / 2, y0 - 6, cols[c], 10.5, 700, TEAL, 'middle')
    for r in range(2):
        b += tl(x0 - 8, y0 + r * ch + ch / 2 - 2, rows[r], 14, 10.5, 700, TEAL, 'end')[0]
        for c in range(2):
            ti, tx = cells[r][c]
            x, y = x0 + c * cw + 2, y0 + r * ch + 2
            b += rect(x, y + 2, cw - 4, ch - 4, fills[r][c])
            b += t(x + 10, y + 20, ti, 12, 700, PET)
            if tx:
                b += tl(x + 10, y + 36, tx, n, 10.5)[0]
    return b


# ---------------------------------------------------------------- one function per diagram

def activites_temps():
    b = ''; x0, x1 = 170, 690
    b += arrow(x0, 102, x1, 102, SLATE, 1.2) + t(x1, 115, 'temps', 10, 400, SLATE, 'end', True)
    rows = [('Veille', 'regarde l\'extérieur, en continu'), ('Audit', 'regarde l\'intérieur, une fois'),
            ('Recherche documentaire', 'une seule question')]
    for i, (a, d) in enumerate(rows):
        y = 16 + i * 30
        b += t(0, y + 4, a, 11.5, 700, PET) + t(0, y + 17, d, 9.8, 400, SLATE)
        b += line(x0, y + 6, x1 - 10, y + 6, PALE, 1, '2 3')
    for k in range(13):
        b += f'<circle cx="{x0 + 10 + k * 40}" cy="22" r="4.5" fill="{TEAL}"/>'
    b += rect(420, 43, 16, 16, AMB, rx=3) + t(444, 55, 'un état des lieux à un moment donné', 10, 400, INK)
    b += rect(230, 78, 190, 8, PALE, rx=4) + f'<circle cx="420" cy="82" r="6" fill="{BRICK}"/>'
    b += t(432, 86, 'réponse trouvée : on s\'arrête', 10, 400, INK)
    return svg(118, b, 'Veille, audit et recherche documentaire dans le temps')


def escalier():
    steps = [('Information brute', 'Node.js 14 n\'est plus maintenu depuis le 30 avril 2023'),
             ('+ le contexte', 'Notre plateforme de suivi des colis tourne encore sur cette version'),
             ('+ l\'impact', 'Plus aucun correctif de sécurité pour une application exposée à Internet, qui contient des adresses de clients'),
             ('+ une option de décision', 'Migrer vers une version maintenue, avec une estimation du temps de travail')]
    b = ''; w = 166; gap = 12; base = 200
    fills = [MIST, TEAL_L, '#c7dfdd', AMB_L]
    for i, (ti, tx) in enumerate(steps):
        x = i * (w + gap); hgt = 96 + i * 26; y = base - hgt
        b += rect(x, y, w, hgt, fills[i])
        b += t(x + 8, y + 18, ti, 11.5, 700, PET) + tl(x + 8, y + 34, tx, 31, 10.2)[0]
    b += arrow(0, 212, W - 4, 212, AMB, 1.8) + t(0, 228, 'Le veilleur ajoute de la valeur, étape par étape', 10, 400, SLATE, italic=True)
    b += t(W, 16, '= un renseignement : il répond à « et alors ? »', 11.5, 700, BRICK, 'end')
    return svg(232, b, 'De l\'information brute au renseignement, en trois ajouts')


def cycle():
    steps = [('1. Expression du besoin', 'Qui a besoin de quoi, pour décider de quoi ?'),
             ('2. Ciblage', 'Où chercher ? Que suit-on, et que ne suit-on pas ?'),
             ('3. Collecte', 'Comment recueillir l\'information ?'),
             ('4. Traitement et analyse', 'Qu\'est-ce que cela change pour nous ?'),
             ('5. Diffusion', 'À qui transmettre l\'information, et sous quelle forme ?'),
             ('6. Capitalisation', 'Comment retrouver l\'information plus tard ?'),
             ('7. Évaluation et ajustement', 'La veille a-t-elle servi ?')]
    cx, cy, rx, ry = 350, 140, 252, 104; bw, bh = 196, 56
    b = f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{PALE}" stroke-width="2.4"/>'
    for i in range(7):  # arrowheads between the boxes, clockwise
        a = math.radians(-90 + 360 / 7 * (i + .5))
        px, py = cx + rx * math.cos(a), cy + ry * math.sin(a)
        dx, dy = -rx * math.sin(a), ry * math.cos(a); L = math.hypot(dx, dy); dx, dy = dx / L, dy / L
        b += arrow(px - dx * 6, py - dy * 6, px + dx * 6, py + dy * 6, TEAL, 2.4)
    for i, (ti, q) in enumerate(steps):
        a = math.radians(-90 + 360 / 7 * i)
        x, y = cx + rx * math.cos(a) - bw / 2, cy + ry * math.sin(a) - bh / 2
        x = min(max(x, 1), W - bw - 1)
        b += rect(x, y, bw, bh, AMB_L if i == 6 else TEAL_L, PET if i == 0 else 'none')
        b += t(x + 8, y + 17, ti, 11.2, 700, PET) + tl(x + 8, y + 32, q, 36, 10)[0]
    b += t(cx, cy - 4, 'Chaque tour', 11.5, 700, SLATE, 'middle') + t(cx, cy + 11, 'améliore le suivant', 11.5, 700, SLATE, 'middle')
    return svg(276, b, 'Le cycle de la veille en sept étapes')


def push_pull():
    b = rect(265, 40, 170, 50, PET) + t(350, 70, 'Le veilleur', 13, 700, '#fff', 'middle')
    b += card(0, 22, 200, 86, 'Pull : je vais chercher', 'Ex. consulter chaque mois les décisions de la CNIL', MIST)
    b += card(500, 22, 200, 86, 'Push : l\'information vient à moi', 'Ex. recevoir le flux RSS des avis du CERT-FR', TEAL_L, n=36)
    b += arrow(263, 55, 204, 55, TEAL, 1.8) + arrow(204, 75, 263, 75, TEAL, 1.8, '4 3')
    b += t(233, 49, 'va voir', 9.5, 400, SLATE, 'middle', True) + t(233, 89, 'rapporte', 9.5, 400, SLATE, 'middle', True)
    b += arrow(498, 65, 437, 65, TEAL, 1.8) + t(467, 55, 'arrive seule', 9.5, 400, SLATE, 'middle', True)
    b += rect(120, 118, 460, 26, AMB_L) + t(350, 135, 'Méthode mixte : pour chaque source, préciser push ou pull, et pourquoi', 10.8, 700, PET, 'middle')
    return svg(148, b, 'Le mode pull et le mode push')


def remonter():
    items = [('Post LinkedIn', 'Le point de départ'), ('Article de presse', 'Reprend et commente'),
             ('Avis du CERT-FR', 'Rapporte l\'avis de l\'éditeur'), ('Avis de l\'éditeur', 'Le document d\'origine : c\'est lui qu\'on cite')]
    b = flow(items, y=24, h=60, fills=[MIST, MIST, TEAL_L, AMB_L], size=10.2)
    b += t(0, 14, 'Remonter à la source : suivre les liens jusqu\'au dernier maillon', 11, 700, SLATE)
    b += line(0, 94, 515, 94, SLATE, 1) + t(257, 108, 'sources secondaires : servent à repérer', 10, 400, SLATE, 'middle', True)
    b += line(528, 94, 700, 94, BRICK, 1.6) + t(614, 108, 'source primaire : sert à prouver', 10, 700, BRICK, 'middle')
    return svg(114, b, 'Remonter à la source primaire')


def echelle_fiabilite():
    cols = {0: MIST, 1: MIST, 2: MIST, 3: MIST, 4: MIST, 5: AMB_L, 6: AMB_L, 7: TEAL_L, 8: TEAL_L, 9: '#a9cfcb', 10: '#a9cfcb'}
    cw = W / 11; b = ''
    for s in range(11):
        b += rect(s * cw + 1, 22, cw - 2, 26, cols[s], rx=3) + t(s * cw + cw / 2, 40, str(s), 11.5, 700, PET, 'middle')
    zones = [(0, 4, 'D · non fiable', 'Écartée, ou gardée seulement pour repérer des sujets'),
             (5, 6, 'C · à recouper', 'Sert à repérer, jamais citée seule'),
             (7, 8, 'B · plutôt fiable', 'À confirmer par une source primaire avant de décider'),
             (9, 10, 'A · fiable', 'Suffit seule à établir une information')]
    for a, z, lab, txt in zones:
        x, w = a * cw + 2, (z - a + 1) * cw - 4
        b += t(x + w / 2, 15, lab, 11, 700, PET, 'middle')
        b += line(x, 54, x + w, 54, TEAL, 2) + tl(x + w / 2, 70, txt, int(w / 5.3), 10, 400, INK, 'middle')[0]
    return svg(108, b, 'Du score de fiabilité sur 10 à la cote')


def circuit():
    items = [('1. Sources', 'Publient l\'information. CERT-FR, CNIL, éditeurs, presse'),
             ('2. Capteurs', 'Détectent les nouveautés. Flux RSS, alertes Google, newsletters, surveillance de pages'),
             ('3. Point d\'entrée unique', 'Rassemble et permet de trier. Agrégateur : Feedly, Inoreader, FreshRSS'),
             ('4. Stockage et partage', 'Conserve et diffuse. OneNote, SharePoint, Notion, Teams')]
    return svg(96, flow(items, y=2, h=90, fills=[MIST, TEAL_L, AMB_L, TEAL_L], size=10.2), 'Les quatre étages du circuit de collecte')


def requete():
    q = [('"Keycloak"', TEAL, 'une expression exacte, entre guillemets'),
         ('("fin de support" OR "end of life")', AMB, 'des synonymes reliés par OR'),
         ('-emploi -offre', BRICK, 'le signe moins retire le bruit')]
    b = rect(0, 30, W, 40, MIST) + t(0, 18, 'Question du plan de veille : quand la version de Keycloak que nous utilisons ne sera-t-elle plus maintenue ?', 10.5, 400, SLATE, italic=True)
    x = 14; centers = []
    for s, col, _ in q:
        w = len(s) * 8.3
        b += f'<text x="{x}" y="56" font-size="15" font-weight="700" fill="{col}" font-family="Consolas, monospace">{escape(s)}</text>'
        centers.append((x + w / 2, col)); x += w + 18
    for k, ((cxx, col), (_, _, lab)) in enumerate(zip(centers, q)):
        ly = 120 if k == 1 else 102
        b += line(cxx, 72, cxx, ly - 13, col, 1.4) + t(0 if k == 0 else cxx, ly, lab, 10.5, 700, col, 'start' if k == 0 else 'middle')
    return svg(126, b, 'Anatomie d\'une requête d\'alerte')


def traitement():
    items = [('Filtrer', 'Écarter ce qui ne sert aucun axe'), ('Vérifier', 'Remonter à la source primaire, dater, recouper'),
             ('Catégoriser', 'Ranger dans la taxonomie'), ('Analyser', 'Dire ce que cela change pour nous'),
             ('Consigner', 'Écrire la fiche dans la base')]
    b = flow(items, y=2, h=62, gap=20, size=10)
    return svg(68, b, 'Les cinq étapes du traitement, dans l\'ordre')


def signaux():
    b = arrow(40, 150, 40, 8, SLATE, 1.2) + arrow(40, 150, 690, 150, SLATE, 1.2)
    b += f'<text x="30" y="80" font-size="10" fill="{SLATE}" font-style="italic" text-anchor="middle" transform="rotate(-90 30 80)">certitude</text>'
    b += t(690, 164, 'temps', 10, 400, SLATE, 'end', True)
    b += f'<path d="M45,138 C260,136 300,120 360,80 S520,22 680,20" fill="none" stroke="{TEAL}" stroke-width="3"/>'
    b += f'<path d="M300,118 C350,114 390,122 430,126" fill="none" stroke="{PALE}" stroke-width="2.4" stroke-dasharray="5 4"/>'
    b += t(330, 142, '… ou s\'éteindre', 10, 400, SLATE, italic=True)
    b += card(56, 14, 250, 66, 'Signal faible : surveiller, documenter', 'Une ou deux sources, souvent informelles. Échéance inconnue ou lointaine.', MIST, n=46)
    b += card(450, 62, 240, 74, 'Signal fort : décider, planifier, agir', 'Plusieurs sources, dont une primaire. Échéance connue, souvent proche.', TEAL_L, n=46)
    return svg(168, b, 'Un signal faible peut se confirmer en signal fort')


def echelle_impact():
    cw = W / 19; b = ''
    for s in range(19):
        f = MIST if s <= 7 else (AMB_L if s <= 13 else '#e8b9b3')
        b += rect(s * cw + 1, 22, cw - 2, 24, f, rx=3) + t(s * cw + cw / 2, 39, str(s), 10.5, 700, PET, 'middle')
    for a, z, lab, txt in [(0, 7, '7 ou moins', 'Archiver sans diffuser'), (8, 13, '8 à 13', 'Garder pour la prochaine revue de veille'),
                           (14, 18, '14 ou plus', 'Diffuser vite et étudier une recommandation')]:
        x, w = a * cw + 2, (z - a + 1) * cw - 4
        b += t(x + w / 2, 15, lab, 11, 700, PET, 'middle') + line(x, 52, x + w, 52, TEAL, 2)
        b += tl(x + w / 2, 68, txt, int(w / 5.3), 10.5, 700 if a == 14 else 400, BRICK if a == 14 else INK, 'middle')[0]
    return svg(94, b, 'Trois seuils pour agir selon le total sur 18')


def radar():
    cx, cy = 175, 118; rings = [('Adopter', 33, '#a9cfcb'), ('Essayer', 61, TEAL_L), ('Évaluer', 89, MIST), ('Suspendre', 117, '#f3e3e3')]
    b = ''
    for name, r, f in reversed(rings):
        b += f'<path d="M{cx - r},{cy} A{r},{r} 0 0 1 {cx + r},{cy} Z" fill="{f}" stroke="#fff" stroke-width="2"/>'
    prev = 0
    for name, r, f in rings:
        b += t(cx, cy - (prev + r) / 2 + 4, name, 11, 700, PET, 'middle'); prev = r
    meaning = ['À utiliser par défaut quand c\'est pertinent', 'À tester sur un projet réel dont le risque est maîtrisé',
               'À explorer pour comprendre ce que cela apporterait', 'À ne plus utiliser pour de nouveaux travaux']
    for i, ((name, r, f), m) in enumerate(zip(rings, meaning)):
        y = 20 + i * 27
        b += rect(345, y - 12, 14, 14, f, PALE, 3, 1) + t(367, y, name, 11.5, 700, PET) + t(440, y, m, 10.5)
    return svg(120, b, 'Les quatre anneaux du radar technologique')


def matrice_impact_maturite():
    cells = [[('Préparer', 'Surveiller de près'), ('Agir', 'Étudier une recommandation')],
             [('Ignorer pour l\'instant', ''), ('Opportunité ponctuelle', 'Utiliser si l\'occasion se présente, sans projet dédié')]]
    return svg(146, matrix('Maturité', 'Impact', ['Maturité faible', 'Maturité forte'], ['Impact fort', 'Impact faible'], cells,
                           [[AMB_L, '#e8b9b3'], [MIST, TEAL_L]], h=146, n=56), 'La matrice impact × maturité')


def matrice_importance_urgence():
    cells = [[('Priorité 2', 'Suivi régulier'), ('Priorité 1', 'Suivi continu, alerte immédiate')],
             [('Priorité 4', 'Surveillance occasionnelle'), ('Priorité 3', 'Suivi léger')]]
    return svg(140, matrix('Urgence', 'Importance', ['Urgence faible', 'Urgence forte'], ['Importance forte', 'Importance faible'], cells,
                           [[AMB_L, '#e8b9b3'], [MIST, TEAL_L]], h=140, n=50), 'La matrice importance × urgence')


def matrice_valeur_effort():
    cells = [[('Gains rapides', 'À lancer en premier'), ('Projets structurants', 'À planifier')],
             [('Compléments', 'Si l\'occasion se présente'), ('À écarter ou à reformuler', '')]]
    return svg(118, matrix('Effort', 'Valeur', ['Effort faible', 'Effort fort'], ['Valeur forte', 'Valeur faible'], cells,
                           [['#a9cfcb', AMB_L], [TEAL_L, MIST]], h=118, n=50), 'La matrice valeur × effort')


def environnement():
    b = ''; x0 = 330; scale = 330 / 5
    rows = [('Part du numérique dans l\'empreinte carbone, 2020', 2.5, '2,5 %', TEAL),
            ('Même part, mise à jour publiée en 2025 (données 2022), en comptant aussi les centres de données situés à l\'étranger', 4.4, '4,4 %', BRICK)]
    for i, (lab, v, vs, col) in enumerate(rows):
        y = 6 + i * 44
        b += tl(0, y + 13, lab, 60, 10.3)[0]
        b += rect(x0, y + 2, v * scale, 24, col, rx=3) + t(x0 + v * scale + 6, y + 19, vs, 12.5, 700, col)
    b += t(x0, 102, '0 %', 9.5, 400, SLATE, 'middle') + t(x0 + 5 * scale, 102, '5 %', 9.5, 400, SLATE, 'middle') + line(x0, 92, x0 + 5 * scale, 92, PALE)
    y = 114
    b += tl(0, y + 14, 'Part des terminaux dans l\'empreinte du numérique (étude de 2020)', 60, 10.3)[0]
    b += rect(x0, y + 2, 330 * .8, 24, AMB, rx=3) + rect(x0 + 330 * .8, y + 2, 330 * .2, 24, PALE, rx=3)
    b += t(x0 + 8, y + 19, 'terminaux : près de 80 %', 11, 700, INK) + t(x0 + 330 * .9, y + 19, 'le reste', 9.5, 400, SLATE, 'middle')
    return svg(144, b, 'Ordres de grandeur de l\'empreinte du numérique')


def statuts():
    items = [('À confirmer', 'La source primaire n\'est pas encore trouvée'), ('Vérifiée', 'La source primaire est trouvée et, si besoin, recoupée'),
             ('Diffusée', 'La fiche a nourri au moins un livrable'), ('Archivée', 'L\'information est dépassée (mais reste consultable)')]
    return svg(76, flow(items, y=2, h=70, fills=[AMB_L, TEAL_L, '#a9cfcb', MIST], size=10.2), 'Le cycle de vie d\'une fiche')


def reglement_directive():
    b = t(0, 14, 'Règlement', 12.5, 700, PET) + t(0, 28, 'ex. RGPD, AI Act, Data Act', 10, 400, SLATE, italic=True)
    b += card(150, 2, 150, 36, 'Texte européen', '', MIST) + arrow(303, 20, 437, 20)
    b += card(440, 2, 260, 36, 'S\'applique directement, partout', '', TEAL_L, n=40)
    b += t(150, 54, 'Pour le veilleur : suivre le calendrier et les textes d\'application', 10.3, 400, INK, italic=True)
    y = 70
    b += t(0, y + 14, 'Directive', 12.5, 700, PET) + t(0, y + 28, 'ex. NIS2', 10, 400, SLATE, italic=True)
    b += card(150, y + 2, 150, 36, 'Texte européen', '', MIST) + arrow(303, y + 20, 337, y + 20)
    b += card(340, y + 2, 190, 36, 'Transposition par pays', '', AMB_L) + arrow(533, y + 20, 567, y + 20)
    b += card(570, y + 2, 130, 36, 'Puis s\'applique', '', TEAL_L)
    b += t(150, y + 54, 'Pour le veilleur : suivre la transposition dans chaque pays concerné', 10.3, 400, INK, italic=True)
    y = 146
    b += line(0, y, W, y, PALE, 1, '3 3')
    b += t(0, y + 22, 'Autre piège', 12.5, 700, BRICK)
    b += arrow(150, y + 30, 690, y + 30, SLATE, 1.2)
    b += f'<circle cx="190" cy="{y + 30}" r="6" fill="{TEAL}"/>' + t(190, y + 18, 'Entrée en vigueur : le texte existe', 10.5, 700, TEAL, 'middle')
    b += f'<circle cx="590" cy="{y + 30}" r="6" fill="{BRICK}"/>' + t(590, y + 18, 'Application : les obligations sont exigibles', 10.5, 700, BRICK, 'middle')
    b += t(390, y + 46, 'parfois plusieurs années d\'écart', 10.3, 400, SLATE, 'middle', True)
    return svg(200, b, 'Règlement ou directive, entrée en vigueur ou application')


def timeline(events, h, y_axis, x0=20, x1=680, m0=0, m1=48, label=''):
    """events = [(month index, date, text, above?, anchor)]."""
    sx = lambda m: x0 + (x1 - x0) * (m - m0) / (m1 - m0)
    b = line(x0 - 10, y_axis, x1 + 10, y_axis, SLATE, 2)
    for ev in events:
        m, d, txt, above, anc = ev[:5]; n = ev[5] if len(ev) > 5 else (30 if above else 34)
        x = sx(m)
        b += f'<circle cx="{x:.1f}" cy="{y_axis}" r="5.5" fill="{TEAL}"/>'
        if above:
            ls = wrap(txt, n); y = y_axis - 12 - len(ls) * 12.5
            b += line(x, y_axis - 6, x, y_axis - 10, TEAL)
            b += t(x, y - 4, d, 10.8, 700, PET, anc) + ''.join(t(x, y + 9 + i * 12.5, l, 10, 400, INK, anc) for i, l in enumerate(ls))
        else:
            ls = wrap(txt, n)
            b += t(x, y_axis + 22, d, 10.8, 700, PET, anc) + ''.join(t(x, y_axis + 35 + i * 12.5, l, 10, 400, INK, anc) for i, l in enumerate(ls))
    return svg(h, b, label)


def ai_act():
    ev = [(0, '1er août 2024', 'Entrée en vigueur', True, 'start'),
          (6, '2 février 2025', 'Pratiques interdites ; maîtrise de l\'IA, c\'est-à-dire former le personnel qui utilise des systèmes d\'IA (article 4, obligation assouplie en 2026 : à vérifier sur EUR-Lex)', False, 'start'),
          (12, '2 août 2025', 'Modèles d\'IA à usage général (comme ceux des assistants conversationnels)', True, 'start'),
          (24, '2 août 2026', 'Application générale, transparence', False, 'start', 20),
          (40, '2 décembre 2027', 'Haut risque, annexe III (usages sensibles : emploi, éducation, accès aux services essentiels…)', True, 'middle'),
          (48, '2 août 2028', 'Haut risque, annexe I (produits réglementés, dont dispositifs médicaux)', False, 'end')]
    return timeline(ev, 196, 82, label='Le calendrier de l\'AI Act')


def textes_cyber():
    ev = [(0, '17 octobre 2024', 'NIS2 : transposition due ; loi « Résilience » en attente', True, 'start'),
          (11, '12 septembre 2025', 'Data Act : applicable', False, 'middle'),
          (23, '11 septembre 2026', 'CRA : signalement des failles exploitées', True, 'middle'),
          (38, '11 décembre 2027', 'CRA : autres obligations', False, 'end')]
    return timeline(ev, 94, 54, m1=38, label='Dates repères de NIS2, du Data Act et du CRA')


def reseau():
    b = card(0, 30, 190, 58, 'Correspondant', 'Signale une information du terrain', MIST)
    b += card(255, 30, 190, 58, 'Veilleur', 'Vérifie, rédige, diffuse', TEAL_L)
    b += card(510, 30, 190, 58, 'Décideur', 'S\'en sert pour décider', AMB_L)
    b += arrow(193, 59, 252, 59) + arrow(448, 59, 507, 59)
    b += f'<path d="M605,90 C605,128 95,128 95,94" fill="none" stroke="{AMB}" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#ar)"/>'
    b += t(350, 136, 'Le retour : dire au correspondant à quoi son signalement a servi', 11, 700, PET, 'middle')
    b += t(350, 18, 'Animer le réseau : rendre la contribution facile', 11, 700, SLATE, 'middle')
    return svg(142, b, 'Animer le réseau de correspondants')


def recommandation():
    items = [('Information de veille', 'Le point de départ'), ('Problème', 'Celui de l\'organisation'),
             ('Solution précise', "Ce qu'on propose, concrètement"), ('Coût estimé', 'Un ordre de grandeur'),
             ('Indicateur de réussite', 'Comment on saura que c\'est réussi')]
    return svg(64, flow(items, y=2, h=60, gap=18, fills=[MIST, TEAL_L, TEAL_L, TEAL_L, AMB_L], size=10), 'Les éléments d\'une recommandation exploitable')


def ia_piste():
    items = [('Réponse de l\'IA', 'Une piste, jamais une source'), ('Document d\'origine', 'L\'ouvrir et le lire'),
             ('Vérification', 'Le fait y figure-t-il vraiment ?'), ('Citation', 'On cite le document, pas l\'IA')]
    return svg(64, flow(items, y=2, h=60, fills=[AMB_L, MIST, TEAL_L, '#a9cfcb'], size=10.2), 'Ce qu\'on fait d\'une réponse d\'IA')


def intersession():
    b = card(0, 22, 120, 70, 'Semaine S1', 'Cours, dispositif mis en place', TEAL_L, n=20)
    for i in range(3):
        x = 140 + i * 148
        b += card(x, 22, 132, 70, f'Période {i + 1}', '2 séances datées et 1 capture par outil', MIST, n=24)
    b += card(588, 22, 112, 70, 'S2, jour 1', 'Contrôle : 3 veilles flash', AMB_L, n=19)
    for x in (122, 274, 422, 570):
        b += arrow(x, 57, x + 16, 57)
    b += line(140, 12, 572, 12, PALE, 1) + t(356, 8, 'en entreprise, environ une semaine par période', 10, 400, SLATE, 'middle', True)
    return svg(96, b, 'L\'intersession entre S1 et S2')


FIGS = {'activites-temps': activites_temps, 'escalier': escalier, 'cycle': cycle, 'push-pull': push_pull, 'remonter': remonter,
        'echelle-fiabilite': echelle_fiabilite, 'circuit': circuit, 'requete': requete, 'traitement': traitement, 'signaux': signaux,
        'echelle-impact': echelle_impact, 'radar': radar, 'matrice-impact-maturite': matrice_impact_maturite,
        'matrice-importance-urgence': matrice_importance_urgence, 'matrice-valeur-effort': matrice_valeur_effort,
        'environnement': environnement, 'statuts': statuts, 'reglement-directive': reglement_directive, 'ai-act': ai_act,
        'textes-cyber': textes_cyber, 'reseau': reseau, 'recommandation': recommandation, 'ia-piste': ia_piste,
        'intersession': intersession}
