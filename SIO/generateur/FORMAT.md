# Livret « Ma veille technologique » (BTS SIO 2) : notice pour les auteurs de fiches

Public : étudiants de deuxième année de BTS SIO (options SISR et SLAM), en alternance ou en formation initiale. Niveau bac+2 : vocabulaire simple, phrases courtes, exemples tirés de leur quotidien de technicien ou de développeur. Le livret remplace le cours magistral de la semaine : chaque fiche apporte la notion ET la fait travailler. Le ton est celui d'un manuel de STMG : clair, concret, vivant, jamais infantilisant.

Chaque fiche suit un parcours fixe en cinq temps : 1 Je découvre les notions, 2 Je teste mes connaissances (un ou deux jeux), 3 J'analyse des documents (dossier documentaire et questions progressives), 4 Je réfléchis (une question ouverte de recul), 5 J'avance sur mon dossier de veille (application à SON sujet), puis l'encadré « Je retiens » à trous. Durée d'une fiche : 60 à 90 minutes. Volume : 4 à 5 pages A4 dans le livret étudiant.

Lire impérativement `REGISTRE.md` (personnages, faits réels autorisés, valeurs de référence communes) avant d'écrire.

## Syntaxe exacte

```
# FICHE 05 | Cadrer sa veille avec le QQOQCCP | Jour 2

@accroche
Deux à quatre phrases qui accrochent : une situation vécue par Inès, Yanis ou Léo, une anecdote réelle autorisée, une question provocante. Le générateur préfixe « Pour commencer · ».

@objectifs
Définir ...
Distinguer ...
Construire ...

@duree 75 minutes

@notions
Paragraphes de cours (séparés par une ligne vide), tableaux Markdown (lignes « | »), et encadrés sur une ligne :
!def Terme | Définition en une ou deux phrases.
!exemple Titre | Texte de l'exemple.
!astuce Titre | Texte.
!attention Titre | Texte.
!savoir Titre | Anecdote réelle (registre) ou chiffre (fictif signalé comme tel).
Schéma en boîtes et flèches : une ou plusieurs lignes consécutives
!schema Cadrer -> Sourcer -> Collecter
Mise en forme dans le texte : **gras**, *italique*, `code`.

@jeu vraifaux | Vrai ou faux ? Cochez, puis corrigez les affirmations fausses
Affirmation | V | Explication courte (affichée dans le livret enseignant)
Autre affirmation | F | Explication

@jeu associe | Reliez chaque terme à sa définition
Terme de gauche | Élément de droite correspondant
(écrire les paires dans l'ordre correct ; le générateur mélange la colonne de droite et affiche la solution côté enseignant)

@jeu quiz | Quiz express
? Question
- mauvaise réponse
+ bonne réponse
- mauvaise réponse

@jeu classe | Classez chaque élément
| Élément | Catégorie 1 | Catégorie 2 | Catégorie 3 |
| --- | --- | --- | --- |
| Élément à classer | x | | |
(x dans la bonne colonne ; l'étudiant voit des cases vides)

@annexe 1 | Titre du document | Source fictive : courriel de Claire Fabre à Yanis, mars 2026
Texte en paragraphes, ou tableau, ou encadrés.

@annexe 2 | Titre | Source fictive : relevé de Yanis
@graphique barres heures par semaine
Lundi : 3
Mardi : 2,5

@annexe 3 | Titre | Source
@schema
Boîte -> [[Boîte à compléter]] -> Boîte

@question 1 | Repérer | Document 1
Texte de la question.
@lignes 4

@question 2 | Calculer | Documents 1 et 2
Texte.
@tableau
| Colonne | Colonne |
| --- | --- |
| valeur | |

@reflexion
Une question ouverte qui fait prendre du recul (éthique, métier, méthode, débat). Peut citer une phrase à discuter.
@lignes 6

@monprojet
Consigne qui applique la notion au sujet de veille DE L'ÉTUDIANT, avec un livrable concret qui ira dans son dossier.
@tableau
| Élément | Pour mon sujet |
| --- | --- |
| ... | |

@retiens
Deux à quatre phrases de synthèse avec 6 à 10 [[mots manquants]].

@corrige 1
Corrigé rédigé.

@corrige 2
| Colonne | Colonne |
| --- | --- |
| valeur | réponse |

@corrige R
Pistes de réflexion attendues, arguments possibles dans les deux sens.

@corrige P
Ce que l'enseignant vérifie dans la production de l'étudiant (critères concrets, erreurs fréquentes).
```

Le troisième champ de l'en-tête est le jour : « Jour 1 » à « Jour 5 », exactement.

## Exigences de fond

**Notions allégées mais justes.** Le bloc notions tient en une page à une page et demie : l'essentiel, deux à quatre encadrés (au moins une définition), au moins un tableau ou un schéma. Pas de jargon de grand groupe (pas de DSI de 24 personnes, pas de comité de direction) : on parle d'un technicien, d'un développeur, d'un service informatique de trois personnes, d'une agence de 14 salariés. Rien sur la veille réglementaire détaillée (RGPD, NIS2, AI Act) au-delà d'une mention : le sujet est la veille TECHNOLOGIQUE, avec sa part de veille sécurité.

**Ludique.** Un ou deux jeux par fiche, variés d'une fiche à l'autre (vrai ou faux, associer, quiz, classer). Six à huit items par jeu. Les pièges doivent être instructifs, pas des pièges de vocabulaire.

**Analyse documentaire.** Deux à quatre documents de natures différentes (au moins un texte : courriel, message Teams, échange avec le tuteur, article de presse fictif, capture de flux décrite ; au moins un document chiffré ou un tableau). Quatre à sept questions progressives, avec une étiquette de capacité parmi : Repérer, Comprendre, Calculer, Classer, Analyser, Appliquer, Comparer, Justifier, Proposer, Argumenter. Au moins une question à tableau à compléter ou un schéma à trous. La dernière question est rédigée (6 à 10 lignes). Chaque question cite les documents à utiliser.

**Réflexion.** Une vraie question ouverte, qui n'a pas une seule bonne réponse : « Un développeur qui ne fait pas de veille est-il un mauvais développeur ? », « Faut-il faire confiance à une IA pour résumer l'actualité ? ». Le corrigé R donne des pistes dans les deux sens.

**Mon dossier.** Toujours une production concrète réutilisable dans le dossier de veille (tableau à remplir, phrase à rédiger, liste de mots-clés, première source cotée…). Préciser la partie du dossier où elle ira. Le corrigé P dit ce que l'enseignant vérifie.

**Corrigés.** Complets, exacts, rédigés comme un livre du professeur : la réponse, puis la justification par les documents, puis la notion. Calculs posés et justes.

**Cohérence.** Respect strict de `REGISTRE.md`. Les faits nouveaux fictifs sont plausibles et signalés comme fictifs par leur source (« Source fictive : … »). Un fait réel hors liste : à éviter, ou à signaler dans le rapport.

**Style.** Français correct avec accents, typographie française (guillemets « », espaces), phrases courtes. Dans les notions, les documents et les corrigés : des paragraphes et des tableaux, pas de listes à puces. Aucun emoji. Aucune date de session, aucune date limite de rendu. Vouvoiement de l'étudiant.

## Vérification obligatoire

`cd C:/Users/admin/Desktop/MBA-3WA/SIO/generateur && PYTHONIOENCODING=utf-8 python build_livret.py <dossier de travail> fiches/fXX.md` construit les deux livrets pour la fiche seule, affiche les avertissements et le nombre de pages, et écrit un PNG par page dans le dossier de travail. Regardez chaque page avec l'outil Read : rien ne déborde, les zones de réponse sont de taille raisonnable, les jeux et schémas sont lisibles. Corrigez jusqu'à zéro avertissement.
