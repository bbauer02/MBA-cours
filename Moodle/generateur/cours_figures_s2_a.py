# SVG figures of the S2 course, chapters 0 to 4 (same drawing helpers and palette as cours_figures.py)
import re
from html import escape
from svgs import T, R, L, svg, INK, QUIET, ACC, ACCBG, AXIS, MUTED, TINT
from frtypo import fr
from cours_figures import wrap, lines, DARK, WARN, WARNBG, OK, OKBG, VIO, VIOBG

RED = '#c92a2a'; REDBG = '#fff1f0'; BLUE = '#1864ab'; BLUEBG = '#e7f0fa'; AMBER = '#e8a317'
MARKS = {'ah': ACC, 'ahq': QUIET, 'ahd': DARK, 'ahr': RED, 'ahw': WARN, 'ahv': VIO, 'ahb': BLUE, 'aho': OK}


def defs():
    m = ''.join(f'<marker id="{k}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" '
                f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>' for k, c in MARKS.items())
    hatch = ('<pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
             f'<rect width="8" height="8" fill="#ffffff"/><line x1="0" y1="0" x2="0" y2="8" stroke="{RED}" stroke-width="2.4" opacity="0.45"/></pattern>')
    return f'<defs>{m}{hatch}</defs>'


def arr(x1, y1, x2, y2, col=ACC, sw=1.6, dash=None, m='ah', both=False):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    s = f' marker-start="url(#{m})"' if both else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{sw}"{d}{s} marker-end="url(#{m})"/>'


def pth(d, col=ACC, sw=1.6, dash=None, m='ah', both=False, end=True):
    da = f' stroke-dasharray="{dash}"' if dash else ''
    s = f' marker-start="url(#{m})"' if both else ''
    e = f' marker-end="url(#{m})"' if end else ''
    return f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linejoin="round"{da}{s}{e}/>'


def halo(t):
    return t.replace('<text ', '<text stroke="#ffffff" stroke-width="4" stroke-linejoin="round" paint-order="stroke" ')


def vtext(x, y, s, size=12, w=600, fill=INK):
    return f'<g transform="translate({x},{y}) rotate(-90)">{T(0, 0, s, size, w, fill, "middle")}</g>'


def rich(x, y, s, n, size=11, w=400, fill=INK, anchor='start', lh=14, acol=BLUE):
    """Wrapped text in which {names} are written in bold, in the colour acol."""
    s = re.sub(r'\{[^}]*\}', lambda mm: mm.group(0).replace(' ', ' '), fr(s))
    out, cur = [], ''
    for wd in s.split(' '):
        ln = len(cur.replace('{', '').replace('}', ''))
        if cur and ln + 1 + len(wd.replace('{', '').replace('}', '')) > n:
            out.append(cur); cur = wd
        else:
            cur = f'{cur} {wd}' if cur else wd
    if cur:
        out.append(cur)
    res = ''
    for i, ln in enumerate(out):
        spans = ''
        for part in re.split(r'(\{[^}]*\})', ln):
            if not part:
                continue
            if part.startswith('{'):
                spans += f'<tspan fill="{acol}" font-weight="700">{escape(part[1:-1])}</tspan>'
            else:
                spans += f'<tspan>{escape(part)}</tspan>'
        res += (f'<text x="{x}" y="{y + i * lh}" font-size="{size}" font-weight="{w}" fill="{fill}" '
                f'text-anchor="{anchor}" xml:space="preserve">{spans}</text>')
    return res, len(out)


def pill(x, y, s, col=BLUE, bg=BLUEBG, size=11, h=19):
    w = round(len(s) * size * 0.58 + 16)
    return R(x, y, w, h, bg, col, 1, h / 2) + T(x + w / 2, y + h - 5.5, s, size, 700, col, 'middle'), w


def diamond(x, y, n, col):
    return (f'<path d="M{x},{y - 11} L{x + 11},{y} L{x},{y + 11} L{x - 11},{y} z" fill="#ffffff" stroke="{col}" stroke-width="2"/>'
            + T(x, y + 4, str(n), 11, 700, col, 'middle'))


def spof(x, y, n):
    return R(x, y, 52, 19, RED, 'none', 0, 4) + T(x + 26, y + 13.5, f'SPOF {n}', 11, 700, '#ffffff', 'middle')


# ---------------------------------------------------------------- chapitre 0
def chaine_d1_d2_d3():
    b = [defs(), T(24, 30, 'De la veille au schéma directeur : la place du dossier D2', 15, 600),
         T(24, 50, 'Les trois dossiers du bloc 1 s’enchaînent ; le D2 établit l’état des lieux dont le D3 a besoin', 11.5, 400, QUIET)]
    for x, t, s in ((24, 'D1 · Veille (S1)', 'ce qui change autour de Medisecure'),
                    (566, 'D3 · Stratégie SI et architecture (S3)', 'où aller, dans quel ordre, avec quel budget')):
        b.append(R(x, 116, 170, 118, '#ffffff', ACC, 1.5, 10))
        nt = len(wrap(t, 20))
        b.append(lines(x + 85, 142, t, 20, 13, 700, DARK, 'middle', lh=17))
        b.append(lines(x + 85, 146 + nt * 17 + 6, s, 24, 11.5, 400, QUIET, 'middle', lh=15))
    b.append(R(244, 70, 272, 284, ACCBG, ACC, 2.2, 12))
    b.append(lines(380, 95, 'D2 · Cartographie, risques, diagnostic (S2)', 30, 13.5, 700, DARK, 'middle', lh=17))
    subs = [('Cartographie :', 'le SI tel qu’il est'), ('Risques et continuité :', 'ce qui peut mal tourner'),
            ('Diagnostic :', 'forces, faiblesses, enjeux')]
    for i, (t, s) in enumerate(subs):
        y = 130 + i * 76
        b.append(R(262, y, 236, 54, '#ffffff', ACC, 1.3, 8))
        b.append(T(380, y + 22, t, 12.5, 700, DARK, 'middle'))
        b.append(T(380, y + 40, s, 11.5, 400, INK, 'middle'))
        if i < 2:
            b.append(arr(380, y + 55, 380, y + 74, sw=1.4))
    b += [arr(195, 175, 241, 175, sw=2), arr(517, 175, 563, 175, sw=2)]
    yd = 130 + 2 * 76 + 27
    b.append(pth(f'M80,235 V{yd} H259', VIO, 1.6, '6 4', 'ahv'))
    b.append(lines(92, 262, 'environnement externe, réglementation', 22, 11, 600, VIO, lh=14))
    b.append(R(24, 374, 712, 32, TINT, 'none', 0, 8))
    b += [L(219, 380, 219, 400, AXIS), L(541, 380, 541, 400, AXIS),
          T(109, 395, 'Compétences : C1 à C3', 12, 600, INK, 'middle'), T(380, 395, 'C4', 12, 700, DARK, 'middle'),
          T(651, 395, 'C5 à C9', 12, 600, INK, 'middle')]
    return svg(424, b)


# ---------------------------------------------------------------- chapitre 1
def le_moigne():
    b = [defs(), T(24, 30, 'Les trois sous-systèmes de l’organisation selon Le Moigne, appliqués à Kestrel Logistique', 15, 600),
         T(24, 50, 'Le système d’information relie le pilotage, qui décide, et le système opérant, qui transporte', 11.5, 400, QUIET)]
    b.append(R(170, 68, 420, 426, TINT, AXIS, 1.4, 12))
    b.append(T(380, 89, 'Kestrel Logistique', 13.5, 700, DARK, 'middle'))
    boxes = [(100, 'Système de pilotage', 'comité de direction, directeur des opérations, chefs de quai, planificateurs', '#ffffff'),
             (250, 'Système d’information', 'Portail EDI, RoutePro, Kestrel Track, KDriver, TeleFleet, ERP finance, Excel', ACCBG),
             (408, 'Système opérant', 'quais de tri, tournées, chauffeurs, camions', '#ffffff')]
    for y, t, s, bg in boxes:
        b.append(R(250, y, 260, 72, bg, ACC, 1.6, 10))
        b.append(T(380, y + 24, t, 13.5, 700, DARK, 'middle'))
        b.append(lines(380, y + 44, s, 42, 11.5, 400, QUIET, 'middle', lh=15))
    for y1, y2, down, up in ((172, 250, 'décisions, objectifs, plans de tournée', 'tableaux de bord, alertes'),
                             (322, 408, 'ordres de transport, tournées affectées', 'scans, preuves de livraison, positions GPS')):
        b.append(arr(330, y1 + 1, 330, y2 - 2, ACC, 1.6, '6 4'))
        b.append(arr(430, y2 - 1, 430, y1 + 2, ACC, 1.6, '6 4'))
        ym = (y1 + y2) / 2
        nd, nu = len(wrap(down, 22)), len(wrap(up, 22))
        b.append(lines(322, ym - (nd - 1) * 7.5 + 4, down, 22, 11.5, 400, INK, 'end'))
        b.append(lines(438, ym - (nu - 1) * 7.5 + 4, up, 22, 11.5, 400, INK, 'start'))
    b.append(lines(24, 96, 'Informations de l’environnement : marché, réglementation, concurrents', 24, 11, 600, ACC, lh=14))
    b.append(arr(24, 156, 248, 156, ACC, 1.6, '6 4'))
    b += [T(24, 262, 'Entrée d’information :', 12, 700, DARK), T(24, 282, 'commandes EDI des clients', 11.5, 400, INK),
          arr(24, 290, 248, 290, ACC, 1.6, '6 4'),
          T(24, 422, 'Entrée physique :', 12, 700, DARK), T(24, 442, 'colis et palettes', 11.5, 400, INK),
          arr(24, 450, 248, 450, DARK, 2.2, m='ahd'),
          T(736, 248, 'Sortie d’information :', 12, 700, DARK, 'end'), T(736, 266, 'informations de suivi', 11.5, 400, INK, 'end'),
          T(736, 281, 'aux clients', 11.5, 400, INK, 'end'), arr(512, 290, 736, 290, ACC, 1.6, '6 4'),
          T(736, 422, 'Sortie physique :', 12, 700, DARK, 'end'), T(736, 442, 'colis livrés', 11.5, 400, INK, 'end'),
          arr(512, 450, 736, 450, DARK, 2.2, m='ahd')]
    b += [L(170, 526, 214, 526, DARK, 2.2), T(222, 530, 'flux physique', 11.5, 400, QUIET),
          L(340, 526, 384, 526, ACC, 1.6, '6 4'), T(392, 530, 'flux d’information', 11.5, 400, QUIET)]
    return svg(546, b)


def chaine_valeur_kestrel():
    x0, x1, xt, y0, ys, y1 = 24, 640, 736, 84, 260, 408
    b = [T(24, 30, 'La chaîne de valeur de Kestrel Logistique', 15, 600),
         T(24, 50, 'Les activités selon Porter, avec les applications qui les soutiennent', 11.5, 400, QUIET),
         T(24, 76, 'ACTIVITÉS DE SOUTIEN', 11, 700, QUIET),
         f'<path d="M{x0},{y0} H{x1} L{xt},{(y0 + y1) / 2} L{x1},{y1} H{x0} z" fill="{TINT}" stroke="{DARK}" stroke-width="1.6"/>']
    sup = [('Infrastructure', 'direction générale, DAF, comptabilité ({ERP finance})'),
           ('Gestion des ressources humaines', 'recrutement des chauffeurs, paie et temps de conduite ({Paie})'),
           ('Développement technologique', 'DSI, développement interne de Kestrel Track et de KDriver, maintenance du parc'),
           ('Approvisionnements', 'carburant, sous-traitants du dernier kilomètre, prestataires informatiques')]
    bh = (ys - y0) / 4
    for i, (t, s) in enumerate(sup):
        y = y0 + i * bh
        b.append(R(x0 + 1, y + 1, x1 - x0 - 1, bh - 1, '#ffffff' if i % 2 == 0 else ACCBG, 'none', 0, 0))
        nt = len(wrap(t, 24))
        b.append(lines(x0 + 12, y + (bh - (nt - 1) * 14) / 2 + 4, t, 24, 12, 700, DARK, lh=14))
        sv, nl = rich(206, 0, s, 66, 11.5, lh=14)
        b.append(f'<g transform="translate(0,{y + (bh - (nl - 1) * 14) / 2 + 4})">{sv}</g>')
    b.append(L(x0, ys, x1, ys, DARK, 1.6))
    b.append(L(196, y0, 196, ys, AXIS, 1))
    prim = [('Logistique d’entrée', 'réception des ordres de transport ({Portail EDI}), enlèvement chez les clients'),
            ('Production', 'tri sur quai, stockage et préparation ({StockFlow}), construction des tournées ({RoutePro}, {Excel})'),
            ('Logistique de sortie', 'tournées de livraison, preuve de livraison ({KDriver}, {TeleFleet})'),
            ('Commercialisation et vente', 'grands comptes, e-commerçants, devis ({site web})'),
            ('Services', 'suivi des colis, réclamations ({Kestrel Track})')]
    cw = (x1 - x0) / 5
    for i, (t, s) in enumerate(prim):
        x = x0 + i * cw
        if i:
            b.append(L(x, ys, x, y1, AXIS, 1))
        nt = len(wrap(t, 17))
        b.append(lines(x + cw / 2, ys + 24, t, 17, 12, 700, DARK, 'middle', lh=15))
        sv, _ = rich(x + cw / 2, ys + 30 + nt * 15, s, 19, 11, anchor='middle', lh=14)
        b.append(sv)
    b.append(L(x1, y0, x1, y1, DARK, 1, '3 3'))
    b.append(T(686, (y0 + y1) / 2 + 5, 'Marge', 14, 700, DARK, 'middle'))
    b.append(T(24, y1 + 18, 'ACTIVITÉS PRINCIPALES', 11, 700, QUIET))
    b.append(R(400, y1 + 28, 336, 24, '#ffffff', AXIS, 1, 6))
    sv, _ = rich(412, y1 + 44, 'en {bleu} : applications du SI qui soutiennent l’activité', 60, 11.5)
    b.append(sv)
    return svg(y1 + 66, b)


# ---------------------------------------------------------------- chapitre 2
def modele_alignement():
    b = [defs(), T(24, 30, 'Le modèle d’alignement stratégique de Henderson et Venkatraman (1993)', 15, 600),
         T(24, 50, 'Quatre domaines, deux types de cohérence, quatre manières de parcourir le carré', 11.5, 400, QUIET)]
    cols, rows, w, h = (150, 460), (104, 296), 220, 112
    b.append(R(136, 94, 558, 324, TINT, 'none', 0, 12))
    b.append(pth('M150,90 Q150,82 160,82 H405 Q415,82 415,72 Q415,82 425,82 H670 Q680,82 680,90', QUIET, 1.4, end=False))
    b.append(T(415, 66, 'Les quatre domaines à aligner', 11.5, 600, QUIET, 'middle'))
    cells = [('Stratégie de l’entreprise', 'périmètre d’activité, compétences distinctives, gouvernance'),
             ('Stratégie des technologies de l’information', 'périmètre technologique, compétences systémiques, gouvernance des TI'),
             ('Infrastructure et processus de l’organisation', 'structure, processus, compétences'),
             ('Infrastructure et processus du SI', 'architecture, processus, compétences')]
    for k, (t, s) in enumerate(cells):
        x, y = cols[k % 2], rows[k // 2]
        b.append(R(x, y, w, h, '#ffffff', ACC, 1.6, 10))
        nt = len(wrap(t, 28))
        b.append(lines(x + w / 2, y + 26, t, 28, 13, 700, DARK, 'middle', lh=16))
        b.append(lines(x + w / 2, y + 30 + nt * 16 + 4, s, 34, 11.5, 400, QUIET, 'middle', lh=15))
    for x in (260, 570):
        b.append(arr(x, 220, x, 292, ACC, 2, both=True))
        b.append(halo(T(x + 9, 260, 'Cohérence stratégique', 11.5, 600, ACC)))
    for y in (168, 360):
        b.append(arr(374, y, 456, y, VIO, 2, m='ahv', both=True))
        b.append(lines(415, y - 24, 'Intégration fonctionnelle', 13, 11.5, 600, VIO, 'middle', lh=13))
    b += [vtext(122, 160, 'Externe', 12.5, 700, QUIET), vtext(122, 352, 'Interne', 12.5, 700, QUIET),
          T(260, 438, 'Métier', 12.5, 700, DARK, 'middle'), T(570, 438, 'Technologies de l’information', 12.5, 700, DARK, 'middle')]
    b.append(L(24, 458, 736, 458, MUTED, 1))
    b.append(T(24, 480, 'Les quatre perspectives : du domaine moteur au domaine qui s’adapte, en passant par un domaine pivot', 12, 600))
    persp = [('Exécution de la stratégie', [0, 2, 3]), ('Transformation technologique', [0, 1, 3]),
             ('Potentiel concurrentiel', [1, 0, 2]), ('Niveau de service', [1, 3, 2])]
    for i, (name, route) in enumerate(persp):
        x, y = 24 + i * 184, 496
        pos = [(x, y), (x + 34, y), (x, y + 26), (x + 34, y + 26)]
        for px, py in pos:
            b.append(R(px, py, 28, 20, '#ffffff', AXIS, 1, 3))
        pts = [(pos[j][0] + 14, pos[j][1] + 10) for j in route]
        b.append(f'<circle cx="{pts[0][0]}" cy="{pts[0][1]}" r="4" fill="{VIO}"/>')
        b.append(pth('M' + ' L'.join(f'{px},{py}' for px, py in pts), VIO, 1.8, m='ahv'))
        b.append(lines(x + 74, y + 14, f'{i + 1}. {name}', 18, 11.5, 600, INK, lh=15))
    b.append(T(24, 566, 'Petites cases : en haut les stratégies, en bas les infrastructures ; à gauche le métier, à droite les TI. '
                        'Le point marque le domaine moteur.', 11, 400, QUIET))
    return svg(582, b)


def plan_urbanisation_kestrel():
    b = [defs(), T(24, 30, 'Plan d’urbanisation de Kestrel Logistique, avec les applications', 15, 600),
         T(24, 50, 'Les blocs fonctionnels sont nommés sans logiciel ; les applications y sont ensuite placées', 11.5, 400, QUIET)]
    body = []

    def block(x, y, w, name, apps=(), hole=None, redund=None, hatch=False):
        hatch = hatch or bool(hole)
        """Functional block (h 40) with application pills below; returns the bottom y."""
        o = []
        o.append(R(x, y, w, 40, 'url(#hatch)' if hatch else '#ffffff', RED if hatch else AXIS, 1.4 if hatch else 1.2, 6))
        nl = len(wrap(name, int(w / 6.3)))
        t = lines(x + w / 2, y + 20 - (nl - 1) * 7 + 4, name, int(w / 6.3), 11.5, 600, INK, 'middle', lh=14)
        o.append(halo(t) if hatch else t)
        yy = y + 46
        px = x
        for a in apps:
            sv, pw = pill(px, yy, a); o.append(sv); px += pw + 6
        if apps:
            yy += 25
        if hole:
            sv, pw = pill(x, yy, hole, RED, REDBG); o.append(sv); yy += 25
        if redund:
            o.insert(0, R(x - 5, y - 5, w + 10, yy - y + 4, WARNBG, WARN, 2, 9))
            sv, pw = pill(x + w + 5 - round(len(redund) * 11 * 0.58 + 16), yy + 3, redund, WARN, '#ffffff'); o.append(sv)
            yy += 29
        return ''.join(o), yy

    def zone(x, y, w, h, name, bg, n=40):
        nl = len(wrap(name, n))
        return R(x, y, w, h, bg, AXIS, 1, 8) + lines(x + 10, y + 18, name, n, 12, 700, DARK, lh=15), y + 18 + nl * 15

    def quartier(x, y, w, h, name):
        return R(x, y, w, h, '#ffffff', AXIS, 1, 6, '4 3').replace('fill="#ffffff"', 'fill="#ffffff" fill-opacity="0.55"') + T(x + 8, y + 15, name, 11.5, 700, QUIET)

    # Pilotage
    zs, _ = zone(28, 96, 704, 58, 'Zone Pilotage', VIOBG)
    body.append(zs)
    sv, _ = block(220, 105, 260, 'Produire les indicateurs de Cap 2029', hatch=True)
    body.append(sv)
    body.append(pill(490, 116, 'trou', RED, REDBG)[0])
    top = 166
    # Left zone: Relations clients et partenaires
    zs, yq = zone(28, top, 212, 0, 'Zone Relations clients et partenaires', ACCBG, 26)
    left = []
    yq += 6
    for q, blocks in (('Commande', [('Recevoir les ordres de transport', ['Portail EDI'], None)]),
                      ('Suivi', [('Informer clients et destinataires', ['Kestrel Track'], None)]),
                      ('Prospection', [('Recevoir les demandes de devis', ['Site web'], None),
                                       ('Suivre les prospects et les devis', [], 'trou : suivi par courriel')])):
        yb, svs = yq + 22 - 8, ''
        for name, apps, hole in blocks:
            sv, yb = block(46, yb + 8, 176, name, apps, hole)
            svs += sv
        left.append(quartier(38, yq, 192, yb - yq + 4, q) + svs)
        yq = yb + 14
    bottom_left = yq
    # Centre zone: Opérations de transport
    zc, yq2 = zone(250, top, 270, 0, 'Zone Opérations de transport', OKBG)
    centre = []
    yq2 += 6
    sv1, yb = block(268, yq2 + 27, 234, 'Construire les tournées du lendemain', ['RoutePro', 'Excel'], None, 'redondance')
    sv2, yb = block(268, yb + 8, 234, 'Optimiser les tournées', [], 'trou : module non acheté')
    centre.append(quartier(258, yq2, 254, yb - yq2 + 4, 'Planification') + sv1 + sv2)
    yq2 = yb + 14
    tele = None
    for q, name, apps in (('Exécution', 'Livrer et prouver la livraison', ['KDriver']),
                          ('Flotte', 'Suivre les véhicules et la conduite', ['TeleFleet'])):
        sv, yb = block(268, yq2 + 22, 234, name, apps)
        centre.append(quartier(258, yq2, 254, yb - yq2 + 4, q) + sv)
        if q == 'Flotte':
            tele = (268 + pill(0, 0, 'TeleFleet')[1], yq2 + 22 + 46 + 9.5)
        yq2 = yb + 14
    # Right column: Entrepôt, Ressources, Gestion
    ze, ye = zone(530, top, 202, 0, 'Zone Entrepôt', '#fff9db')
    sv, yb_e = block(542, ye + 6, 178, 'Réceptionner, stocker, préparer', ['StockFlow'])
    gh = 18 + 15 + 6 + 40 + 6 + 19 + 12
    res_blocks = (('Payer et gérer les temps', 'Paie'), ('Communiquer et partager les documents', 'Microsoft 365'),
                  ('Gérer le support et l’inventaire des postes', 'Outil de tickets'))
    rh = 33 + 6 + 3 * 71 + 25 + 2 * 12 + 6
    bottom = max(bottom_left, yq2, yb_e + 8 + 10 + rh + 10 + gh)
    body.append(zs.replace('height="0"', f'height="{bottom - top}"'))
    body.append(zc.replace('height="0"', f'height="{bottom - top}"'))
    body += left + centre
    body.append(ze.replace('height="0"', f'height="{yb_e - top + 8}"') + sv)
    # Gestion at the bottom, Ressources just above
    yg = bottom - gh
    zg, yy = zone(530, yg, 202, gh, 'Zone Gestion', TINT)
    sv, _ = block(542, yy + 6, 178, 'Comptabiliser, facturer, acheter', ['ERP finance'])
    body.append(zg + sv)
    yr = yg - 10 - rh
    rs, _ = zone(530, yr, 202, rh, 'Zone Ressources', VIOBG)
    body.append(rs)
    yblk = yr + 33 + 6
    paie = None
    for k, (name, app) in enumerate(res_blocks):
        sv, yb = block(547, yblk, 168, name, [app])
        body.append(sv)
        if k == 0:
            paie = (547, yblk + 46 + 9.5)
            body.append(pill(547, yb, 'flux manuel : ressaisie', WARN, '#ffffff')[0])
            yb += 25
        yblk = yb + 12
    body.append(pth(f'M{paie[0] - 2},{paie[1]} H525 V{tele[1]} H{tele[0] + 2}', WARN, 1.8, '5 4', end=False))
    # Référentiels and Échanges
    yref = bottom + 12
    body.append(R(28, yref, 704, 34, '#e7f5ff', AXIS, 1, 8) + T(38, yref + 22, 'Zone Référentiels', 12, 700, DARK)
                + T(180, yref + 22, '(aucun bloc : aucune donnée de référence n’a de source désignée)', 11.5, 400, VIO))
    ye2 = yref + 44
    body.append(R(28, ye2, 704, 34, TINT, AXIS, 1, 8) + T(38, ye2 + 22, 'Zone Échanges', 12, 700, DARK)
                + T(160, ye2 + 22, '(vide)', 11.5, 400, QUIET))
    yend = ye2 + 46
    b.append(R(16, 62, 728, yend - 62, '#ffffff', DARK, 1.6, 10))
    b.append(T(28, 84, 'SI de Kestrel Logistique – plan d’urbanisation, version 1', 13.5, 700, DARK))
    b += body
    # Legend and cartouche
    yl = yend + 14
    b.append(R(16, yl, 300, 64, '#ffffff', DARK, 1.2, 8))
    b += [T(28, yl + 20, 'Cartouche', 12, 700, DARK), T(28, yl + 38, 'Version 1 · mars 2026', 11.5, 400, INK),
          T(28, yl + 54, 'Auteur : DSI de Kestrel Logistique', 11.5, 400, INK)]
    b.append(R(330, yl, 414, 88, '#ffffff', AXIS, 1.2, 8))
    b.append(R(342, yl + 10, 30, 18, '#ffffff', AXIS, 1.2, 4) + T(380, yl + 23, 'bloc fonctionnel', 11.5, 400, INK))
    sv, pw = pill(342, yl + 37, 'Appli'); b.append(sv + T(342 + pw + 8, yl + 51, 'application', 11.5, 400, INK))
    b.append(R(512, yl + 10, 30, 18, 'url(#hatch)', RED, 1.2, 4) + T(550, yl + 23, 'trou (aucune application dédiée)', 11.5, 400, INK))
    b.append(R(512, yl + 37, 30, 18, WARNBG, WARN, 2, 4) + T(550, yl + 50, 'redondance', 11.5, 400, INK))
    b.append(L(342, yl + 72, 372, yl + 72, WARN, 1.8, '5 4'))
    b.append(T(380, yl + 76, 'flux manuel (ressaisie entre deux applications, ni redondance ni trou)', 11.5, 400, INK))
    return svg(yl + 102, b)


# ---------------------------------------------------------------- chapitre 3
def six_vues():
    b = [defs(), T(24, 30, 'Trois visions, sept vues, quatre niveaux', 15, 600),
         T(24, 50, 'Chaque double flèche porte l’objet pivot qui relie deux vues voisines', 11.5, 400, QUIET)]
    LX, RX, BW = 180, 438, 154
    bands = [(96, 80, 'Vision métier', ACCBG, ('Vue de l’écosystème', 'Vue métier du SI'), 'Niveau métier', False),
             (216, 64, 'ajoutée par le D2', TINT, (None, 'Vue fonctionnelle (urbanisation)'), 'Niveau fonctionnel', True),
             (320, 80, 'Vision applicative', OKBG, ('Vue de l’administration', 'Vue des applications'), 'Niveau applicatif', False),
             (440, 80, 'Vision infrastructure', WARNBG, ('Vue des infrastructures physiques', 'Vue des infrastructures logiques'),
              'Niveau infrastructure', False)]
    b.append(lines(680, 66, 'Niveau du référentiel', 14, 11.5, 700, QUIET, 'middle', lh=14))
    boxes = []
    for y, h, lab, bg, (lv, rv), lev, dashed in bands:
        b.append(R(66, y, 538, h, bg, QUIET if dashed else 'none', 1.2 if dashed else 0, 8, '6 4' if dashed else None))
        b.append(lines(78, y + h / 2 - (len(wrap(lab, 12)) - 1) * 8 + 4, lab, 12,
                       11.5 if dashed else 13, 600 if dashed else 700, VIO if dashed else DARK, lh=16))
        b.append(R(616, y, 128, h, bg, QUIET if dashed else 'none', 1.2 if dashed else 0, 8, '6 4' if dashed else None))
        nl = len(wrap(lev, 14))
        b.append(lines(680, y + h / 2 - (nl - 1) * 7.5 + 4, lev, 14, 12, 600, INK, 'middle', lh=15))
        by = y + (h - 44) / 2
        for x, v in ((LX, lv), (RX, rv)):
            if v:
                boxes.append((x, by, v))
    yi = 562
    for k, (x, by, v) in enumerate(boxes):  # thin links to the inventory, drawn behind the boxes
        xx = x + 14 + (k % 4) * 9
        b.append(L(xx, by + 44, xx, yi, AXIS, 0.9))
    for x, by, v in boxes:
        b.append(R(x, by, BW, 44, '#ffffff', ACC, 1.5, 8))
        nl = len(wrap(v, 22))
        b.append(lines(x + BW / 2, by + 22 - (nl - 1) * 7.5 + 4, v, 22, 12, 600, INK, 'middle', lh=15))
    xr = RX + BW / 2
    for y1, y2, t in ((96 + 62, 216 + 10, 'Processus'), (216 + 54, 320 + 18, 'Application'), (320 + 62, 440 + 18, 'Serveur logique')):
        b.append(arr(xr, y1 + 2, xr, y2 - 2, DARK, 1.8, m='ahd', both=True))
        b.append(T(xr + 9, (y1 + y2) / 2 + 4, t, 11.5, 700, DARK))
    for y, t, n in ((96 + 40, 'Entité ou système', 18), (320 + 40, 'Élément administré', 12), (440 + 40, 'Serveur physique, équipement', 18)):
        b.append(arr(LX + BW + 2, y + 8, RX - 2, y + 8, DARK, 1.8, m='ahd', both=True))
        nl = len(wrap(t, n))
        b.append(lines((LX + BW + RX) / 2, y - 4 - (nl - 1) * 13, t, n, 11, 700, DARK, 'middle', lh=13))
    b.append(f'<path d="M30,84 H44 V500 H52 L37,526 L22,500 H30 z" fill="{ACC}"/>')
    b.append(vtext(60, 300, 'du métier vers la technique', 12, 700, ACC).replace('<text ', '<text stroke="#ffffff" stroke-width="4" paint-order="stroke" '))
    b.append(R(LX, yi, RX + BW - LX, 48, TINT, QUIET, 1.4, 8))
    b.append(T((LX + RX + BW) / 2, yi + 20, 'Inventaire (annexes A à D)', 12.5, 700, DARK, 'middle'))
    b.append(T((LX + RX + BW) / 2, yi + 37, 'les vues sont des extraits de l’inventaire', 11.5, 400, QUIET, 'middle'))
    return svg(626, b)


def kestrel_ecosysteme():
    b = [defs(), T(24, 30, 'Vue de l’écosystème de Kestrel Logistique (exemple, version 1.0)', 15, 600),
         T(24, 50, 'Les parties prenantes externes, la nature des échanges et le niveau de dépendance', 11.5, 400, QUIET)]
    CX0, CX1, CY0, CY1 = 286, 466, 196, 392
    SW = {'forte': 5.5, 'moyenne': 2.6, 'faible': 1.2}
    # separators of the four sectors
    b += [L(376, 62, 376, 92, MUTED, 1), L(376, CY1, 376, 780, MUTED, 1), L(500, 256, 744, 256, MUTED, 1), L(16, 256, 262, 256, MUTED, 1)]
    b += [T(744, 72, 'Clients et usagers', 12.5, 700, DARK, 'end'), T(744, 280, 'Fournisseurs de services numériques', 12.5, 700, DARK, 'end'),
          T(16, 72, 'Autorités', 12.5, 700, DARK), T(16, 280, 'Partenaires opérationnels', 12.5, 700, DARK)]
    right = [('PP-01 Grande distribution', 'forte', 'ordres de transport EDI', None),
             ('PP-02 E-commerçants', 'moyenne', 'commandes, suivi', None),
             ('PP-03 Particuliers et petites entreprises', 'faible', 'devis, commandes', None),
             ('PP-13 Destinataires', 'faible', 'adresses, suivi', None),
             ('PP-04 Prestataire EDI', 'forte', 'messages EDI', None),
             ('PP-05 Éditeur de RoutePro', 'forte', 'accès VPN permanent', RED),
             ('PP-06 Éditeur de StockFlow', 'moyenne', 'stocks (SaaS)', None),
             ('PP-07 Fabricant des boîtiers', 'moyenne', 'positions GPS (TeleFleet)', None),
             ('PP-08 Hébergeur cloud de Kestrel Track', 'moyenne', 'hébergement du suivi', None),
             ('PP-09 Microsoft', 'moyenne', 'messagerie, planification', None),
             ('PP-10 Prestataire de paie', 'moyenne', 'variables de paie', None),
             ('PP-11 Hébergeur du site web', 'faible', 'hébergement du site', None),
             ('PP-12 Opérateur télécom', 'forte', 'fibre et tunnels VPN', None)]
    ys = [104 + 42 * i for i in range(4)] + [312 + 42 * i for i in range(9)]
    links, labels, boxes = [], [], []
    for i, ((name, dep, lab, col), y) in enumerate(zip(right, ys)):
        a = CY0 + 16 + i * 14
        c = col or DARK
        links.append(pth(f'M{CX1},{a} L500,{y} H616', c, SW[dep], end=False))
        nl = len(wrap(lab, 19))
        labels.append(halo(lines(558, y - 5 - (nl - 1) * 13, lab, 19, 11, 600 if col else 400, col or QUIET, 'middle', lh=13)))
        nb = len(wrap(name, 20))
        hh = max(32, nb * 13 + 8)
        boxes.append(R(616, y - hh / 2, 128, hh, '#ffffff', AXIS, 1.2, 6))
        boxes.append(lines(680, y + 4 - (nb - 1) * 6.5, name, 20, 11, 600, INK, 'middle', lh=13))
    # authorities: legal obligation (dependency not applicable), drawn in violet; partners: dependency
    left = [('PP-16 CNIL', None, 'notifications RGPD', 104, None, None),
            ('PP-17 ANSSI', None, 'notifications NIS2', 154, 'si NIS2, à confirmer', '6 4'),
            ('PP-14 Sous-traitants du dernier kilomètre', 'moyenne', 'tournées, preuves de livraison', 322, None, None),
            ('PP-15 Banque', 'faible', 'paiements, relevés', 372, None, None),
            ('PP-19 Prestataires disposant d’un accès VPN', 'moyenne', 'accès VPN (deux prestataires)', 422, None, None),
            ('PP-20 Fournisseurs payés par virement', 'moyenne', 'factures, coordonnées bancaires', 472, None, None)]
    for i, (name, dep, lab, y, note, dash) in enumerate(left):
        a = (222, 250, 330, 350, 368, 384)[i]
        col = RED if name.startswith('PP-19') else None
        links.append(pth(f'M{CX0},{a} L262,{y} H144', VIO if dep is None else (col or DARK), 1.8 if dep is None else SW[dep], dash, end=False))
        nl = len(wrap(lab, 19))
        labels.append(halo(lines(203, y - 5 - (nl - 1) * 13, lab, 19, 11, 600 if col else 400, col or QUIET, 'middle', lh=13)))
        hh = 40 if note else max(32, len(wrap(name, 20)) * 13 + 8)
        boxes.append(R(16, y - hh / 2, 128, hh, '#ffffff', AXIS, 1.2, 6, '5 3' if dash else None))
        if note:
            boxes.append(T(80, y - 3, name, 11.5, 700, INK, 'middle') + T(80, y + 12, note, 11, 400, WARN, 'middle'))
        else:
            nb = len(wrap(name, 20))
            boxes.append(lines(80, y + 4 - (nb - 1) * 6.5, name, 20, 11, 600, INK, 'middle', lh=13))
    b += links
    # centre and shareholder (medium dependency)
    b.append(L(376, 138, 376, CY0, DARK, SW['moyenne']))
    b.append(halo(T(384, 172, 'reporting financier', 11, 400, QUIET)))
    b.append(R(281, 94, 190, 44, '#ffffff', DARK, 1.4, 7))
    b.append(T(376, 112, 'PP-18 Vidal Participations', 11.5, 700, INK, 'middle') + T(376, 128, '(actionnaire, 100 %)', 11, 400, QUIET, 'middle'))
    b.append(R(CX0, CY0, CX1 - CX0, CY1 - CY0, ACCBG, ACC, 2, 16))
    b.append(T(376, CY0 + 28, 'Kestrel Logistique SAS', 13, 700, DARK, 'middle'))
    for i, s in enumerate(('SITE-01 Saint-Priest (siège)', 'SITE-02 Moirans', 'SITE-03 Clermont-Ferrand')):
        y = CY0 + 50 + i * 46
        b.append(R(298, y, 156, 34, '#ffffff', ACC, 1.2, 6) + T(376, y + 21.5, s, 11, 600, INK, 'middle'))
    b += boxes + labels
    # cartouche
    x, y = 16, 508
    b.append(R(x, y, 340, 270, '#ffffff', DARK, 1.4, 8))
    b.append(lines(x + 12, y + 22, 'Vue de l’écosystème de Kestrel Logistique', 34, 12.5, 700, DARK, lh=16))
    y += 18
    b += [T(x + 12, y + 42, 'Version 1.0 · date : mars 2026', 11.5, 400, INK), T(x + 12, y + 58, 'Auteur : R. Chevalier', 11.5, 400, INK),
          L(x + 12, y + 70, x + 328, y + 70, MUTED, 1), T(x + 12, y + 90, 'Dépendance de Kestrel envers la partie prenante', 11.5, 700, INK)]
    for i, (dep, t) in enumerate((('forte', 'forte'), ('moyenne', 'moyenne'), ('faible', 'faible'))):
        yy = y + 110 + i * 22
        b += [L(x + 12, yy - 4, x + 60, yy - 4, DARK, SW[dep]), T(x + 70, yy, t, 11.5, 400, INK)]
    b += [L(x + 12, y + 172, x + 60, y + 172, VIO, 1.8), T(x + 70, y + 176, 'obligation légale (dépendance sans objet)', 11.5, 400, INK),
          L(x + 12, y + 194, x + 60, y + 194, RED, 2.6), T(x + 70, y + 198, 'accès au réseau interne', 11.5, 400, INK),
          L(x + 12, y + 216, x + 60, y + 216, VIO, 1.8, '6 4'), T(x + 70, y + 220, 'relation à confirmer', 11.5, 400, INK),
          T(x + 12, y + 244, 'Sur chaque trait : données ou services échangés', 11, 400, QUIET)]
    return svg(796, b)


# ---------------------------------------------------------------- chapitre 4
def i_server(x, y):
    o = R(x, y, 26, 34, '#ffffff', DARK, 1.4, 3)
    for k in range(3):
        o += L(x + 4, y + 8 + k * 9, x + 16, y + 8 + k * 9, DARK, 1.2) + f'<circle cx="{x + 21}" cy="{y + 8 + k * 9}" r="1.6" fill="{OK}"/>'
    return o


def i_nas(x, y):
    return (f'<path d="M{x},{y + 5} V{y + 29} A13,5 0 0 0 {x + 26},{y + 29} V{y + 5}" fill="#ffffff" stroke="{DARK}" stroke-width="1.4"/>'
            f'<ellipse cx="{x + 13}" cy="{y + 5}" rx="13" ry="5" fill="{ACCBG}" stroke="{DARK}" stroke-width="1.4"/>'
            f'<path d="M{x},{y + 17} A13,5 0 0 0 {x + 26},{y + 17}" fill="none" stroke="{DARK}" stroke-width="1"/>')


def i_disk(x, y):
    return R(x, y, 28, 20, '#ffffff', DARK, 1.4, 4) + f'<circle cx="{x + 20}" cy="{y + 10}" r="3" fill="{DARK}"/>'


def i_gateway(x, y):
    return (R(x, y, 44, 26, DARK, 'none', 0, 5) + f'<path d="M{x + 16},{y + 12} v-3 a6,6 0 0 1 12,0 v3" fill="none" stroke="#ffffff" stroke-width="1.8"/>'
            + R(x + 13, y + 12, 18, 10, '#ffffff', 'none', 0, 2))


def i_wifi(x, y):
    o = f'<circle cx="{x + 14}" cy="{y + 24}" r="2.6" fill="{DARK}"/>'
    for r in (7, 13, 19):
        o += f'<path d="M{x + 14 - r * 0.7:.1f},{y + 24 - r * 0.7:.1f} A{r},{r} 0 0 1 {x + 14 + r * 0.7:.1f},{y + 24 - r * 0.7:.1f}" fill="none" stroke="{DARK}" stroke-width="1.8"/>'
    return o


def i_monitor(x, y):
    return R(x, y, 30, 20, '#ffffff', DARK, 1.4, 2) + L(x + 15, y + 20, x + 15, y + 26, DARK, 1.4) + L(x + 8, y + 26, x + 22, y + 26, DARK, 1.6)


def i_truck(x, y):
    return (R(x, y, 26, 18, '#ffffff', DARK, 1.4, 2) + f'<path d="M{x + 26},{y + 5} H{x + 34} L{x + 39},{y + 11} V{y + 18} H{x + 26} z" fill="{ACCBG}" stroke="{DARK}" stroke-width="1.4"/>'
            + f'<circle cx="{x + 8}" cy="{y + 20}" r="3.5" fill="{DARK}"/><circle cx="{x + 31}" cy="{y + 20}" r="3.5" fill="{DARK}"/>')


def i_phone(x, y):
    return R(x, y, 18, 30, '#ffffff', DARK, 1.4, 4) + L(x + 6, y + 25, x + 12, y + 25, DARK, 1.4)


def i_cloud(cx, cy, s=1.0, fill='#ffffff'):
    return (f'<path transform="translate({cx},{cy}) scale({s})" d="M-60,22 H58 A22,22 0 0 0 52,-12 A30,30 0 0 0 0,-26 '
            f'A28,28 0 0 0 -44,-8 A16,16 0 0 0 -60,22 z" fill="{fill}" stroke="{DARK}" stroke-width="{1.5 / s:.2f}"/>')


def kestrel_infra_physique():
    def isol(x, y):  # backup not isolated from what it protects (not a single point of failure)
        return R(x, y, 52, 19, WARN, 'none', 0, 4) + T(x + 26, y + 13.5, 'ISOL', 11, 700, '#ffffff', 'middle')

    b = [defs(), T(24, 30, 'Vue des infrastructures physiques de Kestrel Logistique (exemple, version 1.0)', 15, 600),
         T(24, 50, 'Deux sites reliés au siège, des services externes joints par Internet, quatre points uniques de défaillance', 11.5, 400, QUIET)]
    # Internet and external services
    b.append(i_cloud(300, 104, 1.15, TINT))
    b.append(T(300, 112, 'Internet', 13.5, 700, DARK, 'middle'))
    ext = ['PP-08 Hébergeur cloud de Kestrel Track : 2 machines virtuelles d’APP-03 Kestrel Track, une seule zone',
           'SaaS : APP-02 StockFlow, APP-05 TeleFleet, APP-06 Portail EDI, APP-08 Paie, APP-10 Microsoft 365 (dont APP-09 Planification des tournées)',
           'PP-11 Hébergeur du site web : APP-12 Site web (mutualisé)']
    y, saas = 62, None
    for i, t in enumerate(ext):
        nl = len(wrap(t, 30)); hh = nl * 14 + 12
        b.append(L(370, 106, 520, y + hh / 2, DARK, 1.6))
        b.append(R(520, y, 224, hh, '#ffffff', DARK, 1.4, 8))
        b.append(i_cloud(540, y + hh / 2 + 1, 0.22, ACCBG))
        b.append(lines(560, y + 17, t, 30, 11, 400, INK, lh=14))
        if i == 1:
            saas = y + hh / 2
        y += hh + 8
    # sites
    SY0, SY1 = 290, 470
    b.append(L(300, 133, 300, 290, DARK, 1.6))
    for x0, x1, name, pst in ((16, 130, 'SITE-02 Moirans', 'TRM-04 Postes de Moirans'),
                              (630, 744, 'SITE-03 Clermont-Ferrand', 'TRM-05 Postes de Clermont-Ferrand')):
        b.append(R(x0, SY0, x1 - x0, SY1 - SY0, TINT, DARK, 1.4, 10))
        b.append(lines((x0 + x1) / 2, SY0 + 22, name, 16, 11.5, 700, DARK, 'middle', lh=15))
        b.append(T((x0 + x1) / 2, SY0 + 22 + len(wrap(name, 16)) * 15, '(75 salariés)' if x0 < 100 else '(35 salariés)', 11, 400, DARK, 'middle'))
        b.append(i_monitor((x0 + x1) / 2 - 15, SY0 + 76))
        b.append(lines((x0 + x1) / 2, SY0 + 124, pst, 16, 11, 400, INK, 'middle', lh=14))
    HX0, HX1, HY0, HY1 = 220, 540, 290, 616
    b.append(R(HX0, HY0, HX1 - HX0, HY1 - HY0, TINT, DARK, 2, 10))
    b.append(T(380, HY0 + 22, 'SITE-01 Saint-Priest, siège (190 salariés)', 12.5, 700, DARK, 'middle'))
    # server room
    b.append(R(234, 322, 292, 150, '#ffffff', DARK, 1.4, 8))
    b.append(T(246, 342, 'SAL-01 Salle serveur', 12, 700, DARK))
    b.append(spof(466, 328, 1))
    for cx, nm, us in ((284, 'SRV-01', 'Virtualisation 1'), (378, 'SRV-02', 'Virtualisation 2')):
        b.append(i_server(cx - 13, 352))
        b += [T(cx, 400, nm, 11, 700, INK, 'middle'), T(cx, 413, us, 11, 400, INK, 'middle')]
    b.append(lines(246, 432, '12 machines virtuelles : APP-01 RoutePro, APP-07 ERP finance, APP-11 Outil de tickets…', 44, 11, 400, QUIET, lh=14))
    b.append(i_nas(457, 352))
    b += [T(470, 400, 'STO-01 NAS', 11, 700, INK, 'middle'), T(470, 413, 'de sauvegarde', 11, 400, INK, 'middle'), isol(400, 358)]
    # DAF office and external disk
    b.append(R(384, 482, 146, 84, '#ffffff', DARK, 1.2, 8, '4 3'))
    b.append(T(394, 499, 'Bureau de la DAF', 11.5, 700, DARK))
    b.append(lines(394, 517, 'STO-02 Disque externe (copie hebdomadaire)', 15, 11, 400, INK, lh=14))
    b.append(i_disk(494, 538))
    b.append(pth('M484,369 H518 V536', DARK, 1.6, '5 4', 'ahd'))
    # Wi-Fi
    b.append(i_wifi(236, 486))
    b.append(lines(268, 500, 'RES-03 Wi-Fi des quais', 17, 11, 700, INK, lh=14))
    b.append(lines(268, 532, 'TRM-01 Scanners des quais : 60 au total, répartition non documentée', 18, 11, 400, INK, lh=14))
    # VPN gateway on the border, drivers' terminals
    b.append(L(322, HY1 + 26, 322, HY1 + 62, DARK, 1.6))
    b.append(i_gateway(300, HY1 - 13))
    b.append(spof(240, HY1 + 8, 4))
    b.append(T(352, HY1 + 22, 'SEC-01 Passerelle VPN', 11.5, 700, INK))
    b.append(i_phone(313, HY1 + 64))
    b.append(T(340, HY1 + 78, 'TRM-02 Terminaux des chauffeurs', 11.5, 400, INK) + T(340, HY1 + 94, '(APP-04 KDriver)', 11, 400, INK))
    # site links
    for xa, xb, lab, n in ((130, HX0, 'RES-01 VPN Moirans : fibre, 300 Mbit/s, sans secours', 2),
                           (HX1, 630, 'RES-02 VPN Clermont : fibre, 100 Mbit/s, sans secours', 3)):
        b.append(L(xa, 420, xb, 420, DARK, 5))
        nl = len(wrap(lab, 14))
        b.append(lines((xa + xb) / 2, 412 - (nl - 1) * 14, lab, 14, 11, 400, INK, 'middle', lh=14))
        b.append(spof((xa + xb) / 2 - 26, 430, n))
    # trucks
    b.append(i_truck(570, HY1 + 62))
    b.append(lines(616, HY1 + 72, 'TRM-03 Boîtiers des 40 camions', 20, 11, 400, INK, lh=14))
    b.append(pth(f'M590,{HY1 + 60} V{HY1 + 38} H752 V{saas} H746', DARK, 1.6, '5 4', 'ahd'))
    b.append(halo(T(746, HY1 + 32, 'transmission directe au fabricant', 11, 400, QUIET, 'end')))
    # cartouche
    x, y = 196, 734
    b.append(R(x, y, 548, 172, '#ffffff', DARK, 1.4, 8))
    b += [T(x + 12, y + 20, 'Vue des infrastructures physiques de Kestrel Logistique', 12.5, 700, DARK),
          T(x + 12, y + 37, 'Version 1.0 · date : mars 2026 · auteur : R. Chevalier', 11.5, 400, INK),
          L(x + 12, y + 47, x + 536, y + 47, MUTED, 1)]
    icons = [(i_server, 'serveur'), (i_nas, 'stockage'), (i_disk, 'disque'), (i_gateway, 'passerelle'),
             (i_wifi, 'Wi-Fi'), (i_monitor, 'poste'), (i_truck, 'camion'), (i_phone, 'terminal')]
    for k, (f, nm) in enumerate(icons):
        ix, iy = x + 12 + (k % 4) * 88, y + 60 + (k // 4) * 48
        sc = 0.75
        b.append(f'<g transform="translate({ix},{iy}) scale({sc})">{f(0, 0)}</g>')
        b.append(T(ix + 36, iy + 18, nm, 11, 400, INK))
    lx = x + 376
    b += [L(lx, y + 66, lx + 34, y + 66, DARK, 1.6), T(lx + 42, y + 70, 'lien réseau', 11, 400, INK),
          L(lx, y + 88, lx + 34, y + 88, DARK, 5), T(lx + 42, y + 92, 'lien inter-sites', 11, 400, INK),
          L(lx, y + 110, lx + 34, y + 110, DARK, 1.6, '5 4'), T(lx + 42, y + 114, 'copie, transmission', 11, 400, INK),
          spof(lx - 8, y + 122, 'n'), T(lx + 50, y + 136, 'point unique', 11, 400, INK),
          isol(lx - 8, y + 146), T(lx + 50, y + 160, 'copie non isolée', 11, 400, INK),
          T(x + 12, y + 160, 'Chaque application de l’inventaire est rattachée à un lieu.', 11, 400, QUIET)]
    return svg(916, b)


def kestrel_zones_confiance():
    b = [defs(), T(24, 30, 'Vue de l’administration et zones de confiance de Kestrel Logistique (exemple, version 1.0)', 15, 600),
         T(24, 50, 'Chaque franchissement entre deux zones de niveaux différents est un point de contrôle et un chemin d’attaque', 11.5, 400, QUIET)]
    LEV = {'nulle': (RED, '2 4', REDBG), 'faible': (WARN, '9 4', '#fff8f3'), 'moyenne': (AMBER, '14 4', '#fffbeb'),
           'élevée': (OK, '22 4 3 4', '#f4fbf5')}

    def zone(x, y, w, h, code, lev, name, n=30, content=None, cn=34):
        c, d, bg = LEV[lev]
        o = R(x, y, w, h, bg, c, 2, 8, d)
        corner = f'{code} · confiance {lev}'
        nc = len(wrap(corner, n))
        o += lines(x + 10, y + 17, corner, n, 11.5, 700, c, lh=14)
        yy = y + 17 + nc * 14 + 2
        o += lines(x + 10, yy, name, n, 12, 700, INK, lh=15)
        yy += len(wrap(name, n)) * 15
        if content:
            o += lines(x + 10, yy, content, cn, 11, 400, QUIET, lh=14)
        return o

    b.append(zone(16, 64, 728, 62, 'ZC-01', 'nulle', 'Internet', 60, 'réseau public : tout ce qui en vient est réputé hostile', 80))
    b.append(zone(16, 146, 222, 92, 'ZC-02', 'faible', 'Prestataires et éditeurs', 34, 'PP-05 Éditeur de RoutePro, PP-19 Prestataires disposant d’un accès VPN', 36))
    b.append(zone(250, 146, 162, 92, 'ZC-03', 'faible', 'Terminaux des chauffeurs', 22))
    b.append(zone(424, 146, 180, 92, 'ZC-04', 'faible', 'Wi-Fi des quais', 24, 'TRM-01 Scanners des quais', 26))
    b.append(zone(616, 146, 128, 446, 'ZC-06', 'moyenne', 'Services externalisés', 12, '(hébergeur cloud, SaaS)', 14))
    b.append(zone(16, 362, 588, 230, 'ZC-05', 'élevée', 'Réseau interne du siège', 60))
    for i, (cd, nm) in enumerate((('APP-03', 'Kestrel Track'), ('APP-10', 'Microsoft 365'), ('APP-02', 'StockFlow'))):
        y = 436 + i * 48
        b.append(R(628, y, 104, 40, '#ffffff', AXIS, 1.2, 6) + T(680, y + 16, cd, 11.5, 600, INK, 'middle') + T(680, y + 31, nm, 11.5, 600, INK, 'middle'))
    # servers sub-zone and DSI workstations
    b.append(R(40, 422, 384, 146, '#ffffff', QUIET, 1.4, 8, '4 3'))
    b.append(lines(54, 444, 'Serveurs : APP-01 RoutePro, APP-07 ERP finance, APP-11 Outil de tickets, sur SRV-01 et SRV-02', 44, 12, 600, INK, lh=15))
    b.append(R(150, 559, 222, 20, '#ffffff', VIO, 1.2, 10) + T(261, 573, 'segmentation non documentée (H3)', 11, 600, VIO, 'middle'))
    b.append(R(440, 532, 150, 34, '#ffffff', AXIS, 1.2, 6) + T(515, 553, 'TRM-06 Postes de la DSI', 11, 600, INK, 'middle'))
    # flows
    b.append(pth('M140,240 L193,345 V420', RED, 4.5, m='ahr'))
    b.append(pth('M320,240 L221,345 V420', RED, 2.6, m='ahr'))
    b.append(pth('M500,240 V358', WARN, 2.6, m='ahw'))
    b.append(pth('M590,549 H610 V466 H626', BLUE, 2.2, m='ahb'))
    b.append(pth('M728,126 V432', VIO, 2.2, m='ahv'))
    b.append(pth('M396,146 V136 H610 V446 H624', VIO, 2.2, m='ahv'))
    b.append(pth('M610,504 H626', BLUE, 2.2, m='ahb'))
    b.append(R(162, 348, 148, 28, DARK, 'none', 0, 6) + T(236, 366.5, 'SEC-01 Passerelle VPN', 11, 700, '#ffffff', 'middle'))
    b += [diamond(178, 312, 1, RED), diamond(240, 314, 2, RED), diamond(500, 343, 3, WARN), diamond(610, 525, 4, BLUE),
          diamond(728, 300, 5, VIO), diamond(560, 136, 6, VIO)]
    b.append(lines(24, 262, 'FR-01 : accès permanent de l’éditeur de RoutePro par la passerelle VPN', 21, 11, 600, RED, lh=14))
    b.append(lines(312, 262, 'FR-02 : VPN chauffeurs vers le réseau interne (application de frais)', 23, 11, 600, RED, lh=14))
    b.append(lines(514, 258, 'FR-03 : scanners Wi-Fi vers le réseau interne (H3), puis APP-02 StockFlow', 15, 11, 600, WARN, lh=14))
    b.append(halo(T(716, 97, 'FR-05 : destinataires et clients B2B vers APP-03 Kestrel Track', 11, 600, VIO, 'end')))
    b.append(halo(T(716, 116, 'FR-06 : APP-04 KDriver vers APP-03 Kestrel Track (FLX-03)', 11, 600, VIO, 'end')))
    b.append(lines(440, 456, 'FR-04 : administration de Microsoft 365 et de Kestrel Track depuis les postes de la DSI', 26, 11, 600, BLUE, lh=14))
    # cartouche
    x, y = 16, 608
    b.append(R(x, y, 728, 156, '#ffffff', DARK, 1.4, 8))
    b += [lines(x + 12, y + 20, 'Vue de l’administration et zones de confiance de Kestrel Logistique', 28, 12.5, 700, DARK, lh=16),
          T(x + 12, y + 74, 'Version 1.0', 11.5, 400, INK), T(x + 12, y + 90, 'Date : mars 2026', 11.5, 400, INK),
          T(x + 12, y + 106, 'Auteur : R. Chevalier', 11.5, 400, INK),
          T(x + 236, y + 20, 'Niveau de confiance (bordure)', 11.5, 700, INK)]
    for k, lev in enumerate(('élevée', 'moyenne', 'faible', 'nulle')):
        c, d, bg = LEV[lev]
        yy = y + 40 + k * 22
        b += [R(x + 236, yy - 11, 46, 16, bg, c, 2, 4, d), T(x + 290, yy + 1, lev, 11.5, 400, INK)]
    b.append(T(x + 430, y + 20, 'Franchissements (flèches)', 11.5, 700, INK))
    for k, (c, m, t) in enumerate(((RED, 'ahr', 'permanent depuis une zone de faible confiance'), (WARN, 'ahw', 'local'),
                                   (BLUE, 'ahb', 'administration'), (VIO, 'ahv', 'vers les services externalisés'))):
        yy = y + 40 + k * 22
        b += [arr(x + 430, yy - 4, x + 466, yy - 4, c, 2.4, m=m), T(x + 474, yy, t, 11.5, 400, INK)]
    b += [diamond(x + 441, y + 130, 'n', DARK), T(x + 474, y + 134, 'point de franchissement numéroté', 11.5, 400, INK)]
    return svg(776, b)


FIGS = {'c00-chaine-d1-d2-d3': chaine_d1_d2_d3,
        'c01-le-moigne': le_moigne, 'c01-chaine-valeur-kestrel': chaine_valeur_kestrel,
        'c02-modele-alignement': modele_alignement, 'c02-plan-urbanisation-kestrel': plan_urbanisation_kestrel,
        'c03-six-vues': six_vues, 'c03-kestrel-ecosysteme': kestrel_ecosysteme,
        'c04-kestrel-infra-physique': kestrel_infra_physique, 'c04-kestrel-zones-confiance': kestrel_zones_confiance}
