# Fiches de travail S2 (format « manuel de STMG ») : notice pour les auteurs

Une fiche de travail fait travailler UNE notion clé du cours à partir d'une situation et d'un dossier documentaire, sur Kestrel Logistique. Elle se fait en atelier (45 à 75 minutes), seul ou à deux. Le générateur `build_fiches_travail.py` produit un livret élève (zones de réponse, tableaux et textes à trous vides) et un livret enseignant (mêmes fiches, avec corrigés et mots manquants).

## Structure d'une fiche (syntaxe exacte)

```
# FT 07 | Repérer redondances, trous et flux manuels | 2

@situation
Deux à quatre phrases : qui vous êtes chez Kestrel (stagiaire à la DSI, assistant de la directrice des SI…), ce qui se passe, ce qu'on vous demande. Une mise en situation concrète, datée sans jour de semaine (par exemple « en mars 2026 »).

@capacites
Identifier les fonctions du SI dans un document
Analyser une matrice processus × applications
Mobiliser les définitions de redondance, trou et flux manuel
Argumenter une priorité

@duree 60 minutes

@annexe 1 | Titre de l'annexe | Source fictive : compte rendu d'entretien de la DSI, mars 2026
Texte de l'annexe en paragraphes séparés par une ligne vide (100 à 250 mots).

@annexe 2 | Extrait de l'inventaire applicatif | Inventaire de la DSI, version 1.0
| Application | Domaine | Hébergement |
| --- | --- | --- |
| APP-01 RoutePro | Transport | Salle serveur du siège |

@annexe 3 | Colis livrés en retard, par mois, en 2025 | Tableau de bord des opérations
@graphique barres colis
Janvier : 310
Février : 280
Mars : 295

@annexe 4 | Le circuit d'un ordre de transport | Schéma de la DSI
@schema
APP-06 Portail EDI -> APP-01 RoutePro -> [[APP-09 Planification des tournées]] -> APP-04 KDriver

@question 1 | Identifier | Annexes 1 et 2
Le texte de la question.
@lignes 4

@question 2 | Calculer | Annexe 3
Le texte de la question.
@tableau
| Mois | Retards | Écart à la moyenne |
| --- | --- | --- |
| Janvier | 310 | |
| Février | 280 | |

@question 3 | Argumenter | Toutes les annexes
Le texte.
@lignes 8

@retiens
Une phrase de synthèse avec des [[mots manquants]] que l'élève complète. Deux à quatre phrases, six à dix trous, qui reprennent les définitions exactes du cours.

@corrige 1
Réponse attendue rédigée, comme un corrigé de manuel : la réponse, puis la justification par les annexes, puis la notion du cours mobilisée.

@corrige 2
| Mois | Retards | Écart à la moyenne |
| --- | --- | --- |
| Janvier | 310 | +15 |

@corrige 3
…
```

Règles de syntaxe : le troisième champ de la ligne `# FT` est le numéro du chapitre du cours. Une `@annexe` est de type texte (paragraphes), tableau (lignes `|`), graphique (`@graphique barres|lignes <unité>` puis une ligne `Étiquette : valeur` par point, nombres décimaux avec une virgule ; 3 à 12 points) ou schéma (`@schema` puis une ou plusieurs lignes de boîtes séparées par `->`). Dans un schéma, une boîte écrite `[[texte]]` est vide dans le livret élève (à compléter) et remplie dans le livret enseignant ; une ligne de schéma ne dépasse pas 5 boîtes. Chaque `@question` est suivie soit de `@lignes N` (nombre de lignes de réponse, 2 à 10), soit d'un `@tableau` à compléter (cellules vides laissées vides), soit de rien si la réponse se fait dans un schéma ou une annexe. Chaque question a son `@corrige` de même numéro. Dans `@retiens`, chaque `[[mot]]` devient un trou.

## Exigences de fond

**Une notion, une progression.** Six à neuf questions par fiche, dans l'ordre des capacités : identifier (relever dans une annexe), analyser (mettre en relation deux annexes, classer), calculer (au moins une question de calcul ou de cotation dans la fiche quand la notion s'y prête : écart, pourcentage, niveau de menace, cote de risque, écart en heures, moyenne), mobiliser (appliquer une définition ou une grille du cours), puis argumenter ou proposer (une question finale rédigée, 8 à 12 lignes). Chaque question cite les annexes à utiliser. Variez les activités : au moins un tableau à compléter ou un schéma à compléter par fiche, plus les questions rédigées.

**Un dossier documentaire varié.** Trois à cinq annexes par fiche, de natures différentes : au moins un texte (compte rendu, courriel, entretien, note, article de la presse professionnelle fictive) et au moins un document chiffré (tableau ou graphique). Les annexes sont fictives, signalées comme telles par leur source, et portent des noms de fonctions et de personnes de la fiche Kestrel (Paul Vidal, Isabelle Roux, Sébastien Morin, Léa Fontaine, Nicolas Perrin, Hélène Garnier, Romain Chevalier), ou des rôles (un planificateur, un chef de quai) sans nom.

**Cohérence absolue avec Kestrel.** Toutes les annexes respectent la fiche Kestrel de `cours_s2/CHARTE.md` et les valeurs de référence du cours : nommage APP-xx, SRV-xx, PP-01 à PP-20, flux FLX, franchissements FR-01 à FR-06, hypothèses H1 à H19 (registre du ch04), échelles et matrice (ch05), étude EBIOS (ch06), grille d'impact (ch08), PESTEL (ch09), maturité, F1 à F7 et EN1 à EN5 (ch10). Vous pouvez AJOUTER des faits nouveaux (un graphique mensuel, un entretien, un nouveau courriel, un détail de l'agence de Clermont-Ferrand) à condition qu'ils ne contredisent rien et restent plausibles ; signalez dans votre rapport chaque fait nouveau important.

**Ne pas recopier l'exemple du cours.** Le cours a déjà fait l'analyse de Kestrel dans ses encadrés EXEMPLE : une fiche de travail ne doit pas se résoudre en recopiant ces encadrés. Prenez une autre facette (un autre processus, une autre application, un autre site, un autre incident, d'autres données), ou demandez à l'apprenant de refaire le raisonnement à partir de documents bruts que le cours n'a pas montrés. Les corrigés, eux, peuvent renvoyer au cours.

**Corrigés d'enseignant.** Chaque corrigé est complet et exact, rédigé comme dans un livre du professeur : la réponse attendue, sa justification par les annexes, la notion du cours mobilisée (chapitre et section), et, pour la question finale, les éléments attendus et un barème indicatif sur le nombre de points de la question si utile. Les calculs sont posés et justes.

**Style.** Charte du cours : français correct, typographie française, phrases courtes, pas de listes à puces dans les annexes et les corrigés (tableaux bienvenus), aucun emoji, aucune date de session.

## Volume

Une fiche élève tient en 3 à 4 pages A4. Annexes : 600 à 1 000 mots au total, tableaux et graphiques compris en équivalent.

## Vérification obligatoire

`cd C:/Users/admin/Desktop/MBA-3WA/Moodle/generateur && PYTHONIOENCODING=utf-8 python build_fiches_travail.py <dossier de travail> <fichier.md>` construit les deux livrets pour votre fichier seul et affiche les erreurs de syntaxe et le nombre de pages par fiche. Rendez les PDF en images (le script écrit des PNG de chaque page dans le dossier de travail) et regardez chaque page avec l'outil Read : rien ne déborde, les zones de réponse ont une taille raisonnable, les graphiques et schémas sont lisibles.

## Schémas draw.io (depuis le 12/11/2026)

Les schémas ne sont plus dessinés avec des flèches en texte : `drawio_schema.py` calcule la mise en page, écrit un fichier `.drawio` par schéma et par version (élève, enseignant) dans `fiches_travail_s2/schemas/`, l'exporte en SVG avec draw.io (`C:\Program Files\draw.io\draw.io.exe`, en ligne de commande) et l'insère dans la fiche. L'export n'est relancé que si le schéma a changé. Trois compléments de syntaxe s'ajoutent aux lignes `A -> B -> C` : une ligne qui commence par `... ->` prolonge la ligne précédente (connecteur coudé) ; `Libellé :: A -> B` ajoute une étiquette à la ligne (à gauche, ou au-dessus de la branche dans un schéma en éventail) ; quand toutes les lignes commencent par la même boîte, ou finissent par la même boîte, cette boîte est dessinée une seule fois et les lignes en partent ou y convergent. Les fichiers `.drawio` s'ouvrent dans draw.io pour une retouche ponctuelle, mais la source qui fait foi reste la fiche `.md`.

Un PDF par fiche : `python build_fiches_travail.py split <dossier élève> <dossier enseignant>` (noms `FT_NN_titre.pdf` et `FT_NN_titre_CORRIGE.pdf`).
