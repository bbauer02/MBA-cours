# SVG figures of the S2 course, chapters 5 to 11 (same drawing helpers and palette as the S1 figures)
import math
from svgs import T, R, L, svg, INK, QUIET, ACC, ACCBG, AXIS, MUTED, TINT
from cours_figures import defs, arrow, wrap, lines, DARK, WARN, WARNBG, OK, OKBG, VIO, VIOBG

RED = '#c92a2a'; REDBG = '#fff1f0'; BLUE = '#1971c2'; YEL = '#fff3bf'; ORG = '#ffd8a8'; REDC = '#ffc9c9'


def Ti(*a, **k):
    """Italic text."""
    return T(*a, **k).replace('<text ', '<text font-style="italic" ', 1)


def Th(*a, **k):
    """Text with a white halo, readable over lines."""
    return T(*a, **k).replace('<text ', '<text stroke="#ffffff" stroke-width="5" stroke-linejoin="round" paint-order="stroke" ', 1)


def clines(cx, y, s, n, size=11.5, w=400, fill=INK, lh=15):
    return ''.join(T(cx, y + i * lh, t, size, w, fill, 'middle') for i, t in enumerate(wrap(s, n)))


def rot(x, y, s, size=13, w=700, fill=INK, a=-90):
    return f'<g transform="translate({x},{y}) rotate({a})">{T(0, 0, s, size, w, fill, "middle")}</g>'


def path(d, stroke=ACC, sw=1.6, dash=None, marker='ah', fill='none'):
    ds = f' stroke-dasharray="{dash}"' if dash else ''
    mk = f' marker-end="url(#{marker})"' if marker else ''
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{ds}{mk}/>'


def defs2(*cols):
    """defs() plus one arrowhead marker per extra colour, id 'a' + hex."""
    extra = ''.join(f'<marker id="a{c[1:]}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
                    f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>' for c in cols)
    return defs().replace('</defs>', extra + '</defs>')


def carrow(x1, y1, x2, y2, col, sw=1.6, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{sw}"{d} marker-end="url(#a{col[1:]})"/>'


def diamond(cx, cy, hw, hh, fill, stroke, sw=1.5):
    return f'<path d="M{cx},{cy - hh} L{cx + hw},{cy} L{cx},{cy + hh} L{cx - hw},{cy} z" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def hexagon(cx, cy, hw, hh, fill, stroke, sw=1.8):
    k = hh * 0.6
    return (f'<path d="M{cx - hw + k},{cy - hh} L{cx + hw - k},{cy - hh} L{cx + hw},{cy} L{cx + hw - k},{cy + hh} '
            f'L{cx - hw + k},{cy + hh} L{cx - hw},{cy} z" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def bolt(x, y, s=1.0, col=RED):
    """Lightning bolt whose top is at (x, y), about 26 px high at s = 1."""
    p = [(4, 0), (-6, 14), (0, 14), (-4, 26), (8, 9), (2, 9), (6, 0)]
    pts = ' '.join(f'{x + a * s:.1f},{y + b * s:.1f}' for a, b in p)
    return f'<polygon points="{pts}" fill="{col}"/>'


def scissors(x, y, col=WARN, ang=0):
    return (f'<g transform="translate({x},{y}) rotate({ang})">'
            f'<circle r="11" fill="#ffffff" stroke="{col}" stroke-width="1.4"/>'
            f'<line x1="-4" y1="-4" x2="7" y2="4" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>'
            f'<line x1="-4" y1="4" x2="7" y2="-4" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>'
            f'<circle cx="-5.5" cy="-4.5" r="2.4" fill="#ffffff" stroke="{col}" stroke-width="1.4"/>'
            f'<circle cx="-5.5" cy="4.5" r="2.4" fill="#ffffff" stroke="{col}" stroke-width="1.4"/></g>')


def brace(x1, x2, y, h, col, sw=1.6):
    """Horizontal curly brace; ends at y, tip at y + 2h (h < 0: tip upwards)."""
    m = (x1 + x2) / 2; a = abs(h)
    d = (f'M{x1},{y} Q{x1},{y + h} {x1 + a},{y + h} L{m - a},{y + h} Q{m},{y + h} {m},{y + 2 * h} '
         f'Q{m},{y + h} {m + a},{y + h} L{x2 - a},{y + h} Q{x2},{y + h} {x2},{y}')
    return path(d, col, sw, marker=None)


# ---------------------------------------------------------------- ch05
def processus_iso27005():
    b = [defs(), T(24, 30, 'La démarche de gestion des risques selon ISO/IEC 27005:2022', 15, 600),
         T(24, 50, 'L’appréciation reboucle sur le contexte, le traitement sur lui-même ; deux activités accompagnent tout le processus', 11.5, 400, QUIET)]
    top, bot, cx, bx, bw = 72, 716, 380, 170, 420
    b += [R(24, top, 40, bot - top, VIOBG, VIO, 1.2, 8), rot(49, (top + bot) / 2, 'Communication et concertation', 13, 700, VIO),
          R(696, top, 40, bot - top, OKBG, OK, 1.2, 8), rot(721, (top + bot) / 2, 'Surveillance et revue', 13, 700, OK)]

    def step(y, h, title, sub, fill='#ffffff'):
        out = R(bx, y, bw, h, fill, ACC, 1.5, 9) + T(cx, y + (21 if sub else 25), title, 13, 700, DARK, 'middle')
        return out + (T(cx, y + 39, sub, 11.5, 400, QUIET, 'middle') if sub else '')

    b.append(step(top, 52, 'Établissement du contexte', '(périmètre, critères de risque, critère d’acceptation)'))
    b.append(arrow(cx, 124, cx, 146))
    b += [R(120, 148, 520, 238, ACCBG, ACC, 1.2, 10), T(136, 170, 'Appréciation du risque', 13, 700, DARK)]
    for i, (t, s) in enumerate((('Identification', '(approche par les événements ; approche par les biens)'),
                                ('Analyse', '(conséquences, vraisemblance)'),
                                ('Évaluation', '(comparaison aux critères, priorités)'))):
        y = 184 + i * 68
        b.append(step(y, 50, t, s))
        if i < 2:
            b.append(arrow(cx, y + 50, cx, y + 66))
    b.append(arrow(cx, 386, cx, 406))
    b += [diamond(cx, 442, 150, 34, WARNBG, WARN), T(cx, 446.5, 'Appréciation satisfaisante ?', 12.5, 700, WARN, 'middle')]
    b.append(path(f'M{cx - 150},442 H96 V98 H{bx - 2}'))
    b.append(Th(cx - 160, 436, 'non', 12, 700, WARN, 'end'))
    b += [arrow(cx, 476, cx, 504), T(cx + 8, 494, 'oui', 12, 700, OK)]
    b.append(step(506, 52, 'Traitement du risque', '(options, mesures, plan de traitement)'))
    b.append(arrow(cx, 558, cx, 580))
    b += [diamond(cx, 616, 160, 34, WARNBG, WARN), T(cx, 620.5, 'Risques résiduels acceptables ?', 12.5, 700, WARN, 'middle')]
    b.append(path(f'M{cx + 160},616 H664 V532 H{bx + bw + 2}'))
    b.append(Th(cx + 170, 610, 'non', 12, 700, WARN))
    b += [arrow(cx, 650, cx, 674), T(cx + 8, 666, 'oui', 12, 700, OK)]
    b.append(step(676, 40, 'Acceptation du risque', '', OKBG))
    b.append(Ti(24, 744, 'D’après ISO/IEC 27005:2022, schéma simplifié pour le cours', 11.5, 400, QUIET))
    return svg(758, b)


# ---------------------------------------------------------------- ch06
def cinq_ateliers():
    b = [defs(), T(24, 30, 'Les cinq ateliers d’EBIOS Risk Manager et leurs liens', 15, 600),
         T(24, 50, 'Chaque atelier nourrit le suivant ; l’atelier 1 fournit aussi des entrées directes aux ateliers 3, 4 et 5', 11.5, 400, QUIET)]
    w, gap, x0 = 128, 20, 20
    ys = [196, 170, 158, 170, 196]
    h = 64
    ws = [('Cadrage et socle de sécurité', 'valeurs métier, biens supports, événements redoutés, socle'),
          ('Sources de risque', 'couples SR/OV retenus'),
          ('Scénarios stratégiques', 'cartographie de la menace, scénarios stratégiques, mesures sur l’écosystème'),
          ('Scénarios opérationnels', 'graphes d’attaque, vraisemblance'),
          ('Traitement du risque', 'risques initiaux et résiduels, mesures, cadre de suivi')]
    X = [x0 + i * (w + gap) for i in range(5)]
    C = [x + w / 2 for x in X]
    bottoms = []
    for i, ((t, liv), x, y) in enumerate(zip(ws, X, ys)):
        b.append(R(x, y, w, h, ACCBG if i else WARNBG, ACC if i else WARN, 1.5, 9))
        b.append(T(x + 10, y + 19, f'Atelier {i + 1}', 11.5, 700, ACC if i else WARN))
        b.append(lines(x + 10, y + 37, t, 17, 12.5, 700, DARK, lh=15))
        b.append(lines(x + 6, y + h + 17, liv, 21, 11, 400, QUIET, lh=14))
        bottoms.append(y + h + 17 + 14 * (len(wrap(liv, 21)) - 1) + 6)
        if i < 4:
            b.append(arrow(x + w, y + h / 2, X[i + 1] - 2, ys[i + 1] + h / 2, sw=2))
    # big cycle arrow 5 -> 1, and operational cycle 5 -> 4
    b.append(path(f'M{X[4] + w - 16},{ys[4] - 2} C{X[4] + w - 16},60 {C[0]},60 {C[0]},{ys[0] - 3}', VIO, 2, marker='a5f3dc4'))
    b.append(Th((X[4] + w - 16 + C[0]) / 2, 82, 'cycle stratégique (quelques années)', 12, 700, VIO, 'middle'))
    b.append(path(f'M{C[4] - 14},{ys[4] - 2} C{C[4] - 14},132 {C[3] + 20},126 {C[3] + 20},{ys[3] - 3}', VIO, 1.6, '5 3', marker='a5f3dc4'))
    b.append(Th(C[3] - 34, 140, 'cycle opérationnel (annuel)', 11.5, 700, VIO, 'middle'))
    # dashed links from workshop 1
    lane = [(2, 'événements redoutés et gravité', C[0] + 36), (3, 'biens supports', C[0]), (4, 'écarts au socle', C[0] - 36)]
    ystart = bottoms[0] + 4
    yl0 = max(bottoms) + 18
    for k, (j, lab, xs) in enumerate(lane):
        yl = yl0 + k * 24
        b.append(path(f'M{xs},{ystart} V{yl} H{C[j]} V{bottoms[j] + 2}', QUIET, 1.4, '5 4', 'ahq'))
        lx = (xs + C[j]) / 2 if j < 4 else (C[1] + C[3]) / 2
        b.append(Th(lx, yl + 4, lab, 11, 600, QUIET, 'middle'))
    yb = yl0 + 2 * 24 + 20
    b += [R(X[0], yb, w, 38, WARNBG, WARN, 1.2, 7), clines(C[0], yb + 16, 'Approche par conformité', 14, 11.5, 700, WARN, 14),
          R(X[1], yb, X[3] + w - X[1], 38, ACCBG, ACC, 1.2, 7), T((X[1] + X[3] + w) / 2, yb + 24, 'Approche par scénarios', 12, 700, ACC, 'middle')]
    yg = yb + 64
    b += [L(24, yg - 4, 54, yg - 4, ACC, 2), f'<path d="M54,{yg - 8} l8,4 l-8,4 z" fill="{ACC}"/>', T(68, yg, 'enchaînement des ateliers', 11.5, 400, QUIET),
          L(250, yg - 4, 290, yg - 4, QUIET, 1.4, '5 4'), T(298, yg, 'résultat de l’atelier 1 repris plus loin', 11.5, 400, QUIET),
          L(540, yg - 4, 580, yg - 4, VIO, 2), T(588, yg, 'cycles de mise à jour', 11.5, 400, QUIET),
          Ti(24, yg + 24, 'D’après le guide EBIOS Risk Manager de l’ANSSI, schéma simplifié pour le cours', 11.5, 400, QUIET)]
    b[0] = defs2(VIO)
    return svg(yg + 40, b)


def _actbox(x, y, w, text, pr, support, thin=False, n=23):
    """Attack-graph action: wrapped text, Pr line, grey footer with the supporting asset. Returns (svg, height)."""
    tl = wrap(text, n); sl = wrap(support, 26)
    hm = 12 + 14.5 * len(tl) + 20
    hf = 8 + 13 * len(sl)
    out = R(x, y, w, hm + hf, '#ffffff', QUIET if thin else ACC, 1 if thin else 1.6, 8, '5 3' if thin else None)
    out += f'<rect x="{x + 1}" y="{y + hm}" width="{w - 2}" height="{hf - 1}" rx="7" fill="{TINT}"/>'
    out += L(x, y + hm, x + w, y + hm, AXIS, 0.8)
    out += ''.join(T(x + 9, y + 20 + i * 14.5, t, 11.5, 400, INK) for i, t in enumerate(tl))
    if pr:
        out += T(x + 9, y + 20 + 14.5 * len(tl) + 3, pr, 11.5, 700, DARK)
    out += ''.join(Ti(x + 9, y + hm + 15 + i * 13, t, 10.8, 400, QUIET) for i, t in enumerate(sl))
    return out, hm + hf


def graphe_attaque_so1():
    b = [defs2(RED, '#868e96'), T(24, 30, 'Graphe d’attaque du scénario opérationnel SO1 de Kestrel Logistique', 15, 600),
         T(24, 50, 'Un attaquant passe par l’accès VPN de l’éditeur de RoutePro pour chiffrer le SI du siège', 11.5, 400, QUIET)]
    cw, bw = 178, 152
    cols = [24 + i * cw for i in range(4)]
    for i, t in enumerate(('Connaître', 'Rentrer', 'Trouver', 'Exploiter')):
        b.append(R(cols[i] + 6, 64, cw - 12, 26, DARK, 'none', 0, 6))
        b.append(T(cols[i] + cw / 2, 82, t.upper(), 12, 700, '#ffffff', 'middle'))
    acts = {'1': (0, 0, 'Reconnaissance en sources ouvertes de l’éditeur de RoutePro et de ses techniciens', '4 (4)', 'PP-05 Éditeur de RoutePro'),
            '2a': (1, 0, 'Hameçonnage d’un technicien de l’éditeur, vol des identifiants VPN', '3 (3)', 'PP-05 Éditeur de RoutePro (poste d’un technicien)'),
            '3': (1, 1, 'Connexion par l’accès VPN permanent de l’éditeur', '4 (3)', 'SEC-01 Passerelle VPN'),
            '2b': (1, 2, 'Achat d’identifiants VPN d’un technicien de l’éditeur sur un forum criminel', '2 (2)', 'PP-05 Éditeur de RoutePro'),
            '4': (2, 0, 'Exploration du réseau du siège, obtention d’un compte d’administration', '3 (3)', 'SRV-01 et SRV-02 Virtualisation'),
            '5': (2, 1, 'Localisation du NAS de sauvegarde', '4 (3)', 'STO-01 NAS de sauvegarde'),
            '6': (3, 0, 'Suppression des sauvegardes du NAS', '4 (3)', 'STO-01 NAS de sauvegarde'),
            '7': (3, 1, 'Chiffrement des 12 machines virtuelles du siège un dimanche à 3 h', '4 (3)', 'SRV-01, SRV-02 ; APP-01 RoutePro, APP-07 ERP finance')}
    hs = {k: _actbox(0, 0, bw, f'{k}. {v[2]}', 'Pr ' + v[3], v[4])[1] for k, v in acts.items()}
    rowh = [max(hs[k] for k, v in acts.items() if v[1] == r) for r in range(3)]
    rowh[2] = max(rowh[2], 86)
    ry = [104]
    for r in range(2):
        ry.append(ry[-1] + rowh[r] + 34)
    pos = {}
    for k, (c, r, t, pr, sup) in acts.items():
        x, y = cols[c] + (cw - bw) / 2, ry[r]
        s, hh = _actbox(x, y, bw, f'{k}. {t}', 'Pr ' + pr, sup, thin=(k == '2b'))
        b.append(s); pos[k] = (x, y, hh)
    ybot = ry[2] + rowh[2] + 16
    for xx in cols[1:]:
        b.append(L(xx, 64, xx, ybot, AXIS, 1.2, '4 4'))

    def right(k, f=0.5): x, y, hh = pos[k]; return x + bw, y + hh * f
    def left(k, f=0.5): x, y, hh = pos[k]; return x, y + hh * f
    def bottom(k): x, y, hh = pos[k]; return x + bw / 2, y + hh
    def top(k): x, y, hh = pos[k]; return x + bw / 2, y

    for a, c in (('1', '2a'),):
        b.append(carrow(*right(a, 0.4), left(c, 0.4)[0] - 2, right(a, 0.4)[1], RED, 2.2))
    for a, c in (('2a', '3'), ('4', '5'), ('6', '7')):
        b.append(carrow(*bottom(a), top(c)[0], top(c)[1] - 2, RED, 2.2))
    for a, c in (('3', '4'), ('5', '6')):
        (xa, ya), (xc, yc) = right(a, 0.35), left(c, 0.3)
        b.append(path(f'M{xa},{ya} H{xa + 6} V{yc} H{xc - 2}', RED, 2.2, marker='ac92a2a'))
    (x1, y1), (x2, y2) = right('1', 0.85), left('2b', 0.4)
    b.append(path(f'M{x1},{y1} H{x1 + 9} V{y2} H{x2 - 2}', '#868e96', 1.6, marker='a868e96'))
    (x2, y2), (x3, y3) = top('2b'), bottom('3')
    b.append(carrow(x2 + 30, y2, x3 + 30, y3 + 2, '#868e96', 1.6))
    # feared event
    hx, hy = cols[3] + cw / 2, ry[2] + 44
    b.append(carrow(*bottom('7'), hx, hy - 42, RED, 2.2))
    b.append(hexagon(hx, hy, 82, 40, REDBG, RED, 2))
    b.append(T(hx, hy - 12, 'ER2 (et ER1)', 13, 700, RED, 'middle'))
    b.append(clines(hx, hy + 5, 'Livraisons arrêtées sur tout le réseau plus de 3 jours · G4', 24, 11, 600, RED, 13))
    # retained likelihood and legend
    ly = ybot + 20
    b += [R(512, ly, 224, 46, REDBG, RED, 1.4, 8), T(624, ly + 19, 'Vraisemblance retenue', 12, 700, RED, 'middle'),
          T(624, ly + 36, 'V3 très vraisemblable', 12, 700, RED, 'middle')]
    b += [L(24, ly + 10, 56, ly + 10, RED, 2.2), T(64, ly + 14, 'mode opératoire le plus vraisemblable (1, 2a, 3, 4, 5, 6, 7)', 11.5, 400, QUIET),
          L(24, ly + 30, 56, ly + 30, '#868e96', 1.6), T(64, ly + 34, 'mode opératoire alternatif (1, 2b, 3), cadre en trait fin', 11.5, 400, QUIET),
          T(24, ly + 56, 'Pr = probabilité de succès de 1 à 4 ; entre parenthèses, indice cumulé', 11.5, 600, INK),
          Ti(24, ly + 74, 'En gris sous chaque action : le bien support visé', 11.5, 400, QUIET)]
    return svg(ly + 88, b)


# ---------------------------------------------------------------- ch07
def surface_data_ia():
    b = [defs2('#868e96'), T(24, 30, 'Les points de vulnérabilité d’une chaîne de données et d’IA', 15, 600),
         T(24, 50, 'Chaque maillon de la chaîne peut laisser fuir ou altérer les données', 11.5, 400, QUIET)]
    blocks = [('Sources', ['applications métier', 'appareils connectés', 'API d’un partenaire'], 'API mal authentifiée'),
              ('Collecte et intégration', ['pipeline', 'export CSV', 'API'], 'export en clair, jamais supprimé'),
              ('Stockage', ['base partagée', 'stockage objet', 'entrepôt'], 'droits trop larges, stockage public, pas de journaux'),
              ('Traitement et IA', ['entraînement', 'modèle', 'LLM'], 'empoisonnement, modèle tiers piégé'),
              ('Restitution', ['tableau de bord BI', 'application'], 'injection de prompt, fuite de données'),
              ('Utilisateurs', ['internes', 'patients ou clients'], 'IA fantôme : flux sortant vers un assistant gratuit')]
    w, gap, x0, y0 = 106, 15.2, 24, 152
    X = [x0 + i * (w + gap) for i in range(6)]
    bh = 0
    for t, items, _ in blocks:
        n = len(wrap(t, 16)) * 15 + sum(len(wrap(it, 16)) * 13.5 + 4 for it in items)
        bh = max(bh, n + 22)
    for i, (t, items, vul) in enumerate(blocks):
        x = X[i]
        b.append(R(x, y0, w, bh, ACCBG if i in (0, 5) else '#ffffff', ACC, 1.6, 9))
        tl = wrap(t, 16)
        b.append(clines(x + w / 2, y0 + 19, t, 16, 12, 700, DARK, 15))
        y = y0 + 19 + 15 * len(tl) + 4
        for it in items:
            for j, ln in enumerate(wrap(it, 16)):
                b.append(T(x + w / 2, y + j * 13.5, ln, 11, 400, QUIET, 'middle'))
            y += len(wrap(it, 16)) * 13.5 + 4
        if i < 5:
            ax = x + w + 1.5
            b.append(f'<path d="M{ax},{y0 + bh / 2 - 5} h5 v-5 l7,10 l-7,10 v-5 h-5 z" fill="{ACC}"/>')
        yv = y0 + bh + 14
        b.append(bolt(x + 16, yv, 1.15))
        b.append(f'<circle cx="{x + 36}" cy="{yv + 13}" r="9" fill="{RED}"/>' + T(x + 36, yv + 17, str(i + 1), 11, 700, '#ffffff', 'middle'))
        b.append(lines(x + 4, yv + 50, vul, 17, 11, 600, RED, lh=14))
    # shadow AI cloud
    cx, cy = 556, 92
    circ = [(cx - 62, cy + 6, 22), (cx - 30, cy - 12, 28), (cx + 12, cy - 16, 30), (cx + 52, cy - 2, 26), (cx + 74, cy + 12, 18),
            (cx - 78, cy + 16, 14), (cx, cy + 10, 30)]
    b.append(''.join(f'<circle cx="{a}" cy="{c}" r="{r}" fill="{TINT}" stroke="{QUIET}" stroke-width="1.4" stroke-dasharray="4 3"/>' for a, c, r in circ))
    b.append(''.join(f'<circle cx="{a}" cy="{c}" r="{r - 1.6}" fill="{TINT}"/>' for a, c, r in circ))
    b.append(f'<rect x="{cx - 80}" y="{cy + 12}" width="160" height="17" fill="{TINT}"/>')
    b.append(T(cx, cy - 2, 'Service d’IA grand public', 12, 700, INK, 'middle'))
    b.append(T(cx, cy + 15, '(hors SI)', 11.5, 400, QUIET, 'middle'))
    ux = X[5] + w / 2
    b.append(path(f'M{ux},{y0 - 2} V{cy + 4} H{cx + 96}', '#868e96', 1.6, '5 4', 'a868e96'))
    b.append(Th(ux - 8, 134, 'flux sortant', 11, 600, QUIET, 'end'))
    # legend
    yl = y0 + bh + 14 + 50 + 4 * 14 + 18
    b += [f'<path d="M24,{yl - 9} h12 v-5 l9,10 l-9,10 v-5 h-12 z" fill="{ACC}"/>', T(54, yl, 'flux de données', 11.5, 400, QUIET),
          bolt(176, yl - 15, 0.75), T(190, yl, 'point de vulnérabilité', 11.5, 400, QUIET),
          L(352, yl - 4, 392, yl - 4, '#868e96', 1.6, '5 4'), T(400, yl, 'flux non inventorié', 11.5, 400, QUIET)]
    return svg(yl + 18, b)


def graphe_attaque_donnees():
    b = [defs(), T(24, 30, 'Graphe d’attaque : vol des données de destinataires de Kestrel Logistique', 15, 600),
         T(24, 50, 'Deux chemins mènent aux mêmes données ; une seule mesure bien placée suffit à couper chacun', 11.5, 400, QUIET)]
    cw, bw = 178, 140
    cols = [24 + i * cw for i in range(4)]
    for i, t in enumerate(('CONNAÎTRE', 'RENTRER', 'TROUVER', 'EXPLOITER')):
        b.append(R(cols[i] + 6, 64, cw - 12, 26, DARK, 'none', 0, 6))
        b.append(T(cols[i] + cw / 2, 82, t, 12, 700, '#ffffff', 'middle'))
    acts = {'rep': (0, 0, 'Repérage du portail public Kestrel Track et de sa version', '4 (4)', 'APP-03 Kestrel Track (portail public)'),
            'rec': (0, 1, 'Recensement des contacts logistiques des clients e-commerçants', '3 (3)', 'réseaux professionnels (hors SI)'),
            'dj': (1, 0, 'Exploitation d’une vulnérabilité de Django 3.2 (hors support)', '2 (2)', 'APP-03 Kestrel Track (Django 3.2)'),
            'ham': (1, 1, 'Hameçonnage d’un compte client du portail B2B (mot de passe seul, H12)', '3 (3)', 'APP-03 Kestrel Track, portail B2B'),
            'pg': (2, 0, 'Accès à la base PostgreSQL de Kestrel Track avec le compte applicatif aux droits complets (H14)', '3 (2)', 'Base PostgreSQL d’APP-03 Kestrel Track'),
            'csv': (2, 1, 'Accès à l’export CSV des livraisons sans limite de volume (H13)', '4 (3)', 'Export CSV du portail B2B d’APP-03'),
            'ext': (3, 0, 'Extraction par lots des nom, adresse et téléphone des destinataires, sans détection (lectures non journalisées, H18)', '3 (3)', 'Base PostgreSQL et export CSV d’APP-03')}

    def box(x, y, t, v, sup, measure=False):
        tl = wrap(t, 21); sl = wrap(sup, 22)
        hm = 14 + 14.5 * len(tl)
        hf = 26 + 13 * len(sl)
        if measure:
            return hm + hf
        out = R(x, y, bw, hm, '#ffffff', ACC, 1.6, 8)
        out += ''.join(T(x + 9, y + 19 + i * 14.5, s, 11.5, 400, INK) for i, s in enumerate(tl))
        col = {'2': OK, '3': WARN, '4': RED}[v[0]]
        out += R(x, y + hm + 6, 62, 17, '#ffffff', col, 1.2, 8) + T(x + 31, y + hm + 18.5, 'Pr ' + v, 10.8, 700, col, 'middle')
        out += ''.join(Ti(x + 2, y + hm + 37 + i * 13, s, 10.8, 400, QUIET) for i, s in enumerate(sl))
        return out

    hs = {k: box(0, 0, v[2], v[3], v[4], True) for k, v in acts.items()}
    r0 = max(hs[k] for k in ('rep', 'dj', 'pg'))
    ry = [106, 106 + r0 + 26]
    pos = {}
    for k, (c, r, t, v, sup) in acts.items():
        x, y = cols[c] + (cw - bw) / 2, ry[r]
        b.append(box(x, y, t, v, sup)); pos[k] = (x, y)
    ex, ey = pos['ext']
    # arrows (box main part top at y, text height ~ 14 + 14.5n)
    hmain = {k: 14 + 14.5 * len(wrap(acts[k][2], 21)) for k in acts}
    def mid(k): return pos[k][1] + min(hmain[k], 74) / 2
    for a, c in (('rep', 'dj'), ('dj', 'pg'), ('rec', 'ham'), ('ham', 'csv')):
        y = min(mid(a), mid(c))
        b.append(arrow(pos[a][0] + bw, y, pos[c][0] - 2, y, sw=1.8))
    b.append(arrow(pos['pg'][0] + bw, mid('pg'), ex - 2, mid('pg'), sw=1.8))
    yc = ey + hmain['ext'] - 14
    b.append(arrow(pos['csv'][0] + bw, mid('csv'), ex - 2, yc, sw=1.8))
    # scissors and their labels
    s1x, s1y = (pos['ham'][0] + bw + pos['csv'][0]) / 2, min(mid('ham'), mid('csv'))
    s2x = (pos['csv'][0] + bw + ex) / 2; s2y = (mid('csv') + yc) / 2
    b += [scissors(s1x, s1y), scissors(s2x, s2y)]
    # final event
    dx, dy = cols[3] + cw / 2, ry[1] + 58
    b.append(arrow(cols[3] + cw / 2, ey + hs['ext'] + 2, dx, dy - 46, sw=1.8))
    b += [diamond(dx, dy, 82, 44, REDBG, RED, 1.8), clines(dx, dy - 4, 'Revente ou campagnes de SMS frauduleux', 16, 11.5, 700, RED, 14)]
    ylab = max(ry[1] + max(hs[k] for k in ('rec', 'ham', 'csv')), dy + 44) + 22
    b += [L(s1x, s1y + 11, s1x, ylab - 12, WARN, 1.2, '3 3'), clines(s1x, ylab, 'coupure : authentification multifacteur du portail', 30, 11.5, 700, WARN, 14),
          L(s2x, s2y + 11, s2x, ylab + 22, WARN, 1.2, '3 3'), clines(s2x + 10, ylab + 34, 'coupure : limitation et journalisation des exports', 30, 11.5, 700, WARN, 14)]
    yl = ylab + 82
    b += [R(24, yl - 12, 28, 16, '#ffffff', ACC, 1.4, 4), T(60, yl, 'action élémentaire', 11.5, 400, QUIET),
          arrow(196, yl - 4, 232, yl - 4), T(240, yl, 'enchaînement', 11.5, 400, QUIET),
          scissors(352, yl - 4), T(370, yl, 'mesure qui coupe le chemin', 11.5, 400, QUIET),
          T(24, yl + 24, 'Sous chaque action : probabilité de succès (Pr, de 1 à 4), indice cumulé entre parenthèses,', 11.5, 400, QUIET),
          T(24, yl + 40, 'et, en italique, le bien support visé', 11.5, 400, QUIET),
          R(24, yl + 56, 224, 46, REDBG, RED, 1.4, 8), T(136, yl + 75, 'Vraisemblance retenue', 12, 700, RED, 'middle'),
          T(136, yl + 92, 'V3, comme SO4 (chapitre 6)', 12, 700, RED, 'middle')]
    return svg(yl + 116, b)


# ---------------------------------------------------------------- ch08
def axe_pdma_dmia_mtpd():
    b = [defs2(BLUE, OK, WARN, RED), T(24, 30, 'PDMA, DMIA et MTPD sur l’axe du temps', 15, 600),
         T(24, 50, 'La PDMA regarde en arrière depuis le sinistre ; la DMIA et la MTPD regardent en avant', 11.5, 400, QUIET)]
    ax, xs, xb, xd, xm = 286, 260, 112, 460, 650
    # degraded mode hatch
    b.append('<defs><pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
             f'<rect width="8" height="8" fill="{TINT}"/><line x1="0" y1="0" x2="0" y2="8" stroke="{MUTED}" stroke-width="3"/></pattern></defs>')
    b.append(R(xs + 4, 236, xd - xs - 6, 46, 'url(#hatch)', MUTED, 1, 4))
    b.append(Th((xs + xd) / 2, 264, 'Mode dégradé', 12, 700, QUIET, 'middle'))
    # MTPD and DMIA braces above
    b += [brace(xs + 2, xm, 156, -9, WARN, 1.8), clines((xs + xm) / 2, 114, 'MTPD : seuil au-delà duquel les impacts deviennent inacceptables', 42, 12, 700, WARN, 15),
          brace(xs + 2, xd, 216, -9, OK, 1.8), clines((xs + xd) / 2, 176, 'Reprise de l’application : doit intervenir avant la DMIA (RTO)', 32, 12, 700, OK, 15)]
    b += [L(xd, 216, xd, ax, OK, 1.6, '4 3'), L(xm, 156, xm, ax, WARN, 1.6, '4 3')]
    # margin
    b += [f'<line x1="{xd + 4}" y1="258" x2="{xm - 4}" y2="258" stroke="{QUIET}" stroke-width="1.4" marker-start="url(#ahq)" marker-end="url(#ahq)"/>',
          Th((xd + xm) / 2, 252, 'marge', 11.5, 700, QUIET, 'middle')]
    # time axis
    b += [f'<line x1="24" y1="{ax}" x2="730" y2="{ax}" stroke="{INK}" stroke-width="2" marker-end="url(#ahq)"/>',
          T(736, ax + 20, 'temps', 11.5, 600, QUIET, 'end')]
    b += [T(xd, ax + 20, 'DMIA', 12, 700, OK, 'middle'), T(xm, ax + 20, 'MTPD', 12, 700, WARN, 'middle')]
    # last backup and lost data
    b += [f'<circle cx="{xb}" cy="{ax}" r="7" fill="{BLUE}" stroke="#ffffff" stroke-width="2"/>',
          clines(xb, 240, 'Dernière sauvegarde utilisable', 18, 11.5, 700, BLUE, 15),
          L(xb, 262, xb, ax - 9, BLUE, 1.2, '3 3'),
          brace(xb, xs - 14, ax + 12, 9, BLUE, 1.8),
          clines((xb + xs - 14) / 2, ax + 52, 'Données perdues : doit rester inférieure à la PDMA (RPO)', 28, 11.5, 700, BLUE, 15)]
    # disaster
    b.append(bolt(xs - 12, ax - 40, 3.0))
    b.append(Th(xs + 14, ax + 44, 'Sinistre', 13, 700, RED))
    # cumulated impact staircase
    y0, y1 = 470, 362
    steps = [(300, 10), (360, 22), (420, 30), (xd, 42), (540, 56), (600, 70), (xm, 96)]
    d = f'M{xs},{y0}'
    for x, v in steps:
        d += f' H{x} V{y0 - v}'
    d += ' H722'
    b += [L(24, y0, 730, y0, AXIS, 1.25), L(xd, ax + 26, xd, y0, OK, 1, '4 3'), L(xm, ax + 26, xm, y0, WARN, 1, '4 3')]
    b.append(f'<path d="{d} V{y0} z" fill="{RED}" fill-opacity="0.08"/>')
    b.append(path(d, RED, 2.2, marker=None))
    b.append(lines(24, 418, 'Impact cumulé (financier, clients, juridique, image)', 30, 12, 700, RED))
    yl = y0 + 30
    b += [R(24, yl - 11, 22, 12, BLUE, 'none', 0, 3), T(54, yl, 'bleu : regard vers le passé (données perdues)', 11.5, 400, QUIET),
          R(352, yl - 11, 22, 12, OK, 'none', 0, 3), R(378, yl - 11, 22, 12, WARN, 'none', 0, 3),
          T(408, yl, 'vert et orange : regard vers l’avenir (durées d’arrêt)', 11.5, 400, QUIET)]
    return svg(yl + 16, b)


def dependances_kestrel():
    b = [defs(), T(24, 30, 'Les dépendances des applications critiques de Kestrel Logistique', 15, 600),
         T(24, 50, 'Ce que la cartographie révèle et que les directions n’avaient pas mentionné', 11.5, 400, QUIET)]
    tiers = [(66, 74, 'Activités'), (156, 128, 'Applications'), (292, 168, 'Infrastructure')]
    for y, h, t in tiers:
        b += [R(16, y, 728, h, TINT, 'none', 0, 10), T(28, y + 17, t.upper(), 11, 700, QUIET)]
    # activities
    acts = [(24, 220, 'Recevoir les ordres de transport'), (256, 192, 'Planifier les tournées'), (536, 200, 'Livrer et prouver la livraison')]
    for x, w, t in acts:
        b += [R(x, 90, w, 40, '#ffffff', DARK, 1.5, 18), T(x + w / 2, 114.5, t, 12, 700, DARK, 'middle')]
    # applications (identifier, name, detail)
    apps = {'edi': (24, 100, ['APP-06', 'Portail EDI', '(prestataire)']), 'rp': (148, 92, ['APP-01', 'RoutePro']),
            'pl': (264, 112, ['APP-09', 'Planification', 'des tournées', '(fichiers Excel)']),
            'kt': (400, 112, ['APP-03', 'Kestrel Track', '(cloud, une zone)']),
            'kd': (536, 96, ['APP-04', 'KDriver', '(terminaux)']), 'sf': (656, 80, ['APP-02', 'StockFlow', '(SaaS)'])}
    ya, ha = 182, 62
    for k, (x, w, ls) in apps.items():
        b.append(R(x, ya, w, ha, '#ffffff', ACC, 1.5, 8))
        names = [t for t in ls[1:] if not t.startswith('(')]
        subs = [t for t in ls[1:] if t.startswith('(')]
        n = 1 + len(names) + len(subs)
        y0 = ya + ha / 2 - (n - 1) * 14 / 2 + 4
        b.append(T(x + w / 2, y0, ls[0], 10.8, 700, ACC, 'middle'))
        for i, t in enumerate(names):
            b.append(T(x + w / 2, y0 + 14 * (i + 1), t, 12.5, 700, INK, 'middle'))
        for i, t in enumerate(subs):
            b.append(T(x + w / 2, y0 + 14 * (len(names) + i + 1), t, 10.8, 400, QUIET, 'middle'))
    cxa = {k: x + w / 2 for k, (x, w, _) in apps.items()}
    b += [arrow(74, 130, 74, ya - 2), arrow(280, 130, 194, ya - 2), arrow(330, 130, 330, ya - 2), arrow(584, 130, 584, ya - 2)]
    ym = ya + ha / 2
    b += [arrow(148, ym, 126, ym), arrow(264, ym, 242, ym), arrow(536, ym, 514, ym)]
    b += [Th(136, ya + ha + 15, '70 % des ordres', 11, 600, ACC, 'middle'),
          Th(525, ya + ha + 15, 'synchro toutes', 11, 600, ACC, 'middle'), Th(525, ya + ha + 28, 'les 2 min', 11, 600, ACC, 'middle')]
    # infrastructure
    yi = 316
    b += [R(24, yi, 352, 128, '#ffffff', RED, 3, 10), T(36, yi + 20, 'SAL-01 Salle serveur du siège', 12.5, 700, INK),
          R(36, yi + 32, 160, 58, '#ffffff', ACC, 1.4, 8), T(116, yi + 55, 'SRV-01 Virtualisation 1', 11.5, 700, INK, 'middle'),
          T(116, yi + 72, 'SRV-02 Virtualisation 2', 11.5, 700, INK, 'middle'),
          R(208, yi + 32, 156, 58, WARNBG, WARN, 3, 8), T(286, yi + 50, 'STO-01 NAS', 12, 700, INK, 'middle'),
          T(286, yi + 65, 'de sauvegarde', 12, 700, INK, 'middle'),
          T(286, yi + 80, '(même pièce)', 11, 400, QUIET, 'middle'),
          T(116, yi + 112, 'point unique de défaillance', 11, 700, RED, 'middle'),
          T(286, yi + 112, 'défaut d’isolement', 11, 700, WARN, 'middle'),
          R(400, yi, 168, 72, '#ffffff', DARK, 2, 10, '6 4'), T(484, yi + 26, 'PP-08 Hébergeur cloud', 12.5, 700, INK, 'middle'),
          T(484, yi + 43, '(une zone)', 11, 400, QUIET, 'middle'), T(484, yi + 62, 'à vérifier', 11, 700, DARK, 'middle'),
          R(584, yi, 152, 104, '#ffffff', RED, 3, 10), T(660, yi + 24, 'Tunnels VPN', 12.5, 700, INK, 'middle'),
          T(660, yi + 41, 'RES-01 VPN Moirans', 11.5, 400, INK, 'middle'), T(660, yi + 56, 'RES-02 VPN Clermont', 11.5, 400, INK, 'middle'),
          T(660, yi + 71, '(sans secours)', 11, 400, QUIET, 'middle'), T(660, yi + 92, 'point unique de défaillance', 11, 700, RED, 'middle')]
    # Microsoft 365, below the cloud host; Planification depends on it
    b += [R(400, yi + 82, 168, 40, '#ffffff', ACC, 1.5, 8), T(484, yi + 101, 'APP-10 Microsoft 365', 12.5, 700, INK, 'middle'),
          T(484, yi + 115, '(SaaS)', 10.8, 400, QUIET, 'middle')]
    b.append(path(f'M370,{ya + ha} V300 H388 V{yi + 102} H398', ACC, 1.6, marker='ah'))
    b.append(arrow(cxa['rp'], ya + ha, cxa['rp'], yi - 3))
    b.append(arrow(cxa['kt'], ya + ha, cxa['kt'], yi - 3))
    yl = 486
    b += [arrow(24, yl - 4, 64, yl - 4), T(72, yl, 'dépend de (de l’élément qui dépend vers celui dont il dépend)', 11.5, 400, QUIET),
          R(470, yl - 13, 34, 16, '#ffffff', RED, 3, 4), T(512, yl, 'point unique de défaillance', 11.5, 400, QUIET)]
    y2 = yl + 24
    b += [R(24, y2 - 13, 34, 16, WARNBG, WARN, 3, 4), T(66, y2, 'défaut d’isolement des sauvegardes (pas un point unique)', 11.5, 400, QUIET),
          R(470, y2 - 13, 34, 16, '#ffffff', DARK, 2, 4, '6 4'), T(512, y2, 'redondance à vérifier', 11.5, 400, QUIET)]
    return svg(y2 + 16, b)


# ---------------------------------------------------------------- ch09
def pestel_forces_si():
    b = [defs(), T(24, 30, 'Le SI au centre de son environnement : PESTEL et cinq forces', 15, 600),
         T(24, 50, 'Chaque facteur de l’environnement agit sur une ou plusieurs ressources du SI', 11.5, 400, QUIET)]
    cx, cy, Ro, Ri = 380, 374, 310, 204
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{Ro}" fill="{VIOBG}" stroke="{VIO}" stroke-width="1.5"/>')
    names = ['Politique', 'Économique', 'Socioculturel', 'Technologique', 'Environnemental', 'Légal']
    angs = [-60, 0, 60, 120, 180, 240]
    for k in range(6):
        a = math.radians(angs[k] - 30)
        b.append(L(cx + Ri * math.cos(a), cy + Ri * math.sin(a), cx + Ro * math.cos(a), cy + Ro * math.sin(a), '#ffffff', 3))
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{Ri}" fill="{ACCBG}" stroke="{ACC}" stroke-width="1.5"/>')
    # central SI
    rw, rh = 196, 124
    rx, ry = cx - rw / 2, cy - rh / 2
    b += [R(rx, ry, rw, rh, '#ffffff', DARK, 2, 9), T(cx, ry + 19, 'Système d’information', 12.5, 700, DARK, 'middle'),
          T(cx, ry + 34, 'de l’organisation', 12.5, 700, DARK, 'middle')]
    cells = ['applications', 'données', 'infrastructure', 'sécurité', 'compétences', 'budget']
    for i, c in enumerate(cells):
        x, y = rx + 8 + (i % 2) * 92, ry + 44 + (i // 2) * 25
        b += [R(x, y, 88, 21, TINT, 'none', 0, 4), T(x + 44, y + 15, c, 11, 400, INK, 'middle')]
    # PESTEL labels and arrows
    for nm, a in zip(names, angs):
        r = (Ri + Ro) / 2
        ar = math.radians(a)
        lx, ly = cx + r * math.cos(ar), cy + r * math.sin(ar)
        b.append(T(lx, ly + 5, nm, 12.5, 700, VIO, 'middle'))
        # arrow end on rectangle border along the ray
        t = min(rw / 2 / abs(math.cos(ar)) if abs(math.cos(ar)) > 1e-6 else 1e9, rh / 2 / abs(math.sin(ar)) if abs(math.sin(ar)) > 1e-6 else 1e9)
        sx, sy = cx + (r - 22) * math.cos(ar), cy + (r - 22) * math.sin(ar)
        if abs(math.cos(ar)) > 0.9:
            sx, sy = cx + (r - 62) * math.cos(ar), cy
        ex, ey = cx + (t + 3) * math.cos(ar), cy + (t + 3) * math.sin(ar)
        b.append(f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{VIO}" stroke-width="1.6" marker-end="url(#av)"/>')
    # five forces
    forces = [('Rivalité entre', 'concurrents', cx, cy - 128, cx, ry - 3),
              ('Nouveaux', 'entrants', cx - 152, cy - 52, rx - 3, cy - 40),
              ('Produits de', 'substitution', cx + 152, cy - 52, rx + rw + 3, cy - 40),
              ('Pouvoir des', 'clients', cx + 120, cy + 98, rx + rw - 30, ry + rh + 3),
              ('Pouvoir des', 'fournisseurs', cx - 120, cy + 98, rx + 30, ry + rh + 3)]
    for l1, l2, x, y, ex, ey in forces:
        b += [T(x, y, l1, 12, 700, ACC, 'middle'), T(x, y + 15, l2, 12, 700, ACC, 'middle')]
        if y < ry - 10:
            sx, sy = x, y + 22
        elif abs(ey - (cy - 40)) < 1:
            sx, sy = (x + 46 if x < cx else x - 46), cy - 40
        else:
            sx, sy = (x + 24 if x < cx else x - 24), y - 14
        b.append(arrow(sx, sy, ex, ey))
    # titles of the two circles
    b += [T(24, 84, 'Macro-environnement :', 12.5, 700, VIO), T(24, 100, 'PESTEL', 12.5, 700, VIO),
          L(120, 106, 176, 150, VIO, 1), f'<circle cx="178" cy="151" r="3" fill="{VIO}"/>',
          T(736, 84, 'Micro-environnement :', 12.5, 700, ACC, 'end'), T(736, 100, 'les cinq forces de Porter', 12.5, 700, ACC, 'end'),
          L(650, 106, 520, 222, ACC, 1), f'<circle cx="520" cy="222" r="3" fill="{ACC}"/>']
    # bottom band
    yb = cy + Ro + 26
    boxes = [('Facteur sourcé', 24, 180), ('Effet écrit sur le SI', 250, 200), ('Opportunité ou menace, niveau 1 à 3', 496, 240)]
    for t, x, w in boxes:
        b += [R(x, yb, w, 40, '#ffffff', DARK, 1.5, 8), T(x + w / 2, yb + 25, t, 12, 700, DARK, 'middle')]
    b += [arrow(204, yb + 20, 248, yb + 20, sw=2), arrow(450, yb + 20, 494, yb + 20, sw=2)]
    yl = yb + 68
    b += [L(24, yl - 4, 60, yl - 4, VIO, 1.6), f'<path d="M60,{yl - 8} l8,4 l-8,4 z" fill="{VIO}"/>',
          L(24, yl + 14, 60, yl + 14, ACC, 1.6), f'<path d="M60,{yl + 10} l8,4 l-8,4 z" fill="{ACC}"/>',
          T(76, yl, 'flèche pleine violette : influence d’un facteur du macro-environnement (PESTEL) sur le SI', 11.5, 400, QUIET),
          T(76, yl + 18, 'flèche pleine pétrole : influence d’une force du micro-environnement sur le SI', 11.5, 400, QUIET)]
    b[0] = defs().replace('</defs>', '<marker id="av" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
                          f'<path d="M0,0 L10,5 L0,10 z" fill="{VIO}"/></marker></defs>')
    return svg(yl + 32, b)


# ---------------------------------------------------------------- ch10
def matrice_impact_urgence():
    b = [T(24, 30, 'Matrice impact × urgence des faiblesses du SI de Kestrel Logistique', 15, 600),
         T(24, 50, 'Score = impact × urgence ; la couleur de la case suit le score', 11.5, 400, QUIET)]
    x0, y0, c = 104, 76, 112
    col = {1: TINT, 2: TINT, 3: YEL, 4: YEL, 6: ORG, 9: REDC}
    for i in range(1, 4):          # impact, bottom to top
        for u in range(1, 4):      # urgency, left to right
            x, y = x0 + (u - 1) * c, y0 + (3 - i) * c
            b.append(R(x, y, c, c, col[i * u], '#ffffff', 2, 0))
            b.append(T(x + c - 8, y + 18, f'score {i * u}', 10.8, 600, QUIET, 'end'))
    b.append(R(x0, y0, 3 * c, 3 * c, 'none', AXIS, 1.25, 0))
    for k in range(1, 4):
        b.append(T(x0 + (k - 0.5) * c, y0 + 3 * c + 20, str(k), 12.5, 700, INK, 'middle'))
        b.append(T(x0 - 12, y0 + (3 - k + 0.5) * c + 5, str(k), 12.5, 700, INK, 'end'))
    b += [T(x0 + 1.5 * c, y0 + 3 * c + 42, 'Urgence  →', 13, 700, INK, 'middle'),
          rot(x0 - 36, y0 + 1.5 * c, 'Impact  →', 13, 700, INK)]

    def dot(i, u, name, dx=0, dy=0):
        x, y = x0 + (u - 0.5) * c + dx, y0 + (3 - i + 0.5) * c + dy
        return f'<circle cx="{x}" cy="{y}" r="17" fill="{DARK}" stroke="#ffffff" stroke-width="2"/>' + T(x, y + 4.5, name, 12, 700, '#ffffff', 'middle')
    b += [dot(3, 3, 'F1', -22, 8), dot(3, 3, 'F7', 22, 8),
          dot(3, 2, 'F2', -22, -6), dot(3, 2, 'F3', 22, -6), dot(3, 2, 'F5', -22, 32), dot(3, 2, 'F6', 22, 32),
          dot(2, 3, 'F4', 0, 6)]
    # legend
    lx = 480
    b.append(T(lx, 92, 'Lecture du score', 13, 700))
    leg = [(REDC, 'score 9 : priorité 1'), (ORG, 'score 6 : priorité 2'), (YEL, 'score 3 ou 4 : priorité 3'), (TINT, 'score 1 ou 2 : à surveiller')]
    for k, (cc, t) in enumerate(leg):
        y = 118 + k * 28
        b += [R(lx, y - 13, 22, 18, cc, AXIS, 1, 3), T(lx + 32, y + 1, t, 12, 600, INK)]
    b += [lines(lx, 248, 'Impact et urgence sont notés de 1 à 3 selon une règle écrite ; le produit donne un score de 1 à 9.', 38, 11.5, 400, QUIET)]
    # list of weaknesses
    fl = [('F1', 'une seule salle serveur, sans site de secours'),('F2', 'sauvegardes dans la salle des serveurs'),
          ('F3', 'accès permanent de l’éditeur et authentification multifacteur limitée aux cadres'),
          ('F4', 'Kestrel Track sur un framework hors support'), ('F5', 'absence d’instance de gouvernance du SI'),
          ('F6', 'planification des tournées sous Excel'), ('F7', 'base de RoutePro hors support')]
    y = y0 + 3 * c + 76
    ys = [y, y]
    for k, (f, t) in enumerate(fl):
        cl = 0 if k < 4 else 1
        x = 24 + cl * 366
        yy = ys[cl]
        b += [f'<circle cx="{x + 12}" cy="{yy - 4}" r="12" fill="{DARK}"/>', T(x + 12, yy, f, 10.5, 700, '#ffffff', 'middle'),
              lines(x + 32, yy, t, 50, 12, 400, INK, lh=15)]
        ys[cl] += 15 * len(wrap(t, 50)) + 14
    return svg(max(ys) + 4, b)


# ---------------------------------------------------------------- ch11
def calendrier_d2():
    # d = days from Jour 5 (a Friday), cell [d, d+1]: 1-2, 8-9, 15-16 are the three week-ends,
    # the deposit closes step 4 (no date limit), 17 stands for the oral, after the deposit
    x0, dx = 24, 39.5
    X = lambda d: x0 + d * dx
    b = [defs(), T(24, 30, 'L’intersession du dossier D2 : un ordre de travail conseillé, du pitch du Jour 5 au dépôt', 15, 600),
         T(24, 50, 'Deux semaines en entreprise, trois week-ends, deux périodes, quatre étapes ; adaptez les durées à votre rythme, gardez l’ordre', 11.5, 400, QUIET)]
    yt, yf, hf = 74, 168, 50
    for a in (1, 8, 15):   # week-ends
        b.append(R(X(a), yt, 2 * dx, yf + hf - yt, '#e9ecef', 'none', 0, 0))
        b.append(T(X(a) + dx, yt + 12, 'week-end', 10.5, 600, QUIET, 'middle'))
    for a, t in ((3, '1re semaine en entreprise'), (10, '2e semaine en entreprise')):
        b.append(T(X(a + 2.5), yt + 12, t, 10.5, 400, QUIET, 'middle'))
    b += [R(X(0) + 2, 94, X(18) - X(0) - 4, 22, DARK, 'none', 0, 11),
          T((X(0) + X(18)) / 2, 109, 'registre des hypothèses tenu au fil de l’eau', 11.5, 600, '#ffffff', 'middle'),
          R(X(14) + 2, 124, X(18) - X(14) - 4, 22, VIO, 'none', 0, 11),
          T((X(14) + X(18)) / 2, 139, 'préparation de la restitution', 11.5, 600, '#ffffff', 'middle')]
    # frieze
    b += [R(X(0), yf, dx, hf, DARK, 'none', 0, 6), T(X(0.5), yf + 22, 'Jour 5', 10.5, 700, '#ffffff', 'middle'),
          T(X(0.5), yf + 37, 'pitch', 10.5, 400, '#ffffff', 'middle'),
          R(X(1) + 2, yf, 9 * dx - 2, hf, ACCBG, ACC, 1.4, 6), R(X(10) + 2, yf, 7 * dx - 4, hf, OKBG, OK, 1.4, 6),
          T(X(5.5), yf + 20, 'Période 1 : cartographier', 12.5, 700, ACC, 'middle'),
          T(X(13.5), yf + 20, 'Période 2 : analyser, diagnostiquer, déposer', 12.5, 700, OK, 'middle'),
          R(X(17), yf, dx, hf, VIO, 'none', 0, 6), T(X(17.5), yf + 22, 'oral', 10.5, 700, '#ffffff', 'middle')]
    for a, z, t, colr in ((1, 5, 'étape 1', ACC), (5, 10, 'étape 2', ACC), (10, 14, 'étape 3', OK), (14, 17, 'étape 4', OK)):
        b.append(T(X((a + z) / 2), yf + 39, t, 11, 400, colr, 'middle'))
    b += [L(X(5), yf + 26, X(5), yf + hf - 2, ACC, 1.2, '3 3'), L(X(14), yf + 26, X(14), yf + hf - 2, OK, 1.2, '3 3'),
          L(X(10) + 1, yf - 14, X(10) + 1, yf + hf + 8, INK, 4)]
    # milestones: one row of boxes, fan of leader arrows
    ms = [(5, 'annexes A et B, quatre vues', ACC), (10, 'sept vues version 1.0, annexes C et D, gel des noms, point à mi-parcours', INK),
          (14, 'parties 3 et 4, annexes E et F, section 5.1', OK), (14.6, 'partie 5, partie 6, synthèse, annexes G et H', OK),
          (16.6, 'dépôt sur Moodle', WARN), (17.5, 'restitution orale (après le dépôt)', VIO)]
    bw, gap, yb = 112, 8.6, 290
    hb = max(len(wrap(t, 15)) for _, t, _ in ms) * 14 + 14
    for k, (d, t, colr) in enumerate(ms):
        bx = x0 + k * (bw + gap)
        b.append(R(bx, yb, bw, hb, '#ffffff', colr, 1.4, 7))
        b.append(clines(bx + bw / 2, yb + 18, t, 15, 11, 600, colr, 14))
        b.append(f'<line x1="{bx + bw / 2}" y1="{yb - 2}" x2="{X(d)}" y2="{yf + hf + 4}" stroke="{colr}" stroke-width="1.3" marker-end="url(#ahq)"/>')
    return svg(yb + hb + 16, b)


FIGS = {'c05-processus-iso27005': processus_iso27005,
        'c06-cinq-ateliers': cinq_ateliers, 'c06-graphe-attaque-kestrel': graphe_attaque_so1,
        'c07-surface-data-ia': surface_data_ia, 'c07-graphe-attaque-kestrel': graphe_attaque_donnees,
        'c08-axe-pdma-dmia-mtpd': axe_pdma_dmia_mtpd, 'c08-dependances-kestrel': dependances_kestrel,
        'c09-pestel-forces-si': pestel_forces_si, 'c10-matrice-impact-urgence': matrice_impact_urgence,
        'c11-calendrier': calendrier_d2}
