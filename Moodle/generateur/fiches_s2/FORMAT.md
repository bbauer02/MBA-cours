# Fiches de cours et d'étude S2 : format et règles

Les fiches S2 reprennent les fiches de révision S1 (`fiches_veille/fiches_A.md`, à lire comme modèle) et leur ajoutent une étude de document. Une fiche = une notion du cours = deux pages A4 imprimées recto verso. Le générateur est `build_fiches_s2.py`.

## Structure d'une fiche (syntaxe exacte)

```
# FICHE 07 | Titre court de la notion | 3

@essentiel
Deux ou trois paragraphes courts (90 à 140 mots au total) : la définition, puis ce qu'il faut en comprendre et à quoi elle sert dans le dossier D2.

@tableau Titre du tableau
| Col 1 | Col 2 | Col 3 |
| --- | --- | --- |
| ... | ... | ... |

@rappel Terme technique
Définition en une à trois phrases simples.

@rappel Autre terme
...

@attention Titre facultatif
Un piège fréquent, en deux phrases.

@document Document · nature et source (par exemple : article de presse fictif, « L'Hebdo des Transports », mai 2026 ; ou : cas réel résumé d'après la CNIL, délibération du 15 avril 2022 ; ou : extrait du guide de l'ANSSI « Cartographie du système d'information », 2018)
Le texte à étudier, en un à trois paragraphes séparés par une ligne vide, 160 à 260 mots.

@questions
1. Question de compréhension du document.
2. Question d'analyse qui mobilise la notion de la fiche.
3. Question de réflexion critique ou de transfert (vers Medisecure ou vers l'entreprise d'alternance).

@pistes
1. Éléments de réponse attendus pour la question 1, en deux à quatre phrases.
2. Idem pour la question 2.
3. Idem pour la question 3 ; pour une question de transfert, dire ce qu'une bonne réponse contient, sans donner de réponse sur Medisecure qui ferait le dossier à la place de l'apprenant.

@qcm
Q: Question ?
- Proposition fausse
+ Proposition juste (une seule)
- Proposition fausse
E: Explication en une phrase.

Q: ...
```

Le troisième champ de la ligne `# FICHE` est le numéro du chapitre du cours. Les numéros de fiche ont deux chiffres et se suivent sans trou dans tout le livret.

## Contraintes de volume (la fiche doit tenir sur deux pages)

Recto : `@essentiel` (90 à 140 mots), un seul `@tableau` (4 à 6 lignes, 2 à 4 colonnes, cellules courtes), deux à quatre `@rappel`, au plus un `@attention` ou `@astuce`. Verso : un `@document` de 160 à 260 mots, trois ou quatre `@questions`, trois questions de `@qcm` (trois propositions chacune, comme en S1). Les `@pistes` n'apparaissent que dans le corrigé.

## Règles de fond

Le contenu reprend le cours (`cours_s2/chapitres/chNN.md`) sans le contredire : mêmes définitions, mêmes chiffres, même exemple Kestrel. Lisez le chapitre avant d'écrire ses fiches. Style de la charte du cours (`cours_s2/CHARTE.md`) : phrases courtes, aucune liste à puces, typographie française, aucun emoji.

Les documents varient d'une fiche à l'autre : article de presse fictif, entretien fictif, courriel ou compte rendu interne fictif, cas réel résumé avec vos mots à partir de sources vérifiées (nom de la source et date dans la ligne `@document`), court extrait exact d'une publication publique sous Licence ouverte (ANSSI, CNIL, ANS), 200 mots au plus. Un document fictif est toujours dit fictif dans sa ligne de source. Ne reproduisez jamais un article de presse réel. Les documents des fiches sont DIFFÉRENTS de ceux des encadrés ETUDE du cours : la fiche apporte un nouveau texte. Ils peuvent porter sur une organisation fictive autre que Kestrel et Medisecure (par exemple une mutuelle, une collectivité, un e-commerçant), sur Kestrel, ou sur un cas réel ; ils ne portent pas sur Medisecure, qui est réservée aux exercices et au dossier.

Les questions de QCM ont une seule bonne réponse, des distracteurs plausibles, et ne reprennent pas mot pour mot une question d'une autre fiche. Variez la position de la bonne réponse.

## Banque d'évaluation (questions inédites)

Pour chaque fiche, écrivez aussi quatre questions de QCM INÉDITES (jamais montrées aux apprenants) dans `qcm_eval_s2/eval_X.md`, au format :

```
# FICHE 07 | Titre identique à celui de la fiche | 3

@qcm
Q: Question en situation (cas Kestrel, Medisecure ou autre) ?
- ...
+ ...
- ...
- ...
E: Explication.
```

Quatre propositions par question d'évaluation (comme la banque S1 `qcm_eval/eval_A.md`, à lire comme modèle). Préférez des questions de mise en situation à des questions de définition, et des distracteurs qui correspondent à des erreurs réelles. Une question d'évaluation sur Medisecure peut porter sur une notion (« quel type de bien support est… ») mais ne doit pas trancher une question que le dossier D2 demande d'analyser.
