# Architecture diagrams with technology logos (Simple Icons, CC0) and generic icons.
import json, os
from svgs import T, R, L, svg, INK, QUIET, AXIS, ACC, ACCBG

HERE = os.path.dirname(os.path.abspath(__file__))
LOGOS = json.load(open(os.path.join(HERE, 'logos.json'), encoding='utf8'))
# Classic brand colours that read better on white than the current monochrome ones
COLOR_OVERRIDE = {'angular': 'DD0031', 'react': '149ECA', 'openjdk': 'E76F00', 'keycloak': '4D8FCC'}
BAND = '#f5f8fa'; BADGE = '#ffffff'; BADGE_LINE = '#d9e1e7'


def logo(slug, cx, cy, size=20, badge=True):
    d = LOGOS[slug]['d']
    color = '#' + COLOR_OVERRIDE.get(slug, LOGOS[slug]['hex'])
    s = size / 24
    out = []
    if badge:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{size * 0.85:.1f}" fill="{BADGE}" stroke="{BADGE_LINE}" stroke-width="1"/>')
    out.append(f'<g transform="translate({cx - size / 2:.1f},{cy - size / 2:.1f}) scale({s:.4f})"><path d="{d}" fill="{color}"/></g>')
    return ''.join(out)


def icon(name, cx, cy, size=20, color=ACC, badge=True):
    """Generic line icons drawn on a 24-unit grid."""
    st = f'fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
    shapes = {
        'hopital': f'<rect x="4" y="4" width="16" height="17" rx="1.5" {st}/><path d="M12 7.5v6M9 10.5h6M10 21v-3.5h4V21" {st}/>',
        'reseau': f'<circle cx="12" cy="5" r="2.3" {st}/><circle cx="5" cy="18" r="2.3" {st}/><circle cx="19" cy="18" r="2.3" {st}/><path d="M10.8 7 6.2 16M13.2 7l4.6 9M7.3 18h9.4" {st}/>',
        'parefeu': f'<rect x="3" y="5" width="18" height="14" rx="1" {st}/><path d="M3 9.7h18M3 14.3h18M9 5v4.7M15 5v4.7M6 9.7v4.6M12 9.7v4.6M18 9.7v4.6M9 14.3V19M15 14.3V19" {st}/>',
        'serveur': f'<rect x="4" y="3.5" width="16" height="7" rx="1.5" {st}/><rect x="4" y="13.5" width="16" height="7" rx="1.5" {st}/><path d="M7.5 7h.01M7.5 17h.01" {st}/>',
        'stockage': f'<ellipse cx="12" cy="6" rx="7.5" ry="2.8" {st}/><path d="M4.5 6v12c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8V6M4.5 12c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8" {st}/>',
        'globe': f'<circle cx="12" cy="12" r="9" {st}/><ellipse cx="12" cy="12" rx="4" ry="9" {st}/><path d="M3 12h18" {st}/>',
        'nuage': f'<path d="M7 18.5h10.2a4.3 4.3 0 0 0 .4-8.6A6.2 6.2 0 0 0 5.8 9.8 4.4 4.4 0 0 0 7 18.5z" {st}/>',
        'nuagecadenas': f'<path d="M7 17h10.2a4.3 4.3 0 0 0 .4-8.6A6.2 6.2 0 0 0 5.8 8.3 4.4 4.4 0 0 0 7 17z" {st}/><rect x="9.5" y="13" width="5" height="4" rx=".8" fill="{color}"/><path d="M10.6 13v-1.2a1.4 1.4 0 0 1 2.8 0V13" {st}/>',
        'patient': f'<circle cx="9" cy="7.5" r="3.2" {st}/><path d="M3 20c0-3.6 2.7-6 6-6s6 2.4 6 6" {st}/><rect x="16" y="9" width="5.5" height="10" rx="1.2" {st}/><path d="M18.75 16.8h.01" {st}/>',
        'repartiteur': f'<path d="M3 12h6M9 12l5-5.5h6.5M9 12l5 5.5h6.5M9 12h11.5" {st}/><path d="M18 4.5l2.5 2-2.5 2M18 15.5l2.5 2-2.5 2M18 10l2.5 2-2.5 2" {st}/>',
    }
    s = size / 24
    out = []
    if badge:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{size * 0.85:.1f}" fill="{BADGE}" stroke="{BADGE_LINE}" stroke-width="1"/>')
    out.append(f'<g transform="translate({cx - size / 2:.1f},{cy - size / 2:.1f}) scale({s:.4f})">{shapes[name]}</g>')
    return ''.join(out)


def card(x, y, w, h, name, lines, marks, hot=False, ns=13, ls=11.5, tx=54):
    """A box with one badge (logo or icon) on the left and its text beside it."""
    out = [R(x, y, w, h, ACCBG if hot else '#ffffff', ACC if hot else AXIS, 2 if hot else 1.25)]
    cy = y + h / 2
    out.append(marks(x + 28, cy))
    out.append(T(x + tx, y + 24, name, ns, 600))
    for j, (s, q) in enumerate(lines):
        out.append(T(x + tx, y + 44 + j * 16, s, ls, 400, QUIET if q else INK))
    return out


def band(y0, y1, label, mark=None):
    out = [f'<rect x="16" y="{y0}" width="728" height="{y1 - y0}" rx="10" fill="{BAND}"/>',
           T(32 if mark is None else 50, y0 + 18, label, 11.5, 600, QUIET)]
    if mark:
        out.append(mark)
    return out


def archi():
    b = [T(24, 30, 'Découpée en services, la plateforme reste couplée par une base partagée', 15, 600),
         T(24, 50, 'Architecture de Medisecure Connect, état en septembre 2026', 11.5, 400, QUIET)]
    xs3 = [32, 270, 508]
    b += band(68, 162, 'Clients')
    b += band(168, 262, 'Accès et authentification')
    b += band(268, 402, 'Services métier', logo('python', 38, 282, 13, badge=False))
    b += band(408, 518, 'Données')
    b += band(524, 618, "Messagerie, cache et base d'identités")
    b += band(624, 718, 'Exploitation')
    for x1, y1, x2, y2 in [(380, 152, 380, 196), (380, 252, 380, 296), (96, 392, 96, 436), (238, 392, 238, 436),
                           (380, 392, 380, 436), (522, 392, 522, 436), (664, 392, 664, 436)]:
        b.append(L(x1, y1, x2, y2))
    for x, n, l, slug in [(xs3[0], 'Portail patient web', 'Angular 12, Node.js 14', 'angular'),
                          (xs3[1], 'Application MediSuivi', 'React Native 0.63', 'react'),
                          (xs3[2], 'Console infirmières', 'Java Swing, JDK 8', 'openjdk')]:
        b += card(x, 96, 220, 56, n, [(l, 1)], lambda cx, cy, s=slug: logo(s, cx, cy), ns=12.5)
    for x, n, l, mk in [(xs3[0], 'HAProxy 2.4', 'TLS 1.0 et 1.1 acceptés', lambda cx, cy: icon('repartiteur', cx, cy)),
                        (xs3[1], 'Kong Gateway', 'Sans limitation de débit', lambda cx, cy: logo('kong', cx, cy)),
                        (xs3[2], 'Keycloak 15', 'CentOS 7, failles connues', lambda cx, cy: logo('keycloak', cx, cy))]:
        b += card(x, 196, 220, 56, n, [(l, 1)], mk, ns=12.5, ls=11)
    for x, n, l1, l2, slugs in [(32, 'Patient', 'Python 3.7', 'Django 2.2', ['django', 'python']),
                                (174, 'Rendez-vous', 'Python 3.9', 'Flask 2.0', ['flask', 'python']),
                                (316, 'Facturation', 'Python 3.8', 'FastAPI', ['fastapi', 'python']),
                                (458, 'Télésurveillance', 'Node.js 16', 'Seuils codés en dur', ['nodedotjs']),
                                (600, 'Documents', '.NET Core 3.1', 'Windows Server', ['dotnet'])]:
        b.append(R(x, 296, 128, 96, '#ffffff', AXIS, 1.25))
        for j, s in enumerate(slugs):
            b.append(logo(s, x + 22 + j * 30, 318, 18))
        b += [T(x + 10, 356, n, 12, 600), T(x + 10, 372, l1, 11, 400, QUIET), T(x + 10, 386, l2, 11, 400, QUIET)]
    b += card(32, 436, 554, 72, 'PostgreSQL 13, une seule base pour quatre services',
              [('Chaque service lit et écrit directement dans les tables des autres.', 0),
               ('Index non optimisés ; mesures de télésurveillance : 1,1 To, +60 Go par mois', 1)],
              lambda cx, cy: logo('postgresql', cx, cy, 24), hot=True)
    b.append(R(600, 436, 128, 72, '#ffffff', AXIS, 1.25))
    b += [logo('minio', 622, 456, 18), logo('mongodb', 652, 456, 18),
          T(610, 488, 'MinIO, MongoDB', 12, 600), T(610, 502, 'Sauvegarde incomplète', 10.5, 400, QUIET)]
    for x, n, l, slug in [(xs3[0], 'RabbitMQ 3.8', 'Files jamais purgées', 'rabbitmq'),
                          (xs3[1], 'Redis 6.0', 'Pas de bascule si panne', 'redis'),
                          (xs3[2], 'MariaDB 10.5 (Keycloak)', 'Réplication cassée', 'mariadb')]:
        b += card(x, 552, 220, 56, n, [(l, 1)], lambda cx, cy, s=slug: logo(s, cx, cy), ns=12.5)
    b += card(32, 652, 339, 56, 'Prometheus et Grafana', [("Alertes incomplètes, personne d'astreinte", 1)],
              lambda cx, cy: logo('prometheus', cx - 4, cy, 18) + logo('grafana', cx + 28, cy, 18), tx=86)
    b += card(389, 652, 339, 56, 'Veeam sur Windows Server 2019', [('Rétention de 14 jours, non conforme', 1)],
              lambda cx, cy: logo('veeam', cx, cy))
    return svg(736, b)


def reseau():
    b = [T(24, 30, 'Tout le trafic des centres passe par la salle serveur de Lille', 15, 600),
         T(24, 50, 'Schéma réseau simplifié fourni par la DSI, dernière mise à jour en 2024', 11.5, 400, QUIET)]
    for x1, y1, x2, y2 in [(194, 144, 194, 168), (566, 144, 566, 168), (380, 208, 380, 232), (380, 432, 380, 456),
                           (136, 496, 136, 520), (380, 496, 380, 520), (624, 496, 624, 520)]:
        b.append(L(x1, y1, x2, y2))
    b += card(24, 72, 340, 72, '9 centres Hauts-de-France',
              [('6 historiques sous MediDossier, avec 4G', 0), ("3 de l'Artois sous CareOne, sans secours", 1)],
              lambda cx, cy: icon('hopital', cx, cy))
    b += card(396, 72, 340, 72, '5 centres Île-de-France',
              [('3 sous MediDossier, 2 sous CareOne', 0), ('20 à 50 Mbit/s, sans secours 4G', 1)],
              lambda cx, cy: icon('hopital', cx, cy))
    b += [R(24, 168, 712, 40, '#eef3f6'), icon('reseau', 50, 188, 16),
          T(390, 192, "Réseau privé de l'opérateur (MPLS), de 20 à 100 Mbit/s par centre", 13, 400, INK, 'middle'),
          R(24, 232, 712, 200, BAND), icon('serveur', 50, 256, 16), T(74, 260, 'Salle serveur du siège, Lille', 13, 600)]
    b += card(40, 272, 332, 72, 'Pare-feu', [('Seule sortie vers Internet', 0), ('pour le siège et les 14 centres', 1)],
              lambda cx, cy: icon('parefeu', cx, cy))
    b += card(388, 272, 332, 72, '3 serveurs VMware vSphere 6.7',
              [('Environ 40 machines virtuelles :', 0), ('MediDossier, FactuSanté, ERP, AD, GLPI', 1)],
              lambda cx, cy: logo('vmware', cx, cy))
    b += card(40, 360, 332, 56, 'Baie de stockage de 60 To', [('Remplie à 74 %', 1)], lambda cx, cy: icon('stockage', cx, cy))
    b += card(388, 360, 332, 56, 'NAS de sauvegarde (Veeam)', [('Dans la même salle, non isolé du réseau', 1)],
              lambda cx, cy: logo('veeam', cx, cy))
    b += [R(24, 456, 712, 40, '#eef3f6'), icon('globe', 350, 476, 16), T(372, 480, 'Internet', 13, 400)]
    bottom = [(24, 'Services SaaS', ['CareOne, réservation en ligne,', 'Microsoft 365, paie,', "téléphonie du centre d'appels"], 'nuage'),
              (268, 'Cloud certifié HDS', ['Plateforme Medisecure', 'Connect sur 22 VM, une seule', 'zone, sans réplication'], 'nuagecadenas'),
              (512, 'Patients', ['Application MediSuivi,', 'téléconsultation, réservation,', 'appareils via le fabricant'], 'patient')]
    for x, n, ls_, ic in bottom:
        b += [R(x, 520, 224, 96, '#ffffff', AXIS, 1.25), icon(ic, x + 26, 544), T(x + 52, 549, n, 13, 600)]
        for j, s in enumerate(ls_):
            b.append(T(x + 16, 576 + j * 16, s, 11.5))
    return svg(640, b)
