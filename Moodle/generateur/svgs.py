# Static SVG versions of the document's charts and diagrams (light theme)
from html import escape
from frtypo import fr, NBSP as NB

INK = '#1f2933'; QUIET = '#5f6b76'; GRID = '#e5e7eb'; AXIS = '#9aa5b1'; MUTED = '#c5cbd3'
ACC = '#0b7285'; ACCBG = '#e3f2f4'; TINT = '#f1f4f6'; REF = '#7b8794'
FONT = 'font-family="Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"'


def T(x, y, s, size=13, w=400, fill=INK, anchor='start'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{escape(fr(s))}</text>'


def R(x, y, w, h, fill='none', stroke=AXIS, sw=1.25, rx=8, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def L(x1, y1, x2, y2, stroke=AXIS, sw=1.25, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def svg(h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 {h}" width="760" height="{h}" {FONT}>'
            f'<rect width="760" height="{h}" fill="#ffffff"/>{"".join(body)}</svg>')


def k(v):
    return f'{round(v / 1000):,}'.replace(',', NB) + NB + 'k'


def activite():
    data = [('2018', 560000, 0), ('2019', 700000, 0), ('2020', 610000, 52000), ('2021', 760000, 61000),
            ('2022', 880000, 49000), ('2023', 990000, 42000), ('2024', 1040000, 40000), ('2025', 1062000, 38000)]
    mx = max(c + t for _, c, t in data); base = 340; bw = 48; band = 672 / len(data)
    h = lambda v: v / mx * 200
    xc = lambda i: 64 + i * band + band / 2
    b = [T(24, 30, "L'activité a presque doublé depuis 2018, la téléconsultation recule depuis 2021", 15, 600),
         T(24, 52, 'Consultations par an ; en noir le total, en couleur la part en téléconsultation', 11.5, 400, QUIET),
         R(24, 70, 12, 12, MUTED, 'none', 0, 2), T(42, 80, 'En centre', 11.5),
         R(130, 70, 12, 12, ACC, 'none', 0, 2), T(148, 80, 'Téléconsultation', 11.5),
         L(64, base, 736, base)]
    notes = {'2019': 'Rachat Artois', '2020': 'Crise sanitaire', '2022': 'Rachat Île-de-Fr.', '2023': '3 ouvertures'}
    for i, (y, c, t) in enumerate(data):
        x = xc(i) - bw / 2
        b.append(R(x, base - h(c), bw, h(c), MUTED, 'none', 0, 0))
        if t:
            b.append(R(x, base - h(c) - h(t), bw, h(t), ACC, 'none', 0, 0))
            b.append(T(xc(i), base - h(c + t) - 26, k(t), 11.5, 400, ACC, 'middle'))
        b.append(T(xc(i), base - h(c + t) - 9, k(c + t), 12, 600, INK, 'middle'))
        b.append(T(xc(i), 360, y, 12, 400, QUIET, 'middle'))
        if y in notes:
            b.append(T(xc(i), 380, notes[y], 10.5, 400, QUIET, 'middle'))
    return svg(400, b)


def orga():
    b = [T(24, 30, 'Medisecure : six directions rattachées au directeur général', 15, 600),
         T(396, 80, 'En couleur : la DSI, au cœur du cas fil rouge', 11.5, 400, QUIET),
         L(194, 104, 194, 128), L(364, 156, 396, 156, dash='4 4'), L(60, 184, 60, 684),
         R(24, 48, 340, 56), T(194, 72, 'Instances de gouvernance', 13, 600, INK, 'middle'),
         T(194, 92, "CA de l'association, comité stratégique de la SAS", 11.5, 400, QUIET, 'middle'),
         R(24, 128, 340, 56), T(194, 152, 'Directeur général', 13, 600, INK, 'middle'),
         T(194, 172, 'Thomas Reynaud', 11.5, 400, QUIET, 'middle'),
         R(396, 128, 340, 56, dash='4 4'), T(566, 152, 'DPO externe', 13, 600, INK, 'middle'),
         T(566, 172, 'Prestataire, 2 jours par mois', 11.5, 400, QUIET, 'middle')]
    dirs = [('Direction médicale · Dr Nadia Benali', '230 professionnels de santé salariés : médecins, infirmiers, manipulateurs radio', 'Qualité des soins, protocoles, choix des outils cliniques'),
            ('Direction des opérations · Karim Haddad', "14 directeurs de centre, accueils et secrétariats, centre d'appels (22 téléconseillers)", 'Plannings des praticiens, ouverture des créneaux'),
            ('Direction innovation et e-santé · Claire Vasseur', 'Téléconsultation, télésurveillance MediSuivi, 6 infirmières de coordination', "Porte les projets d'IA et le passage à l'échelle de MediSuivi"),
            ('Direction administrative et financière · Sophie Marchand', 'Comptabilité, contrôle de gestion, achats, data analyst (Laura Petit)', 'Arbitre les budgets, produit le reporting de direction à J+20'),
            ('Direction des ressources humaines · Émilie Roussel', 'Recrutement, paie externalisée, formation', 'Aucun processus formalisé avec la DSI pour les arrivées et les départs'),
            ("Direction des systèmes d'information · Philippe Lemaire", '24 personnes : RSSI (Julien Morel), infrastructure et support (9), applications (3), plateforme (10)', 'Salle serveur du siège, deux DPI, plateforme Medisecure Connect, support des 14 centres')]
    for i, (n, l1, l2) in enumerate(dirs):
        y = 208 + i * 88; hot = i == 5
        b += [L(60, y + 36, 88, y + 36), R(88, y, 648, 72, ACCBG if hot else 'none', ACC if hot else AXIS, 2 if hot else 1.25),
              T(104, y + 24, n, 13, 600), T(104, y + 44, l1, 11.5), T(104, y + 60, l2, 11.5, 400, QUIET)]
    return svg(744, b)


def hbars(title, sub, rows, fmt, accent_first, ref=None, h=360, bx=264, bwmax=380):
    mx = 100 if ref else max(v for _, v in rows)
    total = sum(v for _, v in rows)
    y0 = 92 if ref else 84
    b = [T(24, 30, title, 15, 600), T(24, 52, sub, 11.5, 400, QUIET)]
    for i, (c, v) in enumerate(rows):
        y = y0 + i * 32; w = v / mx * bwmax
        b += [T(bx - 12, y + 17, c, 12, 400, INK, 'end'),
              R(bx, y + 4, w, 18, ACC if (accent_first and i == 0) else MUTED, 'none', 0, 3),
              T(bx + w + 8, y + 17, fmt(v, total), 12)]
    if ref:
        x = bx + ref[1] / 100 * bwmax
        b += [L(x, y0 - 8, x, y0 + len(rows) * 32, REF, 1.25, '4 4'),
              T(x + 6, y0 - 12, f'{ref[0]} : {ref[1]} %', 11.5, 400, QUIET),
              L(bx, y0, bx, y0 + len(rows) * 32)]
    return svg(h, b)


def tickets():
    rows = [('Comptes et mots de passe', 380), ('Lenteurs de MediDossier', 240), ('Imprimantes et lecteurs de cartes', 210),
            ('Postes de travail', 190), ('Téléconsultation', 120), ('MediSuivi (patients et infirmières)', 110), ('Réseau', 90), ('Autres', 110)]
    return hbars('Un ticket sur quatre concerne un compte ou un mot de passe',
                 'Tickets de support par mois, moyenne de janvier à septembre 2026 : 1 450 tickets',
                 rows, lambda v, t: f'{v} ({round(v / t * 100)} %)', True)


def couverture():
    rows = [('Rendez-vous', 48), ('Télésurveillance', 41), ('Facturation', 35), ('Portail patient web', 31),
            ('Patient', 22), ('Documents', 15), ('Application MediSuivi', 9)]
    return hbars('Aucun composant ne dépasse 50 % de code couvert par des tests',
                 'Part des lignes de code exécutées par les tests automatisés, septembre 2026',
                 rows, lambda v, t: f'{v} %', False, ('Cible du tech lead', 70), 352, 200, 500)


def box_txt(x, y, w, h, name, lines, hot=False, ns=13, ls=11.5, dash=None, pad=16, lh=16):
    out = [R(x, y, w, h, ACCBG if hot else 'none', ACC if hot else AXIS, 2 if hot else 1.25, dash=dash),
           T(x + pad, y + 24, name, ns, 600)]
    first = 44 if ns == 13 else 42
    for j, (s, q) in enumerate(lines):
        out.append(T(x + pad, y + first + j * lh, s, ls, 400, QUIET if q else INK))
    return out


# reseau() and archi() live in icons_diagrams.py


def medisuivi():
    rows = [('T3 2023', 300), ('T4 2023', 900), ('T1 2024', 1500), ('T2 2024', 2100), ('T3 2024', 2600), ('T4 2024', 3000),
            ('T1 2025', 3300), ('T2 2025', 3600), ('T3 2025', 3900), ('T4 2025', 4100), ('T1 2026', 4150), ('T2 2026', 4200), ('T3 2026', 4200)]
    x0, x1, base, ht = 72, 712, 330, 220
    X = lambda i: x0 + i * (x1 - x0) / (len(rows) - 1)
    Y = lambda v: base - v / 5000 * ht
    b = [T(24, 30, 'MediSuivi plafonne à 4 200 patients depuis début 2026', 15, 600),
         T(24, 52, 'Patients télésurveillés en fin de trimestre ; cible du plan 2030 : 15 000 patients', 11.5, 400, QUIET),
         T(x1, 84, 'Plafond : 6 infirmières de coordination, environ 700 patients chacune', 11.5, 400, QUIET, 'end')]
    for t in range(0, 5001, 1000):
        b += [L(x0, Y(t), x1, Y(t), GRID, 1), T(x0 - 8, Y(t) + 4, f'{t:,}'.replace(',', NB), 11.5, 400, QUIET, 'end')]
    pts = ' '.join(('M' if i == 0 else 'L') + f'{X(i):.1f} {Y(v):.1f}' for i, (_, v) in enumerate(rows))
    b.append(f'<path d="{pts}" fill="none" stroke="{MUTED}" stroke-width="2"/>')
    for i, (q, v) in enumerate(rows):
        b += [f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="4" fill="{ACC if i >= 10 else MUTED}"/>',
              T(X(i), base + 20, q, 10.5, 400, QUIET, 'middle')]
    b += [T(X(9), Y(4100) - 14, f'4{NB}100', 11.5, 400, INK, 'middle'),
          T(X(12), Y(4200) - 14, f'4{NB}200', 11.5, 600, ACC, 'end')]
    return svg(380, b)


def timeline():
    ev = [('10 mars, 9 h 12', 'Une secrétaire du centre de Lens saisit ses identifiants', 'sur une fausse page de connexion reçue par courriel.', 0),
          ('10 mars, 14 h 30', "L'attaquant se connecte avec ce compte par l'ancien VPN", "du réseau de l'Artois, sans authentification multifacteur.", 1),
          ('12 mars, 2 h 40', 'Un rançongiciel chiffre le serveur de fichiers du centre', 'et 35 postes de travail.', 2),
          ('12 mars, 7 h 45', "L'accueil découvre les demandes de rançon à l'ouverture.", 'La DSI coupe le lien réseau du centre.', 0),
          ('12 au 14 mars', 'Le centre reste fermé : environ 800 rendez-vous sont annulés.', 'Un prestataire de réponse à incident intervient.', 0),
          ('15 mars', 'Reprise partielle avec des postes réinstallés.', "CareOne, en SaaS, n'a pas été touché.", 0),
          ('17 mars', 'Notification de la violation de données à la CNIL,', 'cinq jours après la découverte.', 0)]
    yy = lambda i: 92 + i * 56
    b = [T(24, 30, "Entre l'intrusion et le chiffrement, l'attaquant a eu 36 heures sans être vu", 15, 600),
         T(24, 52, "Chronologie de l'attaque du centre de Lens, mars 2025", 11.5, 400, QUIET),
         L(190, yy(0) - 4, 190, yy(6) - 4), L(190, yy(1) - 4, 190, yy(2) - 4, ACC, 3),
         T(170, yy(1) + 32, '36 heures', 11.5, 600, ACC, 'end')]
    for i, (d, a, c, hot) in enumerate(ev):
        y = yy(i)
        b += [f'<circle cx="190" cy="{y - 4}" r="5" fill="{ACC if hot else MUTED}"/>',
              T(170, y, d, 13, 400, QUIET, 'end'), T(212, y, a, 13, 600 if hot == 2 else 400), T(212, y + 18, c, 13, 400, QUIET)]
    return svg(476, b)


FIGS = {'node/10e299b8-73a8': activite, 'node/92546710-32c7': orga, 'node/1d948e53-bdea': tickets,
        'node/9fed0203-37fa': lambda: __import__('icons_diagrams').archi(), 'node/bdd0a5fa-a76c': couverture, 'node/c98c7687-e471': lambda: __import__('icons_diagrams').reseau(),
        'node/adf0abe1-57c1': medisuivi, 'node/f924e4b1-689f': timeline}
