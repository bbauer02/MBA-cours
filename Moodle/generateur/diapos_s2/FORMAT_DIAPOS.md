# Diaporamas, prompteurs et scripts S2 : notice pour les auteurs

Chaque jour de la semaine S2 a une spécification JSON, `diapos_s2/spec/J1.json` à `J5.json`. Le script `build_diapos.py` en tire trois fichiers : le diaporama PowerPoint (style de la S1, même modèle), le prompteur HTML (même page que la S1) et le script Word. Vous écrivez le contenu ; le générateur fait la mise en page et ajuste la taille du texte.

## Sources à lire

Le cours (`cours_s2/chapitres/chNN.md`) est la référence : une diapositive ne dit rien que le cours ne dise pas, avec les mêmes définitions, les mêmes chiffres et le même exemple Kestrel. Les consignes du D2 (`consignes_D2_cartographie.md`) font foi. La charte (`cours_s2/CHARTE.md`) fixe le style, la fiche Kestrel et les « Définitions et références communes ». Pour le ton du script oral, lisez `diapos_s2/ref/S1_extrait_script.txt` (script de la S1) : vous parlez aux apprenants, phrases courtes, exemples concrets, renvois au cours et au dossier.

## Répartition et numérotation (impératives)

La numérotation des diapositives est continue sur la semaine. Chaque jour a un nombre fixe de diapositives : respectez-le exactement.

| Fichier | Jour | Diapositives | Contenu | Chapitres |
| --- | --- | --- | --- | --- |
| J1.json | Jour 1 | 1 à 17 (17) | Couverture ; organisation de la journée (contrôle du D1 le matin) ; notions de base, fiches FT 01-04 | ch01 |
| J2.json | Jour 2 | 18 à 46 (29) | Stratégie SI, gouvernance, urbanisation ; cartographie ; construire la cartographie ; fiches FT 05-11 | ch02, ch03, ch04 |
| J3.json | Jour 3 | 47 à 67 (21) | Sécurité et risque ; EBIOS RM ateliers 1 et 2 ; fiches FT 12-14 | ch05, ch06 (début) |
| J4.json | Jour 4 | 68 à 91 (24) | Data et IA ; ateliers 3 à 5 ; analyse d'impact ; fiches FT 15-18 | ch07, ch06 (suite), ch08 |
| J5.json | Jour 5 | 92 à 109 (18) | Environnement ; diagnostic ; fiches FT 19-21 ; QCM ; pitch | ch09, ch10 |

Depuis le 13/11/2026 : pas de diapositive sur la compétence, la grille E1-E20 ni l'évaluation du D2 ; chaque fiche de travail a une diapositive `fiche` (champs ft, name, duration, consigne, livrable) placée après la notion, avant l'atelier Medisecure. `first_number` se recalcule quand un jour change de taille.

Chaque jour commence par une diapositive `cover` (titre du jour), puis une diapositive qui annonce le programme de la journée (matin : théorie ; après-midi : ateliers sur Medisecure). Chaque chapitre s'ouvre par une `section`. Chaque jour contient au moins une diapositive `study` (une étude de document du cours, reprise telle quelle et résumée si besoin) et une diapositive `exercise` par exercice lancé l'après-midi (consigne résumée du cours, livrable, élément du D2). Le Jour 5 se termine par le QCM, le pitch d'étape (ce qui doit être prêt), le planning de l'intersession et la restitution du jour de la restitution.

## Format JSON

```json
{
  "day": 2,
  "title": "Semaine S2 · Jour 2 · Stratégie SI et cartographie",
  "first_number": 19,
  "deroule": "Matin : diapositives 19 à 33 (chapitres 2 et 3). Après-midi : diapositives 34 à 40 (chapitre 4) et ateliers…",
  "slides": [ { "pattern": "...", "kicker": "...", "title": "...", "minutes": 2, "notes": [ {"cue": "...", "text": "..."} ], ...champs du modèle... } ]
}
```

Champs communs : `pattern` (modèle), `kicker` (petite ligne au-dessus du titre, par exemple « Chapitre 3 · Les vues de l'ANSSI »), `title` (titre de 60 caractères environ au plus, sur une ligne : le générateur signale un titre trop long ; une phrase qui dit le message de la diapositive, pas un simple thème), `minutes` (durée indicative de parole), `notes` (le script oral, voir plus bas).

## Les modèles

| pattern | Champs | Usage | Limites de texte |
| --- | --- | --- | --- |
| cover | kicker, title, subtitle | Première diapositive du jour (fond sombre) | subtitle ≤ 220 caractères |
| section | kicker (« Chapitre N »), title, subtitle | Ouverture de chapitre (fond sombre) | subtitle ≤ 220 caractères : ce que l'on saura faire |
| definition | term, definition (liste de 1 à 2 phrases), source, side {tag, head, body[]} facultatif, note, note_style | Une notion clé et son exemple | definition ≤ 380 caractères ; side body ≤ 300 |
| cards | intro facultatif, cards [{head, body, tag, fill}], cols, note, note_style | 2 à 6 cartes (exemples, comparaison, rôles) | body ≤ 200 caractères par carte (3 colonnes), ≤ 130 (4 ou 5 colonnes) |
| text_panel | text [phrases], panel {kicker, items [{big, small}] ou body []}, note | Un message à gauche, des chiffres clés dans un panneau sombre | text ≤ 450 caractères ; 2 ou 3 items |
| table | intro, header [], rows [[]], widths [], fills [[]], side {tag, head, body[]}, note | Comparaison, gabarit, extrait Kestrel | 7 lignes et 5 colonnes au plus ; cellules courtes |
| figure | fig (identifiant d'une figure du cours, par exemple c03-six-vues), side (liste de phrases ou {head, body}), note | Reprendre une figure du cours | side ≤ 300 caractères |
| steps | steps [{head, body}] (3 à 6), highlight [indices], cards [] ou text, note | Démarche, frise, enchaînement | body d'étape ≤ 40 caractères |
| pills | items [{pill, head, sub, body}], layout « row » (3 ou 4 items) ou « list » (jusqu'à 8) | Compétences, étapes numérotées, éléments de grille | body ≤ 140 caractères |
| study | source, document [paragraphes], questions [] | Étude de document (texte du cours) | document ≤ 900 caractères (résumez fidèlement et dites « extrait » ou « résumé ») ; 3 à 5 questions |
| exercise | name, duration, consigne [phrases], livrable, dossier | Lancement d'un atelier Medisecure | consigne ≤ 600 caractères ; jamais de corrigé |
| quote | quote, cards [] ou header/rows | Une phrase forte en bandeau, puis cartes ou tableau | quote ≤ 140 caractères |

`note_style` : « info » (bandeau neutre), « warn » (piège, préfixé « Attention · »), « dossier » (lien avec le D2, préfixé « Pour votre dossier D2 · »), « key » (message à retenir, fond sombre). `fill` d'une carte : « mist » (défaut), « pet » (sombre, pour mettre en valeur une carte), « warnbg », « ambbg », « tealbg ». `fills` d'un tableau : couleurs de cellules, `null` pour la couleur par défaut ; pour une matrice des risques, « risk1 » (faible) à « risk4 » (critique).

Les figures disponibles sont celles du cours S2 (c00-chaine-d1-d2-d3, c01-le-moigne, c01-chaine-valeur-kestrel, c02-modele-alignement, c02-plan-urbanisation-kestrel, c03-six-vues, c03-kestrel-ecosysteme, c04-kestrel-infra-physique, c04-kestrel-zones-confiance, c05-processus-iso27005, c06-cinq-ateliers, c06-graphe-attaque-kestrel, c07-surface-data-ia, c07-graphe-attaque-kestrel, c08-axe-pdma-dmia-mtpd, c08-dependances-kestrel, c09-pestel-forces-si, c10-matrice-impact-urgence, c11-calendrier). Utilisez-les : une figure du cours sur une diapositive aide l'apprenant à retrouver le passage.

## Règles de contenu des diapositives

Une diapositive, un message, écrit dans le titre. Le texte à l'écran est court : mots-clés, chiffres, phrases brèves ; le développement est dans le script oral. Pas de listes à puces : cartes, tableaux, pastilles et frises les remplacent (comme en S1). Typographie française, sigles expliqués à leur première apparition dans la journée. Les exemples sont Kestrel ; Medisecure n'apparaît que dans les exercices, les rappels du cas et les consignes, sans jamais donner une réponse du D2. Aucune date de session (« Jour 1 », « jour du rendu », « jour de la restitution ») : les dates figurent dans les consignes. Les valeurs Kestrel (échelles, cotes, F1 à F7, H1 à H19, nommage APP-xx…) sont exactement celles du cours.

## Le script oral (`notes`)

Chaque diapositive a de 2 à 5 blocs `{cue, text}`. `cue` dit ce que l'apprenant regarde à ce moment (« Titre », « Carte de gauche "Kestrel" », « Bandeau du bas ») : il n'est pas lu. `text` est ce que le formateur dit, rédigé intégralement, à la première personne, comme dans la S1 : il explique, donne l'exemple, pose une question à la salle, fait le lien avec le cours (« le chapitre 3, section… ») et avec le dossier (« élément E5 »). Comptez 130 mots par minute : `minutes` doit correspondre au volume du texte (par exemple 260 mots pour 2 minutes). Visez 5 000 à 6 500 mots par jour. Les diapositives d'exercice disent comment l'atelier se déroule (durée, travail seul ou à deux, ce que le formateur vérifie en passant) ; les diapositives d'étude disent comment animer la discussion (temps de lecture, tour de table, éléments de réponse à faire émerger, tirés du cours, sans corrigé Medisecure).

## Vérification obligatoire avant de rendre

1. `cd C:/Users/admin/Desktop/MBA-3WA/Moodle/generateur/diapos_s2 && PYTHONIOENCODING=utf-8 python render_check.py JN <dossier de travail>` : le script construit le jour, affiche les AVERTISSEMENTS (texte réduit sous 11 points, texte ou tableau qui déborde) et écrit des planches PNG de 6 diapositives.
2. Ouvrez chaque planche avec l'outil Read et regardez chaque diapositive : rien ne déborde, rien ne se chevauche, le texte est lisible, la diapositive n'est pas vide aux trois quarts. Corrigez la spécification (raccourcir, changer de modèle, couper en deux diapositives en gardant le nombre total) jusqu'à zéro avertissement et un rendu propre.
3. Vérifiez le nombre de diapositives et la numérotation (first_number).
