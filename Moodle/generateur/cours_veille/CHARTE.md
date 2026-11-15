# Charte de rédaction du cours « Veille technologique et réglementaire »

## Contexte

Cours de la semaine S1 (semaine de lancement) du cycle Expert en informatique et systèmes d'information de la 3W Academy (titre RNCP 40573, niveau 7, option Data et IA). Public : apprenants Bac+5 en alternance, profils variés (développeurs, data analysts, reconversions scientifiques). Le cours doit leur permettre, à la fin de la semaine, de concevoir SEULS leur dossier de veille D1 pendant les trois semaines d'intersession (rendu en fin d’intersession).

Fichiers de référence à lire avant d'écrire :
- `consignes_D1_veille.md` : les consignes du dossier D1 (plan attendu, grille sur 20, compétences C1 à C3). Le cours doit préparer exactement à ce qui est évalué.
- `medisecure_apprenants.md` : le cas fil rouge (organisation fictive Medisecure). Les exercices portent sur ce cas.

## Règle d'or pédagogique

Le cours enseigne des méthodes, il ne fait pas le dossier à la place des apprenants. Les exemples rédigés (« exemple travaillé ») portent sur une AUTRE entreprise fictive : **Kestrel Logistique**, transporteur régional de 300 salariés en Auvergne-Rhône-Alpes, 40 camions connectés, une plateforme web de suivi des colis développée en interne, un projet d'optimisation des tournées par IA, des données personnelles de clients et de chauffeurs (géolocalisation), soumise au RGPD et potentiellement à NIS2 (secteur transport). Les exercices, eux, s'appliquent à Medisecure mais ne donnent jamais la réponse : ils posent des questions, fournissent une démarche, et renvoient aux sections du dossier Medisecure.

## Style (impératif)

- Français correct, accents, typographie française (espace avant « : ; ? ! », guillemets « »).
- Ton naturel, clair, simple, comme un bon cours universitaire rédigé ou un sujet d'examen. Phrases de moins de 25 mots en général. Paragraphes courts (3 à 5 phrases).
- PAS de listes à puces pour exposer des idées : rédiger en paragraphes. Les tableaux sont encouragés pour comparer, classer, résumer. Les listes numérotées sont tolérées uniquement pour des étapes séquentielles. Les cases à cocher (`- [ ]`) sont réservées aux check-lists d'autonomie.
- Pas de texte creux, pas d'emphase artificielle, pas de formules du type « Dans un monde en constante évolution », « Il est crucial de », « En conclusion, nous avons vu ». Pas d'emojis.
- Pas de section « À retenir » en liste à puces. Une synthèse, si utile, prend la forme d'un tableau ou d'un court paragraphe.
- Chaque notion est illustrée par un exemple concret (Kestrel Logistique ou fait réel vérifiable).

## Exactitude

- Tout fait réglementaire, toute date, tout outil cité doit être exact en octobre 2026. Vérifie avec la recherche web les points datés (calendrier de l'AI Act, transposition de NIS2 en France, Data Act, EHDS, European Accessibility Act, référentiel HDS 2024, CRA, etc.).
- Si un point n'est pas certain (par exemple l'état d'une transposition), écris-le explicitement et demande aux apprenants de le vérifier dans leur veille : c'est pédagogiquement utile.
- Cite les sources institutionnelles par leur nom (CNIL, ANSSI, CERT-FR, ANS, HAS, EUR-Lex, Légifrance, ENISA…) ; pas d'URL inventée. Une URL n'est donnée que si tu l'as vérifiée.
- Les outils cités doivent exister et être décrits honnêtement (gratuit, payant, limites).

## Format Markdown (respecter exactement, un convertisseur l'utilise)

- Un fichier par chapitre. Le chapitre commence par `## N. Titre du chapitre` (N = numéro donné).
- Sous-parties : `### Titre`. Pas de niveau `####`.
- Encadrés : un bloc de lignes commençant par `> ` ; la première ligne est `> [!TYPE] Titre de l'encadré`. Types autorisés :
  - `OBJECTIFS` : en tête de chapitre, ce que l'apprenant saura faire (2 à 4 phrases, pas de puces).
  - `EXEMPLE` : exemple travaillé sur Kestrel Logistique.
  - `EXERCICE` : exercice d'application sur Medisecure, avec durée indicative, consigne, livrable attendu. Jamais de corrigé.
  - `METHODE` : une démarche pas à pas (liste numérotée autorisée dans cet encadré).
  - `ATTENTION` : erreur fréquente ou piège.
  - `DOSSIER` : lien explicite avec une partie du dossier D1 et la ligne de la grille d'évaluation concernée.
- Tableaux en syntaxe pipe standard avec ligne d'en-tête.
- Figures : si un schéma serait utile, insère une ligne seule `[[FIGURE:identifiant|Titre explicite de la figure|description précise de ce que le schéma doit montrer]]`. Le coordinateur les dessinera. Au plus deux figures par chapitre.
- Gras avec `**…**` avec parcimonie. Pas d'italique décoratif.

## Longueur

Entre 1 500 et 2 500 mots par chapitre (hors tableaux), sauf indication contraire. Au moins un EXEMPLE, un EXERCICE, un DOSSIER par chapitre de méthode.

## Plan général du cours (pour cohérence, chacun écrit seulement ses chapitres)

0. Introduction : à quoi sert ce cours, compétences visées (C1 à C3), déroulé de la semaine S1, lien avec le dossier D1.
1. Les fondamentaux de la veille : définitions, types de veille, cycle de la veille, veille et intelligence économique, push et pull.
2. Cadrer sa veille : besoins informationnels, parties prenantes, QQOQCCP, axes, priorités, plan de veille.
3. Trouver et évaluer les sources : typologie, sources institutionnelles, normes, critères de fiabilité, cartographie des sources.
4. Outiller la collecte : agrégateurs, alertes, newsletters, réseaux, veille des vulnérabilités et fins de support, IA de recherche, circuit de collecte.
5. Traiter et analyser : filtrage, vérification, catégorisation, signaux faibles et forts, grille d'impact, radar technologique, impact environnemental.
6. Panorama réglementaire : données, santé, IA, cybersécurité, accessibilité, numérique responsable.
7. Veille cybersécurité et IA : menaces, référentiels (OWASP, MITRE ATLAS, ANSSI), vulnérabilités, IA fantôme.
8. Capitaliser et diffuser : base de connaissances, formats selon les publics, canaux, rythme, accessibilité, mesure de l'utilité.
9. De la veille à la recommandation : fiche de recommandation, chiffrage, priorisation, feuille de route.
10. L'IA générative au service de la veille : usages, limites, charte d'usage du cycle.
11. Passer à l'autonomie : planning de l'intersession, livrables intermédiaires, auto-évaluation alignée sur la grille, erreurs fréquentes, FAQ.
12. Annexes : gabarits (fiche de veille, cartographie des sources, grille de fiabilité, QQOQCCP, matrice d'impact, fiche de recommandation), glossaire, sitographie.
