# SVG figures of the veille course (same drawing helpers and palette as the Medisecure figures)
import math
from svgs import T, R, L, svg, INK, QUIET, ACC, ACCBG, AXIS, MUTED, TINT

DARK = '#0b4f6c'; WARN = '#d9480f'; WARNBG = '#fff4e6'; OK = '#2b8a3e'; OKBG = '#ebfbee'; VIO = '#5f3dc4'; VIOBG = '#f3f0ff'


def defs():
    return ('<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{ACC}"/></marker>'
            '<marker id="ahq" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{QUIET}"/></marker></defs>')


def arrow(x1, y1, x2, y2, stroke=ACC, sw=1.6, dash=None, quiet=False):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d} marker-end="url(#{"ahq" if quiet else "ah"})"/>'


def wrap(s, n):
    out, cur = [], ''
    for w in s.split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur); cur = w
        else:
            cur = f'{cur} {w}'.strip()
    return out + [cur] if cur else out


def lines(x, y, s, n, size=11.5, w=400, fill=INK, anchor='start', lh=15):
    return ''.join(T(x, y + i * lh, t, size, w, fill, anchor) for i, t in enumerate(wrap(s, n)))


def cycle_veille():
    steps = [('Expression du besoin', 'Qui a besoin de quoi ?', '1-2'),
             ('Ciblage', 'Où chercher ?', '3'),
             ('Collecte', 'Comment recueillir ?', '3'),
             ('Traitement et analyse', "Qu'est-ce que cela change ?", '4'),
             ('Diffusion', 'À qui le dire et sous quelle forme ?', '5'),
             ('Capitalisation', 'Comment le retrouver ?', '5'),
             ('Évaluation et ajustement', 'La veille a-t-elle servi ?', '7')]
    cx, cy, rx, ry = 380, 318, 268, 212
    b = [defs(), T(24, 30, 'Le cycle de la veille : sept étapes qui tournent autour de la décision', 15, 600),
         T(24, 50, 'En violet, la partie du dossier D1 où chaque étape est attendue', 11.5, 400, QUIET),
         f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{ACC}" stroke-width="2"/>']
    ang = [-90 + i * 360 / 7 for i in range(7)]
    for i in range(7):  # arrowheads half-way between two steps, tangent to the ellipse
        a = math.radians(ang[i] + 180 / 7)
        x, y = cx + rx * math.cos(a), cy + ry * math.sin(a)
        rot = math.degrees(math.atan2(ry * math.cos(a), -rx * math.sin(a)))
        b.append(f'<path d="M-7,-6 L7,0 L-7,6 z" fill="{ACC}" transform="translate({x:.1f},{y:.1f}) rotate({rot:.1f})"/>')
    # shortcut 7 -> 2: adjust the sources without redoing the whole framing
    b.append(f'<path d="M206,224 Q380,298 554,224" fill="none" stroke="{QUIET}" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#ahq)"/>')
    b.append(R(250, 251, 260, 19, '#ffffff', 'none', 0, 9))
    b.append(T(380, 264.5, 'réajuster les sources sans refaire le cadrage', 11, 400, QUIET, 'middle'))
    b.append(f'<circle cx="{cx}" cy="{cy + 14}" r="58" fill="{DARK}"/>')
    b.append(T(cx, cy + 19, 'Décision', 17, 700, '#ffffff', 'middle'))
    bw, bh = 196, 82
    for i, (name, q, part) in enumerate(steps):
        a = math.radians(ang[i])
        x, y = cx + rx * math.cos(a) - bw / 2, cy + ry * math.sin(a) - bh / 2
        b.append(R(x, y, bw, bh, '#ffffff', ACC, 1.5, 10))
        b.append(f'<circle cx="{x + 18}" cy="{y + 20}" r="11" fill="{ACC}"/>')
        b.append(T(x + 18, y + 24.5, str(i + 1), 12, 700, '#ffffff', 'middle'))
        b.append(T(x + 36, y + 25, name, 13, 600))
        b.append(lines(x + 12, y + 46, q, 32, 11.5, 400, QUIET))
        b.append(R(x + bw - 92, y + bh - 9, 84, 18, VIOBG, VIO, 1, 9))
        b.append(T(x + bw - 50, y + bh + 4, f'D1 · partie {part}', 10.5, 600, VIO, 'middle'))
    return svg(580, b)


def matrice_priorisation():
    x0, y0, w, h = 110, 74, 600, 340
    xm, ym = x0 + w / 2, y0 + h / 2
    b = [T(24, 30, 'Priorisation des axes de veille de Kestrel Logistique', 15, 600),
         T(24, 50, "Chaque axe est placé selon l'importance de son impact et la proximité de ses échéances", 11.5, 400, QUIET),
         R(xm, y0, w / 2, h / 2, '#fff1f0', 'none', 0, 0), R(x0, y0, w / 2, h / 2, WARNBG, 'none', 0, 0),
         R(xm, ym, w / 2, h / 2, ACCBG, 'none', 0, 0), R(x0, ym, w / 2, h / 2, TINT, 'none', 0, 0),
         R(x0, y0, w, h, 'none', AXIS, 1.25, 0), L(xm, y0, xm, y0 + h, AXIS), L(x0, ym, x0 + w, ym, AXIS)]
    quads = [(x0 + w - 12, ym - 26, 'Priorité 1', 'suivi continu et alerte immédiate', 'end', '#c92a2a'),
             (x0 + 12, ym - 26, 'Priorité 2', 'suivi régulier et analyse approfondie', 'start', WARN),
             (x0 + w - 12, y0 + h - 30, 'Priorité 3', 'suivi léger, traitement rapide', 'end', ACC),
             (x0 + 12, y0 + h - 30, 'Priorité 4', 'surveillance occasionnelle', 'start', QUIET)]
    for x, y, t, s, anc, col in quads:
        b += [T(x, y, t, 12.5, 700, col, anc), T(x, y + 16, s, 11.5, 400, col, anc)]
    axes = [(0.86, 0.88, 'Cybersécurité de la plateforme', 'left'), (0.70, 0.74, 'Réglementation (RGPD, NIS2, AI Act)', 'left'),
            (0.30, 0.82, 'Technologies et IA', 'right'), (0.36, 0.40, 'Numérique responsable', 'left'),
            (0.62, 0.38, 'Concurrents (axe libre)', 'right')]
    for i, (u, v, name, side) in enumerate(axes):
        x, y = x0 + u * w, y0 + h - v * h
        b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="{DARK}" stroke="#ffffff" stroke-width="2"/>')
        b.append(T(x - 16 if side == 'left' else x + 16, y + 4.5, name, 12.5, 600, INK, 'end' if side == 'left' else 'start'))
    b += [T(x0, y0 + h + 22, 'faible', 11.5, 400, QUIET), T(x0 + w, y0 + h + 22, 'forte', 11.5, 400, QUIET, 'end'),
          T(xm, y0 + h + 24, 'Urgence (proximité des échéances)  →', 12.5, 600, INK, 'middle'),
          f'<g transform="translate({x0 - 22},{ym}) rotate(-90)">{T(0, 0, "Importance (ampleur de l’impact)  →", 12.5, 600, INK, "middle")}</g>',
          T(x0 - 8, y0 + h, 'faible', 11.5, 400, QUIET, 'end'), T(x0 - 8, y0 + 12, 'forte', 11.5, 400, QUIET, 'end')]
    return svg(452, b)


def radar_kestrel():
    cx, cy, rr = 250, 270, 200
    rings = ['Adopter', 'Essayer', 'Évaluer', 'Suspendre']
    fills = ['#c3e6cb', '#d8f0dd', '#eef8f0', '#f6f7f8']
    b = [T(24, 30, 'Radar technologique de Kestrel Logistique, dernière édition', 15, 600),
         T(24, 50, 'Plus un point est proche du centre, plus la recommandation d’usage est forte', 11.5, 400, QUIET)]
    for k in range(4, 0, -1):
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{k * 50}" fill="{fills[k - 1]}" stroke="#ffffff" stroke-width="2"/>')
    b += [L(cx - rr, cy, cx + rr, cy, '#ffffff', 3), L(cx, cy - rr, cx, cy + rr, '#ffffff', 3)]
    for k, name in enumerate(rings):
        b.append(T(cx + k * 50 + 25, cy - 6, name, 10.5, 600, QUIET, 'middle'))
    b += [T(30, 86, 'Techniques', 13, 700, DARK), T(470, 86, 'Outils', 13, 700, DARK, 'end'),
          T(30, 462, 'Plateformes', 13, 700, DARK), T(470, 462, 'Langages et frameworks', 13, 700, DARK, 'end')]
    pts = [(1, 'Authentification multifacteur', 0, 225, False), (2, 'Solveur libre de tournées OR-Tools', 1, 312, True),
           (3, 'Boîtiers télématiques 4G/5G', 2, 120, True), (4, 'Framework hors support (plateforme de suivi)', 3, 40, False),
           (5, 'Conteneurs en production', 2, 155, False), (6, 'IA de maintenance prédictive', 2, 288, True)]
    quad = {225: 'techniques', 312: 'outils', 288: 'outils', 120: 'plateformes', 155: 'plateformes', 40: 'langages et frameworks'}

    def mark(x, y, new, n, col):
        if new:
            shape = f'<path d="M{x:.1f},{y - 13:.1f} L{x + 12:.1f},{y + 9:.1f} L{x - 12:.1f},{y + 9:.1f} z" fill="{col}"/>'
            return shape + T(x, y + 6, str(n), 11, 700, '#ffffff', 'middle')
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="{col}"/>' + T(x, y + 4, str(n), 11, 700, '#ffffff', 'middle')

    for n, name, ring, a, new in pts:
        r = ring * 50 + 25
        x, y = cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))
        b.append(mark(x, y, new, n, WARN if ring == 3 else DARK))
    lx = 510
    b.append(T(lx, 92, 'Légende', 13, 700))
    y = 124
    for n, name, ring, a, new in pts:
        nl = len(wrap(name, 30))
        b.append(mark(lx + 12, y - 4, new, n, WARN if ring == 3 else DARK))
        b.append(lines(lx + 32, y, name, 30, 12, 600, INK, lh=14))
        b.append(T(lx + 32, y + 14 * nl + 2, f'{rings[ring]} · {quad[a]}', 11, 400, QUIET))
        y += 14 * nl + 28
    y += 4
    b += [mark(lx + 12, y, True, '', QUIET), T(lx + 32, y + 4, 'nouveau dans cette édition', 11, 400, QUIET),
          mark(lx + 12, y + 26, False, '', QUIET), T(lx + 32, y + 30, 'inchangé depuis la précédente', 11, 400, QUIET)]
    return svg(490, b)


def matrice_valeur_effort():
    x0, y0, w, h = 100, 74, 440, 340
    xm, ym = x0 + w / 2, y0 + h / 2
    b = [T(24, 30, 'Prioriser les recommandations de Kestrel Logistique', 15, 600),
         T(24, 50, 'Surface des bulles proportionnelle au coût estimé (ordres de grandeur, hypothèses Kestrel)', 11.5, 400, QUIET),
         R(x0, y0, w / 2, h / 2, OKBG, 'none', 0, 0), R(xm, y0, w / 2, h / 2, ACCBG, 'none', 0, 0),
         R(x0, ym, w / 2, h / 2, TINT, 'none', 0, 0), R(xm, ym, w / 2, h / 2, '#fff1f0', 'none', 0, 0),
         R(x0, y0, w, h, 'none', AXIS, 1.25, 0), L(xm, y0, xm, y0 + h, AXIS), L(x0, ym, x0 + w, ym, AXIS),
         T(x0 + 10, y0 + 20, 'Gains rapides', 12.5, 700, OK), T(x0 + w - 10, y0 + 20, 'Projets structurants', 12.5, 700, ACC, 'end'),
         T(x0 + 10, y0 + h - 12, 'Compléments', 12.5, 700, QUIET), T(x0 + w - 10, y0 + h - 12, 'À écarter', 12.5, 700, '#c92a2a', 'end')]
    recs = [('R1', 'Géolocalisation des chauffeurs mise en conformité', 5, 0.14, 0.76),
            ('R2', 'Pilote du solveur de tournées sur une agence', 27, 0.57, 0.68),
            ('R3', 'Authentification multifacteur généralisée', 8, 0.30, 0.88),
            ('R4', 'Renouvellement des boîtiers télématiques', 120, 0.80, 0.62),
            ('R5', 'Maintenance prédictive par IA', 60, 0.78, 0.24)]
    for code, name, cost, u, v in recs:
        x, y, r = x0 + u * w, y0 + h - v * h, 3.6 * math.sqrt(cost)
        col = '#c92a2a' if v < 0.5 else (OK if u < 0.5 else ACC)
        b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="{col}" fill-opacity="0.75" stroke="#ffffff" stroke-width="2"/>')
        b.append(T(x, y + 4.5, code, 12, 700, '#ffffff', 'middle') if r > 14 else T(x + r + 5, y + 4.5, code, 12, 700, col))
    b += [T(x0, y0 + h + 20, 'faible', 11.5, 400, QUIET), T(x0 + w, y0 + h + 20, 'fort', 11.5, 400, QUIET, 'end'),
          T(xm, y0 + h + 22, 'Effort (coût, durée, difficulté)  →', 12.5, 600, INK, 'middle'),
          f'<g transform="translate({x0 - 20},{ym}) rotate(-90)">{T(0, 0, "Valeur (gains, risques évités)  →", 12.5, 600, INK, "middle")}</g>',
          T(x0 - 6, y0 + h, 'faible', 11.5, 400, QUIET, 'end'), T(x0 - 6, y0 + 12, 'forte', 11.5, 400, QUIET, 'end')]
    lx, y = 566, 92
    b.append(T(lx, y, 'Recommandations', 13, 700)); y += 26
    for code, name, cost, u, v in recs:
        zone = 'à écarter' if v < 0.5 else ('gain rapide' if u < 0.5 else 'projet structurant')
        b.append(T(lx, y, code, 12, 700, DARK))
        b.append(lines(lx + 28, y, name, 24, 11.5, 600, INK, lh=14))
        nl = len(wrap(name, 24))
        b.append(T(lx + 28, y + 14 * nl + 1, f'≈ {cost} k€ · {zone}', 11, 400, QUIET))
        y += 14 * nl + 26
    return svg(452, b)


def tbox(x, y, w, text, fill='#ffffff', stroke=AXIS, n=26, size=11.5, wt=400, col=INK, lh=14.5, pad=9):
    """Box with wrapped text; returns (svg, height)."""
    ls = wrap(text, n); hh = pad * 2 + lh * len(ls) - 3
    return R(x, y, w, hh, fill, stroke, 1.2, 7) + lines(x + 10, y + pad + 10, text, n, size, wt, col, lh=lh), hh


def remonter_source():
    b = [defs(), T(24, 30, 'Remonter la chaîne jusqu’à la source primaire', 15, 600),
         T(24, 50, 'Exemple fictif : une alerte sur des routeurs 4G vue sur LinkedIn par un technicien de Kestrel', 11.5, 400, QUIET)]
    cols = [(24, 'formelle, primaire (producteur)', OK, OKBG), (214, 'formelle, primaire (autorité)', OK, OKBG),
            (404, 'formelle, secondaire', WARN, WARNBG), (594, 'informelle, secondaire', '#c92a2a', '#fff1f0')]
    for x, tag, col, bg in cols:
        b.append(R(x, 78, 150, 20, bg, col, 1, 10)); b.append(T(x + 75, 92, tag, 9.8, 600, col, 'middle'))
    boxes = [(24, 108, 66, 'Bulletin de l’éditeur', 'versions touchées, correctif, contournement'),
             (24, 186, 66, 'Fiche CVE', 'identifiant, description, score CVSS'),
             (214, 108, 144, 'Avis du CERT-FR', 'produits concernés, risque, renvoi vers le bulletin de l’éditeur et la CVE'),
             (404, 108, 144, 'Presse spécialisée', '« Une faille critique touche des routeurs 4G » ; cite l’avis du CERT-FR'),
             (594, 108, 144, 'Post LinkedIn', '« Nouvelle faille critique sur les routeurs 4G, patchez vite ! » ; sans lien')]
    for x, y, hh, title, txt in boxes:
        b.append(R(x, y, 150, hh, '#ffffff', ACC, 1.4, 9))
        b.append(T(x + 10, y + 21, title, 12.5, 700, DARK))
        b.append(lines(x + 10, y + 39, txt, 25, 11, 400, QUIET, lh=14))
    b += [arrow(594, 180, 558, 180, quiet=True), arrow(404, 180, 368, 180, quiet=True),
          arrow(214, 150, 178, 141, quiet=True), arrow(214, 210, 178, 219, quiet=True),
          T(576, 172, 'cite', 10.5, 400, QUIET, 'middle'), T(386, 172, 'cite', 10.5, 400, QUIET, 'middle'), T(196, 176, 'cite', 10.5, 400, QUIET, 'middle'),
          f'<line x1="736" y1="290" x2="34" y2="290" stroke="{ACC}" stroke-width="2.5" marker-end="url(#ah)"/>',
          T(385, 280, 'Le veilleur remonte la chaîne jusqu’à l’origine', 12.5, 600, ACC, 'middle'),
          f'<line x1="34" y1="326" x2="736" y2="326" stroke="{WARN}" stroke-width="2" stroke-dasharray="6 4"/>',
          f'<path d="M736,326 l-10,-6 v12 z" fill="{WARN}"/>',
          T(385, 346, 'L’information se déforme et perd ses précisions à chaque reprise', 12, 600, WARN, 'middle')]
    return svg(362, b)


def circuit_collecte():
    b = [defs(), T(24, 30, 'Le circuit de collecte : tout converge vers un point d’entrée unique', 15, 600),
         T(24, 50, 'Les capteurs travaillent en continu (push) ; le veilleur complète par des recherches ponctuelles (pull)', 11.5, 400, QUIET)]
    xs, w = [24, 212, 400, 588], 150
    heads = ['1. Sources', '2. Capteurs', '3. Point d’entrée unique', '4. Stockage et partage']
    for x, hd in zip(xs, heads):
        b.append(R(x, 66, w, 26, DARK, 'none', 0, 7)); b.append(T(x + w / 2, 84, hd, 12, 700, '#ffffff', 'middle'))
    col1 = ['Institutions : CERT-FR, CNIL, ANS, EUR-Lex…', 'Éditeurs et projets open source', 'Presse spécialisée et experts',
            'Réseaux sociaux professionnels', 'Bases de vulnérabilités (CVE, NVD)']
    col2 = ['Flux RSS', 'Alertes par mots-clés (Google Alerts, Talkwalker Alerts)', 'Newsletters reçues sur une adresse dédiée',
            'Surveillance de pages (changedetection.io)', 'Alertes de dépendances (Dependabot, Renovate)', 'OpenCVE et endoflife.date']
    col4 = ['Base de connaissances (OneNote, SharePoint ou Notion)', 'Références bibliographiques (Zotero)', 'Canal de diffusion (Teams)']
    bottoms = []
    for x, items in ((xs[0], col1), (xs[1], col2), (xs[3], col4)):
        y = 104
        for it in items:
            sv, hh = tbox(x, y, w, it, n=23); b.append(sv); y += hh + 8
        bottoms.append(y)
    # entry point
    x = xs[2]
    b.append(R(x, 104, w, 236, ACCBG, ACC, 1.6, 9))
    b.append(T(x + 10, 126, 'Agrégateur', 13, 700, DARK))
    b.append(lines(x + 10, 144, 'Feedly, Inoreader ou FreshRSS', 23, 11.5, 400, INK))
    b.append(lines(x + 10, 190, 'Un dossier par axe de veille, des règles et des filtres par mots-clés', 23, 11.5, 400, INK))
    b.append(R(x + 10, 244, w - 20, 84, '#ffffff', ACC, 1.2, 7, '4 3'))
    b.append(T(x + w / 2, 263, 'Tri quotidien', 12, 700, ACC, 'middle'))
    for i, (t, c) in enumerate((('garder', OK), ('archiver', QUIET), ('écarter', '#c92a2a'))):
        b.append(T(x + w / 2, 284 + i * 16, t, 11.5, 600, c, 'middle'))
    b += [arrow(176, 210, 210, 210), arrow(364, 210, 398, 210), arrow(552, 210, 586, 210)]
    yb = max(bottoms + [340]) + 22
    b.append(R(xs[1], yb, xs[2] + w - xs[1], 46, TINT, QUIET, 1.2, 9, '5 4'))
    b.append(T(xs[1] + 12, yb + 19, 'Pull', 12, 700, QUIET))
    b.append(T(xs[1] + 12, yb + 36, 'recherches ponctuelles, IA de recherche, tour hebdomadaire', 11, 400, QUIET))
    b.append(arrow(xs[2] + w / 2, yb, xs[2] + w / 2, 343, quiet=True))
    yr = yb + 76
    b.append(f'<path d="M{xs[3] + w / 2},{bottoms[2] - 6} V{yr} H{xs[0] + w / 2} V{bottoms[0] + 2}" fill="none" stroke="{VIO}" stroke-width="1.6" stroke-dasharray="6 4"/>')
    b.append(f'<path d="M{xs[0] + w / 2},{bottoms[0] - 2} l-6,10 h12 z" fill="{VIO}"/>')
    b.append(R(300, yr - 11, 160, 22, '#ffffff', 'none', 0, 8))
    b.append(T(380, yr + 4, 'réévaluation des sources', 11.5, 600, VIO, 'middle'))
    return svg(round(yr + 22), b)


def calendrier_intersession():
    x0, dx = 40, 28.0
    X = lambda d: x0 + d * dx  # d = days after Jour 5 (Friday of week S1)
    b = [T(24, 30, 'L’intersession en un coup d’œil : trois périodes, un dossier, une veille qui tourne', 15, 600),
         T(24, 50, 'Du Jour 5 de la semaine S1 au jour du contrôle ; les dates exactes figurent dans les consignes du dossier D1', 11.5, 400, QUIET)]
    weeks = [(1, 10, 'Période 1 · cadrer et collecter', ACCBG), (10, 17, 'Période 2 · analyser', OKBG), (17, 24, 'Période 3 · diffuser', VIOBG)]
    for a, z, name, bg in weeks:
        b.append(R(X(a), 70, X(z) - X(a) - 2, 196, bg, 'none', 0, 6))
        b.append(T((X(a) + X(z)) / 2, 88, name, 12, 700, DARK, 'middle'))
    b.append(R(X(1) + 4, 102, X(24) - X(1) - 10, 22, ACC, 'none', 0, 11))
    b.append(T(X(1) + 16, 117, 'Veille courante : au moins deux séances datées par période, et des captures de chaque outil', 11.5, 600, '#ffffff'))
    b.append(L(X(0), 290, X(25), 290, AXIS, 1.5))
    for d in range(26):
        b.append(L(X(d), 286, X(d), 294, AXIS))
    for d, t in {0: 'Jour 5', 5: 'période 1', 13: 'période 2', 20: 'période 3', 24: 'contrôle'}.items():
        b.append(T(X(d) + dx / 2, 310, t, 10.5, 600, QUIET, 'middle'))
    miles = [(0, 'Pitch d’étape', DARK, 146, 'start'), (9, 'Parties 1 à 3 rédigées', ACC, 146, 'start'),
             (16, 'Parties 4 et 5 rédigées', OK, 176, 'end'), (22, 'Dépôt conseillé', VIO, 146, 'end'),
             (23, 'Jour du rendu', '#c92a2a', 176, 'end'), (24, 'Contrôle : 3 veilles flash', DARK, 240, 'end')]
    for d, t, col, y, anchor in miles:
        x = X(d) + dx / 2
        b.append(L(x, y + 6, x, 284, col, 1.4, '3 3'))
        b.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{col}"/>')
        b.append(T(x - 10 if anchor == 'end' else x + 10, y + 4, t, 11.5, 600, col, anchor)
                 .replace('<text ', '<text stroke="#ffffff" stroke-width="5" stroke-linejoin="round" paint-order="stroke" '))
    b.append(R(X(11) + 2, 196, X(20) - X(11), 38, '#ffffff', VIO, 1.2, 6))
    b.append(T((X(11) + X(20)) / 2 + 2, 211, 'Partie 6 dès la période 2 ; livrables', 10.5, 600, VIO, 'middle'))
    b.append(T((X(11) + X(20)) / 2 + 2, 226, 'de diffusion et synthèse en période 3', 10.5, 600, VIO, 'middle'))
    return svg(330, b)


def circuit_alerte():
    b = [defs(), T(24, 30, 'Le circuit de traitement d’une alerte de vulnérabilité', 15, 600),
         T(24, 50, 'Six étapes, de la réception à la capitalisation ; la boucle de retour affine les filtres des sources', 11.5, 400, QUIET)]
    W, H = 212, 158
    pos = [(44, 72), (284, 72), (524, 72), (524, 268), (284, 268), (44, 268)]
    steps = [('Réception', 'CERT-FR, CERT Santé, bulletins des éditeurs, catalogue KEV de la CISA'),
             ('Qualification', 'Le produit est-il dans l’inventaire ? La version est-elle concernée ? Est-il exposé à Internet ?'),
             ('Priorisation', 'Score CVSS, présence dans le KEV, probabilité EPSS, exposition, données sensibles'),
             ('Action', 'Correctif ou contournement, puis recherche d’indicateurs de compromission'),
             ('Communication', 'DSI et équipes concernées ; signalement éventuel au CERT Santé ou à la CNIL'),
             ('Capitalisation', 'Fiche de veille, délais mesurés, mise à jour de la base de connaissances')]
    for i, ((x, y), (name, txt)) in enumerate(zip(pos, steps)):
        b.append(R(x, y, W, H, '#ffffff', ACC, 1.5, 10))
        b.append(f'<circle cx="{x + 20}" cy="{y + 22}" r="12" fill="{ACC}"/>')
        b.append(T(x + 20, y + 26.5, str(i + 1), 12, 700, '#ffffff', 'middle'))
        b.append(T(x + 40, y + 27, name, 13.5, 700, DARK))
        b.append(lines(x + 14, y + 52, txt, 34, 11.5, 400, INK, lh=15))
    x, y = pos[1]
    b.append(R(x + 14, y + H - 34, W - 28, 22, TINT, QUIET, 1, 11, '4 3'))
    b.append(T(x + W / 2, y + H - 19, 'non concerné → archivage', 11, 600, QUIET, 'middle'))
    x, y = pos[2]
    px = x + 12
    for t, c, bg, pw in (('24-48 h', '#c92a2a', '#fff1f0', 54), ('15 jours', WARN, WARNBG, 58), ('cycle normal', OK, OKBG, 74)):
        b.append(R(px, y + H - 34, pw, 22, bg, c, 1, 11))
        b.append(T(px + pw / 2, y + H - 19, t, 10.5, 700, c, 'middle'))
        px += pw + 4
    b += [arrow(258, 151, 282, 151), arrow(498, 151, 522, 151), arrow(630, 232, 630, 266),
          arrow(522, 347, 498, 347), arrow(282, 347, 258, 347)]
    b.append(f'<path d="M44,347 H24 V151 H40" fill="none" stroke="{VIO}" stroke-width="1.8" stroke-dasharray="6 4" marker-end="url(#ahv)"/>')
    b.append(f'<g transform="translate(18,250) rotate(-90)">{T(0, 0, "ajuster les filtres", 11, 600, VIO, "middle")}</g>'.replace('<text ', '<text stroke="#ffffff" stroke-width="5" paint-order="stroke" '))
    b[0] = b[0].replace('</defs>', f'<marker id="ahv" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{VIO}"/></marker></defs>')
    return svg(440, b)


FIGS = {'cycle-veille': cycle_veille, 'matrice-priorisation': matrice_priorisation, 'radar-kestrel': radar_kestrel,
        'matrice-valeur-effort': matrice_valeur_effort,
        'remonter-source': remonter_source, 'circuit-collecte': circuit_collecte,
        'ch11-calendrier': calendrier_intersession,
        'circuit-alerte-vulnerabilite': circuit_alerte}
